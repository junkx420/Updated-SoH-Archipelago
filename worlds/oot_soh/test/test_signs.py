"""Shuffle Signs from SoH 9.3.1 (ShuffleSigns.cpp, feature 3.3)."""
from .bases import SohTestBase
from ..Locations import signs_overworld_location_table, signs_dungeon_location_table

OVERWORLD = {str(loc) for loc in signs_overworld_location_table}
DUNGEON = {str(loc) for loc in signs_dungeon_location_table}


def player_locations(test: SohTestBase) -> set[str]:
    return {loc.name for loc in test.multiworld.get_locations(test.player)}


class TestSignsOff(SohTestBase):
    def test_no_locations(self):
        self.assertFalse((OVERWORLD | DUNGEON) & player_locations(self))


class TestSignsIds(SohTestBase):
    def test_new_ids(self):
        self.assertEqual(len(OVERWORLD), 74)
        self.assertEqual(len(DUNGEON), 5)
        ids = [data.loc_id for data in signs_overworld_location_table.values()] + \
              [data.loc_id for data in signs_dungeon_location_table.values()]
        self.assertEqual(ids, list(range(2483, 2562)))


class TestSignsOverworld(SohTestBase):
    options = {"shuffle_signs": "overworld"}

    def test_locations(self):
        locations = player_locations(self)
        self.assertTrue(OVERWORLD <= locations)
        self.assertFalse(DUNGEON & locations)


class TestSignsDungeon(SohTestBase):
    options = {"shuffle_signs": "dungeon"}

    def test_locations(self):
        locations = player_locations(self)
        self.assertTrue(DUNGEON <= locations)
        self.assertFalse(OVERWORLD & locations)


class TestSignsAll(SohTestBase):
    options = {"shuffle_signs": "all"}

    def test_all_reachable(self):
        # logic.cpp CanRead is always true; only region access matters
        self.collect_all_but([])
        for location in OVERWORLD | DUNGEON:
            self.assertTrue(self.can_reach_location(location), location)
