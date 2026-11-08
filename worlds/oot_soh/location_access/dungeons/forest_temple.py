"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/dungeons/forest_temple.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    FOREST_TEMPLE_LOBBY_FOREST_MEG = "Forest Temple Lobby Forest Meg"
    FOREST_TEMPLE_LOWER_STALFOS_FAIRY_ACCESS = "Forest Temple Lower Stalfos Fairy Access"
    FOREST_TEMPLE_LOWER_STALFOS_FOREST_CLEAR_BETWEEN_JOELLE_AND_BETH = "Forest Temple Lower Stalfos Forest Clear Between Joelle And Beth"
    FOREST_TEMPLE_NW_COURTYARD_LOWER_STICK_ACCESS = "Forest Temple NW Courtyard Lower Stick Access"
    FOREST_TEMPLE_NW_COURTYARD_LOWER_NUT_ACCESS = "Forest Temple NW Courtyard Lower Nut Access"
    FOREST_TEMPLE_NW_COURTYARD_UPPER_STICK_ACCESS = "Forest Temple NW Courtyard Upper Stick Access"
    FOREST_TEMPLE_NW_COURTYARD_UPPER_NUT_ACCESS = "Forest Temple NW Courtyard Upper Nut Access"
    FOREST_TEMPLE_NE_COURTYARD_LOWER_STICK_ACCESS = "Forest Temple NE Courtyard Lower Stick Access"
    FOREST_TEMPLE_NE_COURTYARD_LOWER_NUT_ACCESS = "Forest Temple NE Courtyard Lower Nut Access"
    FOREST_TEMPLE_NE_COURTYARD_UPPER_STICK_ACCESS = "Forest Temple NE Courtyard Upper Stick Access"
    FOREST_TEMPLE_NE_COURTYARD_UPPER_NUT_ACCESS = "Forest Temple NE Courtyard Upper Nut Access"
    FOREST_TEMPLE_NE_COURTYARD_SWITCH_FOREST_DRAINED_WELL = "Forest Temple NE Courtyard Switch Forest Drained Well"
    FOREST_TEMPLE_NE_COURTYARD_DOORFRAME_FOREST_SUMMON_NE_SCARECROW = "Forest Temple NE Courtyard Doorframe Forest Summon Ne Scarecrow"
    FOREST_TEMPLE_NE_COURTYARD_SCARECROW_LEDGE_FOREST_SUMMON_NE_SCARECROW = "Forest Temple NE Courtyard Scarecrow Ledge Forest Summon Ne Scarecrow"
    FOREST_TEMPLE_RED_POE_ROOM_FOREST_JOELLE = "Forest Temple Red Poe Room Forest Joelle"
    FOREST_TEMPLE_UPPER_STALFOS_FOREST_CLEAR_BETWEEN_JOELLE_AND_BETH = "Forest Temple Upper Stalfos Forest Clear Between Joelle And Beth"
    FOREST_TEMPLE_BLUE_POE_ROOM_FOREST_BETH = "Forest Temple Blue Poe Room Forest Beth"
    FOREST_TEMPLE_GREEN_POE_ROOM_FOREST_AMY = "Forest Temple Green Poe Room Forest Amy"
    FOREST_TEMPLE_BASEMENT_FOREST_OPEN_BOSS_HALLWAY = "Forest Temple Basement Forest Open Boss Hallway"
    FOREST_TEMPLE_BOSS_ROOM_FOREST_TEMPLE_CLEAR = "Forest Temple Boss Room Forest Temple Clear"


