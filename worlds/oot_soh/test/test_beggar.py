"""Shuffle Beggar from SoH 9.3.1 (ShuffleBeggar.cpp, feature 3.1)."""
from .bases import SohTestBase
from ..Enums import Items, Locations
from ..Locations import beggar_location_table

BEGGAR = [str(loc) for loc in beggar_location_table]


def player_locations(test: SohTestBase) -> set[str]:
    return {loc.name for loc in test.multiworld.get_locations(test.player)}


class TestBeggarOff(SohTestBase):
    def test_no_locations(self):
        self.assertFalse(set(BEGGAR) & player_locations(self))


class TestBeggarOn(SohTestBase):
    options = {"shuffle_beggar": True}

    def test_locations(self):
        self.assertTrue(set(BEGGAR) <= player_locations(self))
        ids = [beggar_location_table[loc].loc_id for loc in beggar_location_table]
        self.assertEqual(ids, list(range(2457, 2463)))

    def test_market_needs_bottle_content(self):
        # market.cpp: IsChild && AtDay && CanUse(RG_BOTTLE_WITH_BUGS)
        bottles = [item.value for item in Items if item.value.startswith("Bottle") or item.value == "Empty Bottle"]
        self.collect_all_but(bottles)
        self.assertFalse(self.can_reach_location(Locations.MARKET_BEGGAR_BUGS.value))
        self.assertFalse(self.can_reach_location(Locations.KAK_BEGGAR_BLUE_FIRE.value))
        self.collect_all_but([])
        for location in BEGGAR:
            self.assertTrue(self.can_reach_location(location), location)
