"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/dungeons/dodongos_cavern.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    DODONGOS_CAVERN_LOBBY_FAIRY_ACCESS = "Dodongos Cavern Lobby Fairy Access"
    DODONGOS_CAVERN_LOBBY_DC_EYES_LIT = "Dodongos Cavern Lobby Dc Eyes Lit"
    DODONGOS_CAVERN_LOBBY_SWITCH_DC_STAIRS_ROOM_DOOR = "Dodongos Cavern Lobby Switch Dc Stairs Room Door"
    DODONGOS_CAVERN_LOWER_LIZALFOS_DC_KILLED_LOWER_LIZALFOS = "Dodongos Cavern Lower Lizalfos Dc Killed Lower Lizalfos"
    DODONGOS_CAVERN_FAR_BRIDGE_DC_EYES_LIT = "Dodongos Cavern Far Bridge Dc Eyes Lit"
    DODONGOS_CAVERN_FAR_BRIDGE_DC_LIFT_PLATFORM = "Dodongos Cavern Far Bridge Dc Lift Platform"
    DODONGOS_CAVERN_BOSS_AREA_FAIRY_ACCESS = "Dodongos Cavern Boss Region Fairy Access"
    DODONGOS_CAVERN_BOSS_ROOM_DODONGOS_CAVERN_CLEAR = "Dodongos Cavern Boss Room Dodongos Cavern Clear"


