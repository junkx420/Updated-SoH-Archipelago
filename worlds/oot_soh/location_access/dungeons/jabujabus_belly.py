"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/dungeons/jabujabus_belly.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    JABU_JABUS_BELLY_HOLES_ROOM_JABU_RUTO_IN_B1 = "Jabu Jabus Belly Holes Room Jabu Ruto In B1"
    JABU_JABUS_BELLY_B1_JIGGLY_FAIRY_ACCESS = "Jabu Jabus Belly B1 Jiggly Fairy Access"
    JABU_JABUS_BELLY_WATER_SWITCH_ROOM_NORTH_JABU_RUTO_IN_1F = "Jabu Jabus Belly Water Switch Room North Jabu Ruto In 1f"
    JABU_JABUS_BELLY_WATER_SWITCH_ROOM_LEDGE_FAIRY_ACCESS = "Jabu Jabus Belly Water Switch Room Ledge Fairy Access"
    JABU_JABUS_BELLY_FORK_WEST_JABU_WEST_TENTACLE = "Jabu Jabus Belly Fork West Jabu West Tentacle"
    JABU_JABUS_BELLY_FORK_NORTH_JABU_NORTH_TENTACLE = "Jabu Jabus Belly Fork North Jabu North Tentacle"
    JABU_JABUS_BELLY_FORK_NORTH_EAST_JABU_EAST_TENTACLE = "Jabu Jabus Belly Fork North East Jabu East Tentacle"
    JABU_JABUS_BELLY_ABOVE_BIGOCTO_FAIRY_ACCESS = "Jabu Jabus Belly Above Big Octo Fairy Access"
    JABU_JABUS_BELLY_ABOVE_BIGOCTO_NUT_ACCESS = "Jabu Jabus Belly Above Big Octo Nut Access"
    JABU_JABUS_BELLY_LIFT_UPPER_JABU_LOWERED_PATH = "Jabu Jabus Belly Lift Upper Jabu Lowered Path"
    JABU_JABUS_BELLY_BOSS_ROOM_JABU_JABUS_BELLY_CLEAR = "Jabu Jabus Belly Boss Room Jabu Jabus Belly Clear"


