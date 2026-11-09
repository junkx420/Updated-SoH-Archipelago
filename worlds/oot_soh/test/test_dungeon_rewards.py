"""Dungeon Rewards "Own Dungeon" and Link's Pocket Reward (SoH 9.3.1, feature 2.2)."""
from .bases import SohTestBase
from ..Enums import Items, Locations
from ..KeyShuffle import own_dungeon_rewards
from ..Locations import location_data_table
from ..Options import ShuffleDungeonRewards, StartWithLinksPocket, LinksPocketReward

STONES = (Items.KOKIRIS_EMERALD.value, Items.GORONS_RUBY.value, Items.ZORAS_SAPPHIRE.value)


class TestOwnDungeonRewards(SohTestBase):
    options = {"shuffle_dungeon_rewards": ShuffleDungeonRewards.option_own_dungeon,
               "start_with_links_pocket": StartWithLinksPocket.option_nothing}

    def test_rewards_in_their_dungeon(self):
        self.world_setup()
        from Fill import distribute_items_restrictive
        distribute_items_restrictive(self.multiworld)
        placed = {location.item.name: location for location in self.multiworld.get_locations(self.player)
                  if location.item and location.item.player == self.player}
        for dungeon, reward in own_dungeon_rewards.items():
            location = placed[reward.value]
            self.assertEqual(location_data_table[location.name].dungeon_tag, dungeon, reward)
        # the Light Medallion has no dungeon: Gift from Rauru
        self.assertEqual(placed[Items.LIGHT_MEDALLION.value].name, Locations.GIFT_FROM_RAURU.value)


class TestPocketAnyStone(SohTestBase):
    options = {"shuffle_dungeon_rewards": ShuffleDungeonRewards.option_anywhere,
               "start_with_links_pocket": StartWithLinksPocket.option_dungeon_reward,
               "links_pocket_reward": LinksPocketReward.option_any_stone}

    def test_pocket_has_a_stone(self):
        pocket = self.multiworld.get_location(Locations.LINKS_POCKET.value, self.player)
        self.assertIn(pocket.item.name, STONES)


class TestPocketLightMedallion(SohTestBase):
    options = {"shuffle_dungeon_rewards": ShuffleDungeonRewards.option_end_of_dungeons,
               "links_pocket_reward": LinksPocketReward.option_light_medallion}

    def test_pocket_has_light(self):
        pocket = self.multiworld.get_location(Locations.LINKS_POCKET.value, self.player)
        self.assertEqual(pocket.item.name, Items.LIGHT_MEDALLION.value)
