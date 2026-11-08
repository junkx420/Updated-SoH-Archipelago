"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/dungeons/gerudo_training_ground.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    GERUDO_TRAINING_GROUND_BOULDER_ROOM_GTG_SILVER_SLOPE = "Gerudo Training Ground Boulder Room Gtg Silver Slope"
    GERUDO_TRAINING_GROUND_HEAVY_BLOCK_ROOM_GTG_PUSHED_HEAVY_BLOCK = "Gerudo Training Ground Heavy Block Room Gtg Pushed Heavy Block"
    GERUDO_TRAINING_GROUND_HEAVY_BLOCK_ROOM_UPPER_GTG_UNLOCKED_DOOR_BEHIND_HEAVY_BLOCK = "Gerudo Training Ground Heavy Block Room Upper Gtg Unlocked Door Behind Heavy Block"
    GERUDO_TRAINING_GROUND_EYE_STATUE_LOWER_GTG_CLEARED_EYE_STATUE = "Gerudo Training Ground Eye Statue Lower Gtg Cleared Eye Statue"
    GERUDO_TRAINING_GROUND_LAVA_ROOM_GTG_SILVER_LAVA = "Gerudo Training Ground Lava Room Gtg Silver Lava"
    GERUDO_TRAINING_GROUND_UNDERWATER_GTG_SILVER_WATER = "Gerudo Training Ground Underwater Gtg Silver Water"


