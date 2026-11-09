"""Shuffle Wonder Items from SoH 9.3.1 (ShuffleWonderItems.cpp, feature 3.4)."""
from .bases import SohTestBase
from ..Locations import wonder_items_overworld_location_table, wonder_items_dungeon_location_table

OVERWORLD = {str(loc) for loc in wonder_items_overworld_location_table}
DUNGEON = {str(loc) for loc in wonder_items_dungeon_location_table}


def player_locations(test: SohTestBase) -> set[str]:
    return {loc.name for loc in test.multiworld.get_locations(test.player)}


class TestWonderItemsOff(SohTestBase):
    def test_no_locations(self):
        self.assertFalse((OVERWORLD | DUNGEON) & player_locations(self))

    def test_new_ids(self):
        self.assertEqual(len(OVERWORLD), 115)
        self.assertEqual(len(DUNGEON), 4)
        ids = sorted(data.loc_id for data in list(wonder_items_overworld_location_table.values())
                     + list(wonder_items_dungeon_location_table.values()))
        self.assertEqual(ids, list(range(2562, 2681)))


class TestWonderItemsOverworld(SohTestBase):
    options = {"shuffle_wonder_items": "overworld"}

    def test_locations(self):
        locations = player_locations(self)
        self.assertTrue(OVERWORLD <= locations)
        self.assertFalse(DUNGEON & locations)


class TestWonderItemsDungeon(SohTestBase):
    options = {"shuffle_wonder_items": "dungeon"}

    def test_locations(self):
        locations = player_locations(self)
        self.assertTrue(DUNGEON <= locations)
        self.assertFalse(OVERWORLD & locations)


class TestWonderItemsAll(SohTestBase):
    options = {"shuffle_wonder_items": "all"}

    def test_all_reachable(self):
        self.collect_all_but([])
        for location in OVERWORLD | DUNGEON:
            self.assertTrue(self.can_reach_location(location), location)

    def test_kokiri_training_from_the_start(self):
        # kokiri_forest.cpp: RC_KF_WONDER_TRAINING_1 needs only logic->IsChild (child start)
        self.assertTrue(self.can_reach_location("KF Wonder Training 1"))
