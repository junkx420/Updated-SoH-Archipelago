"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/dungeons/shadow_temple.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    SHADOW_TEMPLE_WHISPERING_WALLS_START_NUT_ACCESS = "Shadow Temple Whispering Walls Start Nut Access"
    SHADOW_TEMPLE_WHISPERING_WALLS_SIDE_NUT_ACCESS = "Shadow Temple Whispering Walls Side Nut Access"
    SHADOW_TEMPLE_SPINNING_BLADES_SHADOW_SILVER_BLADES = "Shadow Temple Spinning Blades Shadow Silver Blades"
    SHADOW_TEMPLE_LOWER_HUGE_PIT_SHADOW_SILVER_PIT = "Shadow Temple Lower Huge Pit Shadow Silver Pit"
    SHADOW_TEMPLE_FLOOR_SPIKES_ROOM_SHADOW_SILVER_SPIKES = "Shadow Temple Floor Spikes Room Shadow Silver Spikes"
    SHADOW_TEMPLE_DOCK_SHADOW_SHORTCUT_BLOCK = "Shadow Temple Dock Shadow Shortcut Block"
    SHADOW_TEMPLE_BEYOND_BOAT_SHADOW_BRIDGE_BEYOND_BOAT_LOWERED = "Shadow Temple Beyond Boat Shadow Bridge Beyond Boat Lowered"
    SHADOW_TEMPLE_ACROSS_CHASM_SHADOW_BRIDGE_BEYOND_BOAT_LOWERED = "Shadow Temple Across Chasm Shadow Bridge Beyond Boat Lowered"
    SHADOW_TEMPLE_BOSS_ROOM_SHADOW_TEMPLE_CLEAR = "Shadow Temple Boss Room Shadow Temple Clear"


