"""Shuffle Rocks and Shuffle Boulders from SoH 9.3.1 (ShuffleRocks.cpp, feature 3.6)."""
from .bases import SohTestBase
from ..Locations import rocks_location_table, boulders_overworld_location_table, boulders_dungeon_location_table

ROCKS = {str(loc) for loc in rocks_location_table}
BOULDERS_OVERWORLD = {str(loc) for loc in boulders_overworld_location_table}
BOULDERS_DUNGEON = {str(loc) for loc in boulders_dungeon_location_table}


def player_locations(test: SohTestBase) -> set[str]:
    return {loc.name for loc in test.multiworld.get_locations(test.player)}


class TestRocksBouldersOff(SohTestBase):
    def test_no_locations(self):
        self.assertFalse((ROCKS | BOULDERS_OVERWORLD | BOULDERS_DUNGEON) & player_locations(self))

    def test_new_ids(self):
        self.assertEqual(len(ROCKS), 121)
        self.assertEqual(len(BOULDERS_OVERWORLD), 113)
        self.assertEqual(len(BOULDERS_DUNGEON), 6)
        self.assertEqual([d.loc_id for d in rocks_location_table.values()], list(range(2788, 2909)))
        boulder_ids = sorted(d.loc_id for d in list(boulders_overworld_location_table.values())
                             + list(boulders_dungeon_location_table.values()))
        self.assertEqual(boulder_ids, list(range(2909, 3028)))


class TestRocksOnly(SohTestBase):
    options = {"shuffle_rocks": True}

    def test_locations(self):
        locations = player_locations(self)
        self.assertTrue(ROCKS <= locations)
        self.assertFalse((BOULDERS_OVERWORLD | BOULDERS_DUNGEON) & locations)


class TestBouldersDungeon(SohTestBase):
    options = {"shuffle_boulders": "dungeon"}

    def test_locations(self):
        locations = player_locations(self)
        self.assertTrue(BOULDERS_DUNGEON <= locations)
        self.assertFalse((BOULDERS_OVERWORLD | ROCKS) & locations)


class TestRocksBouldersAll(SohTestBase):
    options = {"shuffle_rocks": True, "shuffle_boulders": "all"}

    def test_all_reachable(self):
        self.collect_all_but([])
        for location in ROCKS | BOULDERS_OVERWORLD | BOULDERS_DUNGEON:
            self.assertTrue(self.can_reach_location(location), location)
