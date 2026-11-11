"""Presets follow the SoH 9.3.1 rando presets (soh/assets/custom/presets/Rando Seed Settings - *.json).
The option checks are the ones of test/webhost/test_option_presets.py, which needs flask, for this world only."""
import unittest

from BaseClasses import PlandoOptions
from Options import NumericOption, OptionCounter, OptionList, OptionSet, Visibility

from .. import SohWorld
from .bases import SohTestBase
from ..Enums import Tricks
from ..Options import LEGACY_TRICKS
from ..Presets import oot_soh_options_presets


class TestPresets(unittest.TestCase):
    def test_options_valid(self):
        for preset_name, preset in oot_soh_options_presets.items():
            for option_name, value in preset.items():
                with self.subTest(preset=preset_name, option=option_name):
                    option = SohWorld.options_dataclass.type_hints[option_name].from_any(value)
                    option.verify(SohWorld, "Test Player", PlandoOptions(sum(PlandoOptions)))
                    self.assertTrue(Visibility.complex_ui in option.visibility
                                    or Visibility.simple_ui in option.visibility)
                    self.assertTrue(isinstance(option, (NumericOption, OptionSet, OptionList, OptionCounter)))
                    self.assertFalse(str(value).startswith("random-"))

    def test_presets(self):
        self.assertEqual(["Ship Default", "Ship Beginner", "Ship Standard", "Ship Advanced", "Ship Hell Mode",
                          "Ship Demise Difficulty"], list(oot_soh_options_presets))
        for name in ("Ship Beginner", "Ship Standard", "Ship Advanced", "Ship Hell Mode", "Ship Demise Difficulty"):
            preset = oot_soh_options_presets[name]
            # 9.3.1: Shuffle Masks instead of Complete Mask Quest, no Kakariko Gate setting any more
            self.assertTrue(preset["shuffle_masks"], name)
            self.assertFalse(preset["complete_mask_quest"], name)
            self.assertEqual(preset["kakariko_gate"], 0, name)
        for name in ("Ship Beginner", "Ship Standard", "Ship Advanced", "Ship Hell Mode"):
            self.assertEqual(oot_soh_options_presets[name]["closed_forest"], 2, name)  # ClosedForest "Off"
        self.assertTrue(oot_soh_options_presets["Ship Beginner"]["start_with_bunny_hood"])

    def test_demise_tricks(self):
        # 201 tricks upstream, the 42 Master Quest ones don't exist in the apworld
        tricks = oot_soh_options_presets["Ship Demise Difficulty"]["tricks_in_logic"]
        self.assertEqual(159, len(tricks))
        valid = {str(t) for t in Tricks if t not in LEGACY_TRICKS}
        self.assertTrue(set(tricks) <= valid)


class TestFreestandingInDungeons(SohTestBase):
    """dodongos_cavern.cpp lists RC_DODONGOS_CAVERN_LOWER_LIZALFOS_HEART twice in RR_DODONGOS_CAVERN_UPPER_LIZALFOS;
    with dungeon freestanding items shuffled that used to fail with a duplicate entrance (Hell Mode / Demise presets)."""
    options = {"shuffle_freestanding_items": "all"}

    def test_lavafall_heart_from_both_rooms(self):
        location = self.world.get_location("Dodongos Cavern Lower Lizalfos Room Lavafall Heart")
        self.assertEqual("Dodongos Cavern Lower Lizalfos Room Lavafall Heart (shared access)", location.parent_region.name)
        sources = [e.parent_region.name for e in location.parent_region.entrances]
        self.assertEqual(sorted(sources), ["Dodongos Cavern Lower Lizalfos", "Dodongos Cavern Upper Lizalfos"])
