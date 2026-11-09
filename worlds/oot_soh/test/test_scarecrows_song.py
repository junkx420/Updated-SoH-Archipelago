"""Shuffle Scarecrow's Song from SoH 9.3.1 (3drando/item_pool.cpp, logic.cpp ScarecrowsSong, feature 3.8)."""
from BaseClasses import CollectionState

from .bases import SohTestBase
from ..Enums import Items, Locations, Regions
from ..Items import item_data_table
from ..Locations import location_data_table
from ..LogicHelpers import scarecrows_song


def pool_count(test: SohTestBase, item: Items) -> int:
    return sum(1 for i in test.multiworld.itempool if i.player == test.player and i.name == item.value)


def player_locations(test: SohTestBase) -> set[str]:
    return {loc.name for loc in test.multiworld.get_locations(test.player)}


class TestScarecrowsSongOff(SohTestBase):
    def test_default(self):
        self.assertTrue(self.world.options.skip_scarecrows_song)
        self.assertEqual(pool_count(self, Items.SCARECROWS_SONG), 0)
        self.assertNotIn(Locations.LH_SCARECROWS_SONG.value, player_locations(self))
        self.assertEqual(item_data_table[Items.SCARECROWS_SONG].item_id, 285)
        self.assertEqual(location_data_table[Locations.LH_SCARECROWS_SONG].loc_id, 3028)


class TestScarecrowsSongShuffled(SohTestBase):
    options = {"shuffle_scarecrows_song": True}

    def test_skip_turned_off(self):
        # decision 2026-11-09: Shuffle Scarecrow's Song wins over Skip Scarecrow's Song (on by default)
        self.assertFalse(self.world.options.skip_scarecrows_song)

    def test_item_and_location(self):
        self.assertEqual(pool_count(self, Items.SCARECROWS_SONG), 1)
        self.assertIn(Locations.LH_SCARECROWS_SONG.value, player_locations(self))

    def test_song_needs_the_item(self):
        # logic.cpp ScarecrowsSong: the Pierre events don't count with the song shuffled
        self.collect_all_but([Items.SCARECROWS_SONG.value])
        rule = scarecrows_song((Regions.ROOT, self.world)).resolve(self.world)
        self.assertFalse(rule(self.multiworld.state))
        self.collect_by_name([Items.SCARECROWS_SONG.value])
        self.assertTrue(rule(self.multiworld.state))

    def test_location_reachable_without_the_song(self):
        # lake_hylia.cpp: RC_LH_SCARECROWS_SONG needs only the child and adult scarecrow events
        self.collect_all_but([Items.SCARECROWS_SONG.value])
        self.assertTrue(self.can_reach_location(Locations.LH_SCARECROWS_SONG.value))


class TestScarecrowsSongVanilla(SohTestBase):
    options = {"skip_scarecrows_song": False}

    def test_events_count(self):
        self.collect_all_but([])
        rule = scarecrows_song((Regions.ROOT, self.world)).resolve(self.world)
        self.assertTrue(rule(self.multiworld.state))
        self.assertFalse(rule(CollectionState(self.multiworld)))
