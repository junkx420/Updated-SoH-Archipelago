"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/dungeons/fire_temple.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    FIRE_TEMPLE_NEAR_BOSS_UPPER_FAIRY_ACCESS = "Fire Temple Near Boss Upper Fairy Access"
    FIRE_TEMPLE_LOOP_CAGE_SWITCH_FIRE_LOOP_SWITCH = "Fire Temple Loop Cage Switch Fire Loop Switch"
    FIRE_TEMPLE_SHORTCUT_CLIMB_FIRE_OPENED_UPPER_SHORTCUT = "Fire Temple Shortcut Climb Fire Opened Upper Shortcut"
    FIRE_TEMPLE_FIRE_MAZE_PLATFORMS_FIRE_HIT_PLATFORM = "Fire Temple Fire Maze Platforms Fire Hit Platform"
    FIRE_TEMPLE_TOP_OF_COLLAPSING_STAIRS_FIRE_HIT_STAIRS = "Fire Temple Top of Collapsing Stairs Fire Hit Stairs"
    FIRE_TEMPLE_TOP_OF_COLLAPSING_STAIRS_FIRE_CHILD_AT_TOP_OF_STAIRS = "Fire Temple Top of Collapsing Stairs Fire Child At Top Of Stairs"
    FIRE_TEMPLE_ABOVE_FIRE_MAZE_FIRE_HIT_ABOVE_MAZE_PLATFORM = "Fire Temple Above Fire Maze Fire Hit Above Maze Platform"
    FIRE_TEMPLE_BOSS_ROOM_FIRE_TEMPLE_CLEAR = "Fire Temple Boss Room Fire Temple Clear"