def set_region_rules(world: "SohWorld") -> None:

    # Forest Temple Entryway  (upstream RR_FOREST_TEMPLE_ENTRYWAY, SCENE_FOREST_TEMPLE)
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_ENTRYWAY, world, [
        (Regions.FOREST_TEMPLE_TREES,
         lambda bundle: True_()),
        (Regions.SACRED_FOREST_MEADOW,
         lambda bundle: True_()),
    ])

    # Forest Temple Trees  (upstream RR_FOREST_TEMPLE_TREES, SCENE_FOREST_TEMPLE)
    # Locations
    add_locations(Regions.FOREST_TEMPLE_TREES, world, [
        (Locations.FOREST_TEMPLE_FIRST_ROOM_CHEST,
         lambda bundle: (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)) & has_open_chest(bundle)),
        (Locations.FOREST_TEMPLE_GS_FIRST_ROOM,
         lambda bundle: (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)) & (can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG) | ((is_adult(bundle) | can_do_trick(Tricks.BOMB_DETONATION, bundle)) & can_use(Items.BOMB_BAG, bundle)) | (can_do_trick(Tricks.FOREST_FIRST_GS, bundle) & can_jump_slash_except_hammer(bundle)))),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_TREES, world, [
        (Regions.FOREST_TEMPLE_ENTRYWAY,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_OVERGROWN_HALLWAY_LOWER,
         lambda bundle: True_()),
    ])

    # Forest Temple Overgrown Hallway Lower  (upstream RR_FOREST_TEMPLE_OVERGROWN_HALLWAY_LOWER, SCENE_FOREST_TEMPLE)
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_OVERGROWN_HALLWAY_LOWER, world, [
        (Regions.FOREST_TEMPLE_TREES,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_OVERGROWN_HALLWAY_UPPER,
         lambda bundle: can_pass_enemy(bundle, Enemies.BIG_SKULLTULA)),
    ])

    # Forest Temple Overgrown Hallway Upper  (upstream RR_FOREST_TEMPLE_OVERGROWN_HALLWAY_UPPER, SCENE_FOREST_TEMPLE)
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_OVERGROWN_HALLWAY_UPPER, world, [
        (Regions.FOREST_TEMPLE_OVERGROWN_HALLWAY_LOWER,
         lambda bundle: can_pass_enemy(bundle, Enemies.BIG_SKULLTULA)),
        (Regions.FOREST_TEMPLE_LOBBY,
         lambda bundle: True_()),
    ])

    # Forest Temple Lobby  (upstream RR_FOREST_TEMPLE_LOBBY, SCENE_FOREST_TEMPLE)
    # Events
    add_events(Regions.FOREST_TEMPLE_LOBBY, world, [
        (EventLocations.FOREST_TEMPLE_LOBBY_FOREST_MEG, Events.FOREST_MEG,
         lambda bundle: has_item(Events.FOREST_JOELLE, bundle) & has_item(Events.FOREST_BETH, bundle) & has_item(Events.FOREST_AMY, bundle) & can_kill_enemy(bundle, Enemies.MEG)),
    ])
    # Locations
    add_locations(Regions.FOREST_TEMPLE_LOBBY, world, [
        (Locations.FOREST_TEMPLE_GS_LOBBY,
         lambda bundle: hookshot_or_boomerang(bundle)),
        (Locations.FOREST_TEMPLE_LOBBY_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FOREST_TEMPLE_LOBBY_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FOREST_TEMPLE_LOBBY_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FOREST_TEMPLE_LOBBY_POT4,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FOREST_TEMPLE_LOBBY_POT5,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FOREST_TEMPLE_LOBBY_POT6,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_LOBBY, world, [
        (Regions.FOREST_TEMPLE_OVERGROWN_HALLWAY_UPPER,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_NORTH_HALLWAY,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_NW_COURTYARD_LOWER,
         lambda bundle: can_use(Items.SONG_OF_TIME, bundle) | is_child(bundle)),
        (Regions.FOREST_TEMPLE_NE_COURTYARD_LOWER,
         lambda bundle: can_use(Items.FAIRY_BOW, bundle) | can_use(Items.FAIRY_SLINGSHOT, bundle)),
        (Regions.FOREST_TEMPLE_RED_DOORMAT_HALLWAY,
         lambda bundle: small_keys_scene("SCENE_FOREST_TEMPLE", 1, bundle)),
        (Regions.FOREST_TEMPLE_BLUE_DOORMAT_HALLWAY,
         lambda bundle: False_()),
        (Regions.FOREST_TEMPLE_BASEMENT,
         lambda bundle: has_item(Events.FOREST_MEG, bundle)),
        (Regions.FOREST_TEMPLE_BOSS_ENTRYWAY,
         lambda bundle: False_()),
    ])

    # Forest Temple North Hallway  (upstream RR_FOREST_TEMPLE_NORTH_HALLWAY, SCENE_FOREST_TEMPLE)
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_NORTH_HALLWAY, world, [
        (Regions.FOREST_TEMPLE_LOBBY,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_LOWER_STALFOS,
         lambda bundle: True_()),
    ])

    # Forest Temple Lower Stalfos  (upstream RR_FOREST_TEMPLE_LOWER_STALFOS, SCENE_FOREST_TEMPLE)
    # Events
    add_events(Regions.FOREST_TEMPLE_LOWER_STALFOS, world, [
        (EventLocations.FOREST_TEMPLE_LOWER_STALFOS_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: can_break_pots(bundle)),
        (EventLocations.FOREST_TEMPLE_LOWER_STALFOS_FOREST_CLEAR_BETWEEN_JOELLE_AND_BETH, Events.FOREST_CLEAR_BETWEEN_JOELLE_AND_BETH,
         lambda bundle: can_kill_enemy(bundle, Enemies.STALFOS, EnemyDistance.CLOSE, True, 2)),
    ])
    # Locations
    add_locations(Regions.FOREST_TEMPLE_LOWER_STALFOS, world, [
        (Locations.FOREST_TEMPLE_FIRST_STALFOS_CHEST,
         lambda bundle: has_item(Events.FOREST_CLEAR_BETWEEN_JOELLE_AND_BETH, bundle) & has_open_chest(bundle)),
        (Locations.FOREST_TEMPLE_LOWER_STALFOS_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FOREST_TEMPLE_LOWER_STALFOS_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_LOWER_STALFOS, world, [
        (Regions.FOREST_TEMPLE_NORTH_HALLWAY,
         lambda bundle: has_item(Events.FOREST_CLEAR_BETWEEN_JOELLE_AND_BETH, bundle)),
    ])

    # Forest Temple NW Courtyard Lower  (upstream RR_FOREST_TEMPLE_NW_COURTYARD_LOWER, SCENE_FOREST_TEMPLE)
    # Events
    add_events(Regions.FOREST_TEMPLE_NW_COURTYARD_LOWER, world, [
        (EventLocations.FOREST_TEMPLE_NW_COURTYARD_LOWER_STICK_ACCESS, Events.CAN_FARM_STICKS,
         lambda bundle: can_get_deku_baba_sticks(bundle)),
        (EventLocations.FOREST_TEMPLE_NW_COURTYARD_LOWER_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_get_deku_baba_nuts(bundle)),
    ])
    # Locations
    add_locations(Regions.FOREST_TEMPLE_NW_COURTYARD_LOWER, world, [
        (Locations.FOREST_TEMPLE_GS_LEVEL_ISLAND_COURTYARD,
         lambda bundle: can_use(Items.LONGSHOT, bundle)),
        (Locations.FOREST_TEMPLE_WEST_COURTYARD_RIGHT_HEART,
         lambda bundle: can_use(Items.BOOMERANG, bundle) & can_do_trick(Tricks.FOREST_COURTYARD_HEARTS_BOOMERANG, bundle)),
        (Locations.FOREST_TEMPLE_WEST_COURTYARD_LEFT_HEART,
         lambda bundle: can_use(Items.BOOMERANG, bundle) & can_do_trick(Tricks.FOREST_COURTYARD_HEARTS_BOOMERANG, bundle)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_NW_COURTYARD_LOWER, world, [
        (Regions.FOREST_TEMPLE_LOBBY,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_NW_COURTYARD_UPPER,
         lambda bundle: (has_climb(bundle) | can_use(Items.HOOKSHOT, bundle)) & can_use(Items.HOVER_BOOTS, bundle) & ((can_do_trick(Tricks.HOVER_BOOST_SIMPLE, bundle) & (can_do_trick(Tricks.DAMAGE_BOOST_SIMPLE, bundle) & has_explosives(bundle))) | can_middair_ground_jump(bundle))),
        (Regions.FOREST_TEMPLE_NW_COURTYARD_UPPER_ALCOVE,
         lambda bundle: has_climb(bundle) | can_use(Items.LONGSHOT, bundle)),
        (Regions.FOREST_TEMPLE_SEWER,
         lambda bundle: has_item(Items.GOLDEN_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle)),
        (Regions.FOREST_TEMPLE_DRAINED_SEWER,
         lambda bundle: has_item(Events.FOREST_DRAINED_WELL, bundle)),
        (Regions.FOREST_TEMPLE_BOSS_ENTRYWAY,
         lambda bundle: False_()),
    ])

    # Forest Temple NW Courtyard Upper Alcove  (upstream RR_FOREST_TEMPLE_NW_COURTYARD_UPPER_ALCOVE, SCENE_FOREST_TEMPLE)
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_NW_COURTYARD_UPPER_ALCOVE, world, [
        (Regions.FOREST_TEMPLE_NW_COURTYARD_LOWER,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_MAP_ROOM,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_NW_COURTYARD_UPPER,
         lambda bundle: can_do_trick(Tricks.HOVER_BOOST_SIMPLE, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.MEGATON_HAMMER, bundle)),
    ])

    # Forest Temple NW Courtyard Upper  (upstream RR_FOREST_TEMPLE_NW_COURTYARD_UPPER, SCENE_FOREST_TEMPLE)
    # Events
    add_events(Regions.FOREST_TEMPLE_NW_COURTYARD_UPPER, world, [
        (EventLocations.FOREST_TEMPLE_NW_COURTYARD_UPPER_STICK_ACCESS, Events.CAN_FARM_STICKS,
         lambda bundle: can_get_deku_baba_sticks(bundle)),
        (EventLocations.FOREST_TEMPLE_NW_COURTYARD_UPPER_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_get_deku_baba_nuts(bundle)),
    ])
    # Locations
    add_locations(Regions.FOREST_TEMPLE_NW_COURTYARD_UPPER, world, [
        (Locations.FOREST_TEMPLE_GS_LEVEL_ISLAND_COURTYARD,
         lambda bundle: hookshot_or_boomerang(bundle)),
        (Locations.FOREST_TEMPLE_WEST_COURTYARD_RIGHT_HEART,
         lambda bundle: True_()),
        (Locations.FOREST_TEMPLE_WEST_COURTYARD_LEFT_HEART,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_NW_COURTYARD_UPPER, world, [
        (Regions.FOREST_TEMPLE_NW_COURTYARD_LOWER,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_BELOW_BOSS_KEY_CHEST,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_FLOORMASTER_ROOM,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_BLOCK_PUSH_ROOM_COURTYARD_ALCOVE,
         lambda bundle: True_()),
    ])

    # Forest Temple NE Courtyard Lower  (upstream RR_FOREST_TEMPLE_NE_COURTYARD_LOWER, SCENE_FOREST_TEMPLE)
    # Events
    add_events(Regions.FOREST_TEMPLE_NE_COURTYARD_LOWER, world, [
        (EventLocations.FOREST_TEMPLE_NE_COURTYARD_LOWER_STICK_ACCESS, Events.CAN_FARM_STICKS,
         lambda bundle: can_get_deku_baba_sticks(bundle)),
        (EventLocations.FOREST_TEMPLE_NE_COURTYARD_LOWER_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_get_deku_baba_nuts(bundle)),
    ])
    # Locations
    add_locations(Regions.FOREST_TEMPLE_NE_COURTYARD_LOWER, world, [
        (Locations.FOREST_TEMPLE_GS_RAISED_ISLAND_COURTYARD,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) | (can_do_trick(Tricks.FOREST_COURTYARD_EAST_GS, bundle) & can_use(Items.BOOMERANG, bundle))),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_NE_COURTYARD_LOWER, world, [
        (Regions.FOREST_TEMPLE_LOBBY,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_NE_COURTYARD_SWITCH,
         lambda bundle: can_use(Items.LONGSHOT, bundle) | (can_do_trick(Tricks.FOREST_VINES, bundle) & can_use(Items.HOOKSHOT, bundle) & has_climb(bundle))),
        (Regions.FOREST_TEMPLE_NE_COURTYARD_ISLAND,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
        (Regions.FOREST_TEMPLE_SEWER,
         lambda bundle: (((can_use(Items.IRON_BOOTS, bundle) | can_use(Items.LONGSHOT, bundle) | (can_do_trick(Tricks.FOREST_WELL_SWIM, bundle) & can_use(Items.HOOKSHOT, bundle))) & has_item(Items.BRONZE_SCALE, bundle)) | has_item(Items.GOLDEN_SCALE, bundle)) & water_timer_at_least(bundle, 16)),
        (Regions.FOREST_TEMPLE_DRAINED_SEWER,
         lambda bundle: has_item(Events.FOREST_DRAINED_WELL, bundle)),
    ])

    # Forest Temple NE Courtyard Upper  (upstream RR_FOREST_TEMPLE_NE_COURTYARD_UPPER, SCENE_FOREST_TEMPLE)
    # Events
    add_events(Regions.FOREST_TEMPLE_NE_COURTYARD_UPPER, world, [
        (EventLocations.FOREST_TEMPLE_NE_COURTYARD_UPPER_STICK_ACCESS, Events.CAN_FARM_STICKS,
         lambda bundle: can_get_deku_baba_sticks(bundle)),
        (EventLocations.FOREST_TEMPLE_NE_COURTYARD_UPPER_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_get_deku_baba_nuts(bundle)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_NE_COURTYARD_UPPER, world, [
        (Regions.FOREST_TEMPLE_NE_COURTYARD_LOWER,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_NE_COURTYARD_SWITCH,
         lambda bundle: bunny_hood(bundle) | has_climb(bundle) | (is_adult(bundle) & can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle)) | can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle)),
        (Regions.FOREST_TEMPLE_NE_COURTYARD_DOORFRAME,
         lambda bundle: can_recoil_hover(bundle, Recoil.HAMMER) | ((can_do_trick(Tricks.FOREST_DOORFRAME, bundle) & can_use(Items.HOVER_BOOTS, bundle) & (bunny_hood(bundle) | can_jump_slash(bundle))))),
        (Regions.FOREST_TEMPLE_MAP_ROOM,
         lambda bundle: True_()),
    ])

    # Forest Temple NE Courtyard Switch  (upstream RR_FOREST_TEMPLE_NE_COURTYARD_SWITCH, SCENE_FOREST_TEMPLE)
    # Events
    add_events(Regions.FOREST_TEMPLE_NE_COURTYARD_SWITCH, world, [
        (EventLocations.FOREST_TEMPLE_NE_COURTYARD_SWITCH_FOREST_DRAINED_WELL, Events.FOREST_DRAINED_WELL,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_NE_COURTYARD_SWITCH, world, [
        (Regions.FOREST_TEMPLE_NE_COURTYARD_LOWER,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_NE_COURTYARD_UPPER,
         lambda bundle: bunny_hood(bundle) | (is_adult(bundle) & can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle)) | can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle)),
        (Regions.FOREST_TEMPLE_NE_COURTYARD_ISLAND,
         lambda bundle: ((is_adult(bundle) & can_do_trick(Tricks.FOREST_COURTYARD_LEDGE, bundle)) | bunny_hood(bundle)) & can_use(Items.HOVER_BOOTS, bundle)),
    ])

    # Forest Temple NE Courtyard Doorframe  (upstream RR_FOREST_TEMPLE_NE_COURTYARD_DOORFRAME, SCENE_FOREST_TEMPLE)
    # Events
    add_events(Regions.FOREST_TEMPLE_NE_COURTYARD_DOORFRAME, world, [
        (EventLocations.FOREST_TEMPLE_NE_COURTYARD_DOORFRAME_FOREST_SUMMON_NE_SCARECROW, Events.FOREST_SUMMON_NE_SCARECROW,
         lambda bundle: scarecrows_song(bundle)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_NE_COURTYARD_DOORFRAME, world, [
        (Regions.FOREST_TEMPLE_NE_COURTYARD_LOWER,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_NE_COURTYARD_ISLAND,
         lambda bundle: can_recoil_hover(bundle, Recoil.HAMMER)),
    ])

    # Forest Temple NE Courtyard Island  (upstream RR_FOREST_TEMPLE_NE_COURTYARD_ISLAND, SCENE_FOREST_TEMPLE)
    # Locations
    add_locations(Regions.FOREST_TEMPLE_NE_COURTYARD_ISLAND, world, [
        (Locations.FOREST_TEMPLE_RAISED_ISLAND_COURTYARD_CHEST,
         lambda bundle: has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_NE_COURTYARD_ISLAND, world, [
        (Regions.FOREST_TEMPLE_NE_COURTYARD_LOWER,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_NE_COURTYARD_SCARECROW_LEDGE,
         lambda bundle: has_item(Events.FOREST_SUMMON_NE_SCARECROW, bundle) & can_use(Items.HOOKSHOT, bundle)),
    ])

    # Forest Temple NE Courtyard Scarecrow Ledge  (upstream RR_FOREST_TEMPLE_NE_COURTYARD_SCARECROW_LEDGE, SCENE_FOREST_TEMPLE)
    # Events
    add_events(Regions.FOREST_TEMPLE_NE_COURTYARD_SCARECROW_LEDGE, world, [
        (EventLocations.FOREST_TEMPLE_NE_COURTYARD_SCARECROW_LEDGE_FOREST_SUMMON_NE_SCARECROW, Events.FOREST_SUMMON_NE_SCARECROW,
         lambda bundle: scarecrows_song(bundle)),
    ])
    # Locations
    add_locations(Regions.FOREST_TEMPLE_NE_COURTYARD_SCARECROW_LEDGE, world, [
        (Locations.FOREST_TEMPLE_GS_RAISED_ISLAND_COURTYARD,
         lambda bundle: can_use(Items.FAIRY_BOW, bundle) | can_use(Items.FAIRY_SLINGSHOT, bundle) | can_use(Items.DINS_FIRE, bundle) | has_explosives(bundle)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_NE_COURTYARD_SCARECROW_LEDGE, world, [
        (Regions.FOREST_TEMPLE_NE_COURTYARD_ISLAND,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_FALLING_ROOM,
         lambda bundle: True_()),
    ])

    # Forest Temple Map Room  (upstream RR_FOREST_TEMPLE_MAP_ROOM, SCENE_FOREST_TEMPLE)
    # Locations
    add_locations(Regions.FOREST_TEMPLE_MAP_ROOM, world, [
        (Locations.FOREST_TEMPLE_MAP_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.BLUE_BUBBLE) & can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_MAP_ROOM, world, [
        (Regions.FOREST_TEMPLE_NW_COURTYARD_UPPER_ALCOVE,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.BLUE_BUBBLE))),
        (Regions.FOREST_TEMPLE_NE_COURTYARD_UPPER,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.BLUE_BUBBLE))),
    ])

    # Forest Temple Sewer  (upstream RR_FOREST_TEMPLE_SEWER, SCENE_FOREST_TEMPLE)
    # Locations
    add_locations(Regions.FOREST_TEMPLE_SEWER, world, [
        (Locations.FOREST_TEMPLE_WELL_CHEST,
         lambda bundle: can_open_underwater_chest(bundle) & water_timer_at_least(bundle, 8)),
        (Locations.FOREST_TEMPLE_WELL_EAST_HEART,
         lambda bundle: can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8)),
        (Locations.FOREST_TEMPLE_WELL_WEST_HEART,
         lambda bundle: can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_SEWER, world, [
        (Regions.FOREST_TEMPLE_NW_COURTYARD_LOWER,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle)),
        (Regions.FOREST_TEMPLE_NE_COURTYARD_LOWER,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle)),
    ])

    # Forest Temple Drained Sewer  (upstream RR_FOREST_TEMPLE_DRAINED_SEWER, SCENE_FOREST_TEMPLE)
    # Locations
    add_locations(Regions.FOREST_TEMPLE_DRAINED_SEWER, world, [
        (Locations.FOREST_TEMPLE_WELL_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.FOREST_TEMPLE_WELL_EAST_HEART,
         lambda bundle: True_()),
        (Locations.FOREST_TEMPLE_WELL_WEST_HEART,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_DRAINED_SEWER, world, [
        (Regions.FOREST_TEMPLE_NW_COURTYARD_LOWER,
         lambda bundle: has_climb(bundle) | can_use(Items.HOOKSHOT, bundle)),
        (Regions.FOREST_TEMPLE_NE_COURTYARD_LOWER,
         lambda bundle: has_climb(bundle)),
    ])

    # Forest Temple Below Boss Key Chest  (upstream RR_FOREST_TEMPLE_BELOW_BOSS_KEY_CHEST, SCENE_FOREST_TEMPLE)
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_BELOW_BOSS_KEY_CHEST, world, [
        (Regions.FOREST_TEMPLE_NW_COURTYARD_UPPER,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.BLUE_BUBBLE))),
    ])

    # Forest Temple Floormaster Room  (upstream RR_FOREST_TEMPLE_FLOORMASTER_ROOM, SCENE_FOREST_TEMPLE)
    # Locations
    add_locations(Regions.FOREST_TEMPLE_FLOORMASTER_ROOM, world, [
        (Locations.FOREST_TEMPLE_FLOORMASTER_CHEST,
         lambda bundle: can_damage(bundle) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_FLOORMASTER_ROOM, world, [
        (Regions.FOREST_TEMPLE_NW_COURTYARD_UPPER,
         lambda bundle: True_()),
    ])

    # Forest Temple West Hallway  (upstream RR_FOREST_TEMPLE_RED_DOORMAT_HALLWAY, SCENE_FOREST_TEMPLE)
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_RED_DOORMAT_HALLWAY, world, [
        (Regions.FOREST_TEMPLE_LOBBY,
         lambda bundle: small_keys_scene("SCENE_FOREST_TEMPLE", 1, bundle)),
        (Regions.FOREST_TEMPLE_RED_DOORMAT_HALLWAY_DOORMAT,
         lambda bundle: can_pass_enemy(bundle, Enemies.BIG_SKULLTULA)),
    ])

    # Forest Temple West Hallway Doormat  (upstream RR_FOREST_TEMPLE_RED_DOORMAT_HALLWAY_DOORMAT, SCENE_FOREST_TEMPLE)
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_RED_DOORMAT_HALLWAY_DOORMAT, world, [
        (Regions.FOREST_TEMPLE_RED_DOORMAT_HALLWAY,
         lambda bundle: can_pass_enemy(bundle, Enemies.BIG_SKULLTULA)),
        (Regions.FOREST_TEMPLE_BLOCK_PUSH_FLOOR,
         lambda bundle: True_()),
    ])

    # Forest Temple Lower Block Push Floor  (upstream RR_FOREST_TEMPLE_BLOCK_PUSH_FLOOR, SCENE_FOREST_TEMPLE)
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_BLOCK_PUSH_FLOOR, world, [
        (Regions.FOREST_TEMPLE_RED_DOORMAT_HALLWAY_DOORMAT,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_LOWER_BLOCK_PUSH_ROOM,
         lambda bundle: has_climb(bundle) | (is_adult(bundle) & can_ground_jump(bundle))),
    ])

    # Forest Temple Lower Block Push Room  (upstream RR_FOREST_TEMPLE_LOWER_BLOCK_PUSH_ROOM, SCENE_FOREST_TEMPLE)
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_LOWER_BLOCK_PUSH_ROOM, world, [
        (Regions.FOREST_TEMPLE_BLOCK_PUSH_FLOOR,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_MIDDLE_BLOCK_PUSH_ROOM,
         lambda bundle: has_climb(bundle) & has_item(Items.GORONS_BRACELET, bundle)),
        (Regions.FOREST_TEMPLE_UPPER_BLOCK_PUSH_ROOM,
         lambda bundle: is_adult(bundle) & can_ground_jump(bundle) & has_item(Items.GORONS_BRACELET, bundle) & can_use(Items.HOVER_BOOTS, bundle)),
        (Regions.FOREST_TEMPLE_BLOCK_PUSH_ROOM_COURTYARD_ALCOVE,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle)),
    ])

    # Forest Temple Middle Block Push Room  (upstream RR_FOREST_TEMPLE_MIDDLE_BLOCK_PUSH_ROOM, SCENE_FOREST_TEMPLE)
    # Locations
    add_locations(Regions.FOREST_TEMPLE_MIDDLE_BLOCK_PUSH_ROOM, world, [
        (Locations.FOREST_TEMPLE_EYE_SWITCH_CHEST,
         lambda bundle: can_hit_eye_targets(bundle) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_MIDDLE_BLOCK_PUSH_ROOM, world, [
        (Regions.FOREST_TEMPLE_LOWER_BLOCK_PUSH_ROOM,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_BLOCK_PUSH_ROOM_COURTYARD_ALCOVE,
         lambda bundle: (can_do_trick(Tricks.FOREST_OUTSIDE_BACKDOOR, bundle) & can_jump_slash_except_hammer(bundle)) | ((is_adult(bundle) | can_jump_slash(bundle)) & bunny_hood(bundle))),
        (Regions.FOREST_TEMPLE_UPPER_BLOCK_PUSH_ROOM,
         lambda bundle: is_adult(bundle) & has_item(Items.GORONS_BRACELET, bundle)),
    ])

    # Forest Temple Upper Block Push Room  (upstream RR_FOREST_TEMPLE_UPPER_BLOCK_PUSH_ROOM, SCENE_FOREST_TEMPLE)
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_UPPER_BLOCK_PUSH_ROOM, world, [
        (Regions.FOREST_TEMPLE_MIDDLE_BLOCK_PUSH_ROOM,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_BLOCK_PUSH_ROOM_TOP,
         lambda bundle: has_climb(bundle)),
    ])

    # Forest Temple Block Push Room Top  (upstream RR_FOREST_TEMPLE_BLOCK_PUSH_ROOM_TOP, SCENE_FOREST_TEMPLE)
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_BLOCK_PUSH_ROOM_TOP, world, [
        (Regions.FOREST_TEMPLE_UPPER_BLOCK_PUSH_ROOM,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_NW_HALLWAY_TWISTED,
         lambda bundle: small_keys_scene("SCENE_FOREST_TEMPLE", 2, bundle)),
        (Regions.FOREST_TEMPLE_NW_HALLWAY_STRAIGHTENED,
         lambda bundle: can_hit_eye_targets(bundle) & small_keys_scene("SCENE_FOREST_TEMPLE", 2, bundle)),
    ])

    # Forest Temple Block Push Room Courtyard Alcove  (upstream RR_FOREST_TEMPLE_BLOCK_PUSH_ROOM_COURTYARD_ALCOVE, SCENE_FOREST_TEMPLE)
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_BLOCK_PUSH_ROOM_COURTYARD_ALCOVE, world, [
        (Regions.FOREST_TEMPLE_LOWER_BLOCK_PUSH_ROOM,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_NW_COURTYARD_UPPER,
         lambda bundle: True_()),
    ])

    # Forest Temple NW Hallway Twisted  (upstream RR_FOREST_TEMPLE_NW_HALLWAY_TWISTED, SCENE_FOREST_TEMPLE)
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_NW_HALLWAY_TWISTED, world, [
        (Regions.FOREST_TEMPLE_BLOCK_PUSH_ROOM_TOP,
         lambda bundle: small_keys_scene("SCENE_FOREST_TEMPLE", 2, bundle)),
        (Regions.FOREST_TEMPLE_RED_POE_ROOM,
         lambda bundle: small_keys_scene("SCENE_FOREST_TEMPLE", 3, bundle)),
    ])

    # Forest Temple NW Hallway Straightened  (upstream RR_FOREST_TEMPLE_NW_HALLWAY_STRAIGHTENED, SCENE_FOREST_TEMPLE)
    # Locations
    add_locations(Regions.FOREST_TEMPLE_NW_HALLWAY_STRAIGHTENED, world, [
        (Locations.FOREST_TEMPLE_BOSS_KEY_CHEST,
         lambda bundle: can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_NW_HALLWAY_STRAIGHTENED, world, [
        (Regions.FOREST_TEMPLE_BELOW_BOSS_KEY_CHEST,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_BLOCK_PUSH_ROOM_TOP,
         lambda bundle: small_keys_scene("SCENE_FOREST_TEMPLE", 2, bundle)),
    ])

    # Forest Temple Red Poe Room  (upstream RR_FOREST_TEMPLE_RED_POE_ROOM, SCENE_FOREST_TEMPLE)
    # Events
    add_events(Regions.FOREST_TEMPLE_RED_POE_ROOM, world, [
        (EventLocations.FOREST_TEMPLE_RED_POE_ROOM_FOREST_JOELLE, Events.FOREST_JOELLE,
         lambda bundle: can_use(Items.FAIRY_BOW, bundle)),
    ])
    # Locations
    add_locations(Regions.FOREST_TEMPLE_RED_POE_ROOM, world, [
        (Locations.FOREST_TEMPLE_RED_POE_CHEST,
         lambda bundle: has_item(Events.FOREST_JOELLE, bundle) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_RED_POE_ROOM, world, [
        (Regions.FOREST_TEMPLE_NW_HALLWAY_TWISTED,
         lambda bundle: small_keys_scene("SCENE_FOREST_TEMPLE", 3, bundle)),
        (Regions.FOREST_TEMPLE_UPPER_STALFOS,
         lambda bundle: True_()),
    ])

    # Forest Temple Upper Stalfos  (upstream RR_FOREST_TEMPLE_UPPER_STALFOS, SCENE_FOREST_TEMPLE)
    # Events
    add_events(Regions.FOREST_TEMPLE_UPPER_STALFOS, world, [
        (EventLocations.FOREST_TEMPLE_UPPER_STALFOS_FOREST_CLEAR_BETWEEN_JOELLE_AND_BETH, Events.FOREST_CLEAR_BETWEEN_JOELLE_AND_BETH,
         lambda bundle: can_kill_enemy(bundle, Enemies.STALFOS, EnemyDistance.CLOSE, True, 2)),
    ])
    # Locations
    add_locations(Regions.FOREST_TEMPLE_UPPER_STALFOS, world, [
        (Locations.FOREST_TEMPLE_BOW_CHEST,
         lambda bundle: has_item(Events.FOREST_CLEAR_BETWEEN_JOELLE_AND_BETH, bundle) & can_kill_enemy(bundle, Enemies.STALFOS, EnemyDistance.CLOSE, True, 3) & can_open_large_chest(bundle)),
        (Locations.FOREST_TEMPLE_UPPER_STALFOS_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FOREST_TEMPLE_UPPER_STALFOS_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FOREST_TEMPLE_UPPER_STALFOS_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FOREST_TEMPLE_UPPER_STALFOS_POT4,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_UPPER_STALFOS, world, [
        (Regions.FOREST_TEMPLE_RED_POE_ROOM,
         lambda bundle: has_item(Events.FOREST_CLEAR_BETWEEN_JOELLE_AND_BETH, bundle) & can_kill_enemy(bundle, Enemies.STALFOS, EnemyDistance.CLOSE, True, 3)),
        (Regions.FOREST_TEMPLE_BLUE_POE_ROOM,
         lambda bundle: has_item(Events.FOREST_CLEAR_BETWEEN_JOELLE_AND_BETH, bundle) & can_kill_enemy(bundle, Enemies.STALFOS, EnemyDistance.CLOSE, True, 3)),
    ])

    # Forest Temple Blue Poe Room  (upstream RR_FOREST_TEMPLE_BLUE_POE_ROOM, SCENE_FOREST_TEMPLE)
    # Events
    add_events(Regions.FOREST_TEMPLE_BLUE_POE_ROOM, world, [
        (EventLocations.FOREST_TEMPLE_BLUE_POE_ROOM_FOREST_BETH, Events.FOREST_BETH,
         lambda bundle: can_use(Items.FAIRY_BOW, bundle)),
    ])
    # Locations
    add_locations(Regions.FOREST_TEMPLE_BLUE_POE_ROOM, world, [
        (Locations.FOREST_TEMPLE_BLUE_POE_CHEST,
         lambda bundle: has_item(Events.FOREST_BETH, bundle) & can_open_large_chest(bundle)),
        (Locations.FOREST_TEMPLE_BLUE_POE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FOREST_TEMPLE_BLUE_POE_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FOREST_TEMPLE_BLUE_POE_POT3,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_BLUE_POE_ROOM, world, [
        (Regions.FOREST_TEMPLE_UPPER_STALFOS,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_NE_HALLWAY_STRAIGHTENED,
         lambda bundle: small_keys_scene("SCENE_FOREST_TEMPLE", 4, bundle)),
    ])

    # Forest Temple NE Hallway Straightened  (upstream RR_FOREST_TEMPLE_NE_HALLWAY_STRAIGHTENED, SCENE_FOREST_TEMPLE)
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_NE_HALLWAY_STRAIGHTENED, world, [
        (Regions.FOREST_TEMPLE_BLUE_POE_ROOM,
         lambda bundle: small_keys_scene("SCENE_FOREST_TEMPLE", 4, bundle)),
        (Regions.FOREST_TEMPLE_FROZEN_EYE_ROOM,
         lambda bundle: small_keys_scene("SCENE_FOREST_TEMPLE", 5, bundle)),
    ])

    # Forest Temple NE Hallway Twisted  (upstream RR_FOREST_TEMPLE_NE_HALLWAY_TWISTED, SCENE_FOREST_TEMPLE)
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_NE_HALLWAY_TWISTED, world, [
        (Regions.FOREST_TEMPLE_FROZEN_EYE_ROOM,
         lambda bundle: small_keys_scene("SCENE_FOREST_TEMPLE", 5, bundle)),
        (Regions.FOREST_TEMPLE_FALLING_ROOM,
         lambda bundle: True_()),
    ])

    # Forest Temple Frozen Eye Room  (upstream RR_FOREST_TEMPLE_FROZEN_EYE_ROOM, SCENE_FOREST_TEMPLE)
    # Locations
    add_locations(Regions.FOREST_TEMPLE_FROZEN_EYE_ROOM, world, [
        (Locations.FOREST_TEMPLE_FROZEN_EYE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FOREST_TEMPLE_FROZEN_EYE_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_FROZEN_EYE_ROOM, world, [
        (Regions.FOREST_TEMPLE_NE_HALLWAY_STRAIGHTENED,
         lambda bundle: small_keys_scene("SCENE_FOREST_TEMPLE", 5, bundle)),
        (Regions.FOREST_TEMPLE_NE_HALLWAY_TWISTED,
         lambda bundle: small_keys_scene("SCENE_FOREST_TEMPLE", 5, bundle) & (can_use(Items.FAIRY_BOW, bundle) | can_use(Items.DINS_FIRE, bundle))),
    ])

    # Forest Temple Falling Room  (upstream RR_FOREST_TEMPLE_FALLING_ROOM, SCENE_FOREST_TEMPLE)
    # Locations
    add_locations(Regions.FOREST_TEMPLE_FALLING_ROOM, world, [
        (Locations.FOREST_TEMPLE_FALLING_CEILING_ROOM_CHEST,
         lambda bundle: has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_FALLING_ROOM, world, [
        (Regions.FOREST_TEMPLE_NE_COURTYARD_SCARECROW_LEDGE,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_GREEN_POE_ROOM,
         lambda bundle: True_()),
    ])

    # Forest Temple Green Poe Room  (upstream RR_FOREST_TEMPLE_GREEN_POE_ROOM, SCENE_FOREST_TEMPLE)
    # Events
    add_events(Regions.FOREST_TEMPLE_GREEN_POE_ROOM, world, [
        (EventLocations.FOREST_TEMPLE_GREEN_POE_ROOM_FOREST_AMY, Events.FOREST_AMY,
         lambda bundle: can_use(Items.FAIRY_BOW, bundle) & has_grab(bundle)),
    ])
    # Locations
    add_locations(Regions.FOREST_TEMPLE_GREEN_POE_ROOM, world, [
        (Locations.FOREST_TEMPLE_GREEN_POE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.FOREST_TEMPLE_GREEN_POE_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_GREEN_POE_ROOM, world, [
        (Regions.FOREST_TEMPLE_FALLING_ROOM,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_BLUE_DOORMAT_HALLWAY_DOORMAT,
         lambda bundle: has_item(Events.FOREST_AMY, bundle)),
    ])

    # Forest Temple Blue Doormat Hallway Doormat  (upstream RR_FOREST_TEMPLE_BLUE_DOORMAT_HALLWAY_DOORMAT, SCENE_FOREST_TEMPLE)
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_BLUE_DOORMAT_HALLWAY_DOORMAT, world, [
        (Regions.FOREST_TEMPLE_GREEN_POE_ROOM,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_BLUE_DOORMAT_HALLWAY,
         lambda bundle: can_pass_enemy(bundle, Enemies.BIG_SKULLTULA)),
    ])

    # Forest Temple Blue Doormat Hallway  (upstream RR_FOREST_TEMPLE_BLUE_DOORMAT_HALLWAY, SCENE_FOREST_TEMPLE)
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_BLUE_DOORMAT_HALLWAY, world, [
        (Regions.FOREST_TEMPLE_BLUE_DOORMAT_HALLWAY_DOORMAT,
         lambda bundle: can_pass_enemy(bundle, Enemies.BIG_SKULLTULA)),
        (Regions.FOREST_TEMPLE_LOBBY,
         lambda bundle: True_()),
    ])

    # Forest Temple Basement  (upstream RR_FOREST_TEMPLE_BASEMENT, SCENE_FOREST_TEMPLE)
    # Events
    add_events(Regions.FOREST_TEMPLE_BASEMENT, world, [
        (EventLocations.FOREST_TEMPLE_BASEMENT_FOREST_OPEN_BOSS_HALLWAY, Events.FOREST_OPEN_BOSS_HALLWAY,
         lambda bundle: has_grab(bundle)),
    ])
    # Locations
    add_locations(Regions.FOREST_TEMPLE_BASEMENT, world, [
        (Locations.FOREST_TEMPLE_BASEMENT_CHEST,
         lambda bundle: has_grab(bundle) & has_open_chest(bundle)),
        (Locations.FOREST_TEMPLE_GS_BASEMENT,
         lambda bundle: has_grab(bundle) & hookshot_or_boomerang(bundle)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_BASEMENT, world, [
        (Regions.FOREST_TEMPLE_LOBBY,
         lambda bundle: True_()),
        (Regions.FOREST_TEMPLE_BOSS_ENTRYWAY,
         lambda bundle: has_item(Events.FOREST_OPEN_BOSS_HALLWAY, bundle)),
    ])

    # Forest Temple Boss Entryway  (upstream RR_FOREST_TEMPLE_BOSS_ENTRYWAY, SCENE_FOREST_TEMPLE)
    # Locations
    add_locations(Regions.FOREST_TEMPLE_BOSS_ENTRYWAY, world, [
        # DEFERRED RC_FOREST_BOSS_KEY_HINT: true
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_BOSS_ENTRYWAY, world, [
        (Regions.FOREST_TEMPLE_BASEMENT,
         lambda bundle: True_() & has_item(Events.FOREST_OPEN_BOSS_HALLWAY, bundle)),
        (Regions.FOREST_TEMPLE_BOSS_ROOM,
         lambda bundle: has_item(Items.FOREST_TEMPLE_BOSS_KEY, bundle)),
    ])

    # Forest Temple Boss Room  (upstream RR_FOREST_TEMPLE_BOSS_ROOM, SCENE_FOREST_TEMPLE_BOSS)
    # Events
    add_events(Regions.FOREST_TEMPLE_BOSS_ROOM, world, [
        (EventLocations.FOREST_TEMPLE_BOSS_ROOM_FOREST_TEMPLE_CLEAR, Events.FOREST_TEMPLE_COMPLETED,
         lambda bundle: can_kill_enemy(bundle, Enemies.PHANTOM_GANON)),
    ])
    # Locations
    add_locations(Regions.FOREST_TEMPLE_BOSS_ROOM, world, [
        (Locations.FOREST_TEMPLE_PHANTOM_GANON_HEART_CONTAINER,
         lambda bundle: has_item(Events.FOREST_TEMPLE_COMPLETED, bundle)),
        (Locations.PHANTOM_GANON,
         lambda bundle: has_item(Events.FOREST_TEMPLE_COMPLETED, bundle)),
    ])
    # Connections
    connect_regions(Regions.FOREST_TEMPLE_BOSS_ROOM, world, [
        (Regions.FOREST_TEMPLE_BOSS_ENTRYWAY,
         lambda bundle: False_()),
        (Regions.SACRED_FOREST_MEADOW,
         lambda bundle: has_item(Events.FOREST_TEMPLE_COMPLETED, bundle)),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_FAIRIES', 'CAN_FARM_NUTS', 'CAN_FARM_STICKS', 'FOREST_AMY', 'FOREST_BETH', 'FOREST_CLEAR_BETWEEN_JOELLE_AND_BETH', 'FOREST_DRAINED_WELL', 'FOREST_JOELLE', 'FOREST_MEG', 'FOREST_OPEN_BOSS_HALLWAY', 'FOREST_SUMMON_NE_SCARECROW', 'FOREST_TEMPLE_COMPLETED']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (1): ['RC_FOREST_BOSS_KEY_HINT']
