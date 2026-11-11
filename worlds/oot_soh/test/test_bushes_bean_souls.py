"""Shuffle Bushes and Shuffle Bean Souls from SoH 9.3.1 (ShuffleTrees.cpp bushes, feature 3.12)."""
from .bases import SohTestBase
from ..Enums import Items, Locations
from ..ItemPool import BEAN_SOULS
from ..Locations import bushes_location_table

BUSHES = [str(loc) for loc in bushes_location_table]


def player_locations(test: SohTestBase) -> set[str]:
    return {loc.name for loc in test.multiworld.get_locations(test.player)}


def count_items(test: SohTestBase, item: Items) -> int:
    return sum(1 for i in test.multiworld.itempool if i.player == test.player and i.name == item.value)


class TestBushesOff(SohTestBase):
    def test_no_locations(self):
        self.assertFalse(set(BUSHES) & player_locations(self))


class TestBushesOn(SohTestBase):
    options = {"shuffle_bushes": True}

    def test_locations_and_ids(self):
        self.assertEqual(64, len(BUSHES))
        self.assertTrue(set(BUSHES) <= player_locations(self))
        ids = sorted(data.loc_id for data in bushes_location_table.values())
        self.assertEqual(ids, list(range(3030, 3094)))

    def test_child_only_bushes(self):
        # hyrule_field.cpp: the "Child" bushes need IsChild, zoras_fountain.cpp: all ZF bushes need IsChild
        self.collect_all_but([])
        for name in (Locations.HF_CHILD_NORTHERN_BUSH_1, Locations.ZF_BUSH_1, Locations.HF_BUSH_NEAR_LAKE_1):
            self.assertTrue(self.can_reach_location(name.value), name)


class TestBeanSoulsOff(SohTestBase):
    def test_no_souls(self):
        for soul in BEAN_SOULS:
            self.assertEqual(0, count_items(self, soul))

    def test_beans_plant_without_souls(self):
        self.collect_all_but([Items.MAGIC_BEAN_PACK.value, Items.MAGIC_BEAN.value])
        self.assertTrue(self.can_reach_location(Locations.KF_GS_BEAN_PATCH.value))


class TestBeanSoulsOn(SohTestBase):
    options = {"shuffle_bean_souls": True}

    def test_ten_souls(self):
        self.assertEqual(10, len(BEAN_SOULS))
        for soul in BEAN_SOULS:
            self.assertEqual(1, count_items(self, soul))
        self.assertEqual(list(range(286, 296)), [self.world.item_name_to_id[s.value] for s in BEAN_SOULS])

    def test_soul_needed_for_soil_skulltula(self):
        self.collect_all_but([Items.KOKIRI_FOREST_BEAN_SOUL.value])
        self.assertFalse(self.can_reach_location(Locations.KF_GS_BEAN_PATCH.value))
        self.collect(self.world.create_item(Items.KOKIRI_FOREST_BEAN_SOUL))
        self.assertTrue(self.can_reach_location(Locations.KF_GS_BEAN_PATCH.value))
