"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/dungeons/bottom_of_the_well.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    BOTW_PERIMETER_STICK_ACCESS = "Bottom of the Well Perimeter Stick Access"
    BOTW_PERIMETER_NUT_ACCESS = "Bottom of the Well Perimeter Nut Access"
    BOTW_PERIMETER_BOTW_LOWERED_WATER = "Bottom of the Well Perimeter Botw Lowered Water"
    BOTW_SKULL_WALL_ROOM_STICK_ACCESS = "Bottom of the Well Skull Wall Room Stick Access"
    BOTW_SKULL_WALL_ROOM_NUT_ACCESS = "Bottom of the Well Skull Wall Room Nut Access"
    BOTW_LADDER_DOOR_BOTW_SILVER = "Bottom of the Well Ladder Door Botw Silver"


def set_region_rules(world: "SohWorld") -> None:

    # Bottom of the Well Entryway  (upstream RR_BOTW_ENTRYWAY, SCENE_BOTTOM_OF_THE_WELL)
    # Connections
    connect_regions(Regions.BOTW_ENTRYWAY, world, [
        (Regions.BOTW_CORRIDOR,
         lambda bundle: True_() & has_crawl(bundle)),
        (Regions.KAK_WELL,
         lambda bundle: True_()),
    ])

    # Bottom of the Well Corridor  (upstream RR_BOTW_CORRIDOR, SCENE_BOTTOM_OF_THE_WELL)
    # Connections
    connect_regions(Regions.BOTW_CORRIDOR, world, [
        (Regions.BOTW_ENTRYWAY,
         lambda bundle: has_crawl(bundle) & can_climb_ladder(bundle)),
        (Regions.BOTW_PERIMETER,
         lambda bundle: can_pass_enemy(bundle, Enemies.BIG_SKULLTULA)),
    ])

    # Bottom of the Well Perimeter  (upstream RR_BOTW_PERIMETER, SCENE_BOTTOM_OF_THE_WELL)
    # Events
    add_events(Regions.BOTW_PERIMETER, world, [
        (EventLocations.BOTW_PERIMETER_STICK_ACCESS, Events.CAN_FARM_STICKS,
         lambda bundle: can_break_pots(bundle)),
        (EventLocations.BOTW_PERIMETER_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_break_pots(bundle)),
        (EventLocations.BOTW_PERIMETER_BOTW_LOWERED_WATER, Events.BOTW_LOWERED_WATER,
         lambda bundle: can_use(Items.ZELDAS_LULLABY, bundle)),
    ])
    # Locations
    add_locations(Regions.BOTW_PERIMETER, world, [
        (Locations.BOTTOM_OF_THE_WELL_FRONT_LEFT_FAKE_WALL_CHEST,
         lambda bundle: (can_do_trick(Tricks.LENS_BOTW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & has_open_chest(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_RIGHT_BOTTOM_FAKE_WALL_CHEST,
         lambda bundle: (can_do_trick(Tricks.LENS_BOTW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & has_open_chest(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_FRONT_CENTER_BOMBABLE_CHEST,
         lambda bundle: has_explosives(bundle) & has_open_chest(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BACK_LEFT_BOMBABLE_CHEST,
         lambda bundle: has_explosives(bundle) & (can_do_trick(Tricks.LENS_BOTW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & has_open_chest(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_UNDERWATER_FRONT_CHEST,
         lambda bundle: (has_item(Events.BOTW_LOWERED_WATER, bundle) & has_open_chest(bundle)) | can_open_underwater_chest(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_UNDERWATER_LEFT_CHEST,
         lambda bundle: (has_item(Events.BOTW_LOWERED_WATER, bundle) & has_open_chest(bundle)) | can_open_underwater_chest(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_NEAR_ENTRANCE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_NEAR_ENTRANCE_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_UNDERWATER_POT,
         lambda bundle: (can_break_pots(bundle) & has_item(Events.BOTW_LOWERED_WATER, bundle)) | can_use(Items.BOOMERANG, bundle)),
    ])
    # Connections
    connect_regions(Regions.BOTW_PERIMETER, world, [
        (Regions.BOTW_CORRIDOR,
         lambda bundle: can_pass_enemy(bundle, Enemies.BIG_SKULLTULA)),
        (Regions.BOTW_MIDDLE,
         lambda bundle: can_do_trick(Tricks.LENS_BOTW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
        (Regions.BOTW_PIT_CAGE,
         lambda bundle: can_do_trick(Tricks.LENS_BOTW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
        (Regions.BOTW_HIDDEN_POTS,
         lambda bundle: can_do_trick(Tricks.LENS_BOTW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
        (Regions.BOTW_CORNER_CRAWLSPACE,
         lambda bundle: has_crawl(bundle)),
        (Regions.BOTW_BEHIND_MOAT,
         lambda bundle: ((has_item(Events.BOTW_LOWERED_WATER, bundle) & (has_climb(bundle) | can_use(Items.HOOKSHOT, bundle))) | has_item(Items.BRONZE_SCALE, bundle) | (is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & can_use(Items.HOOKSHOT, bundle)))),
        (Regions.BOTW_NEAR_BOSS_LOWER,
         lambda bundle: has_item(Events.BOTW_LOWERED_WATER, bundle) & has_crawl(bundle)),
        (Regions.BOTW_B3_OOZE,
         lambda bundle: True_()),
        (Regions.BOTW_B3_BLOCKED_GRASS,
         lambda bundle: can_do_trick(Tricks.LENS_BOTW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
    ])

    # Bottom of the Well Middle  (upstream RR_BOTW_MIDDLE, SCENE_BOTTOM_OF_THE_WELL)
    # Locations
    add_locations(Regions.BOTW_MIDDLE, world, [
        (Locations.BOTTOM_OF_THE_WELL_CENTER_SKULLTULA_CHEST,
         lambda bundle: (can_pass_enemy(bundle, Enemies.BIG_SKULLTULA) | take_damage(bundle)) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.BOTW_MIDDLE, world, [
        (Regions.BOTW_PERIMETER,
         lambda bundle: can_do_trick(Tricks.LENS_BOTW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
        (Regions.BOTW_PIT_CAGE,
         lambda bundle: can_do_trick(Tricks.BOTW_PITS, bundle) & (can_do_trick(Tricks.LENS_BOTW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle))),
        (Regions.BOTW_SKULL_WALL_ROOM,
         lambda bundle: small_keys_scene("SCENE_BOTTOM_OF_THE_WELL", 3, bundle)),
        (Regions.BOTW_INVISIBLE_PATH,
         lambda bundle: small_keys_scene("SCENE_BOTTOM_OF_THE_WELL", 3, bundle)),
        (Regions.BOTW_B3_OOZE,
         lambda bundle: True_()),
        (Regions.BOTW_B3_PLATFORM,
         lambda bundle: can_do_trick(Tricks.LENS_BOTW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
    ])

    # Bottom of the Well Hidden Pots  (upstream RR_BOTW_HIDDEN_POTS, SCENE_BOTTOM_OF_THE_WELL)
    # Locations
    add_locations(Regions.BOTW_HIDDEN_POTS, world, [
        (Locations.BOTTOM_OF_THE_WELL_LEFT_SIDE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_LEFT_SIDE_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_LEFT_SIDE_POT3,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.BOTW_HIDDEN_POTS, world, [
        (Regions.BOTW_PERIMETER,
         lambda bundle: can_do_trick(Tricks.LENS_BOTW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
    ])

    # Bottom of the Well Corner Crawlspace  (upstream RR_BOTW_CORNER_CRAWLSPACE, SCENE_BOTTOM_OF_THE_WELL)
    # Connections
    connect_regions(Regions.BOTW_CORNER_CRAWLSPACE, world, [
        (Regions.BOTW_PERIMETER,
         lambda bundle: has_crawl(bundle)),
        (Regions.BOTW_HIDDEN_PITS_ROOM,
         lambda bundle: small_keys_scene("SCENE_BOTTOM_OF_THE_WELL", 3, bundle)),
    ])

    # Bottom of the Well Hidden Pits Room  (upstream RR_BOTW_HIDDEN_PITS_ROOM, SCENE_BOTTOM_OF_THE_WELL)
    # Locations
    add_locations(Regions.BOTW_HIDDEN_PITS_ROOM, world, [
        (Locations.BOTTOM_OF_THE_WELL_FIRE_KEESE_CHEST,
         lambda bundle: (can_do_trick(Tricks.LENS_BOTW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & has_open_chest(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_FIRE_KEESE_POT1,
         lambda bundle: can_break_pots(bundle) & (can_do_trick(Tricks.LENS_BOTW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle))),
    ])
    # Connections
    connect_regions(Regions.BOTW_HIDDEN_PITS_ROOM, world, [
        (Regions.BOTW_CORNER_CRAWLSPACE,
         lambda bundle: small_keys_scene("SCENE_BOTTOM_OF_THE_WELL", 3, bundle) & (can_do_trick(Tricks.LENS_BOTW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle))),
        (Regions.BOTW_LOCKED_CAGE,
         lambda bundle: can_do_trick(Tricks.LENS_BOTW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
        (Regions.BOTW_B3_BOMB_FLOWERS,
         lambda bundle: can_do_trick(Tricks.LENS_BOTW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
    ])

    # Bottom of the Well Locked Cage  (upstream RR_BOTW_LOCKED_CAGE, SCENE_BOTTOM_OF_THE_WELL)
    # Locations
    add_locations(Regions.BOTW_LOCKED_CAGE, world, [
        (Locations.BOTTOM_OF_THE_WELL_LIKE_LIKE_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_GS_LIKE_LIKE_CAGE,
         lambda bundle: can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG)),
    ])
    # Connections
    connect_regions(Regions.BOTW_LOCKED_CAGE, world, [
        (Regions.BOTW_HIDDEN_PITS_ROOM,
         lambda bundle: True_()),
    ])

    # Bottom of the Well Pit Cage  (upstream RR_BOTW_PIT_CAGE, SCENE_BOTTOM_OF_THE_WELL)
    # Locations
    add_locations(Regions.BOTW_PIT_CAGE, world, [
        (Locations.BOTTOM_OF_THE_WELL_COMPASS_CHEST,
         lambda bundle: can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.BOTW_PIT_CAGE, world, [
        (Regions.BOTW_PERIMETER,
         lambda bundle: can_do_trick(Tricks.LENS_BOTW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
        (Regions.BOTW_MIDDLE,
         lambda bundle: can_do_trick(Tricks.BOTW_PITS, bundle) & (can_do_trick(Tricks.LENS_BOTW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle))),
        (Regions.BOTW_B3_OOZE,
         lambda bundle: True_()),
    ])

    # Bottom of the Well Skull Wall Room  (upstream RR_BOTW_SKULL_WALL_ROOM, SCENE_BOTTOM_OF_THE_WELL)
    # Events
    add_events(Regions.BOTW_SKULL_WALL_ROOM, world, [
        (EventLocations.BOTW_SKULL_WALL_ROOM_STICK_ACCESS, Events.CAN_FARM_STICKS,
         lambda bundle: can_get_deku_baba_sticks(bundle)),
        (EventLocations.BOTW_SKULL_WALL_ROOM_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_get_deku_baba_nuts(bundle)),
    ])
    # Locations
    add_locations(Regions.BOTW_SKULL_WALL_ROOM, world, [
        (Locations.BOTTOM_OF_THE_WELL_GS_WEST_INNER_ROOM,
         lambda bundle: can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG)),
    ])
    # Connections
    connect_regions(Regions.BOTW_SKULL_WALL_ROOM, world, [
        (Regions.BOTW_MIDDLE,
         lambda bundle: small_keys_scene("SCENE_BOTTOM_OF_THE_WELL", 3, bundle)),
    ])

    # Bottom of the Well Invisible Path  (upstream RR_BOTW_INVISIBLE_PATH, SCENE_BOTTOM_OF_THE_WELL)
    # Locations
    add_locations(Regions.BOTW_INVISIBLE_PATH, world, [
        (Locations.BOTTOM_OF_THE_WELL_GS_EAST_INNER_ROOM,
         lambda bundle: can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG)),
    ])
    # Connections
    connect_regions(Regions.BOTW_INVISIBLE_PATH, world, [
        (Regions.BOTW_MIDDLE,
         lambda bundle: small_keys_scene("SCENE_BOTTOM_OF_THE_WELL", 3, bundle)),
        (Regions.BOTW_B3_OOZE,
         lambda bundle: True_()),
    ])

    # Bottom of the Well Behind Moat  (upstream RR_BOTW_BEHIND_MOAT, SCENE_BOTTOM_OF_THE_WELL)
    # Locations
    add_locations(Regions.BOTW_BEHIND_MOAT, world, [
        (Locations.BOTTOM_OF_THE_WELL_UNDERWATER_LEFT_CHEST,
         lambda bundle: (has_item(Events.BOTW_LOWERED_WATER, bundle) & has_open_chest(bundle)) | can_open_underwater_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.BOTW_BEHIND_MOAT, world, [
        (Regions.BOTW_PERIMETER,
         lambda bundle: (has_item(Events.BOTW_LOWERED_WATER, bundle) | has_item(Items.BRONZE_SCALE, bundle) | (is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & can_use(Items.HOOKSHOT, bundle))) & (has_climb(bundle) | can_use(Items.HOOKSHOT, bundle))),
        (Regions.BOTW_CRYPT,
         lambda bundle: True_()),
    ])

    # Bottom of the Well Crypt  (upstream RR_BOTW_CRYPT, SCENE_BOTTOM_OF_THE_WELL)
    # Locations
    add_locations(Regions.BOTW_CRYPT, world, [
        (Locations.BOTTOM_OF_THE_WELL_FREESTANDING_KEY,
         lambda bundle: has_fire_source_with_torch(bundle) | can_use(Items.FAIRY_BOW, bundle)),
        (Locations.BOTTOM_OF_THE_WELL_COFFIN_ROOM_FRONT_LEFT_HEART,
         lambda bundle: has_fire_source_with_torch(bundle) | can_use(Items.FAIRY_BOW, bundle)),
        (Locations.BOTTOM_OF_THE_WELL_COFFIN_ROOM_MIDDLE_RIGHT_HEART,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.BOTW_CRYPT, world, [
        (Regions.BOTW_BEHIND_MOAT,
         lambda bundle: True_()),
    ])

    # Bottom of the Well Near Boss Lower  (upstream RR_BOTW_NEAR_BOSS_LOWER, SCENE_BOTTOM_OF_THE_WELL)
    # Connections
    connect_regions(Regions.BOTW_NEAR_BOSS_LOWER, world, [
        (Regions.BOTW_PERIMETER,
         lambda bundle: has_crawl(bundle) & (has_item(Events.BOTW_LOWERED_WATER, bundle) | has_item(Items.BRONZE_SCALE, bundle)) & has_climb(bundle)),
        (Regions.BOTW_NEAR_BOSS_UPPER,
         lambda bundle: has_climb(bundle) | (is_adult(bundle) & can_ground_jump(bundle))),
    ])

    # Bottom of the Well Near Boss Upper  (upstream RR_BOTW_NEAR_BOSS_UPPER, SCENE_BOTTOM_OF_THE_WELL)
    # Connections
    connect_regions(Regions.BOTW_NEAR_BOSS_UPPER, world, [
        (Regions.BOTW_NEAR_BOSS_LOWER,
         lambda bundle: True_()),
        (Regions.BOTW_DEAD_HAND_ROOM,
         lambda bundle: True_()),
    ])

    # Bottom of the Well Dead Hand Room  (upstream RR_BOTW_DEAD_HAND_ROOM, SCENE_BOTTOM_OF_THE_WELL)
    # Locations
    add_locations(Regions.BOTW_DEAD_HAND_ROOM, world, [
        (Locations.BOTTOM_OF_THE_WELL_LENS_OF_TRUTH_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.DEAD_HAND) & can_open_large_chest(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_INVISIBLE_CHEST,
         lambda bundle: (can_do_trick(Tricks.LENS_BOTW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.BOTW_DEAD_HAND_ROOM, world, [
        (Regions.BOTW_NEAR_BOSS_UPPER,
         lambda bundle: can_kill_enemy(bundle, Enemies.DEAD_HAND)),
    ])

    # Bottom of the Well B3 Ooze  (upstream RR_BOTW_B3_OOZE, SCENE_BOTTOM_OF_THE_WELL)
    # Locations
    add_locations(Regions.BOTW_B3_OOZE, world, [
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_POT4,
         lambda bundle: can_break_pots(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_POT5,
         lambda bundle: can_break_pots(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_POT6,
         lambda bundle: can_break_pots(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_POT7,
         lambda bundle: can_break_pots(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_POT8,
         lambda bundle: can_break_pots(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_POT9,
         lambda bundle: can_break_pots(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_POT10,
         lambda bundle: can_break_pots(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_POT11,
         lambda bundle: can_break_pots(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_POT12,
         lambda bundle: can_break_pots(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_SUNS_SONG_FAIRY,
         lambda bundle: can_use(Items.SUNS_SONG, bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.BOTW_BOULDER_1,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.BOTW_BOULDER_2,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.BOTW_BOULDER_3,
         lambda bundle: blast_or_smash(bundle) | can_use(Items.DINS_FIRE, bundle) | (can_use(Items.STICKS, bundle) & can_do_trick(Tricks.BOTW_BASEMENT, bundle)) | (can_do_trick(Tricks.BOULDER_COLLISION, bundle) & can_use(Items.FAIRY_BOW, bundle))),
        (Locations.BOTW_BOULDER_4,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.BOTW_BOULDER_5,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.BOTW_BOULDER_6,
         lambda bundle: blast_or_smash(bundle)),
        # DEFERRED RC_BOTW_B2_LADDER_SILVER: logic->CanClimbLadder()
        # DEFERRED RC_BOTW_B3_LADDER_SILVER: true
        # DEFERRED RC_BOTW_NW_OOZE_SILVER: true
        # DEFERRED RC_BOTW_SE_OOZE_SILVER: true
    ])
    # Connections
    connect_regions(Regions.BOTW_B3_OOZE, world, [
        (Regions.BOTW_LADDER_DOOR,
         lambda bundle: can_climb_high_ladder(bundle)),
        (Regions.BOTW_B3_BOMB_FLOWERS,
         lambda bundle: any_age_time(bundle, lambda bundle: blast_or_smash(bundle) | can_use(Items.DINS_FIRE, bundle) | (can_do_trick(Tricks.BOTW_BASEMENT, bundle) & can_use(Items.STICKS, bundle)) | (can_do_trick(Tricks.BOULDER_COLLISION, bundle) & can_use(Items.FAIRY_BOW, bundle)))),
        (Regions.BOTW_B3_BLOCKED_GRASS,
         lambda bundle: any_age_time(bundle, lambda bundle: blast_or_smash(bundle))),
        (Regions.BOTW_B3_CHEST_AREA,
         lambda bundle: any_age_time(bundle, lambda bundle: blast_or_smash(bundle))),
    ])

    # Bottom of the Well Ladder Door  (upstream RR_BOTW_LADDER_DOOR, SCENE_BOTTOM_OF_THE_WELL)
    # Events
    add_events(Regions.BOTW_LADDER_DOOR, world, [
        (EventLocations.BOTW_LADDER_DOOR_BOTW_SILVER, Events.BOTW_SILVER,
         lambda bundle: True_()),
    ])
    # Locations
    add_locations(Regions.BOTW_LADDER_DOOR, world, [
        # DEFERRED RC_BOTW_B1_LADDER_SILVER: true
        # DEFERRED RC_BOTW_B2_LADDER_SILVER: true
    ])
    # Connections
    connect_regions(Regions.BOTW_LADDER_DOOR, world, [
        (Regions.BOTW_B3_OOZE,
         lambda bundle: True_()),
        (Regions.BOTW_HIDDEN_POTS,
         lambda bundle: has_item(Events.BOTW_SILVER, bundle)),
    ])

    # Bottom of the Well B3 Bomb Flowers  (upstream RR_BOTW_B3_BOMB_FLOWERS, SCENE_BOTTOM_OF_THE_WELL)
    # Locations
    add_locations(Regions.BOTW_B3_BOMB_FLOWERS, world, [
        (Locations.BOTW_BOULDER_1,
         lambda bundle: has_item(Items.GORONS_BRACELET, bundle)),
        (Locations.BOTW_BOULDER_2,
         lambda bundle: has_item(Items.GORONS_BRACELET, bundle)),
        (Locations.BOTW_BOULDER_3,
         lambda bundle: can_detonate_upright_bomb_flower(bundle)),
        (Locations.BOTW_BOULDER_4,
         lambda bundle: has_item(Items.GORONS_BRACELET, bundle)),
        (Locations.BOTW_BOULDER_5,
         lambda bundle: has_item(Items.GORONS_BRACELET, bundle)),
        (Locations.BOTW_BOULDER_6,
         lambda bundle: has_item(Items.GORONS_BRACELET, bundle)),
    ])
    # Connections
    connect_regions(Regions.BOTW_B3_BOMB_FLOWERS, world, [
        (Regions.BOTW_B3_OOZE,
         lambda bundle: can_detonate_upright_bomb_flower(bundle)),
        (Regions.BOTW_B3_BLOCKED_GRASS,
         lambda bundle: has_item(Items.GORONS_BRACELET, bundle)),
        (Regions.BOTW_B3_CHEST_AREA,
         lambda bundle: has_item(Items.GORONS_BRACELET, bundle)),
    ])

    # Bottom of the Well B3 Blocked Grass  (upstream RR_BOTW_B3_BLOCKED_GRASS, SCENE_BOTTOM_OF_THE_WELL)
    # Locations
    add_locations(Regions.BOTW_B3_BLOCKED_GRASS, world, [
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_BEHIND_ROCKS_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_BEHIND_ROCKS_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_BEHIND_ROCKS_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_BEHIND_ROCKS_GRASS4,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_BEHIND_ROCKS_GRASS5,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_BEHIND_ROCKS_GRASS6,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_BEHIND_ROCKS_GRASS7,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_BEHIND_ROCKS_GRASS8,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_BEHIND_ROCKS_GRASS9,
         lambda bundle: can_cut_shrubs(bundle)),
    ])
    # Connections
    connect_regions(Regions.BOTW_B3_BLOCKED_GRASS, world, [
        (Regions.BOTW_B3_OOZE,
         lambda bundle: any_age_time(bundle, lambda bundle: blast_or_smash(bundle) | has_item(Items.GORONS_BRACELET, bundle))),
    ])

    # Bottom of the Well B3 Chest Area  (upstream RR_BOTW_B3_CHEST_AREA, SCENE_BOTTOM_OF_THE_WELL)
    # Locations
    add_locations(Regions.BOTW_B3_CHEST_AREA, world, [
        (Locations.BOTTOM_OF_THE_WELL_MAP_CHEST,
         lambda bundle: can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.BOTW_B3_CHEST_AREA, world, [
        (Regions.BOTW_B3_OOZE,
         lambda bundle: any_age_time(bundle, lambda bundle: blast_or_smash(bundle))),
    ])

    # Bottom of the Well B3 Platform  (upstream RR_BOTW_B3_PLATFORM, SCENE_BOTTOM_OF_THE_WELL)
    # Locations
    add_locations(Regions.BOTW_B3_PLATFORM, world, [
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_PLATFORM_LEFT_RUPEE,
         lambda bundle: True_()),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_PLATFORM_BACK_LEFT_RUPEE,
         lambda bundle: True_()),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_PLATFORM_MIDDLE_RUPEE,
         lambda bundle: True_()),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_PLATFORM_BACK_RIGHT_RUPEE,
         lambda bundle: True_()),
        (Locations.BOTTOM_OF_THE_WELL_BASEMENT_PLATFORM_RIGHT_RUPEE,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.BOTW_B3_PLATFORM, world, [
        (Regions.BOTW_B3_OOZE,
         lambda bundle: True_()),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['BOTW_LOWERED_WATER', 'BOTW_SILVER', 'CAN_FARM_NUTS', 'CAN_FARM_STICKS']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (6): ['RC_BOTW_B2_LADDER_SILVER', 'RC_BOTW_B3_LADDER_SILVER', 'RC_BOTW_NW_OOZE_SILVER', 'RC_BOTW_SE_OOZE_SILVER', 'RC_BOTW_B1_LADDER_SILVER', 'RC_BOTW_B2_LADDER_SILVER']
