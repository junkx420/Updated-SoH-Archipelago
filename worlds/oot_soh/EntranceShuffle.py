"""Dungeon entrance shuffle (SoH 9.3.1 RSK_SHUFFLE_DUNGEON_ENTRANCES, soh/soh/Enhancements/randomizer/entrance.cpp).

Pool: EntranceType::Dungeon (+ EntranceType::GanonDungeon with "On + Ganon"), coupled (no decoupled entrances).
Like upstream (entrance.cpp ChangeConnections), every entrance keeps its own rule and only its target changes:
the entrance outside slot A leads into dungeon B, and B's exit leads back out to A's return region.
Blue warps follow the "Determine blue warp targets" block of EntranceShuffler::ShuffleAllEntrances.

Upstream places the entrances one by one with an assumed search after each placement (ShuffleEntrancePool,
ValidateWorld); the only check that applies with dungeon entrances alone is that all locations stay reachable
(allLocationsReachable). Here a whole permutation is drawn and checked with all items of the world, and redrawn
if a location can't be reached.
"""
from typing import NamedTuple, TYPE_CHECKING

from BaseClasses import Entrance, Region
from Options import OptionError
from .Enums import Regions, DungeonLocations
from .Locations import location_data_table
from .Options import ShuffleDungeonEntrances

if TYPE_CHECKING:
    from . import SohWorld


class DungeonEntrance(NamedTuple):
    name: str               # dungeon name, also used in the slot data
    outside: Regions        # region with the entrance (upstream parent region of the forward entrance)
    entryway: Regions       # first region of the dungeon
    exit_to: Regions        # where leaving the dungeon puts you (connected region of the reverse entrance)
    boss_room: Regions | None
    blue_warp_to: Regions | None  # vanilla blue warp landing of this dungeon's boss room


# entrance.cpp SetAllEntrancesData, EntranceType::Dungeon and EntranceType::GanonDungeon (in this order), with the
# EntranceType::BlueWarp entries of the same dungeons
DUNGEON_ENTRANCES: list[DungeonEntrance] = [
    DungeonEntrance("Deku Tree", Regions.KF_OUTSIDE_DEKU_TREE, Regions.DEKU_TREE_ENTRYWAY, Regions.KF_OUTSIDE_DEKU_TREE,
                    Regions.DEKU_TREE_BOSS_ROOM, Regions.KF_OUTSIDE_DEKU_TREE),
    DungeonEntrance("Dodongo's Cavern", Regions.DEATH_MOUNTAIN_TRAIL, Regions.DODONGOS_CAVERN_ENTRYWAY,
                    Regions.DEATH_MOUNTAIN_TRAIL, Regions.DODONGOS_CAVERN_BOSS_ROOM, Regions.DEATH_MOUNTAIN_TRAIL),
    DungeonEntrance("Jabu Jabu's Belly", Regions.ZORAS_FOUNTAIN, Regions.JABU_JABUS_BELLY_ENTRYWAY,
                    Regions.ZORAS_FOUNTAIN, Regions.JABU_JABUS_BELLY_BOSS_ROOM, Regions.ZORAS_FOUNTAIN),
    DungeonEntrance("Forest Temple", Regions.SACRED_FOREST_MEADOW, Regions.FOREST_TEMPLE_ENTRYWAY,
                    Regions.SACRED_FOREST_MEADOW, Regions.FOREST_TEMPLE_BOSS_ROOM, Regions.SACRED_FOREST_MEADOW),
    DungeonEntrance("Fire Temple", Regions.DMC_TEMPLE_EXIT, Regions.FIRE_TEMPLE_ENTRYWAY, Regions.DMC_TEMPLE_ENTRY,
                    Regions.FIRE_TEMPLE_BOSS_ROOM, Regions.DMC_PAD_ENTRY),
    DungeonEntrance("Water Temple", Regions.LH_FROM_WATER_TEMPLE, Regions.WATER_TEMPLE_ENTRYWAY,
                    Regions.LH_FROM_WATER_TEMPLE, Regions.WATER_TEMPLE_BOSS_ROOM, Regions.LAKE_HYLIA),
    DungeonEntrance("Spirit Temple", Regions.DESERT_COLOSSUS, Regions.SPIRIT_TEMPLE_ENTRYWAY,
                    Regions.DESERT_COLOSSUS_OUTSIDE_TEMPLE, Regions.SPIRIT_TEMPLE_BOSS_ROOM, Regions.DESERT_COLOSSUS),
    DungeonEntrance("Shadow Temple", Regions.GRAVEYARD_WARP_PAD_REGION, Regions.SHADOW_TEMPLE_ENTRYWAY,
                    Regions.GRAVEYARD_WARP_PAD_REGION, Regions.SHADOW_TEMPLE_BOSS_ROOM,
                    Regions.GRAVEYARD_WARP_PAD_REGION),
    DungeonEntrance("Bottom of the Well", Regions.KAK_WELL, Regions.BOTW_ENTRYWAY, Regions.KAK_WELL, None, None),
    DungeonEntrance("Ice Cavern", Regions.ZF_LEDGE, Regions.ICE_CAVERN_ENTRYWAY, Regions.ZF_LEDGE, None, None),
    DungeonEntrance("Gerudo Training Ground", Regions.GF_TO_GTG, Regions.GERUDO_TRAINING_GROUND_ENTRYWAY,
                    Regions.GF_EXITING_GTG, None, None),
]
# EntranceType::GanonDungeon. Its blue warp entry (Ganon's Tower Stairs 1 -> Castle Grounds) only gets a game override
# with Shuffle Ganon's Tower Entrance (entrance.cpp CreateEntranceOverrides), so in game it stays vanilla; the apworld
# keeps it vanilla too instead of following upstream's logic-only reconnection.
GANONS_CASTLE_ENTRANCE = DungeonEntrance(
    "Ganon's Castle", Regions.GANONS_CASTLE_LEDGE, Regions.GANONS_CASTLE_ENTRYWAY,
    Regions.CASTLE_GROUNDS_FROM_GANONS_CASTLE, None, Regions.CASTLE_GROUNDS_FROM_GANONS_CASTLE)

