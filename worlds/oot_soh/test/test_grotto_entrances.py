"""Grotto entrance shuffle (SoH 9.3.1 RSK_SHUFFLE_GROTTO_ENTRANCES, entrance.cpp EntranceType::GrottoGrave; 4.2)."""
from .bases import SohTestBase
from ..EntranceShuffle import GROTTO_ENTRANCES, find_exit, grotto_entrance_slot_data, entrance_hint_data


class TestGrottoEntrancesOff(SohTestBase):
    def test_vanilla(self):
        self.assertEqual({}, self.world.grotto_entrance_placement)
        self.assertEqual([], grotto_entrance_slot_data(self.world))
        for g in GROTTO_ENTRANCES:
            find_exit(self.world, g.outside, g.entryway)


class GrottoShuffleChecks:
    def test_table(self):
        self.assertEqual(37, len(GROTTO_ENTRANCES))  # 33 grottos + 4 graves

    def test_placement_is_permutation(self):
        names = sorted(g.name for g in GROTTO_ENTRANCES)
        placement = self.world.grotto_entrance_placement
        self.assertEqual(names, sorted(placement))
        self.assertEqual(names, sorted(placement.values()))
        self.assertTrue(any(slot != placed for slot, placed in placement.items()))

    def test_coupled_connections(self):
        by_name = {g.name: g for g in GROTTO_ENTRANCES}
        region = self.world.get_region
        for slot, placed in self.world.grotto_entrance_placement.items():
            s, g = by_name[slot], by_name[placed]
            forward = [e for e in region(str(s.outside)).exits if e.name == f"{s.outside} -> {s.entryway}"]
            self.assertEqual(1, len(forward), slot)
            self.assertEqual(str(g.entryway), forward[0].connected_region.name, slot)
            reverse = [e for e in region(str(g.entryway)).exits if e.name == f"{g.entryway} -> {g.exit_to}"]
            self.assertEqual(1, len(reverse), placed)
            self.assertEqual(str(s.exit_to), reverse[0].connected_region.name, placed)

    def test_slot_data(self):
        pairs = grotto_entrance_slot_data(self.world)
        self.assertEqual(37, len(pairs))
        self.assertTrue(all(p["from"].startswith("RR_") and p["replacement_to"].startswith("RR_") for p in pairs))

    def test_hints(self):
        hints = entrance_hint_data(self.world)
        self.assertTrue(hints)
        self.assertTrue(all(text.endswith(" Entrance") for text in hints.values()))


class TestGrottoEntrancesOn(GrottoShuffleChecks, SohTestBase):
    options = {"shuffle_grotto_entrances": True}


class TestGrottoEntrancesClosedForest(GrottoShuffleChecks, SohTestBase):
    options = {"shuffle_grotto_entrances": True, "closed_forest": "on"}


class TestGrottoAndDungeonEntrances(GrottoShuffleChecks, SohTestBase):
    options = {"shuffle_grotto_entrances": True, "shuffle_dungeon_entrances": "on_plus_ganon",
               "starting_age": "adult"}

    def test_both_pools_shuffled(self):
        self.assertEqual(12, len(self.world.dungeon_entrance_placement))
        self.assertEqual(37, len(self.world.grotto_entrance_placement))