def set_region_rules(world: "SohWorld") -> None:

    # Gerudo Training Ground Entryway  (upstream RR_GERUDO_TRAINING_GROUND_ENTRYWAY, SCENE_GERUDO_TRAINING_GROUND)
    # Connections
    connect_regions(Regions.GERUDO_TRAINING_GROUND_ENTRYWAY, world, [
        (Regions.GERUDO_TRAINING_GROUND_LOBBY,
         lambda bundle: True_()),
        (Regions.GF_EXITING_GTG,
         lambda bundle: True_()),
    ])

    # Gerudo Training Ground Lobby  (upstream RR_GERUDO_TRAINING_GROUND_LOBBY, SCENE_GERUDO_TRAINING_GROUND)
    # Locations
    add_locations(Regions.GERUDO_TRAINING_GROUND_LOBBY, world, [
        (Locations.GERUDO_TRAINING_GROUND_LOBBY_LEFT_CHEST,
         lambda bundle: can_hit_eye_targets(bundle) & has_open_chest(bundle)),
        (Locations.GERUDO_TRAINING_GROUND_LOBBY_RIGHT_CHEST,
         lambda bundle: can_hit_eye_targets(bundle) & has_open_chest(bundle)),
        (Locations.GERUDO_TRAINING_GROUND_ENTRANCE_SONG_OF_STORMS_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
    ])
    # Connections
    connect_regions(Regions.GERUDO_TRAINING_GROUND_LOBBY, world, [
        (Regions.GERUDO_TRAINING_GROUND_ENTRYWAY,
         lambda bundle: True_()),
        (Regions.GERUDO_TRAINING_GROUND_SAND_ROOM,
         lambda bundle: True_()),
        (Regions.GERUDO_TRAINING_GROUND_DINALFOS,
         lambda bundle: True_()),
        (Regions.GERUDO_TRAINING_GROUND_CENTRAL_MAZE,
         lambda bundle: True_()),
    ])

    # Gerudo Training Ground Sand Room  (upstream RR_GERUDO_TRAINING_GROUND_SAND_ROOM, SCENE_GERUDO_TRAINING_GROUND)
    # Locations
    add_locations(Regions.GERUDO_TRAINING_GROUND_SAND_ROOM, world, [
        (Locations.GERUDO_TRAINING_GROUND_STALFOS_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.STALFOS, EnemyDistance.CLOSE, True, 2, True) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.GERUDO_TRAINING_GROUND_SAND_ROOM, world, [
        (Regions.GERUDO_TRAINING_GROUND_LOBBY,
         lambda bundle: True_()),
        (Regions.GERUDO_TRAINING_GROUND_BOULDER_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.STALFOS, EnemyDistance.CLOSE, True, 2, True))),
    ])

    # Gerudo Training Ground Boulder Room  (upstream RR_GERUDO_TRAINING_GROUND_BOULDER_ROOM, SCENE_GERUDO_TRAINING_GROUND)
    # Events
    add_events(Regions.GERUDO_TRAINING_GROUND_BOULDER_ROOM, world, [
        (EventLocations.GERUDO_TRAINING_GROUND_BOULDER_ROOM_GTG_SILVER_SLOPE, Events.GTG_SILVER_SLOPE,
         lambda bundle: ((is_adult(bundle)) & can_use(Items.HOOKSHOT, bundle) | (is_child(bundle)) & can_use(Items.LONGSHOT, bundle)) | can_do_trick(Tricks.GTG_WITHOUT_HOOKSHOT, bundle)),
    ])
    # Locations
    add_locations(Regions.GERUDO_TRAINING_GROUND_BOULDER_ROOM, world, [
        # DEFERRED RC_GTG_FIRE_WALL_SLOPE_SILVER: true
        # DEFERRED RC_GTG_LOWER_BOULDER_SLOPE_SILVER: true
        # DEFERRED RC_GTG_TARGET_SLOPE_SILVER: logic->CanUse(logic->IsAdult ? RG_HOOKSHOT : RG_LONGSHOT) || ctx->GetTrickOption(RT_GTG_WITHOUT_HOOKSHOT)
        # DEFERRED RC_GTG_JUMPDOWN_SLOPE_SILVER: true
        # DEFERRED RC_GTG_UPPER_BOULDER_SLOPE_SILVER: true
    ])
    # Connections
    connect_regions(Regions.GERUDO_TRAINING_GROUND_BOULDER_ROOM, world, [
        (Regions.GERUDO_TRAINING_GROUND_SAND_ROOM,
         lambda bundle: True_()),
        (Regions.GERUDO_TRAINING_GROUND_HEAVY_BLOCK_ROOM,
         lambda bundle: has_item(Events.GTG_SILVER_SLOPE, bundle)),
    ])

    # Gerudo Training Ground Central Maze  (upstream RR_GERUDO_TRAINING_GROUND_CENTRAL_MAZE, SCENE_GERUDO_TRAINING_GROUND)
    # Locations
    add_locations(Regions.GERUDO_TRAINING_GROUND_CENTRAL_MAZE, world, [
        (Locations.GERUDO_TRAINING_GROUND_HIDDEN_CEILING_CHEST,
         lambda bundle: small_keys_scene("SCENE_GERUDO_TRAINING_GROUND", 3, bundle) & (can_do_trick(Tricks.LENS_GTG, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & (can_use(Items.HOOKSHOT, bundle) | has_climb(bundle)) & has_open_chest(bundle)),
        (Locations.GERUDO_TRAINING_GROUND_MAZE_PATH_FIRST_CHEST,
         lambda bundle: small_keys_scene("SCENE_GERUDO_TRAINING_GROUND", 4, bundle) & has_open_chest(bundle)),
        (Locations.GERUDO_TRAINING_GROUND_MAZE_PATH_SECOND_CHEST,
         lambda bundle: small_keys_scene("SCENE_GERUDO_TRAINING_GROUND", 6, bundle) & has_open_chest(bundle)),
        (Locations.GERUDO_TRAINING_GROUND_MAZE_PATH_THIRD_CHEST,
         lambda bundle: small_keys_scene("SCENE_GERUDO_TRAINING_GROUND", 7, bundle) & has_open_chest(bundle)),
        (Locations.GERUDO_TRAINING_GROUND_MAZE_PATH_FINAL_CHEST,
         lambda bundle: small_keys_scene("SCENE_GERUDO_TRAINING_GROUND", 9, bundle) & can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.GERUDO_TRAINING_GROUND_CENTRAL_MAZE, world, [
        (Regions.GERUDO_TRAINING_GROUND_LOBBY,
         lambda bundle: True_()),
        (Regions.GERUDO_TRAINING_GROUND_CENTRAL_MAZE_RIGHT,
         lambda bundle: small_keys_scene("SCENE_GERUDO_TRAINING_GROUND", 9, bundle)),
    ])

    # Gerudo Training Ground Central Maze Right  (upstream RR_GERUDO_TRAINING_GROUND_CENTRAL_MAZE_RIGHT, SCENE_GERUDO_TRAINING_GROUND)
    # Locations
    add_locations(Regions.GERUDO_TRAINING_GROUND_CENTRAL_MAZE_RIGHT, world, [
        (Locations.GERUDO_TRAINING_GROUND_MAZE_RIGHT_CENTRAL_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.GERUDO_TRAINING_GROUND_MAZE_RIGHT_SIDE_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.GERUDO_TRAINING_GROUND_FREESTANDING_KEY,
         lambda bundle: True_()),
        # DEFERRED RC_GTG_UNDER_LEDGE_LAVA_SILVER: true
    ])
    # Connections
    connect_regions(Regions.GERUDO_TRAINING_GROUND_CENTRAL_MAZE_RIGHT, world, [
        (Regions.GERUDO_TRAINING_GROUND_LAVA_ROOM,
         lambda bundle: True_()),
        (Regions.GERUDO_TRAINING_GROUND_LAVA_ROOM_UPPER_LEDGE,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
        (Regions.GERUDO_TRAINING_GROUND_CENTRAL_MAZE,
         lambda bundle: small_keys_scene("SCENE_GERUDO_TRAINING_GROUND", 9, bundle)),
    ])

    # Gerudo Training Ground Heavy Block Room  (upstream RR_GERUDO_TRAINING_GROUND_HEAVY_BLOCK_ROOM, SCENE_GERUDO_TRAINING_GROUND)
    # Events
    add_events(Regions.GERUDO_TRAINING_GROUND_HEAVY_BLOCK_ROOM, world, [
        (EventLocations.GERUDO_TRAINING_GROUND_HEAVY_BLOCK_ROOM_GTG_PUSHED_HEAVY_BLOCK, Events.GTG_PUSHED_HEAVY_BLOCK,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
    ])
    # Locations
    add_locations(Regions.GERUDO_TRAINING_GROUND_HEAVY_BLOCK_ROOM, world, [
        (Locations.GERUDO_TRAINING_GROUND_BEFORE_HEAVY_BLOCK_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.WOLFOS, EnemyDistance.CLOSE, True, 4, True) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.GERUDO_TRAINING_GROUND_HEAVY_BLOCK_ROOM, world, [
        (Regions.GERUDO_TRAINING_GROUND_HEAVY_BLOCK_ROOM_UPPER,
         lambda bundle: (can_do_trick(Tricks.LENS_GTG, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & (can_use(Items.HOOKSHOT, bundle) | ((can_do_trick(Tricks.GTG_FAKE_WALL, bundle) | bunny_hood(bundle)) & is_adult(bundle) & can_use(Items.HOVER_BOOTS, bundle)) | (is_adult(bundle) & can_ground_jump(bundle)))),
        (Regions.GERUDO_TRAINING_GROUND_BEHIND_HEAVY_BLOCK,
         lambda bundle: has_item(Events.GTG_PUSHED_HEAVY_BLOCK, bundle)),
        (Regions.GERUDO_TRAINING_GROUND_BOULDER_ROOM,
         lambda bundle: True_()),
    ])

    # Gerudo Training Ground Heavy Block Room Upper  (upstream RR_GERUDO_TRAINING_GROUND_HEAVY_BLOCK_ROOM_UPPER, SCENE_GERUDO_TRAINING_GROUND)
    # Events
    add_events(Regions.GERUDO_TRAINING_GROUND_HEAVY_BLOCK_ROOM_UPPER, world, [
        (EventLocations.GERUDO_TRAINING_GROUND_HEAVY_BLOCK_ROOM_UPPER_GTG_UNLOCKED_DOOR_BEHIND_HEAVY_BLOCK, Events.GTG_UNLOCKED_DOOR_BEHIND_HEAVY_BLOCK,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.GERUDO_TRAINING_GROUND_HEAVY_BLOCK_ROOM_UPPER, world, [
        (Regions.GERUDO_TRAINING_GROUND_HEAVY_BLOCK_ROOM,
         lambda bundle: can_do_trick(Tricks.LENS_GTG, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
        (Regions.GERUDO_TRAINING_GROUND_EYE_STATUE_UPPER,
         lambda bundle: True_()),
    ])

    # Gerudo Training Ground Behind Heavy Block  (upstream RR_GERUDO_TRAINING_GROUND_BEHIND_HEAVY_BLOCK, SCENE_GERUDO_TRAINING_GROUND)
    # Connections
    connect_regions(Regions.GERUDO_TRAINING_GROUND_BEHIND_HEAVY_BLOCK, world, [
        (Regions.GERUDO_TRAINING_GROUND_HEAVY_BLOCK_ROOM,
         lambda bundle: has_item(Events.GTG_PUSHED_HEAVY_BLOCK, bundle)),
        (Regions.GERUDO_TRAINING_GROUND_LIKE_LIKE_ROOM,
         lambda bundle: has_item(Events.GTG_UNLOCKED_DOOR_BEHIND_HEAVY_BLOCK, bundle)),
    ])

    # Gerudo Training Ground Like Like Room  (upstream RR_GERUDO_TRAINING_GROUND_LIKE_LIKE_ROOM, SCENE_GERUDO_TRAINING_GROUND)
    # Locations
    add_locations(Regions.GERUDO_TRAINING_GROUND_LIKE_LIKE_ROOM, world, [
        (Locations.GERUDO_TRAINING_GROUND_HEAVY_BLOCK_FIRST_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.LIKE_LIKE) & has_open_chest(bundle)),
        (Locations.GERUDO_TRAINING_GROUND_HEAVY_BLOCK_SECOND_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.LIKE_LIKE) & has_open_chest(bundle)),
        (Locations.GERUDO_TRAINING_GROUND_HEAVY_BLOCK_THIRD_CHEST,
         lambda bundle: (can_do_trick(Tricks.LENS_GTG, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & can_pass_enemy(bundle, Enemies.LIKE_LIKE) & has_open_chest(bundle)),
        (Locations.GERUDO_TRAINING_GROUND_HEAVY_BLOCK_FOURTH_CHEST,
         lambda bundle: has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.GERUDO_TRAINING_GROUND_LIKE_LIKE_ROOM, world, [
        (Regions.GERUDO_TRAINING_GROUND_BEHIND_HEAVY_BLOCK,
         lambda bundle: True_()),
    ])

    # Gerudo Training Ground Eye Statue Upper  (upstream RR_GERUDO_TRAINING_GROUND_EYE_STATUE_UPPER, SCENE_GERUDO_TRAINING_GROUND)
    # Locations
    add_locations(Regions.GERUDO_TRAINING_GROUND_EYE_STATUE_UPPER, world, [
        # DEFERRED RC_GERUDO_TRAINING_GROUND_WONDER_EYE_STATUE_ROOM: logic->CanUse(RG_HOVER_BOOTS) || logic->BunnyHood() || (logic->IsAdult && ctx->GetTrickOption(RT_GTG_STATUE_JUMP))
    ])
    # Connections
    connect_regions(Regions.GERUDO_TRAINING_GROUND_EYE_STATUE_UPPER, world, [
        (Regions.GERUDO_TRAINING_GROUND_EYE_STATUE_LOWER,
         lambda bundle: True_()),
        (Regions.GERUDO_TRAINING_GROUND_HEAVY_BLOCK_ROOM_UPPER,
         lambda bundle: True_()),
        (Regions.GERUDO_TRAINING_GROUND_ABOVE_MAZE,
         lambda bundle: has_item(Events.GTG_CLEARED_EYE_STATUE, bundle)),
    ])

    # Gerudo Training Ground Above Eye  (upstream RR_GERUDO_TRAINING_GROUND_ABOVE_MAZE, SCENE_GERUDO_TRAINING_GROUND)
    # Locations
    add_locations(Regions.GERUDO_TRAINING_GROUND_ABOVE_MAZE, world, [
        (Locations.GERUDO_TRAINING_GROUND_NEAR_SCARECROW_CHEST,
         lambda bundle: has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.GERUDO_TRAINING_GROUND_ABOVE_MAZE, world, [
        (Regions.GERUDO_TRAINING_GROUND_EYE_STATUE_UPPER,
         lambda bundle: True_()),
    ])

    # Gerudo Training Ground Eye Statue Lower  (upstream RR_GERUDO_TRAINING_GROUND_EYE_STATUE_LOWER, SCENE_GERUDO_TRAINING_GROUND)
    # Events
    add_events(Regions.GERUDO_TRAINING_GROUND_EYE_STATUE_LOWER, world, [
        (EventLocations.GERUDO_TRAINING_GROUND_EYE_STATUE_LOWER_GTG_CLEARED_EYE_STATUE, Events.GTG_CLEARED_EYE_STATUE,
         lambda bundle: can_use(Items.FAIRY_BOW, bundle)),
    ])
    # Locations
    add_locations(Regions.GERUDO_TRAINING_GROUND_EYE_STATUE_LOWER, world, [
        (Locations.GERUDO_TRAINING_GROUND_EYE_STATUE_CHEST,
         lambda bundle: has_item(Events.GTG_CLEARED_EYE_STATUE, bundle) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.GERUDO_TRAINING_GROUND_EYE_STATUE_LOWER, world, [
        (Regions.GERUDO_TRAINING_GROUND_HAMMER_ROOM,
         lambda bundle: True_()),
    ])

    # Gerudo Training Ground Hammer Room  (upstream RR_GERUDO_TRAINING_GROUND_HAMMER_ROOM, SCENE_GERUDO_TRAINING_GROUND)
    # Locations
    add_locations(Regions.GERUDO_TRAINING_GROUND_HAMMER_ROOM, world, [
        (Locations.GERUDO_TRAINING_GROUND_HAMMER_ROOM_CLEAR_CHEST,
         lambda bundle: can_attack(bundle) & has_open_chest(bundle)),
        (Locations.GERUDO_TRAINING_GROUND_HAMMER_ROOM_SWITCH_CHEST,
         lambda bundle: (can_use(Items.MEGATON_HAMMER, bundle) | (take_damage(bundle) & can_do_trick(Tricks.FIRE_RINGS, bundle))) & has_open_chest(bundle)),
        # DEFERRED RC_GERUDO_TRAINING_GROUND_WONDER_TORCH_SLUGS_ROOM: logic->CanUse(RG_FAIRY_BOW)
    ])
    # Connections
    connect_regions(Regions.GERUDO_TRAINING_GROUND_HAMMER_ROOM, world, [
        (Regions.GERUDO_TRAINING_GROUND_EYE_STATUE_LOWER,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle) & can_use(Items.FAIRY_BOW, bundle)),
        (Regions.GERUDO_TRAINING_GROUND_LAVA_ROOM_UPPER_LEDGE,
         lambda bundle: True_()),
    ])

    # Gerudo Training Ground Lava Room  (upstream RR_GERUDO_TRAINING_GROUND_LAVA_ROOM, SCENE_GERUDO_TRAINING_GROUND)
    # Events
    add_events(Regions.GERUDO_TRAINING_GROUND_LAVA_ROOM, world, [
        (EventLocations.GERUDO_TRAINING_GROUND_LAVA_ROOM_GTG_SILVER_LAVA, Events.GTG_SILVER_LAVA,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) & (can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle) | can_use(Items.SONG_OF_TIME, bundle) | is_child(bundle))),
    ])
    # Locations
    add_locations(Regions.GERUDO_TRAINING_GROUND_LAVA_ROOM, world, [
        # DEFERRED RC_GTG_NEAR_SWITCH_LAVA_SILVER: true
        # DEFERRED RC_GTG_NEAR_BARRED_DOOR_LAVA_SILVER: true
        # DEFERRED RC_GTG_FIRE_RING_LAVA_SILVER: logic->CanUse(RG_HOVER_BOOTS) || logic->BunnyHood() || logic->CanUse(RG_SONG_OF_TIME) || logic->IsChild
        # DEFERRED RC_GTG_UNDER_LEDGE_LAVA_SILVER: logic->CanUse(RG_HOVER_BOOTS) || logic->BunnyHood() || logic->CanUse(RG_SONG_OF_TIME) || logic->IsChild
    ])
    # Connections
    connect_regions(Regions.GERUDO_TRAINING_GROUND_LAVA_ROOM, world, [
        (Regions.GERUDO_TRAINING_GROUND_DINALFOS,
         lambda bundle: True_()),
        (Regions.GERUDO_TRAINING_GROUND_CENTRAL_MAZE_RIGHT,
         lambda bundle: can_use(Items.SONG_OF_TIME, bundle) | is_child(bundle)),
        (Regions.GERUDO_TRAINING_GROUND_LAVA_ROOM_UPPER_LEDGE,
         lambda bundle: can_use(Items.LONGSHOT, bundle) | (can_use(Items.HOOKSHOT, bundle) & (can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle) | can_use(Items.SONG_OF_TIME, bundle) | is_child(bundle) | (is_adult(bundle) & can_do_trick(Tricks.GTG_LAVA_JUMP, bundle)) | (can_do_trick(Tricks.DAMAGE_BOOST_SIMPLE, bundle) & can_use(Items.BOMB_BAG, bundle) & take_damage(bundle))))),
        (Regions.GERUDO_TRAINING_GROUND_UNDERWATER,
         lambda bundle: has_item(Events.GTG_SILVER_LAVA, bundle)),
    ])

    # Gerudo Training Ground Lava Room  (upstream RR_GERUDO_TRAINING_GROUND_LAVA_ROOM_UPPER_LEDGE, SCENE_GERUDO_TRAINING_GROUND)
    # Locations
    add_locations(Regions.GERUDO_TRAINING_GROUND_LAVA_ROOM_UPPER_LEDGE, world, [
        # DEFERRED RC_GTG_UPPER_LAVA_SILVER: logic->CanUse(RG_HOOKSHOT)
        # DEFERRED RC_GTG_UNDER_LEDGE_LAVA_SILVER: true
    ])
    # Connections
    connect_regions(Regions.GERUDO_TRAINING_GROUND_LAVA_ROOM_UPPER_LEDGE, world, [
        (Regions.GERUDO_TRAINING_GROUND_LAVA_ROOM,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle) | can_use(Items.SONG_OF_TIME, bundle) | is_child(bundle) | (is_adult(bundle) & can_do_trick(Tricks.GTG_LAVA_JUMP, bundle)) | (can_do_trick(Tricks.DAMAGE_BOOST_SIMPLE, bundle) & can_use(Items.BOMB_BAG, bundle) & take_damage(bundle))),
        (Regions.GERUDO_TRAINING_GROUND_HAMMER_ROOM,
         lambda bundle: True_()),
    ])

    # Gerudo Training Ground Underwater  (upstream RR_GERUDO_TRAINING_GROUND_UNDERWATER, SCENE_GERUDO_TRAINING_GROUND)
    # Events
    add_events(Regions.GERUDO_TRAINING_GROUND_UNDERWATER, world, [
        (EventLocations.GERUDO_TRAINING_GROUND_UNDERWATER_GTG_SILVER_WATER, Events.GTG_SILVER_WATER,
         lambda bundle: can_use(Items.SONG_OF_TIME, bundle) & can_use(Items.IRON_BOOTS, bundle) & has_item(Items.BRONZE_SCALE, bundle) & water_timer_at_least(bundle, 24)),
    ])
    # Locations
    add_locations(Regions.GERUDO_TRAINING_GROUND_UNDERWATER, world, [
        (Locations.GERUDO_TRAINING_GROUND_UNDERWATER_SILVER_RUPEE_CHEST,
         lambda bundle: has_item(Events.GTG_SILVER_WATER, bundle) & has_open_chest(bundle)),
        # DEFERRED RC_GTG_MIDDLE_WATER_SILVER: logic->CanUse(RG_SONG_OF_TIME) && logic->CanUse(RG_IRON_BOOTS) && logic->WaterTimer() >= 16
        # DEFERRED RC_GTG_ABOVE_TARGET_WATER_SILVER: logic->CanUse(RG_SONG_OF_TIME) && ((logic->CanUse(RG_IRON_BOOTS) && logic->WaterTimer() >= 16) || logic->HasItem(RG_GOLDEN_SCALE))
        # DEFERRED RC_GTG_LEFT_WATER_SILVER: logic->CanUse(RG_SONG_OF_TIME) && logic->CanUse(RG_IRON_BOOTS) && logic->WaterTimer() >= 16
        # DEFERRED RC_GTG_UNDER_TARGET_WATER_SILVER: logic->CanUse(RG_SONG_OF_TIME) && logic->CanUse(RG_IRON_BOOTS) && (logic->HasItem(RG_BRONZE_SCALE) || logic->CanUse(RG_HOOKSHOT)) && logic->WaterTimer() >= 16
        # DEFERRED RC_GTG_RIGHT_WATER_SILVER: logic->CanUse(RG_SONG_OF_TIME) && logic->CanUse(RG_IRON_BOOTS) && logic->WaterTimer() >= 16
    ])
    # Connections
    connect_regions(Regions.GERUDO_TRAINING_GROUND_UNDERWATER, world, [
        (Regions.GERUDO_TRAINING_GROUND_LAVA_ROOM,
         lambda bundle: True_()),
    ])

    # Gerudo Training Dinalfos  (upstream RR_GERUDO_TRAINING_GROUND_DINALFOS, SCENE_GERUDO_TRAINING_GROUND)
    # Locations
    add_locations(Regions.GERUDO_TRAINING_GROUND_DINALFOS, world, [
        (Locations.GERUDO_TRAINING_GROUND_BEAMOS_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.BEAMOS) & can_kill_enemy(bundle, Enemies.DINOLFOS, EnemyDistance.CLOSE, True, 2, True) & has_open_chest(bundle)),
        (Locations.GERUDO_TRAINING_GROUND_BEAMOS_SOUTH_HEART,
         lambda bundle: True_()),
        (Locations.GERUDO_TRAINING_GROUND_BEAMOS_EAST_HEART,
         lambda bundle: True_()),
        # DEFERRED RC_GERUDO_TRAINING_GROUND_WONDER_BEAMOS_ROOM: logic->CanUse(RG_FAIRY_BOW)
    ])
    # Connections
    connect_regions(Regions.GERUDO_TRAINING_GROUND_DINALFOS, world, [
        (Regions.GERUDO_TRAINING_GROUND_LOBBY,
         lambda bundle: True_()),
        (Regions.GERUDO_TRAINING_GROUND_LAVA_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.BEAMOS) & can_kill_enemy(bundle, Enemies.DINOLFOS, EnemyDistance.CLOSE, True, 2, True))),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['GTG_CLEARED_EYE_STATUE', 'GTG_PUSHED_HEAVY_BLOCK', 'GTG_SILVER_LAVA', 'GTG_SILVER_SLOPE', 'GTG_SILVER_WATER', 'GTG_UNLOCKED_DOOR_BEHIND_HEAVY_BLOCK']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (20): ['RC_GTG_FIRE_WALL_SLOPE_SILVER', 'RC_GTG_LOWER_BOULDER_SLOPE_SILVER', 'RC_GTG_TARGET_SLOPE_SILVER', 'RC_GTG_JUMPDOWN_SLOPE_SILVER', 'RC_GTG_UPPER_BOULDER_SLOPE_SILVER', 'RC_GTG_UNDER_LEDGE_LAVA_SILVER', 'RC_GERUDO_TRAINING_GROUND_WONDER_EYE_STATUE_ROOM', 'RC_GERUDO_TRAINING_GROUND_WONDER_TORCH_SLUGS_ROOM', 'RC_GTG_NEAR_SWITCH_LAVA_SILVER', 'RC_GTG_NEAR_BARRED_DOOR_LAVA_SILVER', 'RC_GTG_FIRE_RING_LAVA_SILVER', 'RC_GTG_UNDER_LEDGE_LAVA_SILVER', 'RC_GTG_UPPER_LAVA_SILVER', 'RC_GTG_UNDER_LEDGE_LAVA_SILVER', 'RC_GTG_MIDDLE_WATER_SILVER', 'RC_GTG_ABOVE_TARGET_WATER_SILVER', 'RC_GTG_LEFT_WATER_SILVER', 'RC_GTG_UNDER_TARGET_WATER_SILVER', 'RC_GTG_RIGHT_WATER_SILVER', 'RC_GERUDO_TRAINING_GROUND_WONDER_BEAMOS_ROOM']