MAX_ATTEMPTS = 100


def dungeon_entrance_pool(world: "SohWorld") -> list[DungeonEntrance]:
    pool = list(DUNGEON_ENTRANCES)
    if world.options.shuffle_dungeon_entrances == ShuffleDungeonEntrances.option_on_plus_ganon:
        pool.append(GANONS_CASTLE_ENTRANCE)
    return pool


def find_exit(world: "SohWorld", parent: Regions, target: Regions) -> Entrance:
    region: Region = world.get_region(str(parent))
    exits = [e for e in region.exits if e.connected_region is not None and e.connected_region.name == str(target)]
    assert len(exits) == 1, f"expected one connection {parent} -> {target}, found {len(exits)}"
    return exits[0]


def reconnect(entrance: Entrance, region: Region) -> None:
    if entrance.connected_region is not None:
        entrance.connected_region.entrances.remove(entrance)
    entrance.connected_region = None
    entrance.connect(region)


class ShuffledDungeons:
    """Entrance objects of the pool, collected once from the vanilla graph."""

    def __init__(self, world: "SohWorld", pool: list[DungeonEntrance]):
        self.world = world
        self.pool = pool
        self.forward = [find_exit(world, d.outside, d.entryway) for d in pool]
        self.reverse = [find_exit(world, d.entryway, d.exit_to) for d in pool]
        self.blue_warp = [find_exit(world, d.boss_room, d.blue_warp_to) if d.boss_room else None for d in pool]

    def apply(self, placement: list[int]) -> None:
        """placement[slot] = index of the dungeon behind the entrance of slot"""
        region = self.world.get_region
        for slot, dungeon in enumerate(placement):
            self_slot, placed = self.pool[slot], self.pool[dungeon]
            reconnect(self.forward[slot], region(str(placed.entryway)))
            reconnect(self.reverse[dungeon], region(str(self_slot.exit_to)))
            if self.blue_warp[dungeon] is not None:
                # bossRoomExitPairs: the blue warp of the placed dungeon goes to the blue warp target of the slot
                # (dungeonExits); slots without one (BotW, Ice Cavern, GTG) send it to the slot's exit
                reconnect(self.blue_warp[dungeon], region(str(self_slot.blue_warp_to or self_slot.exit_to)))