def set_region_rules(world: "SohWorld") -> None:

    # Jabu Jabus Belly Entryway  (upstream RR_JABU_JABUS_BELLY_ENTRYWAY, SCENE_JABU_JABU)
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_ENTRYWAY, world, [
        (Regions.JABU_JABUS_BELLY_BEGINNING,
         lambda bundle: True_()),
        (Regions.ZORAS_FOUNTAIN,
         lambda bundle: True_()),
    ])

    # Jabu Jabus Belly Beginning  (upstream RR_JABU_JABUS_BELLY_BEGINNING, SCENE_JABU_JABU)
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_BEGINNING, world, [
        (Regions.JABU_JABUS_BELLY_ENTRYWAY,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_LIFT_ROOM,
         lambda bundle: can_use_projectile(bundle)),
    ])

    # Jabu Jabus Belly Lift Room  (upstream RR_JABU_JABUS_BELLY_LIFT_ROOM, SCENE_JABU_JABU)
    # Locations
    add_locations(Regions.JABU_JABUS_BELLY_LIFT_ROOM, world, [
        (Locations.JABU_JABUS_BELLY_DEKU_SCRUB,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) & (is_child(bundle) | has_item(Items.SILVER_SCALE, bundle) | can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) | can_use(Items.IRON_BOOTS, bundle)) & can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.JABU_JABUS_BELLY_DEKU_SCRUB, bundle)),
        (Locations.JABU_JABUS_BELLY_PLATFORM_ROOM_SMALL_CRATE1,
         lambda bundle: can_break_small_crates(bundle)),
        (Locations.JABU_JABUS_BELLY_PLATFORM_ROOM_SMALL_CRATE2,
         lambda bundle: can_break_small_crates(bundle)),
    ])
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_LIFT_ROOM, world, [
        (Regions.JABU_JABUS_BELLY_BEGINNING,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_HOLES_ROOM,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_WATER_SWITCH_ROOM_SOUTH,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_NEAR_BOSS_ROOM,
         lambda bundle: (has_item(Events.JABU_LOWERED_PATH, bundle) | ((can_do_trick(Tricks.JABU_BOSS_HOVER, bundle) | bunny_hood(bundle)) & can_use(Items.HOVER_BOOTS, bundle))) & has_grab(bundle)),
    ])

    # Jabu Jabus Belly Holes Room  (upstream RR_JABU_JABUS_BELLY_HOLES_ROOM, SCENE_JABU_JABU)
    # Events
    add_events(Regions.JABU_JABUS_BELLY_HOLES_ROOM, world, [
        (EventLocations.JABU_JABUS_BELLY_HOLES_ROOM_JABU_RUTO_IN_B1, Events.JABU_RUTO_IN_B1,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_HOLES_ROOM, world, [
        (Regions.JABU_JABUS_BELLY_LIFT_ROOM,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_FORKED_CORRIDOR,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_HOLES_LOWER_DOOR_LEDGE,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_BIGOCTO_LEDGE,
         lambda bundle: has_item(Events.JABU_NORTH_TENTACLE, bundle)),
    ])

    # Jabu Jabus Belly Holes Basement  (upstream RR_JABU_JABUS_BELLY_HOLES_BASEMENT, SCENE_JABU_JABU)
    # Locations
    add_locations(Regions.JABU_JABUS_BELLY_HOLES_BASEMENT, world, [
        (Locations.JABU_JABUS_BELLY_GS_LOBBY_BASEMENT_LOWER,
         lambda bundle: hookshot_or_boomerang(bundle)),
        (Locations.JABU_JABUS_BELLY_GS_LOBBY_BASEMENT_UPPER,
         lambda bundle: hookshot_or_boomerang(bundle)),
    ])
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_HOLES_BASEMENT, world, [
        (Regions.JABU_JABUS_BELLY_HOLES_ROOM,
         lambda bundle: has_climb(bundle)),
        (Regions.JABU_JABUS_BELLY_B1_JIGGLY,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_HOLES_LOWER_DOOR_LEDGE,
         lambda bundle: is_adult(bundle)),
    ])

    # Jabu Jabus Belly Holes Lower Door Ledge  (upstream RR_JABU_JABUS_BELLY_HOLES_LOWER_DOOR_LEDGE, SCENE_JABU_JABU)
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_HOLES_LOWER_DOOR_LEDGE, world, [
        (Regions.JABU_JABUS_BELLY_HOLES_BASEMENT,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_WATER_SWITCH_ROOM_NORTH,
         lambda bundle: True_()),
    ])

    # Jabu Jabus Belly B1 Jiggly  (upstream RR_JABU_JABUS_BELLY_B1_JIGGLY, SCENE_JABU_JABU)
    # Events
    add_events(Regions.JABU_JABUS_BELLY_B1_JIGGLY, world, [
        (EventLocations.JABU_JABUS_BELLY_B1_JIGGLY_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: can_use(Items.BOOMERANG, bundle) | (can_break_pots(bundle) & can_do_trick(Tricks.JABU_B1_CUBE_HOVER, bundle) & can_use(Items.HOVER_BOOTS, bundle))),
    ])
    # Locations
    add_locations(Regions.JABU_JABUS_BELLY_B1_JIGGLY, world, [
        (Locations.JABU_JABUS_BELLY_TWO_OCTOROK_POT1,
         lambda bundle: can_use(Items.BOOMERANG, bundle) | (can_break_pots(bundle) & (can_do_trick(Tricks.JABU_B1_CUBE_HOVER, bundle) | bunny_hood(bundle)) & can_use(Items.HOVER_BOOTS, bundle))),
        (Locations.JABU_JABUS_BELLY_TWO_OCTOROK_POT2,
         lambda bundle: can_use(Items.BOOMERANG, bundle) | (can_break_pots(bundle) & (can_do_trick(Tricks.JABU_B1_CUBE_HOVER, bundle) | bunny_hood(bundle)) & can_use(Items.HOVER_BOOTS, bundle))),
        (Locations.JABU_JABUS_BELLY_TWO_OCTOROK_POT3,
         lambda bundle: can_use(Items.BOOMERANG, bundle) | (can_break_pots(bundle) & (can_do_trick(Tricks.JABU_B1_CUBE_HOVER, bundle) | bunny_hood(bundle)) & can_use(Items.HOVER_BOOTS, bundle))),
        (Locations.JABU_JABUS_BELLY_TWO_OCTOROK_POT4,
         lambda bundle: can_use(Items.BOOMERANG, bundle) | (can_break_pots(bundle) & (can_do_trick(Tricks.JABU_B1_CUBE_HOVER, bundle) | bunny_hood(bundle)) & can_use(Items.HOVER_BOOTS, bundle))),
        (Locations.JABU_JABUS_BELLY_TWO_OCTOROK_POT5,
         lambda bundle: can_use(Items.BOOMERANG, bundle) | (can_break_pots(bundle) & (can_do_trick(Tricks.JABU_B1_CUBE_HOVER, bundle) | bunny_hood(bundle)) & can_use(Items.HOVER_BOOTS, bundle))),
    ])
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_B1_JIGGLY, world, [
        (Regions.JABU_JABUS_BELLY_HOLES_BASEMENT,
         lambda bundle: True_()),
    ])

    # Jabu Jabus Belly Water Switch Room North  (upstream RR_JABU_JABUS_BELLY_WATER_SWITCH_ROOM_NORTH, SCENE_JABU_JABU)
    # Events
    add_events(Regions.JABU_JABUS_BELLY_WATER_SWITCH_ROOM_NORTH, world, [
        (EventLocations.JABU_JABUS_BELLY_WATER_SWITCH_ROOM_NORTH_JABU_RUTO_IN_1F, Events.JABU_RUTO_IN_1F,
         lambda bundle: has_item(Events.JABU_RUTO_IN_B1, bundle) & (is_adult(bundle) | has_item(Items.BRONZE_SCALE, bundle)) & has_speak(bundle, "ZORA") & has_grab(bundle)),
    ])
    # Locations
    add_locations(Regions.JABU_JABUS_BELLY_WATER_SWITCH_ROOM_NORTH, world, [
        (Locations.JABU_JABUS_BELLY_GS_WATER_SWITCH_ROOM,
         lambda bundle: can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG)),
    ])
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_WATER_SWITCH_ROOM_NORTH, world, [
        (Regions.JABU_JABUS_BELLY_WATER_SWITCH_ROOM_LEDGE,
         lambda bundle: (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.HOVER_BOOTS, bundle)) & has_climb(bundle)),
        (Regions.JABU_JABUS_BELLY_WATER_SWITCH_ROOM_SOUTH,
         lambda bundle: is_adult(bundle) | has_item(Items.BRONZE_SCALE, bundle)),
        (Regions.JABU_JABUS_BELLY_HOLES_LOWER_DOOR_LEDGE,
         lambda bundle: True_()),
    ])

    # Jabu Jabus Belly Water Switch Room South  (upstream RR_JABU_JABUS_BELLY_WATER_SWITCH_ROOM_SOUTH, SCENE_JABU_JABU)
    # Locations
    add_locations(Regions.JABU_JABUS_BELLY_WATER_SWITCH_ROOM_SOUTH, world, [
        (Locations.JABU_JABUS_BELLY_GS_WATER_SWITCH_ROOM,
         lambda bundle: can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG)),
    ])
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_WATER_SWITCH_ROOM_SOUTH, world, [
        (Regions.JABU_JABUS_BELLY_WATER_SWITCH_ROOM_NORTH,
         lambda bundle: is_adult(bundle) | has_item(Items.BRONZE_SCALE, bundle)),
        (Regions.JABU_JABUS_BELLY_WATER_SWITCH_ROOM_LEDGE,
         lambda bundle: (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.HOVER_BOOTS, bundle)) & has_climb(bundle)),
        (Regions.JABU_JABUS_BELLY_LIFT_ROOM,
         lambda bundle: can_hit_switch(bundle, EnemyDistance.BOMB_THROW)),
    ])

    # Jabu Jabus Belly Water Switch Room Ledge  (upstream RR_JABU_JABUS_BELLY_WATER_SWITCH_ROOM_LEDGE, SCENE_JABU_JABU)
    # Events
    add_events(Regions.JABU_JABUS_BELLY_WATER_SWITCH_ROOM_LEDGE, world, [
        (EventLocations.JABU_JABUS_BELLY_WATER_SWITCH_ROOM_LEDGE_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Locations
    add_locations(Regions.JABU_JABUS_BELLY_WATER_SWITCH_ROOM_LEDGE, world, [
        (Locations.JABU_JABUS_BELLY_GS_WATER_SWITCH_ROOM,
         lambda bundle: has_grab(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | (is_adult(bundle) & can_use(Items.HOVER_BOOTS, bundle))) | can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOMB_THROW)),
        (Locations.JABU_JABUS_BELLY_BASEMENT_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.JABU_JABUS_BELLY_BASEMENT_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.JABU_JABUS_BELLY_BASEMENT_POT3,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_WATER_SWITCH_ROOM_LEDGE, world, [
        (Regions.JABU_JABUS_BELLY_WATER_SWITCH_ROOM_NORTH,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_WATER_SWITCH_ROOM_SOUTH,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_LIFT_ROOM,
         lambda bundle: has_grab(bundle)),
    ])

    # Jabu Jabus Belly Forked Corridor  (upstream RR_JABU_JABUS_BELLY_FORKED_CORRIDOR, SCENE_JABU_JABU)
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_FORKED_CORRIDOR, world, [
        (Regions.JABU_JABUS_BELLY_HOLES_ROOM,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_FORK_WEST,
         lambda bundle: has_item(Events.JABU_RUTO_IN_1F, bundle)),
        (Regions.JABU_JABUS_BELLY_TO_FORK_NORTH_WEST,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_TO_FORK_NORTH,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_TO_FORK_NORTH_EAST,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_FORK_EAST,
         lambda bundle: has_item(Events.JABU_RUTO_IN_1F, bundle)),
    ])

    # Jabu Jabus Belly Fork West  (upstream RR_JABU_JABUS_BELLY_FORK_WEST, SCENE_JABU_JABU)
    # Events
    add_events(Regions.JABU_JABUS_BELLY_FORK_WEST, world, [
        (EventLocations.JABU_JABUS_BELLY_FORK_WEST_JABU_WEST_TENTACLE, Events.JABU_WEST_TENTACLE,
         lambda bundle: can_kill_enemy(bundle, Enemies.TENTACLE, EnemyDistance.BOOMERANG)),
    ])
    # Locations
    add_locations(Regions.JABU_JABUS_BELLY_FORK_WEST, world, [
        (Locations.JABU_JABUS_BELLY_MAP_CHEST,
         lambda bundle: has_item(Events.JABU_WEST_TENTACLE, bundle) & can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_FORK_WEST, world, [
        (Regions.JABU_JABUS_BELLY_FORKED_CORRIDOR,
         lambda bundle: True_()),
    ])

    # Jabu Jabus Belly To Fork North West  (upstream RR_JABU_JABUS_BELLY_TO_FORK_NORTH_WEST, SCENE_JABU_JABU)
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_TO_FORK_NORTH_WEST, world, [
        (Regions.JABU_JABUS_BELLY_FORKED_CORRIDOR,
         lambda bundle: has_item(Events.JABU_WEST_TENTACLE, bundle) | take_damage(bundle)),
        (Regions.JABU_JABUS_BELLY_FORK_NORTH_WEST,
         lambda bundle: has_item(Events.JABU_WEST_TENTACLE, bundle)),
    ])

    # Jabu Jabus Belly Fork North West  (upstream RR_JABU_JABUS_BELLY_FORK_NORTH_WEST, SCENE_JABU_JABU)
    # Locations
    add_locations(Regions.JABU_JABUS_BELLY_FORK_NORTH_WEST, world, [
        (Locations.JABU_JABUS_BELLY_COMPASS_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.SHABOM, EnemyDistance.CLOSE, False, 9) & can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_FORK_NORTH_WEST, world, [
        (Regions.JABU_JABUS_BELLY_TO_FORK_NORTH_WEST,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.SHABOM, EnemyDistance.CLOSE, False, 9))),
    ])

    # Jabu Jabus Belly To Fork North  (upstream RR_JABU_JABUS_BELLY_TO_FORK_NORTH, SCENE_JABU_JABU)
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_TO_FORK_NORTH, world, [
        (Regions.JABU_JABUS_BELLY_FORKED_CORRIDOR,
         lambda bundle: has_item(Events.JABU_EAST_TENTACLE, bundle) | take_damage(bundle)),
        (Regions.JABU_JABUS_BELLY_FORK_NORTH,
         lambda bundle: has_item(Events.JABU_EAST_TENTACLE, bundle)),
    ])

    # Jabu Jabus Belly Fork North  (upstream RR_JABU_JABUS_BELLY_FORK_NORTH, SCENE_JABU_JABU)
    # Events
    add_events(Regions.JABU_JABUS_BELLY_FORK_NORTH, world, [
        (EventLocations.JABU_JABUS_BELLY_FORK_NORTH_JABU_NORTH_TENTACLE, Events.JABU_NORTH_TENTACLE,
         lambda bundle: can_kill_enemy(bundle, Enemies.TENTACLE, EnemyDistance.BOOMERANG)),
    ])
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_FORK_NORTH, world, [
        (Regions.JABU_JABUS_BELLY_TO_FORK_NORTH,
         lambda bundle: has_item(Events.JABU_NORTH_TENTACLE, bundle)),
    ])

    # Jabu Jabus Belly To Fork North East  (upstream RR_JABU_JABUS_BELLY_TO_FORK_NORTH_EAST, SCENE_JABU_JABU)
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_TO_FORK_NORTH_EAST, world, [
        (Regions.JABU_JABUS_BELLY_FORKED_CORRIDOR,
         lambda bundle: has_item(Events.JABU_WEST_TENTACLE, bundle) | take_damage(bundle)),
        (Regions.JABU_JABUS_BELLY_FORK_NORTH_EAST,
         lambda bundle: has_item(Events.JABU_WEST_TENTACLE, bundle)),
    ])

    # Jabu Jabus Belly Fork North East  (upstream RR_JABU_JABUS_BELLY_FORK_NORTH_EAST, SCENE_JABU_JABU)
    # Events
    add_events(Regions.JABU_JABUS_BELLY_FORK_NORTH_EAST, world, [
        (EventLocations.JABU_JABUS_BELLY_FORK_NORTH_EAST_JABU_EAST_TENTACLE, Events.JABU_EAST_TENTACLE,
         lambda bundle: can_kill_enemy(bundle, Enemies.TENTACLE, EnemyDistance.BOOMERANG)),
    ])
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_FORK_NORTH_EAST, world, [
        (Regions.JABU_JABUS_BELLY_TO_FORK_NORTH_EAST,
         lambda bundle: has_item(Events.JABU_EAST_TENTACLE, bundle)),
    ])

    # Jabu Jabus Belly Fork East  (upstream RR_JABU_JABUS_BELLY_FORK_EAST, SCENE_JABU_JABU)
    # Locations
    add_locations(Regions.JABU_JABUS_BELLY_FORK_EAST, world, [
        (Locations.JABU_JABUS_BELLY_BOOMERANG_CHEST,
         lambda bundle: (has_item(Events.JABU_RUTO_IN_1F, bundle) | can_kill_enemy(bundle, Enemies.STINGER, EnemyDistance.CLOSE, True, 4)) & can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_FORK_EAST, world, [
        (Regions.JABU_JABUS_BELLY_FORKED_CORRIDOR,
         lambda bundle: True_()),
    ])

    # Jabu Jabus Belly Big Octo Ledge  (upstream RR_JABU_JABUS_BELLY_BIGOCTO_LEDGE, SCENE_JABU_JABU)
    # Locations
    add_locations(Regions.JABU_JABUS_BELLY_BIGOCTO_LEDGE, world, [
        (Locations.JABU_JABUS_BELLY_GS_LOBBY_BASEMENT_UPPER,
         lambda bundle: is_adult(bundle) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.SHORT_JUMPSLASH)),
    ])
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_BIGOCTO_LEDGE, world, [
        (Regions.JABU_JABUS_BELLY_HOLES_BASEMENT,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_BIGOCTO,
         lambda bundle: has_item(Events.JABU_RUTO_IN_1F, bundle) & any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.BIG_OCTO))),
    ])

    # Jabu Jabus Belly Big Octo  (upstream RR_JABU_JABUS_BELLY_BIGOCTO, SCENE_JABU_JABU)
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_BIGOCTO, world, [
        (Regions.JABU_JABUS_BELLY_BIGOCTO_LEDGE,
         lambda bundle: has_item(Events.JABU_RUTO_IN_1F, bundle) & any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.BIG_OCTO))),
        (Regions.JABU_JABUS_BELLY_ABOVE_BIGOCTO,
         lambda bundle: has_item(Events.JABU_RUTO_IN_1F, bundle) & any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.BIG_OCTO))),
    ])

    # Jabu Jabus Belly Above Big Octo  (upstream RR_JABU_JABUS_BELLY_ABOVE_BIGOCTO, SCENE_JABU_JABU)
    # Events
    add_events(Regions.JABU_JABUS_BELLY_ABOVE_BIGOCTO, world, [
        (EventLocations.JABU_JABUS_BELLY_ABOVE_BIGOCTO_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: can_break_pots(bundle)),
        (EventLocations.JABU_JABUS_BELLY_ABOVE_BIGOCTO_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Locations
    add_locations(Regions.JABU_JABUS_BELLY_ABOVE_BIGOCTO, world, [
        (Locations.JABU_JABUS_BELLY_ABOVE_BIG_OCTO_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.JABU_JABUS_BELLY_ABOVE_BIG_OCTO_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.JABU_JABUS_BELLY_ABOVE_BIG_OCTO_POT3,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_ABOVE_BIGOCTO, world, [
        (Regions.JABU_JABUS_BELLY_BIGOCTO,
         lambda bundle: take_damage(bundle)),
        (Regions.JABU_JABUS_BELLY_JIGGLIES_ROOM,
         lambda bundle: True_()),
    ])

    # Jabu Jabus Belly Jigglies Room  (upstream RR_JABU_JABUS_BELLY_JIGGLIES_ROOM, SCENE_JABU_JABU)
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_JIGGLIES_ROOM, world, [
        (Regions.JABU_JABUS_BELLY_ABOVE_BIGOCTO,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_JIGGLIES_LEDGE,
         lambda bundle: can_use(Items.BOOMERANG, bundle) | (is_adult(bundle) & can_ground_jump(bundle))),
    ])

    # Jabu Jabus Belly Jigglies Ledge  (upstream RR_JABU_JABUS_BELLY_JIGGLIES_LEDGE, SCENE_JABU_JABU)
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_JIGGLIES_LEDGE, world, [
        (Regions.JABU_JABUS_BELLY_JIGGLIES_ROOM,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_LIFT_UPPER,
         lambda bundle: True_()),
    ])

    # Jabu Jabus Belly Lift Upper  (upstream RR_JABU_JABUS_BELLY_LIFT_UPPER, SCENE_JABU_JABU)
    # Events
    add_events(Regions.JABU_JABUS_BELLY_LIFT_UPPER, world, [
        (EventLocations.JABU_JABUS_BELLY_LIFT_UPPER_JABU_LOWERED_PATH, Events.JABU_LOWERED_PATH,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_LIFT_UPPER, world, [
        (Regions.JABU_JABUS_BELLY_LIFT_ROOM,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_JIGGLIES_ROOM,
         lambda bundle: True_()),
    ])

    # Jabu Jabus Belly Near Boss Room  (upstream RR_JABU_JABUS_BELLY_NEAR_BOSS_ROOM, SCENE_JABU_JABU)
    # Locations
    add_locations(Regions.JABU_JABUS_BELLY_NEAR_BOSS_ROOM, world, [
        (Locations.JABU_JABUS_BELLY_GS_NEAR_BOSS,
         lambda bundle: can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOMB_THROW) & (has_climb(bundle) | hookshot_or_boomerang(bundle))),
    ])
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_NEAR_BOSS_ROOM, world, [
        (Regions.JABU_JABUS_BELLY_LIFT_ROOM,
         lambda bundle: True_()),
        (Regions.JABU_JABUS_BELLY_BOSS_ENTRYWAY,
         lambda bundle: (has_climb(bundle) & can_use(Items.BOOMERANG, bundle)) | (can_do_trick(Tricks.JABU_NEAR_BOSS_RANGED, bundle) & (((has_climb(bundle)) & can_use(Items.HOOKSHOT, bundle) | (Not(has_climb(bundle))) & can_use(Items.LONGSHOT, bundle)) | can_use(Items.FAIRY_BOW, bundle) | can_use(Items.FAIRY_SLINGSHOT, bundle))) | (can_do_trick(Tricks.JABU_NEAR_BOSS_EXPLOSIVES, bundle) & (can_use(Items.BOMBCHUS_5, bundle) | (can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.BOMB_BAG, bundle) & has_climb(bundle))))),
    ])

    # Jabu Jabus Belly Boss Entryway  (upstream RR_JABU_JABUS_BELLY_BOSS_ENTRYWAY, SCENE_JABU_JABU)
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_BOSS_ENTRYWAY, world, [
        (Regions.JABU_JABUS_BELLY_BOSS_ROOM,
         lambda bundle: True_()),
    ])

    # Jabu Jabus Belly Boss Exit  (upstream RR_JABU_JABUS_BELLY_BOSS_EXIT, SCENE_JABU_JABU)
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_BOSS_EXIT, world, [
        (Regions.JABU_JABUS_BELLY_NEAR_BOSS_ROOM,
         lambda bundle: True_()),
    ])

    # Jabu Jabus Belly Boss Room  (upstream RR_JABU_JABUS_BELLY_BOSS_ROOM, SCENE_JABU_JABU_BOSS)
    # Events
    add_events(Regions.JABU_JABUS_BELLY_BOSS_ROOM, world, [
        (EventLocations.JABU_JABUS_BELLY_BOSS_ROOM_JABU_JABUS_BELLY_CLEAR, Events.JABU_JABUS_BELLY_COMPLETED,
         lambda bundle: can_kill_enemy(bundle, Enemies.BARINADE)),
    ])
    # Locations
    add_locations(Regions.JABU_JABUS_BELLY_BOSS_ROOM, world, [
        (Locations.JABU_JABUS_BELLY_BARINADE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.JABU_JABUS_BELLY_BARINADE_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.JABU_JABUS_BELLY_BARINADE_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.JABU_JABUS_BELLY_BARINADE_POT4,
         lambda bundle: can_break_pots(bundle)),
        (Locations.JABU_JABUS_BELLY_BARINADE_POT5,
         lambda bundle: can_break_pots(bundle)),
        (Locations.JABU_JABUS_BELLY_BARINADE_POT6,
         lambda bundle: can_break_pots(bundle)),
        (Locations.JABU_JABUS_BELLY_BARINADE_HEART_CONTAINER,
         lambda bundle: has_item(Events.JABU_JABUS_BELLY_COMPLETED, bundle)),
        (Locations.BARINADE,
         lambda bundle: has_item(Events.JABU_JABUS_BELLY_COMPLETED, bundle)),
    ])
    # Connections
    connect_regions(Regions.JABU_JABUS_BELLY_BOSS_ROOM, world, [
        (Regions.JABU_JABUS_BELLY_BOSS_EXIT,
         lambda bundle: False_()),
        (Regions.ZORAS_FOUNTAIN,
         lambda bundle: has_item(Events.JABU_JABUS_BELLY_COMPLETED, bundle)),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_FAIRIES', 'CAN_FARM_NUTS', 'JABU_EAST_TENTACLE', 'JABU_JABUS_BELLY_COMPLETED', 'JABU_LOWERED_PATH', 'JABU_NORTH_TENTACLE', 'JABU_RUTO_IN_1F', 'JABU_RUTO_IN_B1', 'JABU_WEST_TENTACLE']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (0): []
