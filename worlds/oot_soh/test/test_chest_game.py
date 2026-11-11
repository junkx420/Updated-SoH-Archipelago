"""Shuffle Treasure Chest Game from SoH 9.3.1 (ShuffleTreasureChestGame.cpp, feature 3.10)."""
from .bases import SohTestBase
from ..Enums import Items, Locations
from ..Locations import chest_game_location_table

CHEST_GAME = [str(loc) for loc in chest_game_location_table]
ROOM_KEYS = [Locations.MARKET_CHEST_GAME_FIRST_ROOM_KEY, Locations.MARKET_CHEST_GAME_SECOND_ROOM_KEY,
             Locations.MARKET_CHEST_GAME_THIRD_ROOM_KEY, Locations.MARKET_CHEST_GAME_FOURTH_ROOM_KEY,
             Locations.MARKET_CHEST_GAME_FIFTH_ROOM_KEY]


def player_locations(test: SohTestBase) -> set[str]:
    return {loc.name for loc in test.multiworld.get_locations(test.player)}


def count_items(test: SohTestBase, item: Items) -> int:
    return sum(1 for i in test.multiworld.itempool if i.player == test.player and i.name == item.value)


class TestChestGameOff(SohTestBase):
    def test_no_locations_and_keys(self):
        self.assertFalse(set(CHEST_GAME) & player_locations(self))
        self.assertIn(Locations.MARKET_TREASURE_CHEST_GAME_REWARD.value, player_locations(self))
        self.assertEqual(0, count_items(self, Items.TREASURE_GAME_SMALL_KEY))
        self.assertEqual(0, count_items(self, Items.TREASURE_GAME_KEY_RING))


class TestChestGameOn(SohTestBase):
    options = {"shuffle_treasure_chest_game": True}

    def test_locations_and_ids(self):
        self.assertTrue(set(CHEST_GAME) <= player_locations(self))
        ids = sorted(data.loc_id for data in chest_game_location_table.values())
        self.assertEqual(ids, list(range(49, 59)) + [3029])

    def test_six_small_keys(self):
        self.assertEqual(6, count_items(self, Items.TREASURE_GAME_SMALL_KEY))
        self.assertEqual(0, count_items(self, Items.TREASURE_GAME_KEY_RING))

    def test_keys_needed(self):
        # chests need keys: n-th room key chest needs n keys (logic.cpp SmallKeys), the reward needs all 6
        self.collect_all_but([Items.TREASURE_GAME_SMALL_KEY.value])
        self.assertTrue(self.can_reach_location(Locations.MARKET_CHEST_GAME_SHOPKEEPER.value))
        self.assertFalse(self.can_reach_location(Locations.MARKET_CHEST_GAME_FIRST_ROOM_KEY.value))
        key = self.world.create_item(Items.TREASURE_GAME_SMALL_KEY)
        self.collect(key)
        self.assertTrue(self.can_reach_location(Locations.MARKET_CHEST_GAME_FIRST_ROOM_KEY.value))
        self.assertFalse(self.can_reach_location(Locations.MARKET_CHEST_GAME_SECOND_ROOM_KEY.value))
        for _ in range(4):
            self.collect(self.world.create_item(Items.TREASURE_GAME_SMALL_KEY))
        self.assertTrue(self.can_reach_location(Locations.MARKET_CHEST_GAME_FIFTH_ROOM_ITEM.value))
        self.assertFalse(self.can_reach_location(Locations.MARKET_TREASURE_CHEST_GAME_REWARD.value))
        self.collect(self.world.create_item(Items.TREASURE_GAME_SMALL_KEY))
        self.assertTrue(self.can_reach_location(Locations.MARKET_TREASURE_CHEST_GAME_REWARD.value))


class TestChestGameKeyRing(SohTestBase):
    options = {"shuffle_treasure_chest_game": True, "key_rings": "selection", "chest_game_key_ring": True}

    def test_key_ring(self):
        self.assertEqual(1, count_items(self, Items.TREASURE_GAME_KEY_RING))
        self.assertEqual(0, count_items(self, Items.TREASURE_GAME_SMALL_KEY))
        self.collect_all_but([Items.TREASURE_GAME_KEY_RING.value])
        self.assertFalse(self.can_reach_location(Locations.MARKET_CHEST_GAME_FIFTH_ROOM_KEY.value))
        self.collect(self.world.create_item(Items.TREASURE_GAME_KEY_RING))
        self.assertTrue(self.can_reach_location(Locations.MARKET_TREASURE_CHEST_GAME_REWARD.value))


class TestChestGameKeyRingIgnoredWithoutShuffle(SohTestBase):
    options = {"key_rings": "selection", "chest_game_key_ring": True}

    def test_ignored(self):
        self.assertEqual(0, count_items(self, Items.TREASURE_GAME_KEY_RING))
        self.assertFalse(self.world.options.chest_game_key_ring.value)


class TestChestGameKeyRingCount(SohTestBase):
    options = {"shuffle_treasure_chest_game": True, "key_rings": "count", "key_rings_count": 10,
               "gerudo_fortress_key_shuffle": "anywhere", "fortress_carpenters": "normal"}

    def test_all_ten(self):
        self.assertEqual(10, self.world.options.key_rings_count.value)
        self.assertTrue(self.world.options.chest_game_key_ring.value)
        self.assertEqual(1, count_items(self, Items.TREASURE_GAME_KEY_RING))