def all_locations_reachable(world: "SohWorld") -> bool:
    state = world.get_pre_fill_state()
    locations = [loc for loc in world.multiworld.get_locations(world.player) if loc.address is not None]
    return (all(loc.can_reach(state) for loc in locations)
            and world.multiworld.completion_condition[world.player](state))


def shuffle_dungeon_entrances(world: "SohWorld") -> None:
    world.dungeon_entrance_placement = {}
    if world.options.shuffle_dungeon_entrances == ShuffleDungeonEntrances.option_off:
        return
    pool = dungeon_entrance_pool(world)
    dungeons = ShuffledDungeons(world, pool)
    index = {d.name: i for i, d in enumerate(pool)}

    if getattr(world, "using_ut", False):
        # Universal Tracker: rebuild the placement of the generated seed
        placed = world.passthrough.get("dungeon_entrance_placement", {})
        dungeons.apply([index[placed.get(d.name, d.name)] for d in pool])
        world.dungeon_entrance_placement = dict(placed)
        return

    for _ in range(MAX_ATTEMPTS):
        placement = list(range(len(pool)))
        world.random.shuffle(placement)
        dungeons.apply(placement)
        if all_locations_reachable(world):
            world.dungeon_entrance_placement = {pool[slot].name: pool[dungeon].name
                                                for slot, dungeon in enumerate(placement)}
            for slot, dungeon in world.dungeon_entrance_placement.items():
                world.multiworld.spoiler.set_entrance(f"{slot} Entrance", dungeon, "both", world.player)
            return
    raise OptionError(f"Ship of Harkinian (player {world.player}): no valid dungeon entrance placement found in "
                      f"{MAX_ATTEMPTS} attempts")


DUNGEON_TAGS: dict[str, DungeonLocations] = {
    "Deku Tree": DungeonLocations.DEKU_TREE,
    "Dodongo's Cavern": DungeonLocations.DODONGOS_CAVERN,
    "Jabu Jabu's Belly": DungeonLocations.JABU_JABUS_BELLY,
    "Forest Temple": DungeonLocations.FOREST_TEMPLE,
    "Fire Temple": DungeonLocations.FIRE_TEMPLE,
    "Water Temple": DungeonLocations.WATER_TEMPLE,
    "Spirit Temple": DungeonLocations.SPIRIT_TEMPLE,
    "Shadow Temple": DungeonLocations.SHADOW_TEMPLE,
    "Bottom of the Well": DungeonLocations.BOTTOM_OF_THE_WELL,
    "Ice Cavern": DungeonLocations.ICE_CAVERN,
    "Gerudo Training Ground": DungeonLocations.GERUDO_TRAINING_GROUNDS,
    "Ganon's Castle": DungeonLocations.GANONS_CASTLE,
}


def dungeon_entrance_hint_data(world: "SohWorld") -> dict[int, str]:
    """Archipelago hint info (World.extend_hint_information): locations of a moved dungeon get the entrance it is
    behind now, e.g. "Dodongo's Cavern Entrance"."""
    by_tag = {DUNGEON_TAGS[dungeon]: f"{slot} Entrance"
              for slot, dungeon in world.dungeon_entrance_placement.items() if slot != dungeon}
    hints = {}
    for location in world.multiworld.get_locations(world.player):
        data = location_data_table.get(location.name)
        if location.address is not None and data is not None and data.dungeon_tag in by_tag:
            hints[location.address] = by_tag[data.dungeon_tag]
    return hints


def dungeon_entrance_slot_data(world: "SohWorld") -> list[dict[str, str]]:
    """Coupled pairs for the client, as upstream region keys (the apworld region members are named after them): the
    forward entrance of each slot (outside -> entryway) is replaced by the forward entrance of the dungeon placed there
    (upstream Entrance::GetReplacement); the client derives the reverse and blue warps like upstream does."""
    by_name = {d.name: d for d in DUNGEON_ENTRANCES + [GANONS_CASTLE_ENTRANCE]}
    return [{"from": f"RR_{by_name[slot].outside.name}", "to": f"RR_{by_name[slot].entryway.name}",
             "replacement_from": f"RR_{by_name[dungeon].outside.name}",
             "replacement_to": f"RR_{by_name[dungeon].entryway.name}"}
            for slot, dungeon in world.dungeon_entrance_placement.items()]
