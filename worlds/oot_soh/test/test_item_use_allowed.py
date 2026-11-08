"""Per-scene item restrictions, cases taken from upstream SoH 9.3.1 logic.cpp Logic::ItemUseAllowed / Logic::BAllowed."""
import unittest

from ..Enums import Items, Regions
from ..LogicHelpers import item_use_allowed, b_allowed, mask_use_allowed
from ..RegionScenes import REGION_SCENE


class TestItemUseAllowed(unittest.TestCase):
    def test_scene_table(self):
        self.assertEqual(REGION_SCENE[Regions.KF_LINKS_HOUSE], "SCENE_LINKS_HOUSE")
        self.assertEqual(REGION_SCENE[Regions.ROOT], "SCENE_ID_MAX")

    def test_swords(self):
        # BAllowed: no B button in houses and shops
        self.assertFalse(b_allowed(Regions.KF_LINKS_HOUSE))
        self.assertFalse(item_use_allowed(Items.KOKIRI_SWORD, Regions.KF_LINKS_HOUSE))
        self.assertTrue(item_use_allowed(Items.KOKIRI_SWORD, Regions.KOKIRI_FOREST))
        self.assertFalse(item_use_allowed(Items.MASTER_SWORD, Regions.LH_LAB_UNDERWATER))

    def test_always_allowed(self):
        for item in (Items.IRON_BOOTS, Items.HOVER_BOOTS, Items.ZELDAS_LULLABY, Items.GOLDEN_GAUNTLETS):
            self.assertTrue(item_use_allowed(item, Regions.KF_LINKS_HOUSE), item)

    def test_dungeons_allow_everything(self):
        for item in (Items.FARORES_WIND, Items.BOMB_BAG, Items.HOOKSHOT, Items.STICKS):
            self.assertTrue(item_use_allowed(item, Regions.DEKU_TREE_LOBBY), item)

    def test_overworld_no_farores_wind(self):
        self.assertFalse(item_use_allowed(Items.FARORES_WIND, Regions.KOKIRI_FOREST))
        self.assertTrue(item_use_allowed(Items.DINS_FIRE, Regions.KOKIRI_FOREST))

    def test_houses(self):
        # only bottles, masks, trade items and ocarinas
        self.assertFalse(item_use_allowed(Items.BOMB_BAG, Regions.KF_LINKS_HOUSE))
        self.assertFalse(item_use_allowed(Items.STICKS, Regions.KF_LINKS_HOUSE))
        self.assertTrue(item_use_allowed(Items.EMPTY_BOTTLE, Regions.KF_LINKS_HOUSE))
        self.assertTrue(item_use_allowed(Items.FAIRY_OCARINA, Regions.KF_LINKS_HOUSE))

    def test_underwater_lab(self):
        self.assertTrue(item_use_allowed(Items.HOOKSHOT, Regions.LH_LAB_UNDERWATER))
        self.assertFalse(item_use_allowed(Items.BOMB_BAG, Regions.LH_LAB_UNDERWATER))
        self.assertFalse(mask_use_allowed(Regions.LH_LAB_UNDERWATER))
