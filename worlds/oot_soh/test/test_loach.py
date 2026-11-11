"""Hyrule Loach: Fishsanity "Shuffle only Hyrule Loach", pond count 16/17, loach hint (feature 3.13)."""
from .bases import SohTestBase
from ..Enums import Locations
from ..Locations import location_data_table

POND_LOACHES = [Locations.LH_CHILD_POND_LOACH1, Locations.LH_CHILD_POND_LOACH2, Locations.LH_ADULT_POND_LOACH]


def player_locations(test: SohTestBase) -> set[str]:
    return {loc.name for loc in test.multiworld.get_locations(test.player)}


class TestLoachDefaultOff(SohTestBase):
    def test_none(self):
        locs = player_locations(self)
        self.assertNotIn(Locations.LH_HYRULE_LOACH_REWARD.value, locs)
        for loc in POND_LOACHES:
            self.assertNotIn(loc.value, locs)


class TestLoachOnly(SohTestBase):
    options = {"shuffle_fish": "hyrule_loach", "hyrule_loach_hint": True, "shuffle_fishing_pole": True}

    def test_only_reward(self):
        locs = player_locations(self)
        self.assertIn(Locations.LH_HYRULE_LOACH_REWARD.value, locs)
        self.assertEqual(2362, location_data_table[Locations.LH_HYRULE_LOACH_REWARD].loc_id)
        self.assertFalse([l for l in locs if "Pond Fish" in l or "Pond Loach" in l])
        self.assertTrue(self.world.options.hyrule_loach_hint.value)

    def test_needs_pole_and_hylian(self):
        self.collect_all_but(["Fishing Pole"])
        self.assertFalse(self.can_reach_location(Locations.LH_HYRULE_LOACH_REWARD.value))
        self.collect_all_but([])
        self.assertTrue(self.can_reach_location(Locations.LH_HYRULE_LOACH_REWARD.value))


class TestLoachHintNeedsLoachMode(SohTestBase):
    options = {"shuffle_fish": "pond", "hyrule_loach_hint": True}

    def test_hint_off(self):
        self.assertFalse(self.world.options.hyrule_loach_hint.value)
        self.assertNotIn(Locations.LH_HYRULE_LOACH_REWARD.value, player_locations(self))


class TestPondCount17(SohTestBase):
    options = {"shuffle_fish": "pond", "fishsanity_pond_count": 17, "fishsanity_age_split": True}

    def test_loaches(self):
        locs = player_locations(self)
        for loc in POND_LOACHES:
            self.assertIn(loc.value, locs)
        self.assertEqual([2360, 2361, 2378], [location_data_table[l].loc_id for l in POND_LOACHES])


class TestPondCount16NoSplit(SohTestBase):
    options = {"shuffle_fish": "all", "fishsanity_pond_count": 16, "fishsanity_age_split": False}

    def test_only_child_loach_1(self):
        locs = player_locations(self)
        self.assertIn(Locations.LH_CHILD_POND_LOACH1.value, locs)
        self.assertNotIn(Locations.LH_CHILD_POND_LOACH2.value, locs)
        self.assertNotIn(Locations.LH_ADULT_POND_LOACH.value, locs)
