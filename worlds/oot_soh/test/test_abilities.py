"""Abilities from SoH 9.3.1 (logic.cpp Logic::HasItem / Logic::CanUse for RG_CLIMB, RG_CRAWL, RG_OPEN_CHEST,
RG_POWER_BRACELET, RG_SPEAK_*; feature 3.11)."""
from .bases import SohTestBase
from ..Enums import Items, Regions


def reachable(test: SohTestBase, region: Regions, adult: bool) -> bool:
    state = test.multiworld.state
    state._soh_update_age_reachable_regions(test.player)  # type: ignore
    regions = state._soh_adult_reachable_regions if adult else state._soh_child_reachable_regions  # type: ignore
    return test.multiworld.get_region(region.value, test.player) in regions[test.player]


class TestCrawlNeedsChild(SohTestBase):
    """kokiri_forest.cpp: RR_KF_BOULDER_LOOP is entered with CanUse(RG_CRAWL) = HasItem(RG_CRAWL) && IsChild."""

    def test_only_child_crawls(self):
        self.collect_all_but([])
        self.assertTrue(reachable(self, Regions.KF_BOULDER_LOOP, adult=False))
        self.assertFalse(reachable(self, Regions.KF_BOULDER_LOOP, adult=True))
