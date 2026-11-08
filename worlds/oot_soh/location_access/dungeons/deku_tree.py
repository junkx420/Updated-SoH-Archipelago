"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/dungeons/deku_tree.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    DEKU_TREE_LOBBY_STICK_ACCESS = "Deku Tree Lobby Stick Access"
    DEKU_TREE_LOBBY_NUT_ACCESS = "Deku Tree Lobby Nut Access"
    DEKU_TREE_LOBBY_DEKU_TREE_1F_BROKE_WEB = "Deku Tree Lobby Deku Tree 1f Broke Web"
    DEKU_TREE_LOBBY_3F_DEKU_TREE_1F_BROKE_WEB = "Deku Tree Lobby 3F Deku Tree 1f Broke Web"
    DEKU_TREE_COMPASS_ROOM_STICK_ACCESS = "Deku Tree Compass Room Stick Access"
    DEKU_TREE_COMPASS_ROOM_NUT_ACCESS = "Deku Tree Compass Room Nut Access"
    DEKU_TREE_BASEMENT_LOWER_STICK_ACCESS = "Deku Tree Basement Lower Stick Access"
    DEKU_TREE_BASEMENT_LOWER_NUT_ACCESS = "Deku Tree Basement Lower Nut Access"
    DEKU_TREE_BASEMENT_LOWER_DEKU_TREE_B1_BROKE_WEB = "Deku Tree Basement Lower Deku Tree B1 Broke Web"
    DEKU_TREE_BASEMENT_TORCH_ROOM_STICK_ACCESS = "Deku Tree Basement Torch Room Stick Access"
    DEKU_TREE_BASEMENT_TORCH_ROOM_NUT_ACCESS = "Deku Tree Basement Torch Room Nut Access"
    DEKU_TREE_BASEMENT_BACK_LOBBY_STICK_ACCESS = "Deku Tree Basement Back Lobby Stick Access"
    DEKU_TREE_BASEMENT_BACK_LOBBY_NUT_ACCESS = "Deku Tree Basement Back Lobby Nut Access"
    DEKU_TREE_BASEMENT_UPPER_STICK_ACCESS = "Deku Tree Basement Upper Stick Access"
    DEKU_TREE_BASEMENT_UPPER_NUT_ACCESS = "Deku Tree Basement Upper Nut Access"
    DEKU_TREE_BASEMENT_UPPER_DEKU_TREE_PUSHED_BASEMENT_BLOCK = "Deku Tree Basement Upper Deku Tree Pushed Basement Block"
    DEKU_TREE_BASEMENT_UPPER_DEKU_TREE_B1_BROKE_WEB = "Deku Tree Basement Upper Deku Tree B1 Broke Web"
    DEKU_TREE_BOSS_ROOM_DEKU_TREE_CLEAR = "Deku Tree Boss Room Deku Tree Clear"


