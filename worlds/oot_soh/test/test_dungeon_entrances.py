"""Dungeon entrance shuffle (SoH 9.3.1 RSK_SHUFFLE_DUNGEON_ENTRANCES, entrance.cpp; feature 4.1)."""
from .bases import SohTestBase
from ..Enums import Regions
from ..EntranceShuffle import (DUNGEON_ENTRANCES, GANONS_CASTLE_ENTRANCE, find_exit, dungeon_entrance_slot_data,
                               entrance_hint_data)


def target(test: SohTestBase, entrance) -> str:
    return entrance.connected_region.name


class TestDungeonEntrancesOff(SohTestBase):
    def test_vanilla(self):
        self.assertEqual({}, self.world.dungeon_entrance_placement)
        self.assertEqual([], dungeon_entrance_slot_data(self.world))
        for d in DUNGEON_ENTRANCES:
            find_exit(self.world, d.outside, d.entryway)  # still connected as in vanilla


class DungeonShuffleChecks:
    pool: list
    multiworld: object
    world: object

    def placement(self) -> dict[str, str]:
        return self.world.dungeon_entrance_placement

    def test_placement_is_permutation(self):
        names = [d.name for d in self.pool]
        self.assertEqual(sorted(names), sorted(self.placement()))
        self.assertEqual(sorted(names), sorted(self.placement().values()))

    def test_coupled_connections(self):
        by_name = {d.name: d for d in self.pool}
        region = self.world.get_region
        for slot, dungeon in self.placement().items():
            s, d = by_name[slot], by_name[dungeon]
            # the entrance outside the slot leads into the placed dungeon ...
            forward = [e for e in region(str(s.outside)).exits if e.name == f"{s.outside} -> {s.entryway}"]
            self.assertEqual(1, len(forward), slot)
            self.assertEqual(str(d.entryway), forward[0].connected_region.name, slot)
            # ... and leaving that dungeon puts you back outside the slot
            reverse = [e for e in region(str(d.entryway)).exits if e.name == f"{d.entryway} -> {d.exit_to}"]
            self.assertEqual(1, len(reverse), dungeon)
            self.assertEqual(str(s.exit_to), reverse[0].connected_region.name, dungeon)
            # blue warp: the slot's blue warp target, or its exit for slots without one (entrance.cpp dungeonExits)
            if d.boss_room is not None:
                warp = [e for e in region(str(d.boss_room)).exits if e.name == f"{d.boss_room} -> {d.blue_warp_to}"]
                self.assertEqual(1, len(warp), dungeon)
                self.assertEqual(str(s.blue_warp_to or s.exit_to), warp[0].connected_region.name, dungeon)

    def test_slot_data(self):
        pairs = dungeon_entrance_slot_data(self.world)
        self.assertEqual(len(self.pool), len(pairs))
        for pair in pairs:
            for key in ("from", "to", "replacement_from", "replacement_to"):
                self.assertTrue(pair[key].startswith("RR_"), pair)

    def test_hints_name_the_entrance(self):
        hints = entrance_hint_data(self.world)
        moved = {dungeon for slot, dungeon in self.placement().items() if slot != dungeon}
        if moved:
            self.assertTrue(hints)
        for text in hints.values():
            self.assertTrue(text.endswith(" Entrance"))


class TestDungeonEntrancesOn(DungeonShuffleChecks, SohTestBase):
    options = {"shuffle_dungeon_entrances": "on"}
    pool = DUNGEON_ENTRANCES

    def test_ganons_castle_stays(self):
        find_exit(self.world, Regions.GANONS_CASTLE_LEDGE, Regions.GANONS_CASTLE_ENTRYWAY)


class TestDungeonEntrancesOnPlusGanon(DungeonShuffleChecks, SohTestBase):
    options = {"shuffle_dungeon_entrances": "on_plus_ganon"}
    pool = DUNGEON_ENTRANCES + [GANONS_CASTLE_ENTRANCE]


class TestDungeonEntrancesAdultStart(DungeonShuffleChecks, SohTestBase):
    options = {"shuffle_dungeon_entrances": "on_plus_ganon", "starting_age": "adult"}
    pool = DUNGEON_ENTRANCES + [GANONS_CASTLE_ENTRANCE]