def set_region_rules(world: "SohWorld") -> None:

    # Fire Temple Entryway  (upstream RR_FIRE_TEMPLE_ENTRYWAY, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_ENTRYWAY, world, [
        (Regions.FIRE_TEMPLE_FOYER,
         lambda bundle: True_()),
        (Regions.DMC_TEMPLE_ENTRY,
         lambda bundle: True_()),
    ])

    # Fire Temple Foyer  (upstream RR_FIRE_TEMPLE_FOYER, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_FOYER, world, [
        (Regions.FIRE_TEMPLE_ENTRYWAY,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_NEAR_BOSS_ROOM,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_LOOP_HEXAGON_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)) & (small_keys_scene("SCENE_FIRE_TEMPLE", 8, bundle) | Not(is_fire_loop_locked(bundle)))),
        (Regions.FIRE_TEMPLE_LOOP_CAGE_FOYER_SIDE,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_BIG_LAVA_ROOM,
         lambda bundle: small_keys_scene("SCENE_FIRE_TEMPLE", 2, bundle)),
    ])

    # Fire Temple Near Boss Room  (upstream RR_FIRE_TEMPLE_NEAR_BOSS_ROOM, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_NEAR_BOSS_ROOM, world, [
        (Locations.FIRE_TEMPLE_NEAR_BOSS_CHEST,
         lambda bundle: fire_timer_at_least(bundle, 16) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_NEAR_BOSS_ROOM, world, [
        (Regions.FIRE_TEMPLE_FOYER,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_NEAR_BOSS_PILLAR,
         lambda bundle: fire_timer_at_least(bundle, 8) & has_item(Events.FIRE_HIT_PLATFORM, bundle)),
        (Regions.FIRE_TEMPLE_NEAR_BOSS_TARGET,
         lambda bundle: fire_timer_at_least(bundle, 16) & is_adult(bundle) & (can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle))),
        (Regions.FIRE_TEMPLE_NEAR_BOSS_DOOR,
         lambda bundle: fire_timer_at_least(bundle, 16) & (can_use(Items.HOVER_BOOTS, bundle) | (is_adult(bundle) & (can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) | bunny_hood(bundle))))),
    ])

    # Fire Temple Near Boss Pillar  (upstream RR_FIRE_TEMPLE_NEAR_BOSS_PILLAR, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_NEAR_BOSS_PILLAR, world, [
        (Regions.FIRE_TEMPLE_NEAR_BOSS_ROOM,
         lambda bundle: fire_timer_at_least(bundle, 8)),
        (Regions.FIRE_TEMPLE_NEAR_BOSS_TARGET,
         lambda bundle: fire_timer_at_least(bundle, 8) & can_use(Items.LONGSHOT, bundle)),
        (Regions.FIRE_TEMPLE_NEAR_BOSS_DOOR,
         lambda bundle: fire_timer_at_least(bundle, 8) & (is_adult(bundle) | bunny_hood(bundle) | can_use(Items.HOVER_BOOTS, bundle))),
    ])

    # Fire Temple Near Boss Door  (upstream RR_FIRE_TEMPLE_NEAR_BOSS_DOOR, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_NEAR_BOSS_DOOR, world, [
        (Regions.FIRE_TEMPLE_NEAR_BOSS_ROOM,
         lambda bundle: fire_timer_at_least(bundle, 8) & (is_adult(bundle) | can_use(Items.HOVER_BOOTS, bundle))),
        (Regions.FIRE_TEMPLE_NEAR_BOSS_PILLAR,
         lambda bundle: fire_timer_at_least(bundle, 8) & (is_adult(bundle) | can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle))),
        (Regions.FIRE_TEMPLE_NEAR_BOSS_TARGET,
         lambda bundle: fire_timer_at_least(bundle, 8) & (can_use(Items.HOVER_BOOTS, bundle) | can_use(Items.HOOKSHOT, bundle) | (is_adult(bundle) & bunny_hood(bundle)))),
        (Regions.FIRE_TEMPLE_BOSS_ENTRYWAY,
         lambda bundle: True_()),
    ])

    # Fire Temple Near Boss Target  (upstream RR_FIRE_TEMPLE_NEAR_BOSS_TARGET, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_NEAR_BOSS_TARGET, world, [
        (Regions.FIRE_TEMPLE_NEAR_BOSS_ROOM,
         lambda bundle: fire_timer_at_least(bundle, 8) & (is_adult(bundle) | bunny_hood(bundle)) & can_use(Items.HOVER_BOOTS, bundle)),
        (Regions.FIRE_TEMPLE_NEAR_BOSS_DOOR,
         lambda bundle: fire_timer_at_least(bundle, 8) & (can_use(Items.HOVER_BOOTS, bundle) | (is_adult(bundle) & bunny_hood(bundle)))),
        (Regions.FIRE_TEMPLE_NEAR_BOSS_UPPER,
         lambda bundle: fire_timer_at_least(bundle, 8) & is_adult(bundle)),
    ])

    # Fire Temple Near Boss Upper  (upstream RR_FIRE_TEMPLE_NEAR_BOSS_UPPER, SCENE_FIRE_TEMPLE)
    # Events
    add_events(Regions.FIRE_TEMPLE_NEAR_BOSS_UPPER, world, [
        (EventLocations.FIRE_TEMPLE_NEAR_BOSS_UPPER_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Locations
    add_locations(Regions.FIRE_TEMPLE_NEAR_BOSS_UPPER, world, [
        (Locations.FIRE_TEMPLE_NEAR_BOSS_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FIRE_TEMPLE_NEAR_BOSS_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FIRE_TEMPLE_NEAR_BOSS_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FIRE_TEMPLE_NEAR_BOSS_POT4,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_NEAR_BOSS_UPPER, world, [
        (Regions.FIRE_TEMPLE_NEAR_BOSS_ROOM,
         lambda bundle: fire_timer_at_least(bundle, 8)),
        (Regions.FIRE_TEMPLE_NEAR_BOSS_TARGET,
         lambda bundle: fire_timer_at_least(bundle, 8)),
    ])

    # Fire Temple Loop Hexagon Room  (upstream RR_FIRE_TEMPLE_LOOP_HEXAGON_ROOM, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_LOOP_HEXAGON_ROOM, world, [
        (Regions.FIRE_TEMPLE_FOYER,
         lambda bundle: small_keys_scene("SCENE_FIRE_TEMPLE", 8, bundle) | Not(is_fire_loop_locked(bundle))),
        (Regions.FIRE_TEMPLE_LOOP_5_TILE_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.TORCH_SLUG) & can_kill_enemy(bundle, Enemies.FIRE_KEESE))),
    ])

    # Fire Temple Loop 5 Tile Room  (upstream RR_FIRE_TEMPLE_LOOP_5_TILE_ROOM, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_LOOP_5_TILE_ROOM, world, [
        (Locations.FIRE_TEMPLE_GS_BOSS_KEY_LOOP,
         lambda bundle: can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.CLOSE)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_LOOP_5_TILE_ROOM, world, [
        (Regions.FIRE_TEMPLE_LOOP_HEXAGON_ROOM,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_LOOP_FLARE_DANCER,
         lambda bundle: True_()),
    ])

    # Fire Temple Loop Flare Dancer  (upstream RR_FIRE_TEMPLE_LOOP_FLARE_DANCER, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_LOOP_FLARE_DANCER, world, [
        (Locations.FIRE_TEMPLE_FLARE_DANCER_CHEST,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.FLARE_DANCER)) & (is_adult(bundle) | can_ground_jump(bundle) | can_use(Items.HOOKSHOT, bundle)) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_LOOP_FLARE_DANCER, world, [
        (Regions.FIRE_TEMPLE_LOOP_5_TILE_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.FLARE_DANCER))),
        (Regions.FIRE_TEMPLE_LOOP_CAGE_SWITCH,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.FLARE_DANCER))),
    ])

    # Fire Temple Loop Cage Switch  (upstream RR_FIRE_TEMPLE_LOOP_CAGE_SWITCH, SCENE_FIRE_TEMPLE)
    # Events
    add_events(Regions.FIRE_TEMPLE_LOOP_CAGE_SWITCH, world, [
        (EventLocations.FIRE_TEMPLE_LOOP_CAGE_SWITCH_FIRE_LOOP_SWITCH, Events.FIRE_LOOP_SWITCH,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_LOOP_CAGE_SWITCH, world, [
        (Regions.FIRE_TEMPLE_LOOP_FLARE_DANCER,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_LOOP_GORON_CAGE,
         lambda bundle: has_item(Events.FIRE_LOOP_SWITCH, bundle)),
    ])

    # Fire Temple Loop Goron Cage  (upstream RR_FIRE_TEMPLE_LOOP_GORON_CAGE, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_LOOP_GORON_CAGE, world, [
        (Locations.FIRE_TEMPLE_BOSS_KEY_CHEST,
         lambda bundle: can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_LOOP_GORON_CAGE, world, [
        (Regions.FIRE_TEMPLE_LOOP_CAGE_SWITCH,
         lambda bundle: has_item(Events.FIRE_LOOP_SWITCH, bundle)),
        (Regions.FIRE_TEMPLE_LOOP_CAGE_FOYER_SIDE,
         lambda bundle: has_item(Events.FIRE_LOOP_SWITCH, bundle)),
    ])

    # Fire Temple Cage Foyer Side  (upstream RR_FIRE_TEMPLE_LOOP_CAGE_FOYER_SIDE, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_LOOP_CAGE_FOYER_SIDE, world, [
        (Regions.FIRE_TEMPLE_FOYER,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_LOOP_GORON_CAGE,
         lambda bundle: has_item(Events.FIRE_LOOP_SWITCH, bundle)),
    ])

    # Fire Temple Big Lava Room  (upstream RR_FIRE_TEMPLE_BIG_LAVA_ROOM, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_BIG_LAVA_ROOM, world, [
        (Locations.FIRE_TEMPLE_BIG_LAVA_POT1,
         lambda bundle: can_break_pots(bundle) & fire_timer_at_least(bundle, 32)),
        (Locations.FIRE_TEMPLE_BIG_LAVA_POT2,
         lambda bundle: can_break_pots(bundle) & fire_timer_at_least(bundle, 32)),
        (Locations.FIRE_TEMPLE_BIG_LAVA_POT3,
         lambda bundle: can_break_pots(bundle) & fire_timer_at_least(bundle, 32)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_BIG_LAVA_ROOM, world, [
        (Regions.FIRE_TEMPLE_FOYER,
         lambda bundle: small_keys_scene("SCENE_FIRE_TEMPLE", 2, bundle) & fire_timer_at_least(bundle, 24)),
        (Regions.FIRE_TEMPLE_1F_CURVED_CAGE,
         lambda bundle: fire_timer_at_least(bundle, 24)),
        (Regions.FIRE_TEMPLE_8_TILE_ROOM,
         lambda bundle: is_adult(bundle) & fire_timer_at_least(bundle, 32) & (can_use(Items.SONG_OF_TIME, bundle) | can_do_trick(Tricks.FIRE_SOT, bundle))),
        (Regions.FIRE_TEMPLE_STRAIGHTFORWARD_CAGE,
         lambda bundle: (is_adult(bundle) & has_explosives(bundle) & fire_timer_at_least(bundle, 32)) | (can_ground_jump(bundle) & fire_timer_at_least(bundle, 40))),
        (Regions.FIRE_TEMPLE_LAVA_GEYSER_1F,
         lambda bundle: can_use(Items.GORON_TUNIC, bundle) & small_keys_scene("SCENE_FIRE_TEMPLE", 3, bundle)),
    ])

    # Fire Temple 1F Curved Cage  (upstream RR_FIRE_TEMPLE_1F_CURVED_CAGE, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_1F_CURVED_CAGE, world, [
        (Locations.FIRE_TEMPLE_BIG_LAVA_ROOM_LOWER_OPEN_DOOR_CHEST,
         lambda bundle: has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_1F_CURVED_CAGE, world, [
        (Regions.FIRE_TEMPLE_BIG_LAVA_ROOM,
         lambda bundle: True_()),
    ])

    # Fire Temple 8 Tile Room  (upstream RR_FIRE_TEMPLE_8_TILE_ROOM, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_8_TILE_ROOM, world, [
        (Locations.FIRE_TEMPLE_GS_SONG_OF_TIME_ROOM,
         lambda bundle: ((is_adult(bundle)) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.CLOSE) | (is_child(bundle)) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG)) | can_ground_jumpslash(bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_8_TILE_ROOM, world, [
        (Regions.FIRE_TEMPLE_BIG_LAVA_ROOM,
         lambda bundle: True_()),
    ])

    # Fire Temple Straightforward Cage  (upstream RR_FIRE_TEMPLE_STRAIGHTFORWARD_CAGE, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_STRAIGHTFORWARD_CAGE, world, [
        (Locations.FIRE_TEMPLE_BIG_LAVA_ROOM_BLOCKED_DOOR_CHEST,
         lambda bundle: has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_STRAIGHTFORWARD_CAGE, world, [
        (Regions.FIRE_TEMPLE_BIG_LAVA_ROOM,
         lambda bundle: True_()),
    ])

    # Fire Temple Lava Geyser 1F  (upstream RR_FIRE_TEMPLE_LAVA_GEYSER_1F, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_LAVA_GEYSER_1F, world, [
        (Regions.FIRE_TEMPLE_BIG_LAVA_ROOM,
         lambda bundle: small_keys_scene("SCENE_FIRE_TEMPLE", 3, bundle)),
        (Regions.FIRE_TEMPLE_LAVA_GEYSER_GRATE,
         lambda bundle: fire_timer_at_least(bundle, 40) & (has_climb(bundle) | can_use(Items.HOOKSHOT, bundle))),
        (Regions.FIRE_TEMPLE_LAVA_GEYSER_TORCH,
         lambda bundle: can_use(Items.LONGSHOT, bundle) & fire_timer_at_least(bundle, 40)),
    ])

    # Fire Temple Lava Geyser Grate  (upstream RR_FIRE_TEMPLE_LAVA_GEYSER_GRATE, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_LAVA_GEYSER_GRATE, world, [
        (Locations.FIRE_TEMPLE_FIRE_PILLAR_ROOM_LEFT_HEART,
         lambda bundle: True_()),
        (Locations.FIRE_TEMPLE_FIRE_PILLAR_ROOM_RIGHT_HEART,
         lambda bundle: True_()),
        (Locations.FIRE_TEMPLE_FIRE_PILLAR_ROOM_BACK_HEART,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_LAVA_GEYSER_GRATE, world, [
        (Regions.FIRE_TEMPLE_LAVA_GEYSER_1F,
         lambda bundle: take_damage(bundle)),
        (Regions.FIRE_TEMPLE_LAVA_GEYSER_2F,
         lambda bundle: fire_timer_at_least(bundle, 48) & has_grab(bundle)),
    ])

    # Fire Temple Lava Geyser Torch  (upstream RR_FIRE_TEMPLE_LAVA_GEYSER_TORCH, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_LAVA_GEYSER_TORCH, world, [
        (Regions.FIRE_TEMPLE_LAVA_GEYSER_1F,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_LAVA_GEYSER_GRATE,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
    ])

    # Fire Temple Lava Geyser 2F  (upstream RR_FIRE_TEMPLE_LAVA_GEYSER_2F, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_LAVA_GEYSER_2F, world, [
        (Regions.FIRE_TEMPLE_LAVA_GEYSER_TORCH,
         lambda bundle: take_damage(bundle) & fire_timer_at_least(bundle, 24)),
        (Regions.FIRE_TEMPLE_SHORTCUT_ROOM,
         lambda bundle: small_keys_scene("SCENE_FIRE_TEMPLE", 4, bundle)),
    ])

    # Fire Temple Shortcut Room  (upstream RR_FIRE_TEMPLE_SHORTCUT_ROOM, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_SHORTCUT_ROOM, world, [
        (Regions.FIRE_TEMPLE_LAVA_GEYSER_2F,
         lambda bundle: small_keys_scene("SCENE_FIRE_TEMPLE", 4, bundle)),
        (Regions.FIRE_TEMPLE_SHORTCUT_CLIMB,
         lambda bundle: has_item(Events.FIRE_OPENED_UPPER_SHORTCUT, bundle)),
        (Regions.FIRE_TEMPLE_SHORTCUT_ROOM_3F,
         lambda bundle: is_adult(bundle) & has_climb(bundle) & ((has_item(Items.GORONS_BRACELET, bundle) | can_do_trick(Tricks.FIRE_STRENGTH, bundle)) | can_ground_jump(bundle)) & can_hit_switch(bundle, EnemyDistance.BOMB_THROW)),
    ])

    # Fire Temple Shortcut Room 3F  (upstream RR_FIRE_TEMPLE_SHORTCUT_ROOM_3F, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_SHORTCUT_ROOM_3F, world, [
        (Regions.FIRE_TEMPLE_SHORTCUT_ROOM,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_BOULDER_MAZE_LOWER,
         lambda bundle: True_()),
    ])

    # Fire Temple Shortcut Climb  (upstream RR_FIRE_TEMPLE_SHORTCUT_CLIMB, SCENE_FIRE_TEMPLE)
    # Events
    add_events(Regions.FIRE_TEMPLE_SHORTCUT_CLIMB, world, [
        (EventLocations.FIRE_TEMPLE_SHORTCUT_CLIMB_FIRE_OPENED_UPPER_SHORTCUT, Events.FIRE_OPENED_UPPER_SHORTCUT,
         lambda bundle: True_()),
    ])
    # Locations
    add_locations(Regions.FIRE_TEMPLE_SHORTCUT_CLIMB, world, [
        (Locations.FIRE_TEMPLE_BOULDER_MAZE_SHORTCUT_CHEST,
         lambda bundle: has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_SHORTCUT_CLIMB, world, [
        (Regions.FIRE_TEMPLE_SHORTCUT_ROOM,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_BOULDER_MAZE_UPPER,
         lambda bundle: has_climb(bundle)),
    ])

    # Fire Temple Boulder Maze Lower  (upstream RR_FIRE_TEMPLE_BOULDER_MAZE_LOWER, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_BOULDER_MAZE_LOWER, world, [
        (Locations.FIRE_TEMPLE_BOULDER_MAZE_LOWER_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.FIRE_TEMPLE_GS_BOULDER_MAZE,
         lambda bundle: has_explosives(bundle) & (is_adult(bundle) | hookshot_or_boomerang(bundle) | can_ground_jumpslash(bundle))),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_BOULDER_MAZE_LOWER, world, [
        (Regions.FIRE_TEMPLE_SHORTCUT_ROOM,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_3F_CURVED_CAGE,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_NARROW_PATH_ROOM,
         lambda bundle: small_keys_scene("SCENE_FIRE_TEMPLE", 5, bundle)),
        (Regions.FIRE_TEMPLE_BOULDER_MAZE_UPPER,
         lambda bundle: False_()),
    ])

    # Fire Temple 3F Curved Cage  (upstream RR_FIRE_TEMPLE_3F_CURVED_CAGE, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_3F_CURVED_CAGE, world, [
        (Locations.FIRE_TEMPLE_BOULDER_MAZE_SIDE_ROOM_CHEST,
         lambda bundle: has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_3F_CURVED_CAGE, world, [
        (Regions.FIRE_TEMPLE_BOULDER_MAZE_LOWER,
         lambda bundle: True_()),
    ])

    # Fire Temple Narrow Path Room  (upstream RR_FIRE_TEMPLE_NARROW_PATH_ROOM, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_NARROW_PATH_ROOM, world, [
        (Locations.FIRE_TEMPLE_EAST_CENTRAL_ROOM_LEFT_HEART,
         lambda bundle: True_()),
        (Locations.FIRE_TEMPLE_EAST_CENTRAL_ROOM_RIGHT_HEART,
         lambda bundle: True_()),
        (Locations.FIRE_TEMPLE_EAST_CENTRAL_ROOM_MIDDLE_HEART,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_NARROW_PATH_ROOM, world, [
        (Regions.FIRE_TEMPLE_BIG_LAVA_ROOM,
         lambda bundle: take_damage(bundle)),
        (Regions.FIRE_TEMPLE_BOULDER_MAZE_LOWER,
         lambda bundle: small_keys_scene("SCENE_FIRE_TEMPLE", 5, bundle)),
        (Regions.FIRE_TEMPLE_FIRE_WALL_CHASE,
         lambda bundle: small_keys_scene("SCENE_FIRE_TEMPLE", 6, bundle)),
        (Regions.FIRE_TEMPLE_FIRE_WALL_CAGE,
         lambda bundle: can_hit_eye_targets(bundle)),
    ])

    # Fire Temple Fire Wall Chase  (upstream RR_FIRE_TEMPLE_FIRE_WALL_CHASE, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_FIRE_WALL_CHASE, world, [
        (Locations.FIRE_TEMPLE_FIRE_WALL_CHASE_EAST_PILLAR_HEART,
         lambda bundle: fire_timer_at_least(bundle, 24) & (is_adult(bundle) | can_use(Items.BOOMERANG, bundle))),
        (Locations.FIRE_TEMPLE_FIRE_WALL_CHASE_WEST_PILLAR_HEART,
         lambda bundle: fire_timer_at_least(bundle, 24) & (is_adult(bundle) | can_use(Items.BOOMERANG, bundle))),
        (Locations.FIRE_TEMPLE_FIRE_WALL_CHASE_EXIT_PLATFORM_HEART,
         lambda bundle: fire_timer_at_least(bundle, 16)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_FIRE_WALL_CHASE, world, [
        (Regions.FIRE_TEMPLE_NARROW_PATH_ROOM,
         lambda bundle: fire_timer_at_least(bundle, 24) & small_keys_scene("SCENE_FIRE_TEMPLE", 6, bundle)),
        (Regions.FIRE_TEMPLE_FIRE_WALL_CAGE,
         lambda bundle: fire_timer_at_least(bundle, 16) & is_adult(bundle)),
        (Regions.FIRE_TEMPLE_FIRE_WALL_UPPER_DOOR,
         lambda bundle: fire_timer_at_least(bundle, 24) & is_adult(bundle)),
        (Regions.FIRE_TEMPLE_FIRE_WALL_SIDE_DOOR,
         lambda bundle: fire_timer_at_least(bundle, 16) & is_adult(bundle)),
    ])

    # Fire Temple Fire Wall Upper Door  (upstream RR_FIRE_TEMPLE_FIRE_WALL_UPPER_DOOR, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_FIRE_WALL_UPPER_DOOR, world, [
        (Regions.FIRE_TEMPLE_FIRE_WALL_CAGE,
         lambda bundle: fire_timer_at_least(bundle, 8) & is_adult(bundle)),
        (Regions.FIRE_TEMPLE_FIRE_WALL_CHASE,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_BOULDER_MAZE_UPPER,
         lambda bundle: True_()),
    ])

    # Fire Temple Fire Wall Chase  (upstream RR_FIRE_TEMPLE_FIRE_WALL_SIDE_DOOR, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_FIRE_WALL_SIDE_DOOR, world, [
        (Locations.FIRE_TEMPLE_FIRE_WALL_CHASE_EAST_PILLAR_HEART,
         lambda bundle: fire_timer_at_least(bundle, 8) & can_use(Items.HOVER_BOOTS, bundle)),
        (Locations.FIRE_TEMPLE_FIRE_WALL_CHASE_WEST_PILLAR_HEART,
         lambda bundle: fire_timer_at_least(bundle, 8) & can_use(Items.HOVER_BOOTS, bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_FIRE_WALL_SIDE_DOOR, world, [
        (Regions.FIRE_TEMPLE_FIRE_WALL_CHASE,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_CORRIDOR,
         lambda bundle: small_keys_scene("SCENE_FIRE_TEMPLE", 7, bundle)),
    ])

    # Fire Temple Fire Wall Cage  (upstream RR_FIRE_TEMPLE_FIRE_WALL_CAGE, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_FIRE_WALL_CAGE, world, [
        (Locations.FIRE_TEMPLE_MAP_CHEST,
         lambda bundle: fire_timer_at_least(bundle, 8) & can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_FIRE_WALL_CAGE, world, [
        (Regions.FIRE_TEMPLE_NARROW_PATH_ROOM,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_FIRE_WALL_CHASE,
         lambda bundle: False_()),
    ])

    # Fire Temple Boulder Maze Upper  (upstream RR_FIRE_TEMPLE_BOULDER_MAZE_UPPER, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_BOULDER_MAZE_UPPER, world, [
        (Locations.FIRE_TEMPLE_BOULDER_MAZE_UPPER_CHEST,
         lambda bundle: has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_BOULDER_MAZE_UPPER, world, [
        (Regions.FIRE_TEMPLE_SHORTCUT_CLIMB,
         lambda bundle: has_explosives(bundle)),
        (Regions.FIRE_TEMPLE_BOULDER_MAZE_LOWER,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_FIRE_WALL_UPPER_DOOR,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_BOULDER_MAZE_4F,
         lambda bundle: reach_scarecrow(bundle) | (can_do_trick(Tricks.FIRE_SCARECROW, bundle) & is_adult(bundle) & can_use(Items.LONGSHOT, bundle))),
    ])

    # Fire Temple Boulder Maze 4F  (upstream RR_FIRE_TEMPLE_BOULDER_MAZE_4F, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_BOULDER_MAZE_4F, world, [
        (Regions.FIRE_TEMPLE_BOULDER_MAZE_UPPER,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_GS_CLIMB_4F,
         lambda bundle: True_()),
    ])

    # Fire Temple GS Climb 4F  (upstream RR_FIRE_TEMPLE_GS_CLIMB_4F, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_GS_CLIMB_4F, world, [
        (Locations.FIRE_TEMPLE_GS_SCARECROW_CLIMB,
         lambda bundle: can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.LONGSHOT)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_GS_CLIMB_4F, world, [
        (Regions.FIRE_TEMPLE_BOULDER_MAZE_4F,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_GS_CLIMB_5F,
         lambda bundle: has_climb(bundle)),
    ])

    # Fire Temple GS Climb 5F  (upstream RR_FIRE_TEMPLE_GS_CLIMB_5F, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_GS_CLIMB_5F, world, [
        (Locations.FIRE_TEMPLE_GS_SCARECROW_CLIMB,
         lambda bundle: ((has_climb(bundle)) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.SHORT_JUMPSLASH) | can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOMB_THROW))),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_GS_CLIMB_5F, world, [
        (Regions.FIRE_TEMPLE_GS_CLIMB_4F,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_5F_RUINS,
         lambda bundle: True_()),
    ])

    # Fire Temple 5F Ruins  (upstream RR_FIRE_TEMPLE_5F_RUINS, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_5F_RUINS, world, [
        (Locations.FIRE_TEMPLE_SCARECROW_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.FIRE_TEMPLE_GS_SCARECROW_TOP,
         lambda bundle: can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOMB_THROW)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_5F_RUINS, world, [
        (Regions.FIRE_TEMPLE_GS_CLIMB_5F,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_NARROW_PATH_ROOM,
         lambda bundle: take_damage(bundle)),
    ])

    # Fire Temple Corridor  (upstream RR_FIRE_TEMPLE_CORRIDOR, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_CORRIDOR, world, [
        (Regions.FIRE_TEMPLE_FIRE_WALL_SIDE_DOOR,
         lambda bundle: small_keys_scene("SCENE_FIRE_TEMPLE", 7, bundle)),
        (Regions.FIRE_TEMPLE_FIRE_MAZE_MAIN,
         lambda bundle: True_()),
    ])

    # Fire Temple Fire Maze Main  (upstream RR_FIRE_TEMPLE_FIRE_MAZE_MAIN, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_FIRE_MAZE_MAIN, world, [
        (Locations.FIRE_TEMPLE_FLAME_MAZE_LEFT_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FIRE_TEMPLE_FLAME_MAZE_LEFT_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FIRE_TEMPLE_FLAME_MAZE_LEFT_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FIRE_TEMPLE_FLAME_MAZE_LEFT_POT4,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_FIRE_MAZE_MAIN, world, [
        (Regions.FIRE_TEMPLE_NEAR_BOSS_PILLAR,
         lambda bundle: has_item(Events.FIRE_HIT_PLATFORM, bundle)),
        (Regions.FIRE_TEMPLE_NEAR_BOSS_ROOM,
         lambda bundle: has_item(Events.FIRE_HIT_PLATFORM, bundle) & fire_timer_at_least(bundle, 8) & take_damage(bundle)),
        (Regions.FIRE_TEMPLE_NEAR_BOSS_DOOR,
         lambda bundle: has_item(Events.FIRE_HIT_PLATFORM, bundle) & fire_timer_at_least(bundle, 8) & take_damage(bundle)),
        (Regions.FIRE_TEMPLE_CORRIDOR,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_FIRE_MAZE_PLATFORMS,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle) | (is_adult(bundle) & (has_item(Events.FIRE_HIT_ABOVE_MAZE_PLATFORM, bundle) | can_ground_jump(bundle) | bunny_hood(bundle)))),
        (Regions.FIRE_TEMPLE_CAGELESS_CHEST_ROOM,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_SOT_CAGE_LOWER,
         lambda bundle: small_keys_scene("SCENE_FIRE_TEMPLE", 8, bundle)),
        (Regions.FIRE_TEMPLE_FIRE_MAZE_SWITCH,
         lambda bundle: can_do_trick(Tricks.FIRE_SKIP_FLAME_WALLS, bundle)),
    ])

    # Fire Temple Fire Maze Platforms  (upstream RR_FIRE_TEMPLE_FIRE_MAZE_PLATFORMS, SCENE_FIRE_TEMPLE)
    # Events
    add_events(Regions.FIRE_TEMPLE_FIRE_MAZE_PLATFORMS, world, [
        (EventLocations.FIRE_TEMPLE_FIRE_MAZE_PLATFORMS_FIRE_HIT_PLATFORM, Events.FIRE_HIT_PLATFORM,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_FIRE_MAZE_PLATFORMS, world, [
        (Regions.FIRE_TEMPLE_FIRE_MAZE_MAIN,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_SOT_CAGE_UPPER_DOOR,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
    ])

    # Fire Temple Cageless Chest Room  (upstream RR_FIRE_TEMPLE_CAGELESS_CHEST_ROOM, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_CAGELESS_CHEST_ROOM, world, [
        (Locations.FIRE_TEMPLE_COMPASS_CHEST,
         lambda bundle: can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_CAGELESS_CHEST_ROOM, world, [
        (Regions.FIRE_TEMPLE_FIRE_MAZE_MAIN,
         lambda bundle: True_()),
    ])

    # Fire Temple Sot Cage Lower  (upstream RR_FIRE_TEMPLE_SOT_CAGE_LOWER, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_SOT_CAGE_LOWER, world, [
        (Regions.FIRE_TEMPLE_FIRE_MAZE_MAIN,
         lambda bundle: small_keys_scene("SCENE_FIRE_TEMPLE", 8, bundle)),
        (Regions.FIRE_TEMPLE_SOT_CAGE_UPPER_DOOR,
         lambda bundle: is_adult(bundle) & can_use(Items.SONG_OF_TIME, bundle)),
        (Regions.FIRE_TEMPLE_SOT_CAGE_SWITCH,
         lambda bundle: is_adult(bundle) & can_use(Items.SONG_OF_TIME, bundle)),
        (Regions.FIRE_TEMPLE_FIRE_MAZE_SWITCH,
         lambda bundle: True_()),
    ])

    # Fire Temple Sot Cage Upper Door  (upstream RR_FIRE_TEMPLE_SOT_CAGE_UPPER_DOOR, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_SOT_CAGE_UPPER_DOOR, world, [
        (Regions.FIRE_TEMPLE_BOSS_ENTRYWAY,
         lambda bundle: False_()),
        (Regions.FIRE_TEMPLE_SOT_CAGE_SWITCH,
         lambda bundle: is_adult(bundle) | can_use(Items.HOVER_BOOTS, bundle) | can_use(Items.SONG_OF_TIME, bundle) | bunny_hood(bundle)),
        (Regions.FIRE_TEMPLE_FIRE_MAZE_PLATFORMS,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_SOT_CAGE_LOWER,
         lambda bundle: True_()),
    ])

    # Fire Temple Sot Cage Switch  (upstream RR_FIRE_TEMPLE_SOT_CAGE_SWITCH, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_SOT_CAGE_SWITCH, world, [
        (Locations.FIRE_TEMPLE_HIGHEST_GORON_CHEST,
         lambda bundle: (can_use(Items.SONG_OF_TIME, bundle) | can_do_trick(Tricks.VISIBLE_COLLISION, bundle)) & can_use(Items.MEGATON_HAMMER, bundle) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_SOT_CAGE_SWITCH, world, [
        (Regions.FIRE_TEMPLE_BOSS_ENTRYWAY,
         lambda bundle: False_()),
        (Regions.FIRE_TEMPLE_SOT_CAGE_UPPER_DOOR,
         lambda bundle: is_adult(bundle) | can_use(Items.HOVER_BOOTS, bundle) | can_use(Items.SONG_OF_TIME, bundle) | bunny_hood(bundle)),
        (Regions.FIRE_TEMPLE_SOT_CAGE_LOWER,
         lambda bundle: True_()),
    ])

    # Fire Temple Fire Maze Switch  (upstream RR_FIRE_TEMPLE_FIRE_MAZE_SWITCH, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_FIRE_MAZE_SWITCH, world, [
        (Regions.FIRE_TEMPLE_FIRE_MAZE_MAIN,
         lambda bundle: (can_do_trick(Tricks.FIRE_SKIP_FLAME_WALLS, bundle) & take_damage(bundle)) | (is_adult(bundle) & can_standing_shield(bundle) & can_use(Items.BOMB_BAG, bundle) & can_do_trick(Tricks.GROUND_JUMP_HARD, bundle) & (can_jump_slash(bundle) | can_use(Items.HOVER_BOOTS, bundle)))),
        (Regions.FIRE_TEMPLE_SOT_CAGE_LOWER,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_FIRE_MAZE_PAST_WALL,
         lambda bundle: True_()),
    ])

    # Fire Temple Fire Maze Past Wall  (upstream RR_FIRE_TEMPLE_FIRE_MAZE_PAST_WALL, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_FIRE_MAZE_PAST_WALL, world, [
        (Locations.FIRE_TEMPLE_FLAME_MAZE_RIGHT_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FIRE_TEMPLE_FLAME_MAZE_RIGHT_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FIRE_TEMPLE_FLAME_MAZE_RIGHT_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FIRE_TEMPLE_FLAME_MAZE_RIGHT_POT4,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_FIRE_MAZE_PAST_WALL, world, [
        (Regions.FIRE_TEMPLE_3F_FLARE_DANCER,
         lambda bundle: has_explosives(bundle)),
    ])

    # Fire Temple 3F Flare Dancer  (upstream RR_FIRE_TEMPLE_3F_FLARE_DANCER, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_3F_FLARE_DANCER, world, [
        (Regions.FIRE_TEMPLE_FIRE_MAZE_PAST_WALL,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.FLARE_DANCER))),
        (Regions.FIRE_TEMPLE_ABOVE_3F_FLARE_DANCER,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.FLARE_DANCER))),
    ])

    # Fire Temple Above 3F Flare Dancer  (upstream RR_FIRE_TEMPLE_ABOVE_3F_FLARE_DANCER, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_ABOVE_3F_FLARE_DANCER, world, [
        (Regions.FIRE_TEMPLE_3F_FLARE_DANCER,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_SWITCH_CLIMB_4F,
         lambda bundle: True_()),
    ])

    # Fire Temple Switch Climb 4F  (upstream RR_FIRE_TEMPLE_SWITCH_CLIMB_4F, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_SWITCH_CLIMB_4F, world, [
        (Regions.FIRE_TEMPLE_ABOVE_3F_FLARE_DANCER,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_SWITCH_CLIMB_5F,
         lambda bundle: can_hit_switch(bundle, EnemyDistance.BOMB_THROW) & has_climb(bundle)),
    ])

    # Fire Temple Switch Climb 5F  (upstream RR_FIRE_TEMPLE_SWITCH_CLIMB_5F, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_SWITCH_CLIMB_5F, world, [
        (Regions.FIRE_TEMPLE_SWITCH_CLIMB_4F,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_NARROW_STAIRS,
         lambda bundle: True_()),
    ])

    # Fire Temple Narrow Stairs  (upstream RR_FIRE_TEMPLE_NARROW_STAIRS, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_NARROW_STAIRS, world, [
        (Locations.FIRE_TEMPLE_MEGATON_HAMMER_CHEST,
         lambda bundle: can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_NARROW_STAIRS, world, [
        (Regions.FIRE_TEMPLE_SOT_CAGE_UPPER_DOOR,
         lambda bundle: take_damage(bundle)),
        (Regions.FIRE_TEMPLE_SOT_CAGE_SWITCH,
         lambda bundle: take_damage(bundle)),
        (Regions.FIRE_TEMPLE_SWITCH_CLIMB_5F,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_NARROW_STAIRS_4F,
         lambda bundle: any_age_time(bundle, lambda bundle: can_use(Items.MEGATON_HAMMER, bundle))),
    ])

    # Fire Temple Narrow Stairs 4F  (upstream RR_FIRE_TEMPLE_NARROW_STAIRS_4F, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_NARROW_STAIRS_4F, world, [
        (Regions.FIRE_TEMPLE_TOP_OF_COLLAPSING_STAIRS,
         lambda bundle: any_age_time(bundle, lambda bundle: can_use(Items.MEGATON_HAMMER, bundle))),
        (Regions.FIRE_TEMPLE_NARROW_STAIRS,
         lambda bundle: False_()),
    ])

    # Fire Temple Top of Collapsing Stairs  (upstream RR_FIRE_TEMPLE_TOP_OF_COLLAPSING_STAIRS, SCENE_FIRE_TEMPLE)
    # Events
    add_events(Regions.FIRE_TEMPLE_TOP_OF_COLLAPSING_STAIRS, world, [
        (EventLocations.FIRE_TEMPLE_TOP_OF_COLLAPSING_STAIRS_FIRE_HIT_STAIRS, Events.FIRE_HIT_STAIRS,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
        (EventLocations.FIRE_TEMPLE_TOP_OF_COLLAPSING_STAIRS_FIRE_CHILD_AT_TOP_OF_STAIRS, Events.FIRE_CHILD_AT_TOP_OF_STAIRS,
         lambda bundle: is_child(bundle)),
    ])
    # Locations
    add_locations(Regions.FIRE_TEMPLE_TOP_OF_COLLAPSING_STAIRS, world, [
        (Locations.FIRE_TEMPLE_AFTER_HAMMER_SMALL_CRATE1,
         lambda bundle: can_break_small_crates(bundle)),
        (Locations.FIRE_TEMPLE_AFTER_HAMMER_SMALL_CRATE2,
         lambda bundle: can_break_small_crates(bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_TOP_OF_COLLAPSING_STAIRS, world, [
        (Regions.FIRE_TEMPLE_NARROW_STAIRS_4F,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_BASE_OF_COLLAPSING_STAIRS,
         lambda bundle: has_item(Events.FIRE_HIT_STAIRS, bundle)),
    ])

    # Fire Temple Base of Collapsing Stairs  (upstream RR_FIRE_TEMPLE_BASE_OF_COLLAPSING_STAIRS, SCENE_FIRE_TEMPLE)
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_BASE_OF_COLLAPSING_STAIRS, world, [
        (Regions.FIRE_TEMPLE_TOP_OF_COLLAPSING_STAIRS,
         lambda bundle: has_item(Events.FIRE_HIT_STAIRS, bundle) & is_adult(bundle)),
        (Regions.FIRE_TEMPLE_ABOVE_FIRE_MAZE,
         lambda bundle: has_item(Events.FIRE_HIT_STAIRS, bundle) & (is_adult(bundle) | has_item(Events.FIRE_CHILD_AT_TOP_OF_STAIRS, bundle)) & has_grab(bundle)),
    ])

    # Fire Temple Above Fire Maze  (upstream RR_FIRE_TEMPLE_ABOVE_FIRE_MAZE, SCENE_FIRE_TEMPLE)
    # Events
    add_events(Regions.FIRE_TEMPLE_ABOVE_FIRE_MAZE, world, [
        (EventLocations.FIRE_TEMPLE_ABOVE_FIRE_MAZE_FIRE_HIT_ABOVE_MAZE_PLATFORM, Events.FIRE_HIT_ABOVE_MAZE_PLATFORM,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_ABOVE_FIRE_MAZE, world, [
        (Regions.FIRE_TEMPLE_BASE_OF_COLLAPSING_STAIRS,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_FIRE_MAZE_PLATFORMS,
         lambda bundle: has_item(Events.FIRE_HIT_ABOVE_MAZE_PLATFORM, bundle)),
    ])

    # Fire Temple Boss Entryway  (upstream RR_FIRE_TEMPLE_BOSS_ENTRYWAY, SCENE_FIRE_TEMPLE)
    # Locations
    add_locations(Regions.FIRE_TEMPLE_BOSS_ENTRYWAY, world, [
        # DEFERRED RC_FIRE_BOSS_KEY_HINT: true
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_BOSS_ENTRYWAY, world, [
        (Regions.FIRE_TEMPLE_NEAR_BOSS_DOOR,
         lambda bundle: True_()),
        (Regions.FIRE_TEMPLE_BOSS_ROOM,
         lambda bundle: has_item(Items.FIRE_TEMPLE_BOSS_KEY, bundle)),
    ])

    # Fire Temple Boss Room  (upstream RR_FIRE_TEMPLE_BOSS_ROOM, SCENE_FIRE_TEMPLE_BOSS)
    # Events
    add_events(Regions.FIRE_TEMPLE_BOSS_ROOM, world, [
        (EventLocations.FIRE_TEMPLE_BOSS_ROOM_FIRE_TEMPLE_CLEAR, Events.FIRE_TEMPLE_COMPLETED,
         lambda bundle: can_use(Items.GORON_TUNIC, bundle) & can_kill_enemy(bundle, Enemies.VOLVAGIA)),
    ])
    # Locations
    add_locations(Regions.FIRE_TEMPLE_BOSS_ROOM, world, [
        (Locations.FIRE_TEMPLE_VOLVAGIA_HEART_CONTAINER,
         lambda bundle: has_item(Events.FIRE_TEMPLE_COMPLETED, bundle)),
        (Locations.VOLVAGIA,
         lambda bundle: has_item(Events.FIRE_TEMPLE_COMPLETED, bundle)),
    ])
    # Connections
    connect_regions(Regions.FIRE_TEMPLE_BOSS_ROOM, world, [
        (Regions.FIRE_TEMPLE_BOSS_ENTRYWAY,
         lambda bundle: False_()),
        (Regions.DMC_PAD_ENTRY,
         lambda bundle: has_item(Events.FIRE_TEMPLE_COMPLETED, bundle)),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_FAIRIES', 'FIRE_CHILD_AT_TOP_OF_STAIRS', 'FIRE_HIT_ABOVE_MAZE_PLATFORM', 'FIRE_HIT_PLATFORM', 'FIRE_HIT_STAIRS', 'FIRE_LOOP_SWITCH', 'FIRE_OPENED_UPPER_SHORTCUT', 'FIRE_TEMPLE_COMPLETED']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (1): ['RC_FIRE_BOSS_KEY_HINT']