def set_region_rules(world: "SohWorld") -> None:

    # Dodongos Cavern Entryway  (upstream RR_DODONGOS_CAVERN_ENTRYWAY, SCENE_DODONGOS_CAVERN)
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_ENTRYWAY, world, [
        (Regions.DODONGOS_CAVERN_BEGINNING,
         lambda bundle: True_()),
        (Regions.DEATH_MOUNTAIN_TRAIL,
         lambda bundle: True_()),
    ])

    # Dodongos Cavern Beginning  (upstream RR_DODONGOS_CAVERN_BEGINNING, SCENE_DODONGOS_CAVERN)
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_BEGINNING, world, [
        (Regions.DODONGOS_CAVERN_ENTRYWAY,
         lambda bundle: True_()),
        (Regions.DODONGOS_CAVERN_LOBBY,
         lambda bundle: any_age_time(bundle, lambda bundle: can_break_mud_walls(bundle) | has_item(Items.GORONS_BRACELET, bundle))),
    ])

    # Dodongos Cavern Lobby  (upstream RR_DODONGOS_CAVERN_LOBBY, SCENE_DODONGOS_CAVERN)
    # Events
    add_events(Regions.DODONGOS_CAVERN_LOBBY, world, [
        (EventLocations.DODONGOS_CAVERN_LOBBY_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: (any_age_time(bundle, lambda bundle: can_break_mud_walls(bundle)) | has_item(Items.GORONS_BRACELET, bundle)) & call_gossip_fairy(bundle)),
        (EventLocations.DODONGOS_CAVERN_LOBBY_DC_EYES_LIT, Events.DC_EYES_LIT,
         lambda bundle: (can_do_trick(Tricks.DC_EYES_CHU, bundle) & can_use(Items.BOMBCHUS_5, bundle)) | (can_do_trick(Tricks.DC_EYES_BUNNYHOVERS, bundle) & has_item(Items.GORONS_BRACELET, bundle) & bunny_hovers(bundle))),
    ])
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_LOBBY, world, [
        (Locations.DODONGOS_CAVERN_MAP_CHEST,
         lambda bundle: (can_break_mud_walls(bundle) | has_item(Items.GORONS_BRACELET, bundle)) & can_open_large_chest(bundle)),
        (Locations.DODONGOS_CAVERN_DEKU_SCRUB_LOBBY,
         lambda bundle: (can_stun_deku(bundle) | has_item(Items.GORONS_BRACELET, bundle)) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.DODONGOS_CAVERN_DEKU_SCRUB_LOBBY, bundle)),
        (Locations.DODONGOS_CAVERN_GOSSIP_STONE_FAIRY,
         lambda bundle: any_age_time(bundle, lambda bundle: can_break_mud_walls(bundle) | has_item(Items.GORONS_BRACELET, bundle)) & call_gossip_fairy(bundle)),
        (Locations.DODONGOS_CAVERN_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: any_age_time(bundle, lambda bundle: can_break_mud_walls(bundle) | has_item(Items.GORONS_BRACELET, bundle)) & can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_DODONGOS_CAVERN_GOSSIP_STONE: AnyAgeTime([]{return logic->CanBreakMudWalls() || logic->HasItem(RG_GORONS_BRACELET); })
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_LOBBY, world, [
        (Regions.DODONGOS_CAVERN_BEGINNING,
         lambda bundle: True_()),
        (Regions.DODONGOS_CAVERN_LOBBY_SWITCH,
         lambda bundle: is_adult(bundle) | can_ground_jump(bundle, True)),
        (Regions.DODONGOS_CAVERN_SE_CORRIDOR,
         lambda bundle: any_age_time(bundle, lambda bundle: can_break_mud_walls(bundle) | has_item(Items.GORONS_BRACELET, bundle))),
        (Regions.DODONGOS_CAVERN_STAIRS_LOWER,
         lambda bundle: has_item(Events.DC_STAIRS_ROOM_DOOR, bundle)),
        (Regions.DODONGOS_CAVERN_FAR_BRIDGE,
         lambda bundle: has_item(Events.DC_LIFT_PLATFORM, bundle)),
        (Regions.DODONGOS_CAVERN_BOSS_AREA,
         lambda bundle: has_item(Events.DC_EYES_LIT, bundle)),
        (Regions.DODONGOS_CAVERN_BOSS_ENTRYWAY,
         lambda bundle: False_()),
    ])

    # Dodongos Cavern Lobby Switch  (upstream RR_DODONGOS_CAVERN_LOBBY_SWITCH, SCENE_DODONGOS_CAVERN)
    # Events
    add_events(Regions.DODONGOS_CAVERN_LOBBY_SWITCH, world, [
        (EventLocations.DODONGOS_CAVERN_LOBBY_SWITCH_DC_STAIRS_ROOM_DOOR, Events.DC_STAIRS_ROOM_DOOR,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_LOBBY_SWITCH, world, [
        (Regions.DODONGOS_CAVERN_LOBBY,
         lambda bundle: True_()),
        (Regions.DODONGOS_CAVERN_DODONGO_ROOM,
         lambda bundle: True_()),
    ])

    # Dodongos Cavern SE Corridor  (upstream RR_DODONGOS_CAVERN_SE_CORRIDOR, SCENE_DODONGOS_CAVERN)
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_SE_CORRIDOR, world, [
        (Locations.DODONGOS_CAVERN_GS_SCARECROW,
         lambda bundle: reach_scarecrow(bundle) | (is_adult(bundle) & can_use(Items.LONGSHOT, bundle)) | (can_do_trick(Tricks.DC_SCARECROW_GS, bundle) & has_grab(bundle) & (is_adult(bundle) | can_use(Items.LONGSHOT, bundle)) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA))),
        (Locations.DODONGOS_CAVERN_SIDE_ROOM_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_SIDE_ROOM_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_SIDE_ROOM_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_SIDE_ROOM_POT4,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_SE_CORRIDOR, world, [
        (Regions.DODONGOS_CAVERN_LOBBY,
         lambda bundle: True_()),
        (Regions.DODONGOS_CAVERN_SE_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: can_break_mud_walls(bundle) | can_attack(bundle) | (take_damage(bundle) & can_shield(bundle) & has_grab(bundle)))),
        (Regions.DODONGOS_CAVERN_NEAR_LOWER_LIZALFOS,
         lambda bundle: has_grab(bundle)),
    ])

    # Dodongos Cavern SE Room  (upstream RR_DODONGOS_CAVERN_SE_ROOM, SCENE_DODONGOS_CAVERN)
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_SE_ROOM, world, [
        (Locations.DODONGOS_CAVERN_GS_SIDE_ROOM_NEAR_LOWER_LIZALFOS,
         lambda bundle: can_attack(bundle)),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_SE_ROOM, world, [
        (Regions.DODONGOS_CAVERN_SE_CORRIDOR,
         lambda bundle: True_()),
    ])

    # Dodongos Cavern Near Lower Lizalfos  (upstream RR_DODONGOS_CAVERN_NEAR_LOWER_LIZALFOS, SCENE_DODONGOS_CAVERN)
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_NEAR_LOWER_LIZALFOS, world, [
        (Locations.DODONGOS_CAVERN_NEAR_LOWER_LIZALFOS_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_NEAR_LOWER_LIZALFOS_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_NEAR_LOWER_LIZALFOS, world, [
        (Regions.DODONGOS_CAVERN_SE_CORRIDOR,
         lambda bundle: True_()),
        (Regions.DODONGOS_CAVERN_LOWER_LIZALFOS,
         lambda bundle: True_()),
    ])

    # Dodongos Cavern Lower Lizalfos  (upstream RR_DODONGOS_CAVERN_LOWER_LIZALFOS, SCENE_DODONGOS_CAVERN)
    # Events
    add_events(Regions.DODONGOS_CAVERN_LOWER_LIZALFOS, world, [
        (EventLocations.DODONGOS_CAVERN_LOWER_LIZALFOS_DC_KILLED_LOWER_LIZALFOS, Events.DC_KILLED_LOWER_LIZALFOS,
         lambda bundle: can_kill_enemy(bundle, Enemies.LIZALFOS, EnemyDistance.CLOSE, True, 2)),
    ])
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_LOWER_LIZALFOS, world, [
        (Locations.DODONGOS_CAVERN_LIZALFOS_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_LIZALFOS_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_LIZALFOS_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_LIZALFOS_POT4,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_LOWER_LIZALFOS_ROOM_LAVAFALL_HEART,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_LOWER_LIZALFOS, world, [
        (Regions.DODONGOS_CAVERN_NEAR_LOWER_LIZALFOS,
         lambda bundle: has_item(Events.DC_KILLED_LOWER_LIZALFOS, bundle)),
        (Regions.DODONGOS_CAVERN_DODONGO_ROOM,
         lambda bundle: has_item(Events.DC_KILLED_LOWER_LIZALFOS, bundle)),
    ])

    # Dodongos Cavern Dodongo Room  (upstream RR_DODONGOS_CAVERN_DODONGO_ROOM, SCENE_DODONGOS_CAVERN)
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_DODONGO_ROOM, world, [
        (Locations.DODONGOS_CAVERN_TORCH_ROOM_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_TORCH_ROOM_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_TORCH_ROOM_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_TORCH_ROOM_POT4,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_DODONGO_ROOM, world, [
        (Regions.DODONGOS_CAVERN_LOBBY_SWITCH,
         lambda bundle: has_fire_source_with_torch(bundle)),
        (Regions.DODONGOS_CAVERN_LOWER_LIZALFOS,
         lambda bundle: True_()),
        (Regions.DODONGOS_CAVERN_NEAR_DODONGO_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: can_break_mud_walls(bundle) | has_item(Items.GORONS_BRACELET, bundle))),
    ])

    # Dodongos Cavern Near Dodongo Room  (upstream RR_DODONGOS_CAVERN_NEAR_DODONGO_ROOM, SCENE_DODONGOS_CAVERN)
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_NEAR_DODONGO_ROOM, world, [
        (Locations.DODONGOS_CAVERN_DEKU_SCRUB_SIDE_ROOM_NEAR_DODONGOS,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.DODONGOS_CAVERN_DEKU_SCRUB_SIDE_ROOM_NEAR_DODONGOS, bundle)),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_NEAR_DODONGO_ROOM, world, [
        (Regions.DODONGOS_CAVERN_DODONGO_ROOM,
         lambda bundle: True_()),
    ])

    # Dodongos Cavern Stairs Lower  (upstream RR_DODONGOS_CAVERN_STAIRS_LOWER, SCENE_DODONGOS_CAVERN)
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_STAIRS_LOWER, world, [
        (Locations.DODONGOS_CAVERN_GS_ALCOVE_ABOVE_STAIRS,
         lambda bundle: can_do_trick(Tricks.DC_ALCOVE_GS, bundle) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.LONGSHOT)),
        (Locations.DODONGOS_CAVERN_GS_VINES_ABOVE_STAIRS,
         lambda bundle: can_do_trick(Tricks.DC_VINES_GS, bundle) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.LONGSHOT)),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_STAIRS_LOWER, world, [
        (Regions.DODONGOS_CAVERN_LOBBY,
         lambda bundle: True_()),
        (Regions.DODONGOS_CAVERN_STAIRS_UPPER,
         lambda bundle: has_explosives(bundle) | has_item(Items.GORONS_BRACELET, bundle) | can_use(Items.DINS_FIRE, bundle) | (can_do_trick(Tricks.DC_STAIRS_WITH_BOW, bundle) & can_use(Items.FAIRY_BOW, bundle))),
        (Regions.DODONGOS_CAVERN_COMPASS_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: can_break_mud_walls(bundle) | has_item(Items.GORONS_BRACELET, bundle))),
    ])

    # Dodongos Cavern Stairs Upper  (upstream RR_DODONGOS_CAVERN_STAIRS_UPPER, SCENE_DODONGOS_CAVERN)
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_STAIRS_UPPER, world, [
        (Locations.DODONGOS_CAVERN_GS_ALCOVE_ABOVE_STAIRS,
         lambda bundle: ((has_item(Events.DC_LIFT_PLATFORM, bundle)) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG) | can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.LONGSHOT))),
        (Locations.DODONGOS_CAVERN_GS_VINES_ABOVE_STAIRS,
         lambda bundle: (has_climb(bundle) & has_grab(bundle)) | can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG)),
        (Locations.DODONGOS_CAVERN_STAIRCASE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_STAIRCASE_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_STAIRCASE_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_STAIRCASE_POT4,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_STAIRS_UPPER, world, [
        (Regions.DODONGOS_CAVERN_STAIRS_LOWER,
         lambda bundle: True_()),
        (Regions.DODONGOS_CAVERN_ARMOS_ROOM,
         lambda bundle: True_()),
    ])

    # Dodongos Cavern Compass Room  (upstream RR_DODONGOS_CAVERN_COMPASS_ROOM, SCENE_DODONGOS_CAVERN)
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_COMPASS_ROOM, world, [
        (Locations.DODONGOS_CAVERN_COMPASS_CHEST,
         lambda bundle: can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_COMPASS_ROOM, world, [
        (Regions.DODONGOS_CAVERN_STAIRS_LOWER,
         lambda bundle: can_use(Items.MASTER_SWORD, bundle) | can_use(Items.BIGGORONS_SWORD, bundle) | can_use(Items.MEGATON_HAMMER, bundle) | has_explosives(bundle) | has_item(Items.GORONS_BRACELET, bundle)),
    ])

    # Dodongos Cavern Armos Room  (upstream RR_DODONGOS_CAVERN_ARMOS_ROOM, SCENE_DODONGOS_CAVERN)
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_ARMOS_ROOM, world, [
        (Regions.DODONGOS_CAVERN_STAIRS_UPPER,
         lambda bundle: True_()),
        (Regions.DODONGOS_CAVERN_BOMB_ROOM_LOWER,
         lambda bundle: is_adult(bundle) | (has_grab(bundle) & has_climb(bundle)) | can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) | can_use(Items.HOOKSHOT, bundle)),
    ])

    # Dodongos Cavern Entrance Side Bridge  (upstream RR_DODONGOS_CAVERN_ENTRANCE_SIDE_BRIDGE, SCENE_DODONGOS_CAVERN)
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_ENTRANCE_SIDE_BRIDGE, world, [
        (Locations.DODONGOS_CAVERN_FIRST_BRIDGE_GRASS,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DODONGOS_CAVERN_BLADE_POT1,
         lambda bundle: can_use(Items.BOOMERANG, bundle)),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_ENTRANCE_SIDE_BRIDGE, world, [
        (Regions.DODONGOS_CAVERN_LOBBY,
         lambda bundle: take_damage(bundle)),
        (Regions.DODONGOS_CAVERN_ARMOS_ROOM,
         lambda bundle: True_()),
        (Regions.DODONGOS_CAVERN_BOMB_ROOM_UPPER,
         lambda bundle: ((is_adult(bundle) | bunny_hood(bundle)) & can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle)) | can_use(Items.HOVER_BOOTS, bundle) | (can_do_trick(Tricks.DAMAGE_BOOST_SIMPLE, bundle) & has_explosives(bundle) & can_jump_slash(bundle))),
    ])

    # Dodongos Cavern Bomb Room Lower  (upstream RR_DODONGOS_CAVERN_BOMB_ROOM_LOWER, SCENE_DODONGOS_CAVERN)
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_BOMB_ROOM_LOWER, world, [
        (Locations.DODONGOS_CAVERN_BOMB_FLOWER_PLATFORM_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.DODONGOS_CAVERN_BLADE_ROOM_HEART,
         lambda bundle: has_grab(bundle)),
        (Locations.DODONGOS_CAVERN_BLADE_ROOM_GRASS,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DODONGOS_CAVERN_BLADE_POT2,
         lambda bundle: can_use(Items.BOOMERANG, bundle)),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_BOMB_ROOM_LOWER, world, [
        (Regions.DODONGOS_CAVERN_ENTRANCE_SIDE_BRIDGE,
         lambda bundle: can_climb_ladder(bundle) | ((is_adult(bundle) | can_middair_ground_jump(bundle, True)) & bunny_hovers(bundle))),
        (Regions.DODONGOS_CAVERN_2F_SIDE_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: can_break_mud_walls(bundle) | (can_do_trick(Tricks.DC_SCRUB_ROOM, bundle) & (is_adult(bundle) | bunny_hood(bundle)) & has_item(Items.GORONS_BRACELET, bundle)))),
        (Regions.DODONGOS_CAVERN_FIRST_SLINGSHOT_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: can_break_mud_walls(bundle) | has_item(Items.GORONS_BRACELET, bundle))),
        (Regions.DODONGOS_CAVERN_BOMB_ROOM_UPPER,
         lambda bundle: (is_adult(bundle) & ((can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & bunny_hood(bundle)) | can_ground_jump(bundle, True) | can_use(Items.HOVER_BOOTS, bundle))) | can_use(Items.LONGSHOT, bundle) | (can_do_trick(Tricks.DAMAGE_BOOST_SIMPLE, bundle) & has_explosives(bundle) & can_jump_slash(bundle)) | can_middair_ground_jump(bundle)),
    ])

    # Dodongos Cavern 2F Side Room  (upstream RR_DODONGOS_CAVERN_2F_SIDE_ROOM, SCENE_DODONGOS_CAVERN)
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_2F_SIDE_ROOM, world, [
        (Locations.DODONGOS_CAVERN_DEKU_SCRUB_NEAR_BOMB_BAG_LEFT,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.DODONGOS_CAVERN_DEKU_SCRUB_NEAR_BOMB_BAG_LEFT, bundle)),
        (Locations.DODONGOS_CAVERN_DEKU_SCRUB_NEAR_BOMB_BAG_RIGHT,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.DODONGOS_CAVERN_DEKU_SCRUB_NEAR_BOMB_BAG_RIGHT, bundle)),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_2F_SIDE_ROOM, world, [
        (Regions.DODONGOS_CAVERN_BOMB_ROOM_LOWER,
         lambda bundle: True_()),
    ])

    # Dodongos Cavern First Slingshot Room  (upstream RR_DODONGOS_CAVERN_FIRST_SLINGSHOT_ROOM, SCENE_DODONGOS_CAVERN)
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_FIRST_SLINGSHOT_ROOM, world, [
        (Locations.DODONGOS_CAVERN_SINGLE_EYE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_SINGLE_EYE_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_SINGLE_EYE_GRASS,
         lambda bundle: can_cut_shrubs(bundle)),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_FIRST_SLINGSHOT_ROOM, world, [
        (Regions.DODONGOS_CAVERN_BOMB_ROOM_LOWER,
         lambda bundle: True_()),
        (Regions.DODONGOS_CAVERN_UPPER_LIZALFOS,
         lambda bundle: can_hit_eye_targets(bundle) | can_do_trick(Tricks.DC_SLINGSHOT_SKIP, bundle) | (is_adult(bundle) & can_ground_jump(bundle)) | can_use(Items.HOVER_BOOTS, bundle)),
    ])

    # Dodongos Cavern Upper Lizalfos  (upstream RR_DODONGOS_CAVERN_UPPER_LIZALFOS, SCENE_DODONGOS_CAVERN)
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_UPPER_LIZALFOS, world, [
        (Locations.DODONGOS_CAVERN_LOWER_LIZALFOS_ROOM_LAVAFALL_HEART,
         lambda bundle: True_()),
        (Locations.DODONGOS_CAVERN_UPPER_LIZALFOS_ROOM_LEFT_HEART,
         lambda bundle: True_()),
        (Locations.DODONGOS_CAVERN_UPPER_LIZALFOS_ROOM_RIGHT_HEART,
         lambda bundle: True_()),
        (Locations.DODONGOS_CAVERN_LIZALFOS_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_LIZALFOS_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_LIZALFOS_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_LIZALFOS_POT4,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_LOWER_LIZALFOS_ROOM_LAVAFALL_HEART,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_UPPER_LIZALFOS, world, [
        (Regions.DODONGOS_CAVERN_FIRST_SLINGSHOT_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.LIZALFOS, EnemyDistance.CLOSE, True, 2))),
        (Regions.DODONGOS_CAVERN_SECOND_SLINGSHOT_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.LIZALFOS, EnemyDistance.CLOSE, True, 2))),
        (Regions.DODONGOS_CAVERN_NEAR_LOWER_LIZALFOS,
         lambda bundle: has_item(Events.DC_KILLED_LOWER_LIZALFOS, bundle)),
        (Regions.DODONGOS_CAVERN_DODONGO_ROOM,
         lambda bundle: has_item(Events.DC_KILLED_LOWER_LIZALFOS, bundle)),
    ])

    # Dodongos Cavern Second Slingshot Room  (upstream RR_DODONGOS_CAVERN_SECOND_SLINGSHOT_ROOM, SCENE_DODONGOS_CAVERN)
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_SECOND_SLINGSHOT_ROOM, world, [
        (Locations.DODONGOS_CAVERN_DOUBLE_EYE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_DOUBLE_EYE_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_SECOND_SLINGSHOT_ROOM, world, [
        (Regions.DODONGOS_CAVERN_UPPER_LIZALFOS,
         lambda bundle: True_()),
        (Regions.DODONGOS_CAVERN_BOMB_ROOM_UPPER,
         lambda bundle: can_hit_eye_targets(bundle) | can_do_trick(Tricks.DC_SLINGSHOT_SKIP, bundle) | (is_adult(bundle) & can_ground_jump(bundle)) | can_recoil_hover(bundle, Recoil.SWORD_AND_SHIELD) | bunny_hovers(bundle)),
    ])

    # Dodongos Cavern Bomb Room Upper  (upstream RR_DODONGOS_CAVERN_BOMB_ROOM_UPPER, SCENE_DODONGOS_CAVERN)
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_BOMB_ROOM_UPPER, world, [
        (Locations.DODONGOS_CAVERN_BOMB_BAG_CHEST,
         lambda bundle: can_open_large_chest(bundle)),
        (Locations.DODONGOS_CAVERN_BLADE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_BLADE_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_BOMB_ROOM_UPPER, world, [
        (Regions.DODONGOS_CAVERN_ENTRANCE_SIDE_BRIDGE,
         lambda bundle: True_()),
        (Regions.DODONGOS_CAVERN_BOMB_ROOM_LOWER,
         lambda bundle: True_()),
        (Regions.DODONGOS_CAVERN_SECOND_SLINGSHOT_ROOM,
         lambda bundle: True_()),
        (Regions.DODONGOS_CAVERN_FAR_BRIDGE,
         lambda bundle: True_()),
    ])

    # Dodongos Cavern Far Bridge  (upstream RR_DODONGOS_CAVERN_FAR_BRIDGE, SCENE_DODONGOS_CAVERN)
    # Events
    add_events(Regions.DODONGOS_CAVERN_FAR_BRIDGE, world, [
        (EventLocations.DODONGOS_CAVERN_FAR_BRIDGE_DC_EYES_LIT, Events.DC_EYES_LIT,
         lambda bundle: has_explosives(bundle)),
        (EventLocations.DODONGOS_CAVERN_FAR_BRIDGE_DC_LIFT_PLATFORM, Events.DC_LIFT_PLATFORM,
         lambda bundle: True_()),
    ])
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_FAR_BRIDGE, world, [
        (Locations.DODONGOS_CAVERN_END_OF_BRIDGE_CHEST,
         lambda bundle: can_break_mud_walls(bundle) & has_open_chest(bundle)),
        (Locations.DODONGOS_CAVERN_TOP_FLOOR_PEDESTAL,
         lambda bundle: can_read(bundle)),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_FAR_BRIDGE, world, [
        (Regions.DODONGOS_CAVERN_LOBBY,
         lambda bundle: True_()),
        (Regions.DODONGOS_CAVERN_LOBBY_SWITCH,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle) | (can_do_trick(Tricks.DC_CHILD_LOBBY, bundle) & can_jump_slash_except_hammer(bundle) & take_damage(bundle))),
        (Regions.DODONGOS_CAVERN_BOMB_ROOM_UPPER,
         lambda bundle: True_()),
    ])

    # Dodongos Cavern Boss Region  (upstream RR_DODONGOS_CAVERN_BOSS_AREA, SCENE_DODONGOS_CAVERN)
    # Events
    add_events(Regions.DODONGOS_CAVERN_BOSS_AREA, world, [
        (EventLocations.DODONGOS_CAVERN_BOSS_AREA_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_BOSS_AREA, world, [
        (Locations.DODONGOS_CAVERN_BEFORE_BOSS_GRASS,
         lambda bundle: can_cut_shrubs(bundle)),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_BOSS_AREA, world, [
        (Regions.DODONGOS_CAVERN_LOBBY,
         lambda bundle: True_()),
        (Regions.DODONGOS_CAVERN_BACK_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: can_break_mud_walls(bundle))),
        (Regions.DODONGOS_CAVERN_BOSS_ENTRYWAY,
         lambda bundle: has_grab(bundle)),
    ])

    # Dodongos Cavern Back Room  (upstream RR_DODONGOS_CAVERN_BACK_ROOM, SCENE_DODONGOS_CAVERN)
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_BACK_ROOM, world, [
        (Locations.DODONGOS_CAVERN_GS_BACK_ROOM,
         lambda bundle: can_attack(bundle)),
        (Locations.DODONGOS_CAVERN_BACK_ROOM_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_BACK_ROOM_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_BACK_ROOM_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DODONGOS_CAVERN_BACK_ROOM_POT4,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_BACK_ROOM, world, [
        (Regions.DODONGOS_CAVERN_BOSS_AREA,
         lambda bundle: True_()),
    ])

    # Dodongos Cavern Boss Entryway  (upstream RR_DODONGOS_CAVERN_BOSS_ENTRYWAY, SCENE_DODONGOS_CAVERN)
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_BOSS_ENTRYWAY, world, [
        (Regions.DODONGOS_CAVERN_BOSS_ROOM,
         lambda bundle: True_()),
    ])

    # Dodongos Cavern Boss Exit  (upstream RR_DODONGOS_CAVERN_BOSS_EXIT, SCENE_DODONGOS_CAVERN)
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_BOSS_EXIT, world, [
        (Regions.DODONGOS_CAVERN_BOSS_AREA,
         lambda bundle: True_()),
    ])

    # Dodongos Cavern Boss Room  (upstream RR_DODONGOS_CAVERN_BOSS_ROOM, SCENE_DODONGOS_CAVERN_BOSS)
    # Events
    add_events(Regions.DODONGOS_CAVERN_BOSS_ROOM, world, [
        (EventLocations.DODONGOS_CAVERN_BOSS_ROOM_DODONGOS_CAVERN_CLEAR, Events.DODONGOS_CAVERN_COMPLETED,
         lambda bundle: any_age_time(bundle, lambda bundle: has_explosives(bundle) | (((can_do_trick(Tricks.DC_HAMMER_FLOOR, bundle)) & can_use(Items.MEGATON_HAMMER, bundle) | (can_do_trick(Tricks.BLUE_FIRE_MUD_WALLS, bundle) & blue_fire(bundle)) | (trick_disabled(Tricks.DC_HAMMER_FLOOR, bundle)) & can_do_trick(Tricks.BLUE_FIRE_MUD_WALLS, bundle) & can_use(Items.BOTTLE_WITH_BLUE_FIRE, bundle)))) & can_kill_enemy(bundle, Enemies.KING_DODONGO)),
    ])
    # Locations
    add_locations(Regions.DODONGOS_CAVERN_BOSS_ROOM, world, [
        (Locations.DODONGOS_CAVERN_BOSS_ROOM_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.DODONGOS_CAVERN_KING_DODONGO_HEART_CONTAINER,
         lambda bundle: has_item(Events.DODONGOS_CAVERN_COMPLETED, bundle)),
        (Locations.KING_DODONGO,
         lambda bundle: has_item(Events.DODONGOS_CAVERN_COMPLETED, bundle)),
    ])
    # Connections
    connect_regions(Regions.DODONGOS_CAVERN_BOSS_ROOM, world, [
        (Regions.DODONGOS_CAVERN_BOSS_EXIT,
         lambda bundle: True_()),
        (Regions.DEATH_MOUNTAIN_TRAIL,
         lambda bundle: has_item(Events.DODONGOS_CAVERN_COMPLETED, bundle)),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_FAIRIES', 'DC_EYES_LIT', 'DC_KILLED_LOWER_LIZALFOS', 'DC_LIFT_PLATFORM', 'DC_STAIRS_ROOM_DOOR', 'DODONGOS_CAVERN_COMPLETED']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (1): ['RC_DODONGOS_CAVERN_GOSSIP_STONE']
