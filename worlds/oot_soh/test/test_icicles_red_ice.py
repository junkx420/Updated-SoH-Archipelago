"""Shuffle Icicles and Shuffle Red Ice from SoH 9.3.1 (ShuffleIcicles.cpp, ShuffleRedIce.cpp, feature 3.5)."""
from .bases import SohTestBase
from ..Enums import Items, Locations
from ..Locations import icicle_location_table, red_ice_location_table

ICICLES = {str(loc) for loc in icicle_location_table}
RED_ICE = {str(loc) for loc in red_ice_location_table}


def player_locations(test: SohTestBase) -> set[str]:
    return {loc.name for loc in test.multiworld.get_locations(test.player)}


class TestIceOff(SohTestBase):
    def test_no_locations(self):
        self.assertFalse((ICICLES | RED_ICE) & player_locations(self))

    def test_new_ids(self):
        self.assertEqual(len(ICICLES), 90)
        self.assertEqual(len(RED_ICE), 17)
        self.assertEqual([d.loc_id for d in icicle_location_table.values()], list(range(2681, 2771)))
        self.assertEqual([d.loc_id for d in red_ice_location_table.values()], list(range(2771, 2788)))


class TestIciclesOnly(SohTestBase):
    options = {"shuffle_icicles": True}

    def test_locations(self):
        locations = player_locations(self)
        self.assertTrue(ICICLES <= locations)
        self.assertFalse(RED_ICE & locations)


class TestRedIce(SohTestBase):
    options = {"shuffle_red_ice": True, "shuffle_icicles": True}

    def test_all_reachable(self):
        self.collect_all_but([])
        for location in ICICLES | RED_ICE:
            self.assertTrue(self.can_reach_location(location), location)



class TestRedIceNeedsBlueFire(SohTestBase):
    # Blue Fire Arrows (on by default) would let ice arrows count as Blue Fire
    options = {"shuffle_red_ice": True, "blue_fire_arrows": False}

    def test_red_ice_needs_blue_fire(self):
        # ice_cavern.cpp: RC_ICE_CAVERN_ENTRANCE_RED_ICE needs logic->BlueFire()
        bottles = [item.value for item in Items if item.value.startswith("Bottle") or item.value == "Empty Bottle"]
        self.collect_all_but(bottles)
        self.assertFalse(self.can_reach_location(Locations.ICE_CAVERN_ENTRANCE_RED_ICE.value))
