"""Kakariko Gate / Skip Child Zelda after SoH 9.3.1 (feature 1.5).

The client maps them like upstream ConfigVersion7Updater (SeedContext.cpp ParseArchipelagoOptions):
Skip Child Zelda -> start with Zelda's Letter + Weird Egg "Skip Waking Talon"; Kakariko Gate open -> start with
Zelda's Letter. An unshuffled starting letter skips child Zelda (savefile.cpp gives Song from Impa and HC Zelda's
Letter at the start), so those checks are in logic from the start.
"""
from BaseClasses import CollectionState

from .bases import SohTestBase
from ..Enums import Locations, Events


class ZeldaBase(SohTestBase):
    __test__ = False

    def reachable_from_start(self, location: Locations) -> bool:
        state = CollectionState(self.multiworld)
        return self.multiworld.get_location(location.value, self.player).can_reach(state)


class TestSkipChildZelda(ZeldaBase):
    __test__ = True
    options = {"skip_child_zelda": True}

    def test_start_checks(self):
        self.assertTrue(self.reachable_from_start(Locations.SONG_FROM_IMPA))
        # letter and egg are starting items here, so their locations aren't part of the multiworld (#255)
        names = [location.name for location in self.multiworld.get_locations(self.player)]
        self.assertNotIn(Locations.HC_ZELDAS_LETTER.value, names)
        self.assertNotIn(Locations.HC_MALON_EGG.value, names)


class TestGateOpenNoSkip(ZeldaBase):
    __test__ = True
    options = {"skip_child_zelda": False, "kakariko_gate": "open", "shuffle_weird_egg": True}

    def test_start_checks(self):
        self.assertTrue(self.reachable_from_start(Locations.SONG_FROM_IMPA))
        self.assertTrue(self.reachable_from_start(Locations.HC_ZELDAS_LETTER))


class TestGateClosedNoSkip(ZeldaBase):
    __test__ = True
    options = {"skip_child_zelda": False, "kakariko_gate": "closed", "shuffle_weird_egg": True}

    def test_zelda_needs_egg(self):
        self.assertFalse(self.reachable_from_start(Locations.SONG_FROM_IMPA))
        self.assertFalse(self.reachable_from_start(Locations.HC_ZELDAS_LETTER))


class TestSkipWakingTalonOnly(ZeldaBase):
    # 9.3.1 Weird Egg "Skip Waking Talon" without Skip Child Zelda: Talon and Malon are back at the ranch from the
    # start, the Malon egg check is done; Zelda still has to be met
    __test__ = True
    options = {"skip_child_zelda": False, "kakariko_gate": "closed", "shuffle_weird_egg": "skip_waking_talon"}

    def test_talon_skipped(self):
        self.assertTrue(self.reachable_from_start(Locations.HC_MALON_EGG))
        self.assertFalse(self.reachable_from_start(Locations.SONG_FROM_IMPA))


class TestSkipChildZeldaSetsEgg(ZeldaBase):
    __test__ = True
    options = {"skip_child_zelda": True, "shuffle_weird_egg": True}

    def test_egg_option(self):
        from ..Options import ShuffleWeirdEgg
        self.assertEqual(self.world.options.shuffle_weird_egg.value, ShuffleWeirdEgg.option_skip_waking_talon)
