"""Trick options after the SoH 9.3.1 update (feature 1.3)."""
import unittest

from .bases import SohTestBase
from ..Enums import Tricks
from ..Options import LEGACY_TRICKS
from ..TrickNames import TRICK_SOH_NAMES


class TestTrickTables(unittest.TestCase):
    def test_every_trick_is_upstream_or_legacy(self):
        # TrickNames.py lists the tricks that exist in SoH 9.3.1 (generated from its sources)
        for trick in Tricks:
            self.assertTrue(trick.name in TRICK_SOH_NAMES or trick in LEGACY_TRICKS, trick.name)

    def test_legacy_redirects_point_to_upstream_tricks(self):
        for old, target in LEGACY_TRICKS.items():
            self.assertNotIn(old.name, TRICK_SOH_NAMES, old.name)
            if isinstance(target, Tricks):
                self.assertIn(target.name, TRICK_SOH_NAMES, target.name)

    def test_yaml_names_unique(self):
        values = [trick.value for trick in Tricks]
        self.assertEqual(len(values), len(set(values)))


class TestLegacyTricks(SohTestBase):
    options = {"tricks_in_logic": [Tricks.FOREST_OUTDOORS_LEDGE.value, Tricks.DC_JUMP.value,
                                   Tricks.RUSTED_SWITCHES.value, Tricks.LW_BRIDGE.value]}

    def test_redirect_and_slot_data(self):
        tricks = self.world.options.tricks_in_logic.value
        # 1:1 rename: the new trick is on
        self.assertIn(Tricks.FOREST_COURTYARD_LEDGE.value, tricks)
        # merged into a broader trick: not turned on
        self.assertNotIn(Tricks.UNINTUITIVE_JUMPS.value, tricks)
        # the client gets upstream enum names only, no legacy names
        self.assertEqual(self.world.slot_data_tricks(), ["RT_FOREST_COURTYARD_LEDGE", "RT_LW_BRIDGE"])
