"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/dungeons/ice_cavern.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    ICE_CAVERN_HUB_ICE_CAVERN_SILVER_BLADES = "Ice Cavern Hub Ice Cavern Silver Blades"
    ICE_CAVERN_MAP_ROOM_BLUE_FIRE_ACCESS = "Ice Cavern Map Room Blue Fire Access"
    ICE_CAVERN_COMPASS_ROOM_BLUE_FIRE_ACCESS = "Ice Cavern Compass Room Blue Fire Access"
    ICE_CAVERN_BLOCK_ROOM_NOOKS_BLUE_FIRE_ACCESS = "Ice Cavern Block Room Nooks Blue Fire Access"
    ICE_CAVERN_BLOCK_ROOM_NOOKS_ICE_CAVERN_SILVER_BLOCK = "Ice Cavern Block Room Nooks Ice Cavern Silver Block"


def set_region_rules(world: "SohWorld") -> None:

    # Ice Cavern Entryway  (upstream RR_ICE_CAVERN_ENTRYWAY, SCENE_ICE_CAVERN)
    # Connections
    connect_regions(Regions.ICE_CAVERN_ENTRYWAY, world, [
        (Regions.ICE_CAVERN_BEGINNING,
         lambda bundle: True_()),
        (Regions.ZF_LEDGE,
         lambda bundle: True_()),
    ])

    # Ice Cavern Beginning  (upstream RR_ICE_CAVERN_BEGINNING, SCENE_ICE_CAVERN)
    # Locations
    add_locations(Regions.ICE_CAVERN_BEGINNING, world, [
        (Locations.ICE_CAVERN_ENTRANCE_SONG_OF_STORMS_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.ICE_CAVERN_LOBBY_RUPEE,
         lambda bundle: blue_fire(bundle) | (can_do_trick(Tricks.VISIBLE_COLLISION, bundle) & can_jump_slash(bundle))),
        (Locations.ICE_CAVERN_ENTRANCE_LEFT_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_ENTRANCE_MIDDLE_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_ENTRANCE_RIGHT_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_ENTRANCE_STALACTITE_1,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_ENTRANCE_STALACTITE_2,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_LOBBY_STALACTITE,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_LOBBY_LEFT_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_LOBBY_MIDDLE_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_LOBBY_RIGHT_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_ENTRANCE_RED_ICE,
         lambda bundle: blue_fire(bundle)),
        (Locations.ICE_CAVERN_LOBBY_LEFT_RED_ICE,
         lambda bundle: blue_fire(bundle)),
        (Locations.ICE_CAVERN_LOBBY_RIGHT_RED_ICE,
         lambda bundle: blue_fire(bundle)),
    ])
    # Connections
    connect_regions(Regions.ICE_CAVERN_BEGINNING, world, [
        (Regions.ICE_CAVERN_ENTRYWAY,
         lambda bundle: True_()),
        (Regions.ICE_CAVERN_HUB,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.FREEZARD, EnemyDistance.CLOSE, True, 4))),
        (Regions.ICE_CAVERN_ABOVE_BEGINNING,
         lambda bundle: False_()),
    ])

    # Ice Cavern Hub  (upstream RR_ICE_CAVERN_HUB, SCENE_ICE_CAVERN)
    # Events
    add_events(Regions.ICE_CAVERN_HUB, world, [
        (EventLocations.ICE_CAVERN_HUB_ICE_CAVERN_SILVER_BLADES, Events.ICE_CAVERN_SILVER_BLADES,
         lambda bundle: (is_adult(bundle)) & can_clear_stalagmite(bundle)),
    ])
    # Locations
    add_locations(Regions.ICE_CAVERN_HUB, world, [
        (Locations.ICE_CAVERN_GS_SPINNING_SCYTHE_ROOM,
         lambda bundle: hookshot_or_boomerang(bundle)),
        (Locations.ICE_CAVERN_HALL_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.ICE_CAVERN_HALL_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.ICE_CAVERN_SPINNING_BLADE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.ICE_CAVERN_SPINNING_BLADE_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.ICE_CAVERN_SPINNING_BLADE_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.ICE_CAVERN_AFTER_LOBBY_STALACTITE,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_AFTER_LOBBY_LEFT_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_AFTER_LOBBY_CENTER_LEFT_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_AFTER_LOBBY_CENTER_RIGHT_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_AFTER_LOBBY_RIGHT_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_SPINNING_BLADE_LEFT_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_SPINNING_BLADE_MIDDLE_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_SPINNING_BLADE_RIGHT_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_SPINNING_BLADE_EAST_RED_ICE,
         lambda bundle: blue_fire(bundle)),
        (Locations.ICE_CAVERN_SPINNING_BLADE_WEST_RED_ICE,
         lambda bundle: blue_fire(bundle)),
        # DEFERRED RC_ICE_CAVERN_ICICLES_BLADE_SILVER: logic->CanClearStalagmite()
        # DEFERRED RC_ICE_CAVERN_W_INNER_BLADE_SILVER: true
        # DEFERRED RC_ICE_CAVERN_OUTER_BLADE_SILVER: true
        # DEFERRED RC_ICE_CAVERN_E_INNER_BLADE_SILVER: true
        # DEFERRED RC_ICE_CAVERN_AIRBORNE_BLADE_SILVER: logic->IsAdult
    ])
    # Connections
    connect_regions(Regions.ICE_CAVERN_HUB, world, [
        (Regions.ICE_CAVERN_BEGINNING,
         lambda bundle: True_()),
        (Regions.ICE_CAVERN_MAP_ROOM,
         lambda bundle: (is_adult(bundle)) & has_item(Events.ICE_CAVERN_SILVER_BLADES, bundle)),
        (Regions.ICE_CAVERN_COMPASS_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: blue_fire(bundle))),
        (Regions.ICE_CAVERN_BLOCK_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: blue_fire(bundle)) & (can_clear_stalagmite(bundle) | can_do_trick(Tricks.ICE_STALAGMITE_CLIP, bundle))),
    ])

    # Ice Cavern Map Room  (upstream RR_ICE_CAVERN_MAP_ROOM, SCENE_ICE_CAVERN)
    # Events
    add_events(Regions.ICE_CAVERN_MAP_ROOM, world, [
        (EventLocations.ICE_CAVERN_MAP_ROOM_BLUE_FIRE_ACCESS, Events.CAN_ACCESS_BLUE_FIRE,
         lambda bundle: True_()),
    ])
    # Locations
    add_locations(Regions.ICE_CAVERN_MAP_ROOM, world, [
        (Locations.ICE_CAVERN_MAP_CHEST,
         lambda bundle: blue_fire(bundle) & can_open_large_chest(bundle)),
        (Locations.ICE_CAVERN_FROZEN_POT1,
         lambda bundle: (can_break_pots(bundle) & blue_fire(bundle)) | has_explosives(bundle) | (can_do_trick(Tricks.VISIBLE_COLLISION, bundle) & (can_jump_slash(bundle))) | (can_do_trick(Tricks.ITEM_EXTENSION, bundle) & can_use(Items.HOOKSHOT, bundle))),
        (Locations.ICE_CAVERN_MAP_ROOM_LEFT_HEART,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_MAP_ROOM_MIDDLE_HEART,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_MAP_ROOM_RIGHT_HEART,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_MAP_HALLWAY_STALACTITE_1,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_MAP_HALLWAY_STALACTITE_2,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_MAP_HALLWAY_STALACTITE_3,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_MAP_HALLWAY_STALACTITE_4,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_MAP_HALLWAY_STALACTITE_5,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_MAP_HALLWAY_LEFT_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_MAP_HALLWAY_MIDDLE_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_MAP_HALLWAY_RIGHT_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_MAP_ROOM_POT_RED_ICE,
         lambda bundle: blue_fire(bundle)),
        (Locations.ICE_CAVERN_MAP_ROOM_CHEST_RED_ICE,
         lambda bundle: blue_fire(bundle)),
    ])
    # Connections
    connect_regions(Regions.ICE_CAVERN_MAP_ROOM, world, [
        (Regions.ICE_CAVERN_HUB,
         lambda bundle: True_()),
    ])

    # Ice Cavern Compass Room  (upstream RR_ICE_CAVERN_COMPASS_ROOM, SCENE_ICE_CAVERN)
    # Events
    add_events(Regions.ICE_CAVERN_COMPASS_ROOM, world, [
        (EventLocations.ICE_CAVERN_COMPASS_ROOM_BLUE_FIRE_ACCESS, Events.CAN_ACCESS_BLUE_FIRE,
         lambda bundle: True_()),
    ])
    # Locations
    add_locations(Regions.ICE_CAVERN_COMPASS_ROOM, world, [
        (Locations.ICE_CAVERN_COMPASS_CHEST,
         lambda bundle: (is_child(bundle) | can_clear_stalagmite(bundle) | can_do_trick(Tricks.ICE_STALAGMITE_CLIP, bundle)) & blue_fire(bundle) & can_open_large_chest(bundle)),
        (Locations.ICE_CAVERN_FREESTANDING_POH,
         lambda bundle: (can_clear_stalagmite(bundle) | can_do_trick(Tricks.ICE_STALAGMITE_CLIP, bundle)) & blue_fire(bundle)),
        (Locations.ICE_CAVERN_GS_HEART_PIECE_ROOM,
         lambda bundle: hookshot_or_boomerang(bundle)),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_CENTER_STALACTITE_1,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_CENTER_STALACTITE_2,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_CENTER_STALACTITE_3,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_CENTER_STALACTITE_4,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_CENTER_STALACTITE_5,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_LEFT_STALACTITE_1,
         lambda bundle: can_clear_stalagmite(bundle) | can_do_trick(Tricks.ICE_STALAGMITE_CLIP, bundle)),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_LEFT_STALACTITE_2,
         lambda bundle: can_clear_stalagmite(bundle) | can_do_trick(Tricks.ICE_STALAGMITE_CLIP, bundle)),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_CENTER_STALAGMITE_1,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_CENTER_STALAGMITE_2,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_CENTER_STALAGMITE_3,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_CENTER_STALAGMITE_4,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_CENTER_STALAGMITE_5,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_CENTER_STALAGMITE_6,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_LEFT_STALAGMITE_1,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_LEFT_STALAGMITE_2,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_LEFT_STALAGMITE_3,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_RIGHT_STALAGMITE_1,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_RIGHT_STALAGMITE_2,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_RIGHT_STALAGMITE_3,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_RIGHT_STALAGMITE_4,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_FREESTANDING_RED_ICE,
         lambda bundle: (can_clear_stalagmite(bundle) | can_do_trick(Tricks.ICE_STALAGMITE_CLIP, bundle)) & blue_fire(bundle)),
        (Locations.ICE_CAVERN_HEART_PIECE_ROOM_CHEST_RED_ICE,
         lambda bundle: (is_child(bundle) | can_clear_stalagmite(bundle) | can_do_trick(Tricks.ICE_STALAGMITE_CLIP, bundle)) & blue_fire(bundle)),
    ])
    # Connections
    connect_regions(Regions.ICE_CAVERN_COMPASS_ROOM, world, [
        (Regions.ICE_CAVERN_HUB,
         lambda bundle: True_()),
    ])

    # Ice Cavern Block Room  (upstream RR_ICE_CAVERN_BLOCK_ROOM, SCENE_ICE_CAVERN)
    # Locations
    add_locations(Regions.ICE_CAVERN_BLOCK_ROOM, world, [
        (Locations.ICE_CAVERN_GS_PUSH_BLOCK_ROOM,
         lambda bundle: hookshot_or_boomerang(bundle) | (can_do_trick(Tricks.ICE_BLOCK_GS, bundle) & is_adult(bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.SHORT_JUMPSLASH))),
        (Locations.ICE_CAVERN_SLIDING_BLOCK_ROOM_RUPEE1,
         lambda bundle: can_use(Items.BOOMERANG, bundle)),
        (Locations.ICE_CAVERN_SLIDING_BLOCK_ROOM_RUPEE2,
         lambda bundle: can_use(Items.BOOMERANG, bundle)),
        (Locations.ICE_CAVERN_SLIDING_BLOCK_ROOM_RUPEE3,
         lambda bundle: can_use(Items.BOOMERANG, bundle)),
        (Locations.ICE_CAVERN_PUSH_BLOCK_HALL_LEFT_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_PUSH_BLOCK_HALL_CENTER_LEFT_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_PUSH_BLOCK_HALL_CENTER_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_PUSH_BLOCK_HALL_CENTER_RIGHT_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_PUSH_BLOCK_HALL_RIGHT_STALAGMITE,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_PUSH_BLOCK_HALL_STALACTITE_1,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_PUSH_BLOCK_HALL_STALACTITE_2,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_PUSH_BLOCK_HALL_STALACTITE_3,
         lambda bundle: True_()),
        # DEFERRED RC_ICE_CAVERN_LOWER_BLOCK_SILVER: true
        # DEFERRED RC_ICE_CAVERN_NEAR_BLOCK_SILVER: logic->IsAdult || logic->HasItem(RG_POWER_BRACELET) || logic->CanUse(RG_HOVER_BOOTS) || logic->BunnyHood()
        # DEFERRED RC_ICE_CAVERN_NEAR_GS_BLOCK_SILVER: logic->IsAdult || logic->HasItem(RG_POWER_BRACELET) || logic->CanUse(RG_HOVER_BOOTS) || logic->BunnyHood()
    ])
    # Connections
    connect_regions(Regions.ICE_CAVERN_BLOCK_ROOM, world, [
        (Regions.ICE_CAVERN_HUB,
         lambda bundle: can_clear_stalagmite(bundle) | can_do_trick(Tricks.ICE_STALAGMITE_CLIP, bundle)),
        (Regions.ICE_CAVERN_BLOCK_ROOM_NOOKS,
         lambda bundle: has_grab(bundle) | (is_adult(bundle) & (can_ground_jump(bundle) | can_do_trick(Tricks.SLIDE_JUMP, bundle)))),
        (Regions.ICE_CAVERN_AFTER_BLOCK_ROOM,
         lambda bundle: (has_grab(bundle) | (is_adult(bundle) & (can_ground_jump(bundle) | can_do_trick(Tricks.SLIDE_JUMP, bundle)))) & has_item(Events.ICE_CAVERN_SILVER_BLOCK, bundle)),
    ])

    # Ice Cavern Block Room Nooks  (upstream RR_ICE_CAVERN_BLOCK_ROOM_NOOKS, SCENE_ICE_CAVERN)
    # Events
    add_events(Regions.ICE_CAVERN_BLOCK_ROOM_NOOKS, world, [
        (EventLocations.ICE_CAVERN_BLOCK_ROOM_NOOKS_BLUE_FIRE_ACCESS, Events.CAN_ACCESS_BLUE_FIRE,
         lambda bundle: True_()),
        (EventLocations.ICE_CAVERN_BLOCK_ROOM_NOOKS_ICE_CAVERN_SILVER_BLOCK, Events.ICE_CAVERN_SILVER_BLOCK,
         lambda bundle: (is_adult(bundle) | has_grab(bundle) | can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle)) & (blue_fire(bundle) | (can_do_trick(Tricks.VISIBLE_COLLISION, bundle) & can_jump_slash(bundle)))),
    ])
    # Locations
    add_locations(Regions.ICE_CAVERN_BLOCK_ROOM_NOOKS, world, [
        (Locations.ICE_CAVERN_SLIDING_BLOCK_ROOM_RUPEE1,
         lambda bundle: can_use(Items.SONG_OF_TIME, bundle)),
        (Locations.ICE_CAVERN_SLIDING_BLOCK_ROOM_RUPEE2,
         lambda bundle: can_use(Items.SONG_OF_TIME, bundle)),
        (Locations.ICE_CAVERN_SLIDING_BLOCK_ROOM_RUPEE3,
         lambda bundle: can_use(Items.SONG_OF_TIME, bundle)),
        (Locations.ICE_CAVERN_SILVER_RUPEE_RED_ICE,
         lambda bundle: blue_fire(bundle)),
        # DEFERRED RC_ICE_CAVERN_NEAR_FIRE_BLOCK_SILVER: true
        # DEFERRED RC_ICE_CAVERN_FROZEN_BLOCK_SILVER: logic->BlueFire() || (ctx->GetTrickOption(RT_VISIBLE_COLLISION) && logic->CanJumpslash())
    ])
    # Connections
    connect_regions(Regions.ICE_CAVERN_BLOCK_ROOM_NOOKS, world, [
        (Regions.ICE_CAVERN_BLOCK_ROOM,
         lambda bundle: True_()),
    ])

    # Ice Cavern After Block Room  (upstream RR_ICE_CAVERN_AFTER_BLOCK_ROOM, SCENE_ICE_CAVERN)
    # Locations
    add_locations(Regions.ICE_CAVERN_AFTER_BLOCK_ROOM, world, [
        (Locations.ICE_CAVERN_GS_PUSH_BLOCK_ROOM,
         lambda bundle: can_do_trick(Tricks.ICE_BLOCK_GS, bundle) & is_adult(bundle) & can_use(Items.HOVER_BOOTS, bundle) & blue_fire(bundle) & has_grab(bundle)),
        (Locations.ICE_CAVERN_NEAR_END_STALACTITE_1,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_NEAR_END_STALACTITE_2,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_NEAR_END_STALACTITE_3,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_NEAR_END_STALACTITE_4,
         lambda bundle: True_()),
        (Locations.ICE_CAVERN_NEAR_END_STALAGMITE_1,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_NEAR_END_STALAGMITE_2,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_NEAR_END_STALAGMITE_3,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_NEAR_END_STALAGMITE_4,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_NEAR_END_STALAGMITE_5,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_NEAR_END_STALAGMITE_6,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_NEAR_END_STALAGMITE_7,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.ICE_CAVERN_NEAR_END_STALAGMITE_8,
         lambda bundle: can_clear_stalagmite(bundle)),
    ])
    # Connections
    connect_regions(Regions.ICE_CAVERN_AFTER_BLOCK_ROOM, world, [
        (Regions.ICE_CAVERN_BLOCK_ROOM,
         lambda bundle: True_()),
        (Regions.ICE_CAVERN_BEFORE_FINAL_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: blue_fire(bundle))),
    ])

    # Ice Cavern Before Final Room  (upstream RR_ICE_CAVERN_BEFORE_FINAL_ROOM, SCENE_ICE_CAVERN)
    # Locations
    add_locations(Regions.ICE_CAVERN_BEFORE_FINAL_ROOM, world, [
        (Locations.ICE_CAVERN_NEAR_END_POT1,
         lambda bundle: can_break_pots(bundle) & blue_fire(bundle)),
        (Locations.ICE_CAVERN_NEAR_END_POT2,
         lambda bundle: can_break_pots(bundle) & blue_fire(bundle)),
        (Locations.ICE_CAVERN_NEAR_END_LEFT_RED_ICE,
         lambda bundle: blue_fire(bundle)),
        (Locations.ICE_CAVERN_NEAR_END_MIDDLE_RED_ICE,
         lambda bundle: blue_fire(bundle)),
        (Locations.ICE_CAVERN_NEAR_END_RIGHT_RED_ICE,
         lambda bundle: blue_fire(bundle)),
    ])
    # Connections
    connect_regions(Regions.ICE_CAVERN_BEFORE_FINAL_ROOM, world, [
        (Regions.ICE_CAVERN_AFTER_BLOCK_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: blue_fire(bundle))),
        (Regions.ICE_CAVERN_FINAL_ROOM,
         lambda bundle: True_()),
    ])

    # Ice Cavern Final Room  (upstream RR_ICE_CAVERN_FINAL_ROOM, SCENE_ICE_CAVERN)
    # Locations
    add_locations(Regions.ICE_CAVERN_FINAL_ROOM, world, [
        (Locations.ICE_CAVERN_IRON_BOOTS_CHEST,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.WOLFOS)) & can_open_large_chest(bundle)),
        (Locations.SHEIK_IN_ICE_CAVERN,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.WOLFOS)) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.ICE_CAVERN_FINAL_ROOM, world, [
        (Regions.ICE_CAVERN_BEFORE_FINAL_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.WOLFOS))),
        (Regions.ICE_CAVERN_FINAL_ROOM_UNDERWATER,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.WOLFOS)) & can_use(Items.IRON_BOOTS, bundle)),
    ])

    # Ice Cavern Final Room Underwater  (upstream RR_ICE_CAVERN_FINAL_ROOM_UNDERWATER, SCENE_ICE_CAVERN)
    # Connections
    connect_regions(Regions.ICE_CAVERN_FINAL_ROOM_UNDERWATER, world, [
        (Regions.ICE_CAVERN_FINAL_ROOM,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle)),
        (Regions.ICE_CAVERN_ABOVE_BEGINNING,
         lambda bundle: can_use(Items.IRON_BOOTS, bundle)),
    ])

    # Ice Cavern Above Beginning  (upstream RR_ICE_CAVERN_ABOVE_BEGINNING, SCENE_ICE_CAVERN)
    # Connections
    connect_regions(Regions.ICE_CAVERN_ABOVE_BEGINNING, world, [
        (Regions.ICE_CAVERN_FINAL_ROOM_UNDERWATER,
         lambda bundle: can_use(Items.IRON_BOOTS, bundle)),
        (Regions.ICE_CAVERN_BEGINNING,
         lambda bundle: True_()),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_BLUE_FIRE', 'ICE_CAVERN_SILVER_BLADES', 'ICE_CAVERN_SILVER_BLOCK']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (10): ['RC_ICE_CAVERN_ICICLES_BLADE_SILVER', 'RC_ICE_CAVERN_W_INNER_BLADE_SILVER', 'RC_ICE_CAVERN_OUTER_BLADE_SILVER', 'RC_ICE_CAVERN_E_INNER_BLADE_SILVER', 'RC_ICE_CAVERN_AIRBORNE_BLADE_SILVER', 'RC_ICE_CAVERN_LOWER_BLOCK_SILVER', 'RC_ICE_CAVERN_NEAR_BLOCK_SILVER', 'RC_ICE_CAVERN_NEAR_GS_BLOCK_SILVER', 'RC_ICE_CAVERN_NEAR_FIRE_BLOCK_SILVER', 'RC_ICE_CAVERN_FROZEN_BLOCK_SILVER']
