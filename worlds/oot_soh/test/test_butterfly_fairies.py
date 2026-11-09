"""Shuffle Butterfly Fairies from SoH 9.3.1 (ShuffleFairies.cpp, feature 3.2)."""
from .bases import SohTestBase
from ..Enums import Items, Locations
from ..Locations import fairies_butterfly_location_table

BUTTERFLY = [str(loc) for loc in fairies_butterfly_location_table]


def player_locations(test: SohTestBase) -> set[str]:
    return {loc.name for loc in test.multiworld.get_locations(test.player)}


class TestButterflyFairiesOff(SohTestBase):
    def test_no_locations(self):
        self.assertFalse(set(BUTTERFLY) & player_locations(self))


class TestButterflyFairiesOn(SohTestBase):
    options = {"shuffle_butterfly_fairies": True}

    def test_locations(self):
        self.assertEqual(len(BUTTERFLY), 20)
        self.assertTrue(set(BUTTERFLY) <= player_locations(self))
        ids = [fairies_butterfly_location_table[loc].loc_id for loc in fairies_butterfly_location_table]
        self.assertEqual(ids, list(range(2463, 2483)))


class TestButterflyFairiesNeedSticks(SohTestBase):
    options = {"shuffle_butterfly_fairies": True, "shuffle_deku_stick_bag": True}

    def test_need_sticks(self):
        # all of them: logic->CanUse(RG_STICKS) (castle_grounds.cpp, zoras_river.cpp, ...)
        self.collect_all_but([Items.DEKU_STICK_BAG.value, Items.PROGRESSIVE_STICK_CAPACITY.value])
        self.assertFalse(self.can_reach_location(Locations.HC_NEAR_WALL_BUTTERFLY_FAIRY.value))
        self.collect_all_but([])
        for location in BUTTERFLY:
            self.assertTrue(self.can_reach_location(location), location)