def set_region_rules(world: "SohWorld") -> None:

    # Deku Tree Entryway  (upstream RR_DEKU_TREE_ENTRYWAY, SCENE_DEKU_TREE)
    # Connections
    connect_regions(Regions.DEKU_TREE_ENTRYWAY, world, [
        (Regions.DEKU_TREE_LOBBY,
         lambda bundle: True_()),
        (Regions.KF_OUTSIDE_DEKU_TREE,
         lambda bundle: True_()),
    ])

    # Deku Tree Lobby  (upstream RR_DEKU_TREE_LOBBY, SCENE_DEKU_TREE)
    # Events
    add_events(Regions.DEKU_TREE_LOBBY, world, [
        (EventLocations.DEKU_TREE_LOBBY_STICK_ACCESS, Events.CAN_FARM_STICKS,
         lambda bundle: can_get_deku_baba_sticks(bundle)),
        (EventLocations.DEKU_TREE_LOBBY_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_get_deku_baba_nuts(bundle)),
        (EventLocations.DEKU_TREE_LOBBY_DEKU_TREE_1F_BROKE_WEB, Events.DEKU_TREE_1F_BROKE_WEB,
         lambda bundle: has_fire_source(bundle)),
    ])
    # Locations
    add_locations(Regions.DEKU_TREE_LOBBY, world, [
        (Locations.DEKU_TREE_LOBBY_LOWER_HEART,
         lambda bundle: can_use(Items.BOOMERANG, bundle)),
        (Locations.DEKU_TREE_LOBBY_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_LOBBY_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_LOBBY_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
    ])
    # Connections
    connect_regions(Regions.DEKU_TREE_LOBBY, world, [
        (Regions.DEKU_TREE_ENTRYWAY,
         lambda bundle: True_()),
        (Regions.DEKU_TREE_LOBBY_2F,
         lambda bundle: has_climb(bundle) | can_use(Items.HOOKSHOT, bundle)),
        (Regions.DEKU_TREE_BASEMENT_LOWER,
         lambda bundle: has_item(Events.DEKU_TREE_1F_BROKE_WEB, bundle)),
        (Regions.DEKU_TREE_OUTSIDE_BOSS_ROOM,
         lambda bundle: False_()),
        (Regions.DEKU_TREE_BOSS_ENTRYWAY,
         lambda bundle: False_()),
    ])

    # Deku Tree Lobby 2F  (upstream RR_DEKU_TREE_LOBBY_2F, SCENE_DEKU_TREE)
    # Locations
    add_locations(Regions.DEKU_TREE_LOBBY_2F, world, [
        (Locations.DEKU_TREE_MAP_CHEST,
         lambda bundle: can_open_large_chest(bundle)),
        (Locations.DEKU_TREE_LOBBY_LOWER_HEART,
         lambda bundle: True_()),
        (Locations.DEKU_TREE_2F_GRASS_1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_2F_GRASS_2,
         lambda bundle: can_cut_shrubs(bundle)),
    ])
    # Connections
    connect_regions(Regions.DEKU_TREE_LOBBY_2F, world, [
        (Regions.DEKU_TREE_LOBBY,
         lambda bundle: True_()),
        (Regions.DEKU_TREE_LOBBY_3F,
         lambda bundle: has_climb(bundle) | can_use(Items.LONGSHOT, bundle)),
        (Regions.DEKU_TREE_2F_MIDDLE_ROOM,
         lambda bundle: True_()),
    ])

    # Deku Tree Lobby 3F  (upstream RR_DEKU_TREE_LOBBY_3F, SCENE_DEKU_TREE)
    # Events
    add_events(Regions.DEKU_TREE_LOBBY_3F, world, [
        (EventLocations.DEKU_TREE_LOBBY_3F_DEKU_TREE_1F_BROKE_WEB, Events.DEKU_TREE_1F_BROKE_WEB,
         lambda bundle: can_pass_enemy(bundle, Enemies.BIG_SKULLTULA)),
    ])
    # Locations
    add_locations(Regions.DEKU_TREE_LOBBY_3F, world, [
        (Locations.DEKU_TREE_LOBBY_UPPER_HEART,
         lambda bundle: can_pass_enemy(bundle, Enemies.BIG_SKULLTULA)),
    ])
    # Connections
    connect_regions(Regions.DEKU_TREE_LOBBY_3F, world, [
        (Regions.DEKU_TREE_LOBBY_2F,
         lambda bundle: True_()),
        (Regions.DEKU_TREE_COMPASS_ROOM,
         lambda bundle: True_()),
    ])

    # Deku Tree 2F Middle Room  (upstream RR_DEKU_TREE_2F_MIDDLE_ROOM, SCENE_DEKU_TREE)
    # Connections
    connect_regions(Regions.DEKU_TREE_2F_MIDDLE_ROOM, world, [
        (Regions.DEKU_TREE_LOBBY_2F,
         lambda bundle: any_age_time(bundle, lambda bundle: can_reflect_nuts(bundle) | can_use(Items.MEGATON_HAMMER, bundle))),
        (Regions.DEKU_TREE_SLINGSHOT_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: can_reflect_nuts(bundle) | can_use(Items.MEGATON_HAMMER, bundle))),
    ])

    # Deku Tree Slingshot Room  (upstream RR_DEKU_TREE_SLINGSHOT_ROOM, SCENE_DEKU_TREE)
    # Locations
    add_locations(Regions.DEKU_TREE_SLINGSHOT_ROOM, world, [
        (Locations.DEKU_TREE_SLINGSHOT_CHEST,
         lambda bundle: can_open_large_chest(bundle)),
        (Locations.DEKU_TREE_SLINGSHOT_ROOM_SIDE_CHEST,
         lambda bundle: (has_climb(bundle) | can_use(Items.HOOKSHOT, bundle)) & has_open_chest(bundle)),
        (Locations.DEKU_TREE_SLINGSHOT_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_SLINGSHOT_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_SLINGSHOT_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_SLINGSHOT_GRASS4,
         lambda bundle: can_cut_shrubs(bundle)),
    ])
    # Connections
    connect_regions(Regions.DEKU_TREE_SLINGSHOT_ROOM, world, [
        (Regions.DEKU_TREE_2F_MIDDLE_ROOM,
         lambda bundle: True_()),
    ])

    # Deku Tree Compass Room  (upstream RR_DEKU_TREE_COMPASS_ROOM, SCENE_DEKU_TREE)
    # Events
    add_events(Regions.DEKU_TREE_COMPASS_ROOM, world, [
        (EventLocations.DEKU_TREE_COMPASS_ROOM_STICK_ACCESS, Events.CAN_FARM_STICKS,
         lambda bundle: can_get_deku_baba_sticks(bundle)),
        (EventLocations.DEKU_TREE_COMPASS_ROOM_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_get_deku_baba_nuts(bundle)),
    ])
    # Locations
    add_locations(Regions.DEKU_TREE_COMPASS_ROOM, world, [
        (Locations.DEKU_TREE_COMPASS_CHEST,
         lambda bundle: can_open_large_chest(bundle)),
        (Locations.DEKU_TREE_COMPASS_ROOM_SIDE_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.DEKU_TREE_GS_COMPASS_ROOM,
         lambda bundle: can_attack(bundle)),
        (Locations.DEKU_TREE_COMPASS_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_COMPASS_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
    ])
    # Connections
    connect_regions(Regions.DEKU_TREE_COMPASS_ROOM, world, [
        (Regions.DEKU_TREE_LOBBY_3F,
         lambda bundle: has_fire_source_with_torch(bundle) | can_use(Items.FAIRY_BOW, bundle)),
        (Regions.DEKU_TREE_BOSS_ENTRYWAY,
         lambda bundle: False_()),
    ])

    # Deku Tree Basement Lower  (upstream RR_DEKU_TREE_BASEMENT_LOWER, SCENE_DEKU_TREE)
    # Events
    add_events(Regions.DEKU_TREE_BASEMENT_LOWER, world, [
        (EventLocations.DEKU_TREE_BASEMENT_LOWER_STICK_ACCESS, Events.CAN_FARM_STICKS,
         lambda bundle: can_get_deku_baba_sticks(bundle)),
        (EventLocations.DEKU_TREE_BASEMENT_LOWER_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_get_deku_baba_nuts(bundle)),
        (EventLocations.DEKU_TREE_BASEMENT_LOWER_DEKU_TREE_B1_BROKE_WEB, Events.DEKU_TREE_B1_BROKE_WEB,
         lambda bundle: (can_use(Items.STICKS, bundle) & (has_item(Events.DEKU_TREE_PUSHED_BASEMENT_BLOCK, bundle) | is_adult(bundle) | can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle))) | (can_do_trick(Tricks.DEKU_B1_BOW_WEBS, bundle) & is_adult(bundle) & can_use(Items.FAIRY_BOW, bundle))),
    ])
    # Locations
    add_locations(Regions.DEKU_TREE_BASEMENT_LOWER, world, [
        (Locations.DEKU_TREE_BASEMENT_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.DEKU_TREE_GS_BASEMENT_GATE,
         lambda bundle: can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.SHORT_JUMPSLASH)),
        (Locations.DEKU_TREE_GS_BASEMENT_VINES,
         lambda bundle: ((can_do_trick(Tricks.DEKU_MQ_COMPASS_GS, bundle)) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.SHORT_JUMPSLASH) | (trick_disabled(Tricks.DEKU_MQ_COMPASS_GS, bundle)) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOMB_THROW)) & (has_climb(bundle) | can_use(Items.HOOKSHOT, bundle) | can_use(Items.BOOMERANG, bundle))),
        (Locations.DEKU_TREE_BASEMENT_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_BASEMENT_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
    ])
    # Connections
    connect_regions(Regions.DEKU_TREE_BASEMENT_LOWER, world, [
        (Regions.DEKU_TREE_LOBBY,
         lambda bundle: has_climb(bundle) | (is_adult(bundle) & can_use(Items.LONGSHOT, bundle))),
        (Regions.DEKU_TREE_BASEMENT_SCRUB_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: has_fire_source_with_torch(bundle) | can_use(Items.FAIRY_BOW, bundle))),
        (Regions.DEKU_TREE_BASEMENT_UPPER,
         lambda bundle: is_adult(bundle) | bunny_hood(bundle) | can_do_trick(Tricks.DEKU_B1_SKIP, bundle) | can_ground_jump(bundle) | has_item(Events.DEKU_TREE_PUSHED_BASEMENT_BLOCK, bundle)),
        (Regions.DEKU_TREE_OUTSIDE_BOSS_ROOM,
         lambda bundle: False_()),
    ])

    # Deku Tree Basement Scrub Room  (upstream RR_DEKU_TREE_BASEMENT_SCRUB_ROOM, SCENE_DEKU_TREE)
    # Locations
    add_locations(Regions.DEKU_TREE_BASEMENT_SCRUB_ROOM, world, [
        (Locations.DEKU_TREE_EYE_SWITCH_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_EYE_SWITCH_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_EYE_SWITCH_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_EYE_SWITCH_GRASS4,
         lambda bundle: can_cut_shrubs(bundle)),
    ])
    # Connections
    connect_regions(Regions.DEKU_TREE_BASEMENT_SCRUB_ROOM, world, [
        (Regions.DEKU_TREE_BASEMENT_LOWER,
         lambda bundle: True_()),
        (Regions.DEKU_TREE_BASEMENT_WATER_ROOM_FRONT,
         lambda bundle: any_age_time(bundle, lambda bundle: can_hit_eye_targets(bundle))),
    ])

    # Deku Tree Basement Water Room Front  (upstream RR_DEKU_TREE_BASEMENT_WATER_ROOM_FRONT, SCENE_DEKU_TREE)
    # Connections
    connect_regions(Regions.DEKU_TREE_BASEMENT_WATER_ROOM_FRONT, world, [
        (Regions.DEKU_TREE_BASEMENT_SCRUB_ROOM,
         lambda bundle: True_()),
        (Regions.DEKU_TREE_BASEMENT_WATER_ROOM_BACK,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_do_trick(Tricks.DEKU_B1_BACKFLIP_OVER_SPIKED_LOG, bundle)),
    ])

    # Deku Tree Basement Water Room Back  (upstream RR_DEKU_TREE_BASEMENT_WATER_ROOM_BACK, SCENE_DEKU_TREE)
    # Locations
    add_locations(Regions.DEKU_TREE_BASEMENT_WATER_ROOM_BACK, world, [
        (Locations.DEKU_TREE_SPIKE_ROLLER_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_SPIKE_ROLLER_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
    ])
    # Connections
    connect_regions(Regions.DEKU_TREE_BASEMENT_WATER_ROOM_BACK, world, [
        (Regions.DEKU_TREE_BASEMENT_WATER_ROOM_FRONT,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_do_trick(Tricks.DEKU_B1_BACKFLIP_OVER_SPIKED_LOG, bundle)),
        (Regions.DEKU_TREE_BASEMENT_TORCH_ROOM,
         lambda bundle: True_()),
    ])

    # Deku Tree Basement Torch Room  (upstream RR_DEKU_TREE_BASEMENT_TORCH_ROOM, SCENE_DEKU_TREE)
    # Events
    add_events(Regions.DEKU_TREE_BASEMENT_TORCH_ROOM, world, [
        (EventLocations.DEKU_TREE_BASEMENT_TORCH_ROOM_STICK_ACCESS, Events.CAN_FARM_STICKS,
         lambda bundle: can_get_deku_baba_sticks(bundle)),
        (EventLocations.DEKU_TREE_BASEMENT_TORCH_ROOM_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_get_deku_baba_nuts(bundle)),
    ])
    # Locations
    add_locations(Regions.DEKU_TREE_BASEMENT_TORCH_ROOM, world, [
        (Locations.DEKU_TREE_TORCHES_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_TORCHES_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
    ])
    # Connections
    connect_regions(Regions.DEKU_TREE_BASEMENT_TORCH_ROOM, world, [
        (Regions.DEKU_TREE_BASEMENT_WATER_ROOM_BACK,
         lambda bundle: any_age_time(bundle, lambda bundle: has_fire_source_with_torch(bundle) | can_use(Items.FAIRY_BOW, bundle))),
        (Regions.DEKU_TREE_BASEMENT_BACK_LOBBY,
         lambda bundle: any_age_time(bundle, lambda bundle: has_fire_source_with_torch(bundle) | can_use(Items.FAIRY_BOW, bundle))),
    ])

    # Deku Tree Basement Back Lobby  (upstream RR_DEKU_TREE_BASEMENT_BACK_LOBBY, SCENE_DEKU_TREE)
    # Events
    add_events(Regions.DEKU_TREE_BASEMENT_BACK_LOBBY, world, [
        (EventLocations.DEKU_TREE_BASEMENT_BACK_LOBBY_STICK_ACCESS, Events.CAN_FARM_STICKS,
         lambda bundle: can_get_deku_baba_sticks(bundle)),
        (EventLocations.DEKU_TREE_BASEMENT_BACK_LOBBY_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_get_deku_baba_nuts(bundle)),
    ])
    # Locations
    add_locations(Regions.DEKU_TREE_BASEMENT_BACK_LOBBY, world, [
        (Locations.DEKU_TREE_LARVAE_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_LARVAE_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
    ])
    # Connections
    connect_regions(Regions.DEKU_TREE_BASEMENT_BACK_LOBBY, world, [
        (Regions.DEKU_TREE_BASEMENT_TORCH_ROOM,
         lambda bundle: True_()),
        (Regions.DEKU_TREE_BASEMENT_BACK_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: has_fire_source_with_torch(bundle) | can_use(Items.FAIRY_BOW, bundle)) & any_age_time(bundle, lambda bundle: blast_or_smash(bundle))),
        (Regions.DEKU_TREE_BASEMENT_UPPER,
         lambda bundle: any_age_time(bundle, lambda bundle: has_fire_source_with_torch(bundle) | can_use(Items.FAIRY_BOW, bundle)) & has_crawl(bundle)),
    ])

    # Deku Tree Basement Back Room  (upstream RR_DEKU_TREE_BASEMENT_BACK_ROOM, SCENE_DEKU_TREE)
    # Locations
    add_locations(Regions.DEKU_TREE_BASEMENT_BACK_ROOM, world, [
        (Locations.DEKU_TREE_GS_BASEMENT_BACK_ROOM,
         lambda bundle: hookshot_or_boomerang(bundle)),
    ])
    # Connections
    connect_regions(Regions.DEKU_TREE_BASEMENT_BACK_ROOM, world, [
        (Regions.DEKU_TREE_BASEMENT_BACK_LOBBY,
         lambda bundle: True_()),
    ])

    # Deku Tree Basement Upper  (upstream RR_DEKU_TREE_BASEMENT_UPPER, SCENE_DEKU_TREE)
    # Events
    add_events(Regions.DEKU_TREE_BASEMENT_UPPER, world, [
        (EventLocations.DEKU_TREE_BASEMENT_UPPER_STICK_ACCESS, Events.CAN_FARM_STICKS,
         lambda bundle: can_get_deku_baba_sticks(bundle)),
        (EventLocations.DEKU_TREE_BASEMENT_UPPER_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_get_deku_baba_nuts(bundle)),
        (EventLocations.DEKU_TREE_BASEMENT_UPPER_DEKU_TREE_PUSHED_BASEMENT_BLOCK, Events.DEKU_TREE_PUSHED_BASEMENT_BLOCK,
         lambda bundle: has_grab(bundle)),
        (EventLocations.DEKU_TREE_BASEMENT_UPPER_DEKU_TREE_B1_BROKE_WEB, Events.DEKU_TREE_B1_BROKE_WEB,
         lambda bundle: has_fire_source(bundle)),
    ])
    # Locations
    add_locations(Regions.DEKU_TREE_BASEMENT_UPPER, world, [
        (Locations.DEKU_TREE_FINAL_ROOM_LEFT_BACK_HEART,
         lambda bundle: can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)),
    ])
    # Connections
    connect_regions(Regions.DEKU_TREE_BASEMENT_UPPER, world, [
        (Regions.DEKU_TREE_BASEMENT_LOWER,
         lambda bundle: True_()),
        (Regions.DEKU_TREE_BASEMENT_BACK_LOBBY,
         lambda bundle: has_crawl(bundle)),
        (Regions.DEKU_TREE_OUTSIDE_BOSS_ROOM,
         lambda bundle: has_item(Events.DEKU_TREE_B1_BROKE_WEB, bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle))),
    ])

    # Deku Tree Outside Boss Room  (upstream RR_DEKU_TREE_OUTSIDE_BOSS_ROOM, SCENE_DEKU_TREE)
    # Locations
    add_locations(Regions.DEKU_TREE_OUTSIDE_BOSS_ROOM, world, [
        (Locations.DEKU_TREE_FINAL_ROOM_LEFT_FRONT_HEART,
         lambda bundle: is_adult(bundle) | (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.DEKU_TREE_FINAL_ROOM_LEFT_BACK_HEART,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle) | ((can_use(Items.HOVER_BOOTS, bundle) | is_adult(bundle)) & (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.DEKU_TREE_FINAL_ROOM_RIGHT_HEART,
         lambda bundle: is_adult(bundle) | (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.DEKU_TREE_BEFORE_BOSS_GRASS1,
         lambda bundle: can_cut_shrubs(bundle) & has_fire_source_with_torch(bundle)),
        (Locations.DEKU_TREE_BEFORE_BOSS_GRASS2,
         lambda bundle: can_cut_shrubs(bundle) & has_fire_source_with_torch(bundle)),
        (Locations.DEKU_TREE_BEFORE_BOSS_GRASS3,
         lambda bundle: can_cut_shrubs(bundle) & has_fire_source_with_torch(bundle)),
    ])
    # Connections
    connect_regions(Regions.DEKU_TREE_OUTSIDE_BOSS_ROOM, world, [
        (Regions.DEKU_TREE_BASEMENT_UPPER,
         lambda bundle: has_climb(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.HOOKSHOT, bundle))),
        (Regions.DEKU_TREE_BOSS_ENTRYWAY,
         lambda bundle: any_age_time(bundle, lambda bundle: can_reflect_nuts(bundle))),
    ])

    # Deku Tree Boss Entryway  (upstream RR_DEKU_TREE_BOSS_ENTRYWAY, SCENE_DEKU_TREE)
    # Connections
    connect_regions(Regions.DEKU_TREE_BOSS_ENTRYWAY, world, [
        (Regions.DEKU_TREE_BOSS_ROOM,
         lambda bundle: True_()),
    ])

    # Deku Tree Boss Exit  (upstream RR_DEKU_TREE_BOSS_EXIT, SCENE_DEKU_TREE)
    # Connections
    connect_regions(Regions.DEKU_TREE_BOSS_EXIT, world, [
        (Regions.DEKU_TREE_OUTSIDE_BOSS_ROOM,
         lambda bundle: True_()),
    ])

    # Deku Tree Boss Room  (upstream RR_DEKU_TREE_BOSS_ROOM, SCENE_DEKU_TREE_BOSS)
    # Events
    add_events(Regions.DEKU_TREE_BOSS_ROOM, world, [
        (EventLocations.DEKU_TREE_BOSS_ROOM_DEKU_TREE_CLEAR, Events.DEKU_TREE_COMPLETED,
         lambda bundle: can_kill_enemy(bundle, Enemies.GOHMA)),
    ])
    # Locations
    add_locations(Regions.DEKU_TREE_BOSS_ROOM, world, [
        (Locations.QUEEN_GOHMA,
         lambda bundle: has_item(Events.DEKU_TREE_COMPLETED, bundle)),
        (Locations.DEKU_TREE_QUEEN_GOHMA_HEART_CONTAINER,
         lambda bundle: has_item(Events.DEKU_TREE_COMPLETED, bundle)),
        (Locations.DEKU_TREE_QUEEN_GOHMA_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_QUEEN_GOHMA_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_QUEEN_GOHMA_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_QUEEN_GOHMA_GRASS4,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_QUEEN_GOHMA_GRASS5,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_QUEEN_GOHMA_GRASS6,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_QUEEN_GOHMA_GRASS7,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DEKU_TREE_QUEEN_GOHMA_GRASS8,
         lambda bundle: can_cut_shrubs(bundle)),
    ])
    # Connections
    connect_regions(Regions.DEKU_TREE_BOSS_ROOM, world, [
        (Regions.DEKU_TREE_BOSS_EXIT,
         lambda bundle: True_()),
        (Regions.KF_OUTSIDE_DEKU_TREE,
         lambda bundle: has_item(Events.DEKU_TREE_COMPLETED, bundle)),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_FARM_NUTS', 'CAN_FARM_STICKS', 'DEKU_TREE_1F_BROKE_WEB', 'DEKU_TREE_B1_BROKE_WEB', 'DEKU_TREE_COMPLETED', 'DEKU_TREE_PUSHED_BASEMENT_BLOCK']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (0): []
