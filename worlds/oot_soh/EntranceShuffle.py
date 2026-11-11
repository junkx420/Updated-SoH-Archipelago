"""Dungeon and grotto entrance shuffle (SoH 9.3.1 RSK_SHUFFLE_DUNGEON_ENTRANCES / RSK_SHUFFLE_GROTTO_ENTRANCES,
soh/soh/Enhancements/randomizer/entrance.cpp).

Pools: EntranceType::Dungeon (+ EntranceType::GanonDungeon with "On + Ganon") and EntranceType::GrottoGrave, each
coupled (no decoupled or mixed pools). Like upstream (ShuffleAllEntrances) the pools are shuffled one after the
other, dungeons first; a pool is drawn again until the world validates, with the pools before it already fixed.
Like upstream (entrance.cpp ChangeConnections), every entrance keeps its own rule and only its target changes:
the entrance outside slot A leads into dungeon B, and B's exit leads back out to A's return region.
Blue warps follow the "Determine blue warp targets" block of EntranceShuffler::ShuffleAllEntrances.

Upstream places the entrances one by one with an assumed search after each placement (ShuffleEntrancePool,
ValidateWorld); the only check that applies with dungeon entrances alone is that all locations stay reachable
(allLocationsReachable). Here a whole permutation is drawn and checked with all items of the world, and redrawn
if a location can't be reached. Not ported: the extra sphere-0 checks ValidateWorld makes for Closed Forest "On"
with grotto shuffle (starting area, time passing and Temple of Time without items); upstream assumes both ages from
the start there, the apworld only gets adult Link through time travel (decision 2026-11-11).
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

# Upstream's rules leave fewer valid placements than one might think (e.g. Jabu Jabu's entrance needs child Link with a
# fish, so no adult-only dungeon fits there). Measured over 30 seeds: up to 29 draws with "On", up to 79 with
# "On + Ganon" and adult start; one draw costs about 30 ms, so 2000 makes a failure practically impossible.
MAX_ATTEMPTS = 2000

# entrance.cpp SetAllEntrancesData, EntranceType::GrottoGrave (in this order): 33 grottos and the 4 graves.
# Generated from the upstream table; name = apworld name of the grotto region.
GROTTO_ENTRANCES: list[DungeonEntrance] = [
    DungeonEntrance("Colossus Grotto", Regions.DESERT_COLOSSUS, Regions.COLOSSUS_GROTTO, Regions.DESERT_COLOSSUS, None, None),
    DungeonEntrance("LH Grotto", Regions.LAKE_HYLIA, Regions.LH_GROTTO, Regions.LAKE_HYLIA, None, None),
    DungeonEntrance("ZR Storms Grotto", Regions.ZORAS_RIVER, Regions.ZR_STORMS_GROTTO, Regions.ZORAS_RIVER, None, None),
    DungeonEntrance("ZR Fairy Grotto", Regions.ZR_ATOP_LADDER, Regions.ZR_FAIRY_GROTTO, Regions.ZR_ATOP_LADDER, None, None),
    DungeonEntrance("ZR Open Grotto", Regions.ZR_ATOP_LADDER, Regions.ZR_OPEN_GROTTO, Regions.ZR_ATOP_LADDER, None, None),
    DungeonEntrance("DMC Scrub Grotto", Regions.DMC_POT_GROTTO_EXIT, Regions.DMC_SCRUB_GROTTO, Regions.DMC_POT_GROTTO_ENTRY, None, None),
    DungeonEntrance("DMC Upper Grotto", Regions.DMC_ROCK_GROTTO, Regions.DMC_UPPER_GROTTO, Regions.DMC_ROCKS_GROTTO_ENTRY, None, None),
    DungeonEntrance("GC Grotto", Regions.GC_GROTTO_PLATFORM, Regions.GC_GROTTO, Regions.GC_GROTTO_PLATFORM, None, None),
    DungeonEntrance("DMT Storms Grotto", Regions.DEATH_MOUNTAIN_TRAIL, Regions.DMT_STORMS_GROTTO, Regions.DEATH_MOUNTAIN_TRAIL, None, None),
    DungeonEntrance("DMT Cow Grotto", Regions.DEATH_MOUNTAIN_ROCKFALL, Regions.DMT_COW_GROTTO, Regions.DEATH_MOUNTAIN_ROCKFALL, None, None),
    DungeonEntrance("Kak Open Grotto", Regions.KAK_BACKYARD, Regions.KAK_OPEN_GROTTO, Regions.KAK_BACKYARD, None, None),
    DungeonEntrance("Kak Redead Grotto", Regions.KAKARIKO_VILLAGE, Regions.KAK_REDEAD_GROTTO, Regions.KAKARIKO_VILLAGE, None, None),
    DungeonEntrance("HC Storms Grotto", Regions.HC_MOAT, Regions.HC_STORMS_GROTTO, Regions.CASTLE_GROUNDS_FROM_GROTTO, None, None),
    DungeonEntrance("HF Tektite Grotto", Regions.HYRULE_FIELD, Regions.HF_TEKTITE_GROTTO, Regions.HYRULE_FIELD, None, None),
    DungeonEntrance("HF Near Kak Grotto", Regions.HYRULE_FIELD, Regions.HF_NEAR_KAK_GROTTO, Regions.HYRULE_FIELD, None, None),
    DungeonEntrance("HF Fairy Grotto", Regions.HYRULE_FIELD, Regions.HF_FAIRY_GROTTO, Regions.HYRULE_FIELD, None, None),
    DungeonEntrance("HF Near Market Grotto", Regions.HYRULE_FIELD, Regions.HF_NEAR_MARKET_GROTTO, Regions.HYRULE_FIELD, None, None),
    DungeonEntrance("HF Cow Grotto", Regions.HYRULE_FIELD, Regions.HF_COW_GROTTO, Regions.HYRULE_FIELD, None, None),
    DungeonEntrance("HF Inside Fence Grotto", Regions.HYRULE_FIELD, Regions.HF_INSIDE_FENCE_GROTTO, Regions.HYRULE_FIELD, None, None),
    DungeonEntrance("HF Open Grotto", Regions.HYRULE_FIELD, Regions.HF_OPEN_GROTTO, Regions.HYRULE_FIELD, None, None),
    DungeonEntrance("HF Southeast Grotto", Regions.HYRULE_FIELD, Regions.HF_SOUTHEAST_GROTTO, Regions.HYRULE_FIELD, None, None),
    DungeonEntrance("LLR Grotto", Regions.LON_LON_RANCH, Regions.LLR_GROTTO, Regions.LON_LON_RANCH, None, None),
    DungeonEntrance("SFM Wolfos Grotto", Regions.SFM_ENTRYWAY, Regions.SFM_WOLFOS_GROTTO, Regions.SFM_ENTRYWAY, None, None),
    DungeonEntrance("SFM Storms Grotto", Regions.SACRED_FOREST_MEADOW, Regions.SFM_STORMS_GROTTO, Regions.SACRED_FOREST_MEADOW, None, None),
    DungeonEntrance("SFM Fairy Grotto", Regions.SFM_OUTSIDE_FAIRY_GROTTO, Regions.SFM_FAIRY_GROTTO, Regions.SFM_OUTSIDE_FAIRY_GROTTO, None, None),
    DungeonEntrance("LW Scrubs Grotto", Regions.LW_BEYOND_MIDO, Regions.LW_SCRUBS_GROTTO, Regions.LW_BEYOND_MIDO, None, None),
    DungeonEntrance("LW Near Shortcuts Grotto", Regions.THE_LOST_WOODS, Regions.LW_NEAR_SHORTCUTS_GROTTO, Regions.THE_LOST_WOODS, None, None),
    DungeonEntrance("KF Storms Grotto", Regions.KF_OUTSIDE_LOST_WOODS, Regions.KF_STORMS_GROTTO, Regions.KF_OUTSIDE_LOST_WOODS, None, None),
    DungeonEntrance("ZD Storms Grotto", Regions.ZORAS_DOMAIN_ISLAND, Regions.ZD_STORMS_GROTTO, Regions.ZORAS_DOMAIN_ISLAND, None, None),
    DungeonEntrance("GF Storms Grotto", Regions.GF_NEAR_GROTTO, Regions.GF_STORMS_GROTTO, Regions.GF_NEAR_GROTTO, None, None),
    DungeonEntrance("GV Storms Grotto", Regions.GV_FORTRESS_SIDE, Regions.GV_STORMS_GROTTO, Regions.GV_FORTRESS_SIDE, None, None),
    DungeonEntrance("GV Octorok Grotto", Regions.GV_GROTTO_LEDGE, Regions.GV_OCTOROK_GROTTO, Regions.GV_GROTTO_LEDGE, None, None),
    DungeonEntrance("Deku Theater", Regions.LW_BEYOND_MIDO, Regions.DEKU_THEATER, Regions.LW_BEYOND_MIDO, None, None),
    DungeonEntrance("Graveyard Shield Grave", Regions.THE_GRAVEYARD, Regions.GRAVEYARD_SHIELD_GRAVE, Regions.THE_GRAVEYARD, None, None),
    DungeonEntrance("Graveyard Heart Piece Grave", Regions.THE_GRAVEYARD, Regions.GRAVEYARD_HEART_PIECE_GRAVE, Regions.THE_GRAVEYARD, None, None),
    DungeonEntrance("Graveyard Composers Grave", Regions.THE_GRAVEYARD, Regions.GRAVEYARD_COMPOSERS_GRAVE, Regions.THE_GRAVEYARD, None, None),
    DungeonEntrance("Graveyard Dampes Grave", Regions.THE_GRAVEYARD, Regions.GRAVEYARD_DAMPES_GRAVE, Regions.THE_GRAVEYARD, None, None),
]


def dungeon_entrance_pool(world: "SohWorld") -> list[DungeonEntrance]:
    if world.options.shuffle_dungeon_entrances == ShuffleDungeonEntrances.option_off:
        return []
    pool = list(DUNGEON_ENTRANCES)
    if world.options.shuffle_dungeon_entrances == ShuffleDungeonEntrances.option_on_plus_ganon:
        pool.append(GANONS_CASTLE_ENTRANCE)
    return pool


def grotto_entrance_pool(world: "SohWorld") -> list[DungeonEntrance]:
    return list(GROTTO_ENTRANCES) if world.options.shuffle_grotto_entrances else []


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


class ShuffledPool:
    """Entrance objects of a pool, collected once from the vanilla graph."""

    def __init__(self, world: "SohWorld", pool: list[DungeonEntrance]):
        self.world = world
        self.pool = pool
        self.forward = [find_exit(world, d.outside, d.entryway) for d in pool]
        self.reverse = [find_exit(world, d.entryway, d.exit_to) for d in pool]
        self.blue_warp = [find_exit(world, d.boss_room, d.blue_warp_to) if d.boss_room else None for d in pool]

    def apply(self, placement: list[int]) -> None:
        """placement[slot] = index of the entry (dungeon, grotto) behind the entrance of slot"""
        region = self.world.get_region
        for slot, placed_index in enumerate(placement):
            self_slot, placed = self.pool[slot], self.pool[placed_index]
            reconnect(self.forward[slot], region(str(placed.entryway)))
            reconnect(self.reverse[placed_index], region(str(self_slot.exit_to)))
            if self.blue_warp[placed_index] is not None:
                # bossRoomExitPairs: the blue warp of the placed dungeon goes to the blue warp target of the slot
                # (dungeonExits); slots without one (BotW, Ice Cavern, GTG) send it to the slot's exit
                reconnect(self.blue_warp[placed_index], region(str(self_slot.blue_warp_to or self_slot.exit_to)))


def all_locations_reachable(world: "SohWorld") -> bool:
    state = world.get_pre_fill_state()
    locations = [loc for loc in world.multiworld.get_locations(world.player) if loc.address is not None]
    return (all(loc.can_reach(state) for loc in locations)
            and world.multiworld.completion_condition[world.player](state))


def shuffle_pool(world: "SohWorld", pool: list[DungeonEntrance], passthrough_key: str, what: str) -> dict[str, str]:
    """Shuffles one coupled pool and returns slot name -> placed name."""
    if not pool:
        return {}
    shuffled = ShuffledPool(world, pool)
    index = {d.name: i for i, d in enumerate(pool)}

    if getattr(world, "using_ut", False):
        # Universal Tracker: rebuild the placement of the generated seed
        placed = world.passthrough.get(passthrough_key, {})
        shuffled.apply([index[placed.get(d.name, d.name)] for d in pool])
        return dict(placed)

    for _ in range(MAX_ATTEMPTS):
        placement = list(range(len(pool)))
        world.random.shuffle(placement)
        shuffled.apply(placement)
        if all_locations_reachable(world):
            result = {pool[slot].name: pool[placed].name for slot, placed in enumerate(placement)}
            for slot, placed in result.items():
                world.multiworld.spoiler.set_entrance(f"{slot} Entrance", placed, "both", world.player)
            return result
    raise OptionError(f"Ship of Harkinian (player {world.player}): no valid {what} entrance placement found in "
                      f"{MAX_ATTEMPTS} attempts")


def shuffle_entrances(world: "SohWorld") -> None:
    world.dungeon_entrance_placement = shuffle_pool(world, dungeon_entrance_pool(world),
                                                    "dungeon_entrance_placement", "dungeon")
    world.grotto_entrance_placement = shuffle_pool(world, grotto_entrance_pool(world),
                                                   "grotto_entrance_placement", "grotto")


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


def entrance_hint_data(world: "SohWorld") -> dict[int, str]:
    """Archipelago hint info (World.extend_hint_information): locations of a moved dungeon or grotto get the entrance
    they are behind now, e.g. "Dodongo's Cavern Entrance". Grotto locations are found by their region."""
    dungeon_by_tag = {DUNGEON_TAGS[placed]: f"{slot} Entrance"
                      for slot, placed in world.dungeon_entrance_placement.items() if slot != placed}
    region_of = {d.name: str(d.entryway) for d in GROTTO_ENTRANCES}
    grotto_by_region = {region_of[placed]: f"{slot} Entrance"
                        for slot, placed in world.grotto_entrance_placement.items() if slot != placed}
    hints = {}
    for location in world.multiworld.get_locations(world.player):
        if location.address is None:
            continue
        data = location_data_table.get(location.name)
        if data is not None and data.dungeon_tag in dungeon_by_tag:
            hints[location.address] = dungeon_by_tag[data.dungeon_tag]
        elif location.parent_region is not None and location.parent_region.name in grotto_by_region:
            hints[location.address] = grotto_by_region[location.parent_region.name]
    return hints


def entrance_slot_data(placement: dict[str, str], pool: list[DungeonEntrance]) -> list[dict[str, str]]:
    """Coupled pairs for the client, as upstream region keys (the apworld region members are named after them): the
    forward entrance of each slot (outside -> entryway) is replaced by the forward entrance of the entry placed there
    (upstream Entrance::GetReplacement); the client derives the reverse and blue warps like upstream does."""
    by_name = {d.name: d for d in pool}
    return [{"from": f"RR_{by_name[slot].outside.name}", "to": f"RR_{by_name[slot].entryway.name}",
             "replacement_from": f"RR_{by_name[placed].outside.name}",
             "replacement_to": f"RR_{by_name[placed].entryway.name}"}
            for slot, placed in placement.items()]


def dungeon_entrance_slot_data(world: "SohWorld") -> list[dict[str, str]]:
    return entrance_slot_data(world.dungeon_entrance_placement, DUNGEON_ENTRANCES + [GANONS_CASTLE_ENTRANCE])


def grotto_entrance_slot_data(world: "SohWorld") -> list[dict[str, str]]:
    return entrance_slot_data(world.grotto_entrance_placement, GROTTO_ENTRANCES)
