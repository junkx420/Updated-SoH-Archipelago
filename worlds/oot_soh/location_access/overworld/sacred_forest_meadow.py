"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/sacred_forest_meadow.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    SFM_ENTRYWAY_OPEN_SFM_GATE = "SFM Entryway Open Sfm Gate"
    SFM_ABOVE_MAZE_FAIRY_ACCESS = "SFM Above Maze Fairy Access"
    SACRED_FOREST_MEADOW_FAIRY_ACCESS = "Sacred Forest Meadow Fairy Access"
    SFM_FAIRY_GROTTO_FAIRY_ACCESS = "SFM Fairy Grotto Fairy Access"


def set_region_rules(world: "SohWorld") -> None:

    # SFM Entryway  (upstream RR_SFM_ENTRYWAY, SCENE_SACRED_FOREST_MEADOW)
    # Events
    add_events(Regions.SFM_ENTRYWAY, world, [
        (EventLocations.SFM_ENTRYWAY_OPEN_SFM_GATE, Events.OPEN_SFM_GATE,
         lambda bundle: is_child(bundle) & can_kill_enemy(bundle, Enemies.WOLFOS)),
    ])
    # Locations
    add_locations(Regions.SFM_ENTRYWAY, world, [
        (Locations.SFM_WONDER_ENTRANCE,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.SFM_ENTRYWAY, world, [
        (Regions.LW_BEYOND_MIDO,
         lambda bundle: True_()),
        (Regions.SACRED_FOREST_MEADOW,
         lambda bundle: is_adult(bundle) | has_item(Events.OPEN_SFM_GATE, bundle)),
        (Regions.SFM_WOLFOS_GROTTO,
         lambda bundle: can_open_bomb_grotto(bundle)),
    ])

    # SFM Above Maze  (upstream RR_SFM_ABOVE_MAZE, SCENE_SACRED_FOREST_MEADOW)
    # Events
    add_events(Regions.SFM_ABOVE_MAZE, world, [
        (EventLocations.SFM_ABOVE_MAZE_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
    ])
    # Locations
    add_locations(Regions.SFM_ABOVE_MAZE, world, [
        (Locations.SFM_GS,
         lambda bundle: is_adult(bundle) & hookshot_or_boomerang(bundle) & can_get_nighttime_gs(bundle)),
        (Locations.SFM_MAZE_LOWER_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
        (Locations.SFM_MAZE_LOWER_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.SFM_MAZE_UPPER_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
        (Locations.SFM_MAZE_UPPER_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_SFM_MAZE_LOWER_GOSSIP_STONE: true
        # DEFERRED RC_SFM_MAZE_UPPER_GOSSIP_STONE: true
    ])
    # Connections
    connect_regions(Regions.SFM_ABOVE_MAZE, world, [
        (Regions.SFM_ENTRYWAY,
         lambda bundle: True_()),
        (Regions.SFM_OUTSIDE_FAIRY_GROTTO,
         lambda bundle: True_()),
        (Regions.SACRED_FOREST_MEADOW,
         lambda bundle: True_()),
    ])

    # Sacred Forest Meadow  (upstream RR_SACRED_FOREST_MEADOW, SCENE_SACRED_FOREST_MEADOW)
    # Events
    add_events(Regions.SACRED_FOREST_MEADOW, world, [
        (EventLocations.SACRED_FOREST_MEADOW_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
    ])
    # Locations
    add_locations(Regions.SACRED_FOREST_MEADOW, world, [
        (Locations.SONG_FROM_SARIA,
         lambda bundle: is_child(bundle) & has_item(Events.MET_ZELDA, bundle)),
        (Locations.SHEIK_IN_FOREST,
         lambda bundle: is_adult(bundle)),
        (Locations.SFM_SARIA_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
        (Locations.SFM_SARIA_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_SFM_SARIA_GOSSIP_STONE: true
        (Locations.SFM_WONDER_MAZE_1,
         lambda bundle: True_()),
        (Locations.SFM_WONDER_MAZE_2,
         lambda bundle: True_()),
        (Locations.SFM_WONDER_MAZE_3,
         lambda bundle: True_()),
        (Locations.SFM_WONDER_MAZE_4,
         lambda bundle: True_()),
        (Locations.SFM_WONDER_MAZE_5,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.SACRED_FOREST_MEADOW, world, [
        (Regions.FOREST_TEMPLE_ENTRYWAY,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
        (Regions.SFM_ENTRYWAY,
         lambda bundle: is_adult(bundle) | has_item(Events.OPEN_SFM_GATE, bundle)),
        (Regions.SFM_ABOVE_MAZE,
         lambda bundle: can_climb_ladder(bundle) | (is_adult(bundle) & (can_ground_jump(bundle) | (can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & bunny_hood(bundle))))),
        (Regions.SFM_STORMS_GROTTO,
         lambda bundle: can_open_storms_grotto(bundle)),
    ])

    # SFM Outside Fairy Grotto  (upstream RR_SFM_OUTSIDE_FAIRY_GROTTO, SCENE_SACRED_FOREST_MEADOW)
    # Connections
    connect_regions(Regions.SFM_OUTSIDE_FAIRY_GROTTO, world, [
        (Regions.SFM_FAIRY_GROTTO,
         lambda bundle: True_()),
        (Regions.SFM_ABOVE_MAZE,
         lambda bundle: can_climb_ladder(bundle)),
    ])

    # SFM Fairy Grotto  (upstream RR_SFM_FAIRY_GROTTO, SCENE_GROTTOS)
    # Events
    add_events(Regions.SFM_FAIRY_GROTTO, world, [
        (EventLocations.SFM_FAIRY_GROTTO_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: True_()),
    ])
    # Locations
    add_locations(Regions.SFM_FAIRY_GROTTO, world, [
        (Locations.SFM_FAIRY_GROTTO_FAIRY1,
         lambda bundle: True_()),
        (Locations.SFM_FAIRY_GROTTO_FAIRY2,
         lambda bundle: True_()),
        (Locations.SFM_FAIRY_GROTTO_FAIRY3,
         lambda bundle: True_()),
        (Locations.SFM_FAIRY_GROTTO_FAIRY4,
         lambda bundle: True_()),
        (Locations.SFM_FAIRY_GROTTO_FAIRY5,
         lambda bundle: True_()),
        (Locations.SFM_FAIRY_GROTTO_FAIRY6,
         lambda bundle: True_()),
        (Locations.SFM_FAIRY_GROTTO_FAIRY7,
         lambda bundle: True_()),
        (Locations.SFM_FAIRY_GROTTO_FAIRY8,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.SFM_FAIRY_GROTTO, world, [
        (Regions.SFM_OUTSIDE_FAIRY_GROTTO,
         lambda bundle: True_()),
    ])

    # SFM Wolfos Grotto  (upstream RR_SFM_WOLFOS_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.SFM_WOLFOS_GROTTO, world, [
        (Locations.SFM_WOLFOS_GROTTO_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.WOLFOS, EnemyDistance.CLOSE, True, 2) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.SFM_WOLFOS_GROTTO, world, [
        (Regions.SFM_ENTRYWAY,
         lambda bundle: True_()),
    ])

    # SFM Storms Grotto  (upstream RR_SFM_STORMS_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.SFM_STORMS_GROTTO, world, [
        (Locations.SFM_DEKU_SCRUB_GROTTO_REAR,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.SFM_DEKU_SCRUB_GROTTO_REAR, bundle)),
        (Locations.SFM_DEKU_SCRUB_GROTTO_FRONT,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.SFM_DEKU_SCRUB_GROTTO_FRONT, bundle)),
        (Locations.SFM_DEKU_SCRUB_GROTTO_BEEHIVE,
         lambda bundle: can_break_upper_beehives(bundle)),
    ])
    # Connections
    connect_regions(Regions.SFM_STORMS_GROTTO, world, [
        (Regions.SACRED_FOREST_MEADOW,
         lambda bundle: True_()),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_FAIRIES', 'MET_ZELDA', 'OPEN_SFM_GATE']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (3): ['RC_SFM_MAZE_LOWER_GOSSIP_STONE', 'RC_SFM_MAZE_UPPER_GOSSIP_STONE', 'RC_SFM_SARIA_GOSSIP_STONE']