def set_region_rules(world: "SohWorld") -> None:

    # Shadow Temple Entryway  (upstream RR_SHADOW_TEMPLE_ENTRYWAY, SCENE_SHADOW_TEMPLE)
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_ENTRYWAY, world, [
        (Regions.SHADOW_TEMPLE_BEGINNING,
         lambda bundle: True_() & (can_use(Items.HOVER_BOOTS, bundle) | can_use(Items.HOOKSHOT, bundle))),
        (Regions.GRAVEYARD_WARP_PAD_REGION,
         lambda bundle: True_()),
    ])

    # Shadow Temple Beginning  (upstream RR_SHADOW_TEMPLE_BEGINNING, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_BEGINNING, world, [
        (Locations.SHADOW_TEMPLE_TRUTHSPINNER_RECTANGLE_SIGN,
         lambda bundle: can_read(bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_BEGINNING, world, [
        (Regions.SHADOW_TEMPLE_ENTRYWAY,
         lambda bundle: (can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & (can_use(Items.HOVER_BOOTS, bundle) | can_use(Items.HOOKSHOT, bundle))),
        (Regions.SHADOW_TEMPLE_WHISPERING_WALLS_START,
         lambda bundle: can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
        (Regions.SHADOW_TEMPLE_FIRST_BEAMOS,
         lambda bundle: (can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & has_grab(bundle) & (can_use(Items.HOVER_BOOTS, bundle) | (is_adult(bundle) & bunny_hood(bundle)))),
    ])

    # Shadow Temple Whispering Walls Start  (upstream RR_SHADOW_TEMPLE_WHISPERING_WALLS_START, SCENE_SHADOW_TEMPLE)
    # Events
    add_events(Regions.SHADOW_TEMPLE_WHISPERING_WALLS_START, world, [
        (EventLocations.SHADOW_TEMPLE_WHISPERING_WALLS_START_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_WHISPERING_WALLS_START, world, [
        (Locations.SHADOW_TEMPLE_WHISPERING_WALLS_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.SHADOW_TEMPLE_WHISPERING_WALLS_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_WHISPERING_WALLS_START, world, [
        (Regions.SHADOW_TEMPLE_BEGINNING,
         lambda bundle: True_()),
        (Regions.SHADOW_TEMPLE_WHISPERING_WALLS_SIDE,
         lambda bundle: can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
        (Regions.SHADOW_TEMPLE_WHISPERING_WALLS_END,
         lambda bundle: can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
    ])

    # Shadow Temple Whispering Walls Side  (upstream RR_SHADOW_TEMPLE_WHISPERING_WALLS_SIDE, SCENE_SHADOW_TEMPLE)
    # Events
    add_events(Regions.SHADOW_TEMPLE_WHISPERING_WALLS_SIDE, world, [
        (EventLocations.SHADOW_TEMPLE_WHISPERING_WALLS_SIDE_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_WHISPERING_WALLS_SIDE, world, [
        (Locations.SHADOW_TEMPLE_WHISPERING_WALLS_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.SHADOW_TEMPLE_WHISPERING_WALLS_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_WHISPERING_WALLS_SIDE, world, [
        (Regions.SHADOW_TEMPLE_WHISPERING_WALLS_START,
         lambda bundle: can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
        (Regions.SHADOW_TEMPLE_WHISPERING_WALLS_SIDE_ROOM,
         lambda bundle: True_()),
    ])

    # Shadow Temple Whispering Walls End  (upstream RR_SHADOW_TEMPLE_WHISPERING_WALLS_END, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_WHISPERING_WALLS_END, world, [
        (Locations.SHADOW_TEMPLE_WHISPERING_WALLS_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.SHADOW_TEMPLE_WHISPERING_WALLS_POT4,
         lambda bundle: can_break_pots(bundle)),
        (Locations.SHADOW_TEMPLE_WHISPERING_WALLS_POT5,
         lambda bundle: can_break_pots(bundle)),
        (Locations.SHADOW_TEMPLE_NEAR_DEAD_HAND_POT1,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_WHISPERING_WALLS_END, world, [
        (Regions.SHADOW_TEMPLE_WHISPERING_WALLS_START,
         lambda bundle: can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
        (Regions.SHADOW_TEMPLE_DEAD_HAND,
         lambda bundle: True_()),
    ])

    # Shadow Temple Whispering Walls Side Room  (upstream RR_SHADOW_TEMPLE_WHISPERING_WALLS_SIDE_ROOM, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_WHISPERING_WALLS_SIDE_ROOM, world, [
        (Locations.SHADOW_TEMPLE_MAP_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.REDEAD) & can_kill_enemy(bundle, Enemies.KEESE) & can_open_large_chest(bundle)),
        (Locations.SHADOW_TEMPLE_MAP_CHEST_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.SHADOW_TEMPLE_MAP_CHEST_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_WHISPERING_WALLS_SIDE_ROOM, world, [
        (Regions.SHADOW_TEMPLE_WHISPERING_WALLS_SIDE,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.REDEAD) & can_kill_enemy(bundle, Enemies.KEESE))),
    ])

    # Shadow Temple Dead Hand  (upstream RR_SHADOW_TEMPLE_DEAD_HAND, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_DEAD_HAND, world, [
        (Locations.SHADOW_TEMPLE_HOVER_BOOTS_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.DEAD_HAND) & can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_DEAD_HAND, world, [
        (Regions.SHADOW_TEMPLE_WHISPERING_WALLS_END,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.DEAD_HAND))),
    ])

    # Shadow Temple First Beamos  (upstream RR_SHADOW_TEMPLE_FIRST_BEAMOS, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_FIRST_BEAMOS, world, [
        (Locations.SHADOW_TEMPLE_BEAMOS_SONG_OF_STORMS_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_FIRST_BEAMOS, world, [
        (Regions.SHADOW_TEMPLE_BEGINNING,
         lambda bundle: can_do_trick(Tricks.VISIBLE_COLLISION, bundle) & (can_use(Items.HOVER_BOOTS, bundle) | can_use(Items.HOOKSHOT, bundle) | (is_adult(bundle) & bunny_hood(bundle)))),
        (Regions.SHADOW_TEMPLE_COMPASS_ROOM,
         lambda bundle: True_()),
        (Regions.SHADOW_TEMPLE_SPINNING_BLADES,
         lambda bundle: True_()),
        (Regions.SHADOW_TEMPLE_B2_TO_B3_CORRIDOR_B2,
         lambda bundle: has_explosives(bundle) & small_keys_scene("SCENE_SHADOW_TEMPLE", 1, bundle)),
    ])

    # Shadow Temple Compass Room  (upstream RR_SHADOW_TEMPLE_COMPASS_ROOM, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_COMPASS_ROOM, world, [
        (Locations.SHADOW_TEMPLE_COMPASS_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.GIBDO) & can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_COMPASS_ROOM, world, [
        (Regions.SHADOW_TEMPLE_FIRST_BEAMOS,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.GIBDO))),
    ])

    # Shadow Temple Spinning Blades  (upstream RR_SHADOW_TEMPLE_SPINNING_BLADES, SCENE_SHADOW_TEMPLE)
    # Events
    add_events(Regions.SHADOW_TEMPLE_SPINNING_BLADES, world, [
        (EventLocations.SHADOW_TEMPLE_SPINNING_BLADES_SHADOW_SILVER_BLADES, Events.SHADOW_SILVER_BLADES,
         lambda bundle: (is_adult(bundle) & (can_use(Items.HOVER_BOOTS, bundle) | can_ground_jump(bundle))) | can_use(Items.HOOKSHOT, bundle) | bunny_hood(bundle)),
    ])
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_SPINNING_BLADES, world, [
        (Locations.SHADOW_TEMPLE_EARLY_SILVER_RUPEE_CHEST,
         lambda bundle: has_item(Events.SHADOW_SILVER_BLADES, bundle) & has_open_chest(bundle)),
        # DEFERRED RC_SHADOW_N_UNDER_BLADE_SILVER: true
        # DEFERRED RC_SHADOW_TALL_BLOCK_BLADE_SILVER: (logic->IsAdult && (logic->CanUse(RG_HOVER_BOOTS) || logic->CanGroundJump())) || logic->CanUse(RG_HOOKSHOT) || logic->BunnyHood()
        # DEFERRED RC_SHADOW_N_NOOK_BLADE_SILVER: true
        # DEFERRED RC_SHADOW_W_NOOK_BLADE_SILVER: true
        # DEFERRED RC_SHADOW_S_UNDER_BLADE_SILVER: true
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_SPINNING_BLADES, world, [
        (Regions.SHADOW_TEMPLE_FIRST_BEAMOS,
         lambda bundle: True_()),
        (Regions.SHADOW_TEMPLE_DOCK,
         lambda bundle: has_item(Events.SHADOW_SHORTCUT_BLOCK, bundle)),
    ])

    # Shadow Temple B2 to B3 Corridor B2  (upstream RR_SHADOW_TEMPLE_B2_TO_B3_CORRIDOR_B2, SCENE_SHADOW_TEMPLE)
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_B2_TO_B3_CORRIDOR_B2, world, [
        (Regions.SHADOW_TEMPLE_FIRST_BEAMOS,
         lambda bundle: small_keys_scene("SCENE_SHADOW_TEMPLE", 1, bundle)),
        (Regions.SHADOW_TEMPLE_B2_TO_B3_CORRIDOR_B3,
         lambda bundle: can_pass_enemy(bundle, Enemies.BIG_SKULLTULA)),
    ])

    # Shadow Temple B2 to B3 Corridor B3  (upstream RR_SHADOW_TEMPLE_B2_TO_B3_CORRIDOR_B3, SCENE_SHADOW_TEMPLE)
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_B2_TO_B3_CORRIDOR_B3, world, [
        (Regions.SHADOW_TEMPLE_B2_TO_B3_CORRIDOR_B2,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
        (Regions.SHADOW_TEMPLE_UPPER_HUGE_PIT,
         lambda bundle: can_pass_enemy(bundle, Enemies.BIG_SKULLTULA)),
    ])

    # Shadow Temple Upper Huge Pit  (upstream RR_SHADOW_TEMPLE_UPPER_HUGE_PIT, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_UPPER_HUGE_PIT, world, [
        (Locations.SHADOW_TEMPLE_PIT_ROOM_SONG_OF_STORMS_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_UPPER_HUGE_PIT, world, [
        (Regions.SHADOW_TEMPLE_B2_TO_B3_CORRIDOR_B3,
         lambda bundle: can_use(Items.LONGSHOT, bundle)),
        (Regions.SHADOW_TEMPLE_UPPER_HUGE_PIT_DOOR_LEDGE,
         lambda bundle: can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
        (Regions.SHADOW_TEMPLE_LOWER_HUGE_PIT,
         lambda bundle: is_adult(bundle) | can_jump_slash(bundle) | bunny_hood(bundle) | can_do_trick(Tricks.SHADOW_MQ_HUGE_PIT, bundle)),
    ])

    # Shadow Temple Upper Huge Pit Door Ledge  (upstream RR_SHADOW_TEMPLE_UPPER_HUGE_PIT_DOOR_LEDGE, SCENE_SHADOW_TEMPLE)
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_UPPER_HUGE_PIT_DOOR_LEDGE, world, [
        (Regions.SHADOW_TEMPLE_UPPER_HUGE_PIT,
         lambda bundle: can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
        (Regions.SHADOW_TEMPLE_INVISIBLE_SPINNING_BLADES,
         lambda bundle: small_keys_scene("SCENE_SHADOW_TEMPLE", 2, bundle)),
    ])

    # Shadow Temple Lower Huge Pit  (upstream RR_SHADOW_TEMPLE_LOWER_HUGE_PIT, SCENE_SHADOW_TEMPLE)
    # Events
    add_events(Regions.SHADOW_TEMPLE_LOWER_HUGE_PIT, world, [
        (EventLocations.SHADOW_TEMPLE_LOWER_HUGE_PIT_SHADOW_SILVER_PIT, Events.SHADOW_SILVER_PIT,
         lambda bundle: True_()),
    ])
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_LOWER_HUGE_PIT, world, [
        # DEFERRED RC_SHADOW_N_PIT_SILVER: true
        # DEFERRED RC_SHADOW_S_PIT_SILVER: true
        # DEFERRED RC_SHADOW_BEAMOS_PIT_SILVER: true
        # DEFERRED RC_SHADOW_E_PIT_SILVER: true
        # DEFERRED RC_SHADOW_W_PIT_SILVER: true
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_LOWER_HUGE_PIT, world, [
        (Regions.SHADOW_TEMPLE_UPPER_HUGE_PIT,
         lambda bundle: is_adult(bundle) | can_jump_slash(bundle) | can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle)),
        (Regions.SHADOW_TEMPLE_LOWER_HUGE_PIT_DOOR_LEDGE,
         lambda bundle: (can_do_trick(Tricks.LENS_SHADOW_PLATFORM, bundle) & can_do_trick(Tricks.LENS_SHADOW, bundle)) | can_use(Items.LENS_OF_TRUTH, bundle)),
        (Regions.SHADOW_TEMPLE_STONE_UMBRELLA,
         lambda bundle: has_item(Events.SHADOW_SILVER_PIT, bundle)),
    ])

    # Shadow Temple Stone Umbrella  (upstream RR_SHADOW_TEMPLE_STONE_UMBRELLA, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_STONE_UMBRELLA, world, [
        (Locations.SHADOW_TEMPLE_FALLING_SPIKES_LOWER_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.SHADOW_TEMPLE_GS_FALLING_SPIKES_ROOM,
         lambda bundle: can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG) | (is_adult(bundle) & can_ground_jumpslash(bundle))),
        (Locations.SHADOW_TEMPLE_FALLING_SPIKES_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.SHADOW_TEMPLE_FALLING_SPIKES_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.SHADOW_TEMPLE_FALLING_SPIKES_POT3,
         lambda bundle: can_use(Items.BOOMERANG, bundle)),
        (Locations.SHADOW_TEMPLE_FALLING_SPIKES_RECTANGLE_SIGN,
         lambda bundle: can_read(bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_STONE_UMBRELLA, world, [
        (Regions.SHADOW_TEMPLE_LOWER_HUGE_PIT,
         lambda bundle: can_do_trick(Tricks.VISIBLE_COLLISION, bundle)),
        (Regions.SHADOW_TEMPLE_STONE_UMBRELLA_UPPER,
         lambda bundle: can_do_trick(Tricks.SHADOW_UMBRELLA_CLIP, bundle) | (can_do_trick(Tricks.DAMAGE_BOOST_SIMPLE, bundle) & take_damage(bundle)) | (is_adult(bundle) & ((can_do_trick(Tricks.SHADOW_UMBRELLA_HOVER, bundle) & can_use(Items.HOVER_BOOTS, bundle)) | has_item(Items.GORONS_BRACELET, bundle)))),
    ])

    # Shadow Temple Stone Umbrella Upper  (upstream RR_SHADOW_TEMPLE_STONE_UMBRELLA_UPPER, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_STONE_UMBRELLA_UPPER, world, [
        (Locations.SHADOW_TEMPLE_FALLING_SPIKES_UPPER_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.SHADOW_TEMPLE_FALLING_SPIKES_SWITCH_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.SHADOW_TEMPLE_GS_FALLING_SPIKES_ROOM,
         lambda bundle: can_do_trick(Tricks.SHADOW_UMBRELLA_GS, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_standing_shield(bundle) & can_use(Items.MASTER_SWORD, bundle)),
        (Locations.SHADOW_TEMPLE_FALLING_SPIKES_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.SHADOW_TEMPLE_FALLING_SPIKES_POT4,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_STONE_UMBRELLA_UPPER, world, [
        (Regions.SHADOW_TEMPLE_STONE_UMBRELLA,
         lambda bundle: True_()),
    ])

    # Shadow Temple Lower Huge Pit Door Ledge  (upstream RR_SHADOW_TEMPLE_LOWER_HUGE_PIT_DOOR_LEDGE, SCENE_SHADOW_TEMPLE)
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_LOWER_HUGE_PIT_DOOR_LEDGE, world, [
        (Regions.SHADOW_TEMPLE_LOWER_HUGE_PIT,
         lambda bundle: (can_do_trick(Tricks.LENS_SHADOW_PLATFORM, bundle) & can_do_trick(Tricks.LENS_SHADOW, bundle)) | can_use(Items.LENS_OF_TRUTH, bundle)),
        (Regions.SHADOW_TEMPLE_FLOOR_SPIKES_S_DOOR,
         lambda bundle: small_keys_scene("SCENE_SHADOW_TEMPLE", 2, bundle)),
    ])

    # Shadow Temple Invisible Spinning Blades  (upstream RR_SHADOW_TEMPLE_INVISIBLE_SPINNING_BLADES, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_INVISIBLE_SPINNING_BLADES, world, [
        (Locations.SHADOW_TEMPLE_INVISIBLE_BLADES_VISIBLE_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.LIKE_LIKE) & can_kill_enemy(bundle, Enemies.KEESE) & has_open_chest(bundle)),
        (Locations.SHADOW_TEMPLE_INVISIBLE_BLADES_INVISIBLE_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.LIKE_LIKE) & can_kill_enemy(bundle, Enemies.KEESE) & (can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & has_open_chest(bundle)),
        (Locations.SHADOW_TEMPLE_GS_LIKE_LIKE_ROOM,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.LIKE_LIKE) & can_kill_enemy(bundle, Enemies.KEESE)) & ((is_adult(bundle) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.SHORT_JUMPSLASH)) | can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG))),
        (Locations.SHADOW_TEMPLE_INVISIBLE_BLADES_LEFT_HEART,
         lambda bundle: (can_use(Items.SONG_OF_TIME, bundle) & is_adult(bundle)) | can_use(Items.BOOMERANG, bundle)),
        (Locations.SHADOW_TEMPLE_INVISIBLE_BLADES_RIGHT_HEART,
         lambda bundle: (can_use(Items.SONG_OF_TIME, bundle) & is_adult(bundle)) | can_use(Items.BOOMERANG, bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_INVISIBLE_SPINNING_BLADES, world, [
        (Regions.SHADOW_TEMPLE_UPPER_HUGE_PIT_DOOR_LEDGE,
         lambda bundle: True_()),
    ])

    # Shadow Temple Floor Spikes South Door  (upstream RR_SHADOW_TEMPLE_FLOOR_SPIKES_S_DOOR, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_FLOOR_SPIKES_S_DOOR, world, [
        # DEFERRED RC_SHADOW_W_TARGET_SPIKES_SILVER: logic->CanUse(RG_HOOKSHOT)
        # DEFERRED RC_SHADOW_E_TARGET_SPIKES_SILVER: logic->CanUse(RG_LONGSHOT)
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_FLOOR_SPIKES_S_DOOR, world, [
        (Regions.SHADOW_TEMPLE_LOWER_HUGE_PIT_DOOR_LEDGE,
         lambda bundle: small_keys_scene("SCENE_SHADOW_TEMPLE", 2, bundle)),
        (Regions.SHADOW_TEMPLE_FLOOR_SPIKES_ROOM,
         lambda bundle: can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle) | can_use(Items.HOVER_BOOTS, bundle) | can_use(Items.GORON_TUNIC, bundle) | take_damage(bundle)),
    ])

    # Shadow Temple Floor Spikes Room  (upstream RR_SHADOW_TEMPLE_FLOOR_SPIKES_ROOM, SCENE_SHADOW_TEMPLE)
    # Events
    add_events(Regions.SHADOW_TEMPLE_FLOOR_SPIKES_ROOM, world, [
        (EventLocations.SHADOW_TEMPLE_FLOOR_SPIKES_ROOM_SHADOW_SILVER_SPIKES, Events.SHADOW_SILVER_SPIKES,
         lambda bundle: (can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & (can_use(Items.HOOKSHOT, bundle) | (is_adult(bundle) & can_middair_ground_jump(bundle) & ((bunny_hovers(bundle) & can_jump_slash(bundle)) | can_recoil_hover(bundle, Recoil.HAMMER))))),
    ])
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_FLOOR_SPIKES_ROOM, world, [
        (Locations.SHADOW_TEMPLE_INVISIBLE_SPIKES_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.REDEAD) & has_open_chest(bundle)),
        # DEFERRED RC_SHADOW_E_TARGET_SPIKES_SILVER: logic->CanUse(RG_HOOKSHOT)
        # DEFERRED RC_SHADOW_FLOOR_SPIKES_SILVER: true
        # DEFERRED RC_SHADOW_W_TARGET_SPIKES_SILVER: logic->CanUse(RG_HOOKSHOT)
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_FLOOR_SPIKES_ROOM, world, [
        (Regions.SHADOW_TEMPLE_FLOOR_SPIKES_S_DOOR,
         lambda bundle: True_()),
        (Regions.SHADOW_TEMPLE_FLOOR_SPIKES_W_DOOR,
         lambda bundle: True_()),
        (Regions.SHADOW_TEMPLE_SPIKES_CORNER_PLATFORM,
         lambda bundle: (can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & (is_adult(bundle) & can_middair_ground_jump(bundle) | can_use(Items.HOOKSHOT, bundle))),
        (Regions.SHADOW_TEMPLE_SPIKES_DOOR_PLATFORM,
         lambda bundle: (can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & ((is_adult(bundle) & can_middair_ground_jump(bundle)) | (((is_adult(bundle) & any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.REDEAD))) & can_use(Items.HOOKSHOT, bundle) | can_use(Items.LONGSHOT, bundle))))),
    ])

    # Shadow Temple Floor Spikes West Door  (upstream RR_SHADOW_TEMPLE_FLOOR_SPIKES_W_DOOR, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_FLOOR_SPIKES_W_DOOR, world, [
        # DEFERRED RC_SHADOW_W_TARGET_SPIKES_SILVER: logic->CanUse(RG_HOOKSHOT)
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_FLOOR_SPIKES_W_DOOR, world, [
        (Regions.SHADOW_TEMPLE_SKULL_JAR,
         lambda bundle: has_item(Events.SHADOW_SILVER_SPIKES, bundle)),
        (Regions.SHADOW_TEMPLE_FLOOR_SPIKES_ROOM,
         lambda bundle: can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle) | can_use(Items.HOVER_BOOTS, bundle) | can_use(Items.GORON_TUNIC, bundle) | take_damage(bundle)),
    ])

    # Shadow Temple Spikes Corner Platform  (upstream RR_SHADOW_TEMPLE_SPIKES_CORNER_PLATFORM, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_SPIKES_CORNER_PLATFORM, world, [
        # DEFERRED RC_SHADOW_PLATFORM_SPIKES_SILVER: true
        # DEFERRED RC_SHADOW_AIRBORNE_SPIKES_SILVER: ctx->GetTrickOption(RT_LENS_SHADOW) || logic->CanUse(RG_LENS_OF_TRUTH) || logic->CanUse(RG_HOVER_BOOTS) || logic->CanUse(RG_GORON_TUNIC) || logic->TakeDamage()
        # DEFERRED RC_SHADOW_W_TARGET_SPIKES_SILVER: (logic->BunnyHovers() && logic->CanJumpslash()) || logic->CanUse(RG_HOOKSHOT) || logic->CanRecoilHover(RECOIL_SWORD_AND_SHIELD)
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_SPIKES_CORNER_PLATFORM, world, [
        (Regions.SHADOW_TEMPLE_FLOOR_SPIKES_ROOM,
         lambda bundle: can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle) | can_use(Items.HOVER_BOOTS, bundle) | can_use(Items.GORON_TUNIC, bundle) | take_damage(bundle)),
    ])

    # Shadow Temple Spikes Door Platform  (upstream RR_SHADOW_TEMPLE_SPIKES_DOOR_PLATFORM, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_SPIKES_DOOR_PLATFORM, world, [
        # DEFERRED RC_SHADOW_AIRBORNE_SPIKES_SILVER: true
        # DEFERRED RC_SHADOW_E_TARGET_SPIKES_SILVER: (logic->BunnyHovers() && logic->CanJumpslash()) || logic->CanUse(RG_LONGSHOT) || logic->CanRecoilHover(RECOIL_HAMMER)
        # DEFERRED RC_SHADOW_W_TARGET_SPIKES_SILVER: logic->CanUse(RG_LONGSHOT)
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_SPIKES_DOOR_PLATFORM, world, [
        (Regions.SHADOW_TEMPLE_FLOOR_SPIKES_ROOM,
         lambda bundle: can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle) | can_use(Items.HOVER_BOOTS, bundle) | can_use(Items.GORON_TUNIC, bundle) | take_damage(bundle)),
        (Regions.SHADOW_TEMPLE_SPIKES_CORNER_PLATFORM,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle)),
        (Regions.SHADOW_TEMPLE_UPPER_WIND_TUNNEL,
         lambda bundle: small_keys_scene("SCENE_SHADOW_TEMPLE", 3, bundle)),
    ])

    # Shadow Temple Skull Jar  (upstream RR_SHADOW_TEMPLE_SKULL_JAR, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_SKULL_JAR, world, [
        (Locations.SHADOW_TEMPLE_FREESTANDING_KEY,
         lambda bundle: can_use(Items.BOMB_BAG, bundle) | has_item(Items.GORONS_BRACELET, bundle) | (can_do_trick(Tricks.SHADOW_FREESTANDING_KEY, bundle) & can_use(Items.BOMBCHUS_5, bundle))),
        (Locations.SHADOW_TEMPLE_GS_SINGLE_GIANT_POT,
         lambda bundle: can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_SKULL_JAR, world, [
        (Regions.SHADOW_TEMPLE_FLOOR_SPIKES_W_DOOR,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.KEESE))),
    ])

    # Shadow Temple Upper Wind Tunnel  (upstream RR_SHADOW_TEMPLE_UPPER_WIND_TUNNEL, SCENE_SHADOW_TEMPLE)
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_UPPER_WIND_TUNNEL, world, [
        (Regions.SHADOW_TEMPLE_SPIKES_DOOR_PLATFORM,
         lambda bundle: small_keys_scene("SCENE_SHADOW_TEMPLE", 3, bundle)),
        (Regions.SHADOW_TEMPLE_LOWER_WIND_TUNNEL,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) | ((can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle)) & can_pass_enemy(bundle, Enemies.BIG_SKULLTULA))),
    ])

    # Shadow Temple Lower Wind Tunnel  (upstream RR_SHADOW_TEMPLE_LOWER_WIND_TUNNEL, SCENE_SHADOW_TEMPLE)
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_LOWER_WIND_TUNNEL, world, [
        (Regions.SHADOW_TEMPLE_UPPER_WIND_TUNNEL,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
        (Regions.SHADOW_TEMPLE_WIND_TUNNEL_ALCOVE,
         lambda bundle: can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
        (Regions.SHADOW_TEMPLE_WIND_TUNNEL_HINT_ROOM,
         lambda bundle: True_()),
    ])

    # Shadow Temple Wind Tunnel Alcove  (upstream RR_SHADOW_TEMPLE_WIND_TUNNEL_ALCOVE, SCENE_SHADOW_TEMPLE)
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_WIND_TUNNEL_ALCOVE, world, [
        (Regions.SHADOW_TEMPLE_LOWER_WIND_TUNNEL,
         lambda bundle: (can_do_trick(Tricks.SHADOW_MQ_WINDY_WALKWAY, bundle)) | can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle)),
        (Regions.SHADOW_TEMPLE_ROOM_TO_BOAT,
         lambda bundle: True_()),
    ])

    # Shadow Temple Wind Tunnel Hint Room  (upstream RR_SHADOW_TEMPLE_WIND_TUNNEL_HINT_ROOM, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_WIND_TUNNEL_HINT_ROOM, world, [
        (Locations.SHADOW_TEMPLE_WIND_HINT_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.REDEAD) & has_open_chest(bundle)),
        (Locations.SHADOW_TEMPLE_WIND_HINT_SUNS_SONG_FAIRY,
         lambda bundle: can_use(Items.SUNS_SONG, bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_WIND_TUNNEL_HINT_ROOM, world, [
        (Regions.SHADOW_TEMPLE_LOWER_WIND_TUNNEL,
         lambda bundle: can_kill_enemy(bundle, Enemies.REDEAD)),
    ])

    # Shadow Temple Room to Boat  (upstream RR_SHADOW_TEMPLE_ROOM_TO_BOAT, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_ROOM_TO_BOAT, world, [
        (Locations.SHADOW_TEMPLE_AFTER_WIND_ENEMY_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.GIBDO, EnemyDistance.CLOSE, True, 2) & has_open_chest(bundle)),
        (Locations.SHADOW_TEMPLE_AFTER_WIND_HIDDEN_CHEST,
         lambda bundle: (can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & has_explosives(bundle) & has_open_chest(bundle)),
        (Locations.SHADOW_TEMPLE_AFTER_WIND_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.SHADOW_TEMPLE_AFTER_WIND_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_ROOM_TO_BOAT, world, [
        (Regions.SHADOW_TEMPLE_WIND_TUNNEL_ALCOVE,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.GIBDO, EnemyDistance.CLOSE, True, 2))),
        (Regions.SHADOW_TEMPLE_DOCK,
         lambda bundle: small_keys_scene("SCENE_SHADOW_TEMPLE", 4, bundle)),
    ])

    # Shadow Temple Dock  (upstream RR_SHADOW_TEMPLE_DOCK, SCENE_SHADOW_TEMPLE)
    # Events
    add_events(Regions.SHADOW_TEMPLE_DOCK, world, [
        (EventLocations.SHADOW_TEMPLE_DOCK_SHADOW_SHORTCUT_BLOCK, Events.SHADOW_SHORTCUT_BLOCK,
         lambda bundle: has_item(Items.GORONS_BRACELET, bundle)),
    ])
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_DOCK, world, [
        (Locations.SHADOW_TEMPLE_GS_NEAR_SHIP,
         lambda bundle: can_use(Items.LONGSHOT, bundle)),
        (Locations.SHADOW_TEMPLE_SCARECROW_NEAR_SHIP_NORTH_HEART,
         lambda bundle: reach_distant_scarecrow(bundle)),
        (Locations.SHADOW_TEMPLE_SCARECROW_NEAR_SHIP_SOUTH_HEART,
         lambda bundle: reach_distant_scarecrow(bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_DOCK, world, [
        (Regions.SHADOW_TEMPLE_ROOM_TO_BOAT,
         lambda bundle: small_keys_scene("SCENE_SHADOW_TEMPLE", 4, bundle)),
        (Regions.SHADOW_TEMPLE_SPINNING_BLADES,
         lambda bundle: has_item(Events.SHADOW_SHORTCUT_BLOCK, bundle) & has_climb(bundle)),
        (Regions.SHADOW_TEMPLE_BEYOND_BOAT,
         lambda bundle: ((is_adult(bundle) & ((has_item(Items.GORONS_BRACELET, bundle) & has_climb(bundle)) | can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle))) | (can_do_trick(Tricks.HOOKSHOT_LADDERS, bundle) & can_use(Items.HOOKSHOT, bundle))) & can_use(Items.ZELDAS_LULLABY, bundle)),
    ])

    # Shadow Temple Beyond Boat  (upstream RR_SHADOW_TEMPLE_BEYOND_BOAT, SCENE_SHADOW_TEMPLE)
    # Events
    add_events(Regions.SHADOW_TEMPLE_BEYOND_BOAT, world, [
        (EventLocations.SHADOW_TEMPLE_BEYOND_BOAT_SHADOW_BRIDGE_BEYOND_BOAT_LOWERED, Events.SHADOW_BRIDGE_BEYOND_BOAT_LOWERED,
         lambda bundle: can_use(Items.FAIRY_BOW, bundle) | (can_do_trick(Tricks.SHADOW_STATUE, bundle) & can_use(Items.BOMBCHUS_5, bundle))),
    ])
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_BEYOND_BOAT, world, [
        (Locations.SHADOW_TEMPLE_AFTER_BOAT_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.SHADOW_TEMPLE_AFTER_BOAT_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_BEYOND_BOAT, world, [
        (Regions.SHADOW_TEMPLE_MAZE,
         lambda bundle: True_()),
        (Regions.SHADOW_TEMPLE_CHASM_SCARECROW,
         lambda bundle: reach_distant_scarecrow(bundle)),
        (Regions.SHADOW_TEMPLE_ACROSS_CHASM,
         lambda bundle: has_item(Events.SHADOW_BRIDGE_BEYOND_BOAT_LOWERED, bundle) | can_recoil_hover(bundle, Recoil.HAMMER_AND_SHIELD)),
    ])

    # Shadow Temple Chasm Scarecrow  (upstream RR_SHADOW_TEMPLE_CHASM_SCARECROW, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_CHASM_SCARECROW, world, [
        (Locations.SHADOW_TEMPLE_AFTER_SHIP_UPPER_LEFT_HEART,
         lambda bundle: True_()),
        (Locations.SHADOW_TEMPLE_AFTER_SHIP_UPPER_RIGHT_HEART,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_CHASM_SCARECROW, world, [
        (Regions.SHADOW_TEMPLE_ACROSS_CHASM,
         lambda bundle: True_()),
        (Regions.SHADOW_TEMPLE_BROKEN_PILLAR,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle) | (bunny_hood(bundle) & can_jump_slash(bundle)) | (is_adult(bundle) & ((can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & can_jump_slash(bundle)) | bunny_hood(bundle)))),
    ])

    # Shadow Temple Across Chasm  (upstream RR_SHADOW_TEMPLE_ACROSS_CHASM, SCENE_SHADOW_TEMPLE)
    # Events
    add_events(Regions.SHADOW_TEMPLE_ACROSS_CHASM, world, [
        (EventLocations.SHADOW_TEMPLE_ACROSS_CHASM_SHADOW_BRIDGE_BEYOND_BOAT_LOWERED, Events.SHADOW_BRIDGE_BEYOND_BOAT_LOWERED,
         lambda bundle: can_detonate_upright_bomb_flower(bundle)),
    ])
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_ACROSS_CHASM, world, [
        (Locations.SHADOW_TEMPLE_AFTER_BOAT_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.SHADOW_TEMPLE_AFTER_BOAT_POT4,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_ACROSS_CHASM, world, [
        (Regions.SHADOW_TEMPLE_BEYOND_BOAT,
         lambda bundle: (has_item(Events.SHADOW_BRIDGE_BEYOND_BOAT_LOWERED, bundle) & is_adult(bundle)) | can_recoil_hover(bundle, Recoil.HAMMER)),
        (Regions.SHADOW_TEMPLE_BROKEN_PILLAR,
         lambda bundle: is_adult(bundle) & can_use(Items.SONG_OF_TIME, bundle)),
        (Regions.SHADOW_TEMPLE_PRE_BOSS_ROOM,
         lambda bundle: small_keys_scene("SCENE_SHADOW_TEMPLE", 5, bundle)),
    ])

    # Shadow Temple Broken Pillar  (upstream RR_SHADOW_TEMPLE_BROKEN_PILLAR, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_BROKEN_PILLAR, world, [
        (Locations.SHADOW_TEMPLE_AFTER_SHIP_LOWER_HEART,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_BROKEN_PILLAR, world, [
        (Regions.SHADOW_TEMPLE_ACROSS_CHASM,
         lambda bundle: True_()),
        (Regions.SHADOW_TEMPLE_CHASM_SCARECROW,
         lambda bundle: ((is_adult(bundle)) & reach_scarecrow(bundle) | (is_child(bundle)) & reach_distant_scarecrow(bundle))),
    ])

    # Shadow Temple Maze  (upstream RR_SHADOW_TEMPLE_MAZE, SCENE_SHADOW_TEMPLE)
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_MAZE, world, [
        (Regions.SHADOW_TEMPLE_BEYOND_BOAT,
         lambda bundle: True_()),
        (Regions.SHADOW_TEMPLE_X_CROSS,
         lambda bundle: True_()),
        (Regions.SHADOW_TEMPLE_THREE_SKULL_JARS,
         lambda bundle: True_()),
        (Regions.SHADOW_TEMPLE_WOODEN_SPIKES,
         lambda bundle: True_()),
    ])

    # Shadow Temple X-Cross  (upstream RR_SHADOW_TEMPLE_X_CROSS, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_X_CROSS, world, [
        (Locations.SHADOW_TEMPLE_INVISIBLE_FLOORMASTER_CHEST,
         lambda bundle: (can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & can_kill_enemy(bundle, Enemies.FLOORMASTER) & has_open_chest(bundle)),
        (Locations.SHADOW_TEMPLE_FLOORMASTER_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.SHADOW_TEMPLE_FLOORMASTER_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_X_CROSS, world, [
        (Regions.SHADOW_TEMPLE_MAZE,
         lambda bundle: any_age_time(bundle, lambda bundle: (can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & can_kill_enemy(bundle, Enemies.FLOORMASTER))),
    ])

    # Shadow Temple Three Skull Jars  (upstream RR_SHADOW_TEMPLE_THREE_SKULL_JARS, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_THREE_SKULL_JARS, world, [
        (Locations.SHADOW_TEMPLE_GS_TRIPLE_GIANT_POT,
         lambda bundle: has_item(Items.GORONS_BRACELET, bundle) | can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.SHORT_JUMPSLASH)),
        # DEFERRED RC_SHADOW_TEMPLE_WONDER_THREE_POTS: logic->CanUse(RG_FAIRY_BOW)
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_THREE_SKULL_JARS, world, [
        (Regions.SHADOW_TEMPLE_MAZE,
         lambda bundle: True_()),
    ])

    # Shadow Temple Wooden Spikes  (upstream RR_SHADOW_TEMPLE_WOODEN_SPIKES, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_WOODEN_SPIKES, world, [
        (Locations.SHADOW_TEMPLE_SPIKE_WALLS_LEFT_CHEST,
         lambda bundle: can_use(Items.DINS_FIRE, bundle) & has_open_chest(bundle)),
        (Locations.SHADOW_TEMPLE_BOSS_KEY_CHEST,
         lambda bundle: can_use(Items.DINS_FIRE, bundle) & can_open_large_chest(bundle)),
        (Locations.SHADOW_TEMPLE_SPIKE_WALLS_POT1,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_WOODEN_SPIKES, world, [
        (Regions.SHADOW_TEMPLE_MAZE,
         lambda bundle: True_()),
    ])

    # Shadow Temple Pre Boss Room  (upstream RR_SHADOW_TEMPLE_PRE_BOSS_ROOM, SCENE_SHADOW_TEMPLE)
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_PRE_BOSS_ROOM, world, [
        (Regions.SHADOW_TEMPLE_ACROSS_CHASM,
         lambda bundle: small_keys_scene("SCENE_SHADOW_TEMPLE", 5, bundle)),
        (Regions.SHADOW_TEMPLE_BOSS_DOOR,
         lambda bundle: (can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & (can_use(Items.HOVER_BOOTS, bundle) | (bunny_hood(bundle) & is_adult(bundle)))),
    ])

    # Shadow Temple Boss Door  (upstream RR_SHADOW_TEMPLE_BOSS_DOOR, SCENE_SHADOW_TEMPLE)
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_BOSS_DOOR, world, [
        # DEFERRED RC_SHADOW_BOSS_KEY_HINT: true
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_BOSS_DOOR, world, [
        (Regions.SHADOW_TEMPLE_PRE_BOSS_ROOM,
         lambda bundle: (can_do_trick(Tricks.LENS_SHADOW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & (can_use(Items.HOVER_BOOTS, bundle) | (bunny_hood(bundle) & is_adult(bundle)))),
        (Regions.SHADOW_TEMPLE_BOSS_ENTRYWAY,
         lambda bundle: True_()),
    ])

    # Shadow Temple Boss Entryway  (upstream RR_SHADOW_TEMPLE_BOSS_ENTRYWAY, SCENE_SHADOW_TEMPLE)
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_BOSS_ENTRYWAY, world, [
        (Regions.SHADOW_TEMPLE_BOSS_DOOR,
         lambda bundle: True_()),
        (Regions.SHADOW_TEMPLE_BOSS_ROOM,
         lambda bundle: has_item(Items.SHADOW_TEMPLE_BOSS_KEY, bundle)),
    ])

    # Shadow Temple Boss Room  (upstream RR_SHADOW_TEMPLE_BOSS_ROOM, SCENE_SHADOW_TEMPLE_BOSS)
    # Events
    add_events(Regions.SHADOW_TEMPLE_BOSS_ROOM, world, [
        (EventLocations.SHADOW_TEMPLE_BOSS_ROOM_SHADOW_TEMPLE_CLEAR, Events.SHADOW_TEMPLE_COMPLETED,
         lambda bundle: can_kill_enemy(bundle, Enemies.BONGO_BONGO)),
    ])
    # Locations
    add_locations(Regions.SHADOW_TEMPLE_BOSS_ROOM, world, [
        (Locations.SHADOW_TEMPLE_BONGO_BONGO_HEART_CONTAINER,
         lambda bundle: has_item(Events.SHADOW_TEMPLE_COMPLETED, bundle)),
        (Locations.BONGO_BONGO,
         lambda bundle: has_item(Events.SHADOW_TEMPLE_COMPLETED, bundle)),
    ])
    # Connections
    connect_regions(Regions.SHADOW_TEMPLE_BOSS_ROOM, world, [
        (Regions.SHADOW_TEMPLE_BOSS_ENTRYWAY,
         lambda bundle: False_()),
        (Regions.GRAVEYARD_WARP_PAD_REGION,
         lambda bundle: has_item(Events.SHADOW_TEMPLE_COMPLETED, bundle)),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_FARM_NUTS', 'SHADOW_BRIDGE_BEYOND_BOAT_LOWERED', 'SHADOW_SHORTCUT_BLOCK', 'SHADOW_SILVER_BLADES', 'SHADOW_SILVER_PIT', 'SHADOW_SILVER_SPIKES', 'SHADOW_TEMPLE_COMPLETED']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (24): ['RC_SHADOW_N_UNDER_BLADE_SILVER', 'RC_SHADOW_TALL_BLOCK_BLADE_SILVER', 'RC_SHADOW_N_NOOK_BLADE_SILVER', 'RC_SHADOW_W_NOOK_BLADE_SILVER', 'RC_SHADOW_S_UNDER_BLADE_SILVER', 'RC_SHADOW_N_PIT_SILVER', 'RC_SHADOW_S_PIT_SILVER', 'RC_SHADOW_BEAMOS_PIT_SILVER', 'RC_SHADOW_E_PIT_SILVER', 'RC_SHADOW_W_PIT_SILVER', 'RC_SHADOW_W_TARGET_SPIKES_SILVER', 'RC_SHADOW_E_TARGET_SPIKES_SILVER', 'RC_SHADOW_E_TARGET_SPIKES_SILVER', 'RC_SHADOW_FLOOR_SPIKES_SILVER', 'RC_SHADOW_W_TARGET_SPIKES_SILVER', 'RC_SHADOW_W_TARGET_SPIKES_SILVER', 'RC_SHADOW_PLATFORM_SPIKES_SILVER', 'RC_SHADOW_AIRBORNE_SPIKES_SILVER', 'RC_SHADOW_W_TARGET_SPIKES_SILVER', 'RC_SHADOW_AIRBORNE_SPIKES_SILVER', 'RC_SHADOW_E_TARGET_SPIKES_SILVER', 'RC_SHADOW_W_TARGET_SPIKES_SILVER', 'RC_SHADOW_TEMPLE_WONDER_THREE_POTS', 'RC_SHADOW_BOSS_KEY_HINT']
