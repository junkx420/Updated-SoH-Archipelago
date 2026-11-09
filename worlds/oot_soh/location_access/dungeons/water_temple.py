"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/dungeons/water_temple.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    WATER_TEMPLE_ENTRANCE_LEDGE_WATER_COULD_MIDDLE = "Water Temple Entrance Ledge Water Could Middle"
    WATER_TEMPLE_ENTRANCE_LEDGE_WATER_COULD_HIGH_FROM_MID = "Water Temple Entrance Ledge Water Could High From Mid"
    WATER_TEMPLE_MAIN_WATER_PUSHED_1F_BLOCK = "Water Temple Main Water Pushed 1f Block"
    WATER_TEMPLE_MAIN_WATER_COULD_MIDDLE = "Water Temple Main Water Could Middle"
    WATER_TEMPLE_MAIN_WATER_COULD_HIGH_FROM_MID = "Water Temple Main Water Could High From Mid"
    WATER_TEMPLE_SIDE_TOWER_1F_WATER_COULD_LOW_FROM_HIGH = "Water Temple Side Tower 1F Water Could Low From High"
    WATER_TEMPLE_LOW_EMBLEM_WATER_LOW = "Water Temple Low Emblem Water Low"
    WATER_TEMPLE_LOW_EMBLEM_WATER_COULD_LOW = "Water Temple Low Emblem Water Could Low"
    WATER_TEMPLE_BOSS_KEY_ROOM_FAIRY_ACCESS = "Water Temple Boss Key Room Fairy Access"
    WATER_TEMPLE_PILLAR_2F_WATER_MIDDLE = "Water Temple Pillar 2F Water Middle"
    WATER_TEMPLE_PILLAR_2F_WATER_COULD_MIDDLE = "Water Temple Pillar 2F Water Could Middle"
    WATER_TEMPLE_HIGH_EMBLEM_WATER_HIGH = "Water Temple High Emblem Water High"
    WATER_TEMPLE_HIGH_EMBLEM_WATER_SCARECROW = "Water Temple High Emblem Water Scarecrow"
    WATER_TEMPLE_RISING_TARGET_LEDGE_FAIRY_ACCESS = "Water Temple Rising Target Ledge Fairy Access"
    WATER_TEMPLE_RISING_TARGET_LEDGE_WATER_COULD_MIDDLE = "Water Temple Rising Target Ledge Water Could Middle"
    WATER_TEMPLE_RISING_TARGET_LEDGE_WATER_COULD_HIGH_FROM_MID = "Water Temple Rising Target Ledge Water Could High From Mid"
    WATER_TEMPLE_RISING_TARGET_LEDGE_WATER_COULD_LOW = "Water Temple Rising Target Ledge Water Could Low"
    WATER_TEMPLE_BOSS_ROOM_WATER_TEMPLE_CLEAR = "Water Temple Boss Room Water Temple Clear"


def set_region_rules(world: "SohWorld") -> None:

    # Water Temple Entryway  (upstream RR_WATER_TEMPLE_ENTRYWAY, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_ENTRYWAY, world, [
        (Regions.WATER_TEMPLE_ENTRANCE_LEDGE,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) & True_()),
        (Regions.LH_FROM_WATER_TEMPLE,
         lambda bundle: True_()),
    ])

    # Water Temple Entrance Ledge  (upstream RR_WATER_TEMPLE_ENTRANCE_LEDGE, SCENE_WATER_TEMPLE)
    # Events
    add_events(Regions.WATER_TEMPLE_ENTRANCE_LEDGE, world, [
        (EventLocations.WATER_TEMPLE_ENTRANCE_LEDGE_WATER_COULD_MIDDLE, Events.WATER_COULD_MIDDLE,
         lambda bundle: has_fire_source_with_torch(bundle) | can_use(Items.FAIRY_BOW, bundle)),
        (EventLocations.WATER_TEMPLE_ENTRANCE_LEDGE_WATER_COULD_HIGH_FROM_MID, Events.WATER_COULD_HIGH_FROM_MID,
         lambda bundle: (is_adult(bundle) | can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | has_item(Items.BRONZE_SCALE, bundle) | bunny_hood(bundle)) & can_hit_switch(bundle, EnemyDistance.BOMB_THROW)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_ENTRANCE_LEDGE, world, [
        (Regions.WATER_TEMPLE_ENTRYWAY,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle)),
        (Regions.WATER_TEMPLE_MAIN,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_3F_CENTRAL_A,
         lambda bundle: (water_level(bundle, WaterLevel.HIGH) & can_use(Items.HOOKSHOT, bundle)) | can_use(Items.HOVER_BOOTS, bundle) | (is_adult(bundle) & bunny_hood(bundle))),
        (Regions.WATER_TEMPLE_3F_CENTRAL_H,
         lambda bundle: water_level(bundle, WaterLevel.HIGH) & (can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | (is_adult(bundle) & bunny_hood(bundle)))),
        (Regions.WATER_TEMPLE_3F_CENTRAL_LM,
         lambda bundle: (can_use(Items.HOVER_BOOTS, bundle) | (is_adult(bundle) & bunny_hood(bundle))) & water_level(bundle, WaterLevel.LOW_OR_MID)),
        (Regions.WATER_TEMPLE_2F_CENTRAL_LM,
         lambda bundle: water_level(bundle, WaterLevel.LOW_OR_MID)),
    ])

    # Water Temple Main  (upstream RR_WATER_TEMPLE_MAIN, SCENE_WATER_TEMPLE)
    # Events
    add_events(Regions.WATER_TEMPLE_MAIN, world, [
        (EventLocations.WATER_TEMPLE_MAIN_WATER_PUSHED_1F_BLOCK, Events.WATER_PUSHED_1F_BLOCK,
         lambda bundle: water_level(bundle, WaterLevel.LOW) & has_item(Items.GORONS_BRACELET, bundle)),
        (EventLocations.WATER_TEMPLE_MAIN_WATER_COULD_MIDDLE, Events.WATER_COULD_MIDDLE,
         lambda bundle: (can_use(Items.LONGSHOT, bundle) & (has_fire_source_with_torch(bundle) | can_use(Items.FAIRY_BOW, bundle))) | (can_use(Items.HOOKSHOT, bundle) & small_keys_scene("SCENE_WATER_TEMPLE", 5, bundle))),
        (EventLocations.WATER_TEMPLE_MAIN_WATER_COULD_HIGH_FROM_MID, Events.WATER_COULD_HIGH_FROM_MID,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) & can_hit_switch(bundle, EnemyDistance.BOMB_THROW)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_MAIN, world, [
        (Regions.WATER_TEMPLE_ENTRANCE_LEDGE,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) & water_level(bundle, WaterLevel.HIGH)),
        (Regions.WATER_TEMPLE_SIDE_TOWER_1F,
         lambda bundle: (water_timer_at_least(bundle, 24) & can_use(Items.IRON_BOOTS, bundle)) | (water_level(bundle, WaterLevel.MID) & has_item(Items.GOLDEN_SCALE, bundle) & water_timer_at_least(bundle, 16)) | water_level(bundle, WaterLevel.LOW) | (can_use(Items.LONGSHOT, bundle) & can_do_trick(Tricks.WATER_LONGSHOT_TORCH, bundle) & has_item(Items.BRONZE_SCALE, bundle) & water_timer_at_least(bundle, 8))),
        (Regions.WATER_TEMPLE_3F_CENTRAL_A,
         lambda bundle: water_level(bundle, WaterLevel.HIGH) & has_item(Items.BRONZE_SCALE, bundle)),
        (Regions.WATER_TEMPLE_3F_CENTRAL_H,
         lambda bundle: water_level(bundle, WaterLevel.HIGH) & has_item(Items.BRONZE_SCALE, bundle)),
        (Regions.WATER_TEMPLE_2F_CENTRAL_H,
         lambda bundle: water_level(bundle, WaterLevel.HIGH) & can_use(Items.IRON_BOOTS, bundle) & ((water_timer_at_least(bundle, 8) & has_item(Items.BRONZE_SCALE, bundle)) | (water_timer_at_least(bundle, 40) & can_use(Items.LONGSHOT, bundle)))),
        (Regions.WATER_TEMPLE_2F_CENTRAL_LM,
         lambda bundle: water_level(bundle, WaterLevel.LOW_OR_MID) & ((water_level(bundle, WaterLevel.MID) & has_item(Items.BRONZE_SCALE, bundle)) | ((water_level(bundle, WaterLevel.LOW) | (can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 40))) & can_use(Items.LONGSHOT, bundle)))),
        (Regions.WATER_TEMPLE_PILLAR_1F,
         lambda bundle: water_level(bundle, WaterLevel.LOW) & small_keys_scene("SCENE_WATER_TEMPLE", 5, bundle)),
        (Regions.WATER_TEMPLE_SPIKE_MOAT,
         lambda bundle: ((water_level(bundle, WaterLevel.LOW) & has_item(Items.BRONZE_SCALE, bundle)) | (can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16) & (can_use(Items.HOOKSHOT, bundle) | has_item(Items.BRONZE_SCALE, bundle))))),
        (Regions.WATER_TEMPLE_BLOCK_U_BEND,
         lambda bundle: has_item(Events.WATER_PUSHED_1F_BLOCK, bundle) & ((can_use(Items.IRON_BOOTS, bundle) & has_item(Items.BRONZE_SCALE, bundle) & water_timer_at_least(bundle, 16)) | (water_level(bundle, WaterLevel.LOW) & has_item(Items.SILVER_SCALE, bundle)))),
        (Regions.WATER_TEMPLE_NEAR_CAGE_STEPS,
         lambda bundle: any_age_time(bundle, lambda bundle: water_level(bundle, WaterLevel.LOW) & has_explosives(bundle)) & (water_level(bundle, WaterLevel.LOW) & has_item(Items.SILVER_SCALE, bundle) | (can_use(Items.IRON_BOOTS, bundle) & has_item(Items.BRONZE_SCALE, bundle) & water_timer_at_least(bundle, 16)))),
        (Regions.WATER_TEMPLE_RISING_TARGET_LEDGE,
         lambda bundle: water_level(bundle, WaterLevel.HIGH) & can_do_trick(Tricks.WATER_IRON_BOOTS_LEDGE_GRAB, bundle) & is_adult(bundle) & has_item(Items.BRONZE_SCALE, bundle) & can_use(Items.IRON_BOOTS, bundle)),
    ])

    # Water Temple 3F Central Any Water  (upstream RR_WATER_TEMPLE_3F_CENTRAL_A, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_3F_CENTRAL_A, world, [
        (Locations.WATER_TEMPLE_MAIN_LEVEL2_POT1,
         lambda bundle: can_use(Items.BOOMERANG, bundle) | (can_break_pots(bundle, EnemyDistance.BOOMERANG, False, True) & has_item(Items.GOLDEN_SCALE, bundle))),
        (Locations.WATER_TEMPLE_MAIN_LEVEL2_POT2,
         lambda bundle: can_use(Items.BOOMERANG, bundle) | (can_break_pots(bundle, EnemyDistance.BOOMERANG, False, True) & has_item(Items.GOLDEN_SCALE, bundle))),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_3F_CENTRAL_A, world, [
        (Regions.WATER_TEMPLE_MAIN,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_ENTRANCE_LEDGE,
         lambda bundle: can_use(Items.LONGSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | (is_adult(bundle) & bunny_hood(bundle))),
        (Regions.WATER_TEMPLE_HIGH_EMBLEM,
         lambda bundle: water_3f_central_to_high_emblem(bundle)),
        (Regions.WATER_TEMPLE_JET_CHEST_ROOM,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
        (Regions.WATER_TEMPLE_RISING_TARGET_LEDGE,
         lambda bundle: can_do_trick(Tricks.HOVER_BOOST_SIMPLE, bundle) & can_use(Items.HOVER_BOOTS, bundle) & (can_use(Items.MEGATON_HAMMER, bundle) | (can_do_trick(Tricks.DAMAGE_BOOST_SIMPLE, bundle) & has_explosives(bundle)))),
    ])

    # Water Temple 3F Central High Water  (upstream RR_WATER_TEMPLE_3F_CENTRAL_H, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_3F_CENTRAL_H, world, [
        (Regions.WATER_TEMPLE_3F_CENTRAL_A,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_2F_CENTRAL_H,
         lambda bundle: can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8) & has_item(Items.BRONZE_SCALE, bundle)),
        (Regions.WATER_TEMPLE_OUTSIDE_WATERFALL,
         lambda bundle: is_adult(bundle) | has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle)),
        (Regions.WATER_TEMPLE_BLOCK_LOOP_3F_H,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle) | has_item(Items.BRONZE_SCALE, bundle)),
        (Regions.WATER_TEMPLE_RISING_TARGET_LEDGE,
         lambda bundle: can_use(Items.LONGSHOT, bundle) | (can_do_trick(Tricks.WATER_IRON_BOOTS_LEDGE_GRAB, bundle) & is_adult(bundle) & has_item(Items.BRONZE_SCALE, bundle) & can_use(Items.IRON_BOOTS, bundle))),
    ])

    # Water Temple 3F Central Low Or Mid Water  (upstream RR_WATER_TEMPLE_3F_CENTRAL_LM, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_3F_CENTRAL_LM, world, [
        (Regions.WATER_TEMPLE_3F_CENTRAL_A,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_2F_CENTRAL_LM,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_BLOCK_LOOP,
         lambda bundle: can_do_trick(Tricks.WATER_CENTRAL_BOW, bundle) & can_hit_eye_targets(bundle)),
        (Regions.WATER_TEMPLE_BLOCK_LOOP_3F_LM,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle)),
        (Regions.WATER_TEMPLE_PILLAR_H,
         lambda bundle: can_do_trick(Tricks.WATER_IRONS_CENTRAL_GS, bundle) & can_use(Items.DINS_FIRE, bundle) & water_3f_central_to_high_emblem(bundle)),
    ])

    # Water Temple 2F Central High Water  (upstream RR_WATER_TEMPLE_2F_CENTRAL_H, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_2F_CENTRAL_H, world, [
        (Locations.WATER_TEMPLE_MAIN_LEVEL2_POT1,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
        (Locations.WATER_TEMPLE_MAIN_LEVEL2_POT2,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_2F_CENTRAL_H, world, [
        (Regions.WATER_TEMPLE_MAIN,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_JET_CHEST_ROOM,
         lambda bundle: (can_use(Items.HOOKSHOT, bundle) | (can_do_trick(Tricks.WATER_IRON_BOOTS_LEDGE_GRAB, bundle) & has_item(Items.BRONZE_SCALE, bundle) & take_damage(bundle))) & water_timer_at_least(bundle, 48)),
        (Regions.WATER_TEMPLE_3F_CENTRAL_H,
         lambda bundle: can_use(Items.LONGSHOT, bundle) & water_timer_at_least(bundle, 40)),
    ])

    # Water Temple 2F Central Low Or Mid Water  (upstream RR_WATER_TEMPLE_2F_CENTRAL_LM, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_2F_CENTRAL_LM, world, [
        (Locations.WATER_TEMPLE_MAIN_LEVEL2_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.WATER_TEMPLE_MAIN_LEVEL2_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_2F_CENTRAL_LM, world, [
        (Regions.WATER_TEMPLE_MAIN,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_JET_CHEST_ROOM,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
        (Regions.WATER_TEMPLE_OUTSIDE_JET_LIFT_2F,
         lambda bundle: water_level(bundle, WaterLevel.MID) & (is_adult(bundle) | can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | has_item(Items.BRONZE_SCALE, bundle) | bunny_hood(bundle))),
        (Regions.WATER_TEMPLE_PILLAR_2F,
         lambda bundle: has_fire_source_with_torch(bundle) | can_use(Items.FAIRY_BOW, bundle)),
        (Regions.WATER_TEMPLE_PILLAR_H,
         lambda bundle: can_do_trick(Tricks.WATER_IRONS_CENTRAL_GS, bundle) & (has_fire_source_with_torch(bundle) | can_use(Items.FAIRY_BOW, bundle)) & can_use(Items.LONGSHOT, bundle) & water_3f_central_to_high_emblem(bundle)),
        (Regions.WATER_TEMPLE_3F_CENTRAL_LM,
         lambda bundle: can_use(Items.LONGSHOT, bundle)),
        (Regions.WATER_TEMPLE_BLOCK_LOOP,
         lambda bundle: can_hit_eye_targets(bundle) & (can_use(Items.LONGSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | (is_adult(bundle) & bunny_hood(bundle)))),
    ])

    # Water Temple Side Tower 1F  (upstream RR_WATER_TEMPLE_SIDE_TOWER_1F, SCENE_WATER_TEMPLE)
    # Events
    add_events(Regions.WATER_TEMPLE_SIDE_TOWER_1F, world, [
        (EventLocations.WATER_TEMPLE_SIDE_TOWER_1F_WATER_COULD_LOW_FROM_HIGH, Events.WATER_COULD_LOW_FROM_HIGH,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle)),
    ])
    # Locations
    add_locations(Regions.WATER_TEMPLE_SIDE_TOWER_1F, world, [
        (Locations.WATER_TEMPLE_TORCH_POT1,
         lambda bundle: (water_level(bundle, WaterLevel.LOW) & can_break_pots(bundle)) | (can_use(Items.HOOKSHOT, bundle) & can_use(Items.IRON_BOOTS, bundle))),
        (Locations.WATER_TEMPLE_TORCH_POT2,
         lambda bundle: (water_level(bundle, WaterLevel.LOW) & can_break_pots(bundle)) | (can_use(Items.HOOKSHOT, bundle) & can_use(Items.IRON_BOOTS, bundle))),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_SIDE_TOWER_1F, world, [
        (Regions.WATER_TEMPLE_MAIN,
         lambda bundle: water_level(bundle, WaterLevel.LOW) | (can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8))),
        (Regions.WATER_TEMPLE_LOW_EMBLEM,
         lambda bundle: water_level(bundle, WaterLevel.HIGH) & has_item(Items.BRONZE_SCALE, bundle) & water_timer_at_least(bundle, 8)),
        (Regions.WATER_TEMPLE_SIDE_TOWER_2F,
         lambda bundle: water_level(bundle, WaterLevel.MID) & has_item(Items.BRONZE_SCALE, bundle) & water_timer_at_least(bundle, 8)),
        (Regions.WATER_TEMPLE_TORCH_ROOM,
         lambda bundle: water_level(bundle, WaterLevel.LOW) & (has_fire_source_with_torch(bundle) | can_use(Items.FAIRY_BOW, bundle))),
    ])

    # Water Temple Side Tower 2F  (upstream RR_WATER_TEMPLE_SIDE_TOWER_2F, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_SIDE_TOWER_2F, world, [
        (Regions.WATER_TEMPLE_MAIN,
         lambda bundle: (can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8)) | water_level(bundle, WaterLevel.LOW)),
        (Regions.WATER_TEMPLE_CRACKED_WALL,
         lambda bundle: water_level(bundle, WaterLevel.LOW_OR_MID) & has_explosives(bundle)),
    ])

    # Water Temple Low Emblem  (upstream RR_WATER_TEMPLE_LOW_EMBLEM, SCENE_WATER_TEMPLE)
    # Events
    add_events(Regions.WATER_TEMPLE_LOW_EMBLEM, world, [
        (EventLocations.WATER_TEMPLE_LOW_EMBLEM_WATER_LOW, Events.WATER_LOW,
         lambda bundle: can_use(Items.ZELDAS_LULLABY, bundle)),
        (EventLocations.WATER_TEMPLE_LOW_EMBLEM_WATER_COULD_LOW, Events.WATER_COULD_LOW,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_LOW_EMBLEM, world, [
        (Regions.WATER_TEMPLE_MAIN,
         lambda bundle: water_level(bundle, WaterLevel.LOW) | (water_timer_at_least(bundle, 24) & can_use(Items.IRON_BOOTS, bundle))),
        (Regions.WATER_TEMPLE_SIDE_TOWER_2F,
         lambda bundle: water_level(bundle, WaterLevel.LOW_OR_MID) & ((can_use(Items.HOVER_BOOTS, bundle) & can_do_trick(Tricks.WATER_CRACKED_WALL_HOVERS, bundle)) | can_do_trick(Tricks.WATER_CRACKED_WALL, bundle)) | water_level(bundle, WaterLevel.MID) & has_item(Items.BRONZE_SCALE, bundle)),
        (Regions.WATER_TEMPLE_4_SPIKES_ROOM,
         lambda bundle: True_()),
    ])

    # Water Temple 4 Spikes Room  (upstream RR_WATER_TEMPLE_4_SPIKES_ROOM, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_4_SPIKES_ROOM, world, [
        (Locations.WATER_TEMPLE_MAP_CHEST,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.SPIKE, EnemyDistance.CLOSE, True, 4)) & can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_4_SPIKES_ROOM, world, [
        (Regions.WATER_TEMPLE_LOW_EMBLEM,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.SPIKE, EnemyDistance.CLOSE, True, 4))),
    ])

    # Water Temple Cracked Wall  (upstream RR_WATER_TEMPLE_CRACKED_WALL, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_CRACKED_WALL, world, [
        (Locations.WATER_TEMPLE_CRACKED_WALL_CHEST,
         lambda bundle: (water_level(bundle, WaterLevel.LOW_OR_MID) | can_open_underwater_chest(bundle)) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_CRACKED_WALL, world, [
        (Regions.WATER_TEMPLE_SIDE_TOWER_2F,
         lambda bundle: True_()),
    ])

    # Water Temple Torch Room  (upstream RR_WATER_TEMPLE_TORCH_ROOM, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_TORCH_ROOM, world, [
        (Locations.WATER_TEMPLE_TORCHES_CHEST,
         lambda bundle: any_age_time(bundle, lambda bundle: (water_level(bundle, WaterLevel.LOW) & can_kill_enemy(bundle, Enemies.SHELL_BLADE, EnemyDistance.CLOSE, True, 3) & has_open_chest(bundle)) | can_open_underwater_chest(bundle))),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_TORCH_ROOM, world, [
        (Regions.WATER_TEMPLE_SIDE_TOWER_1F,
         lambda bundle: ((water_level(bundle, WaterLevel.LOW) | can_use(Items.IRON_BOOTS, bundle)) & any_age_time(bundle, lambda bundle: (water_level(bundle, WaterLevel.LOW) & can_kill_enemy(bundle, Enemies.SHELL_BLADE, EnemyDistance.CLOSE, True, 3)) | can_use(Items.HOOKSHOT, bundle)))),
    ])

    # Water Temple Spike Moat  (upstream RR_WATER_TEMPLE_SPIKE_MOAT, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_SPIKE_MOAT, world, [
        (Regions.WATER_TEMPLE_MAIN,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle)),
        (Regions.WATER_TEMPLE_BEHIND_SPIKE_MOAT,
         lambda bundle: (can_use(Items.LONGSHOT, bundle) | (can_do_trick(Tricks.WATER_BK_REGION, bundle) & can_use(Items.HOVER_BOOTS, bundle)))),
    ])

    # Water Temple Behind Spike Moat  (upstream RR_WATER_TEMPLE_BEHIND_SPIKE_MOAT, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_BEHIND_SPIKE_MOAT, world, [
        (Regions.WATER_TEMPLE_SPIKE_MOAT,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.LONGSHOT, bundle) | (can_use(Items.HOOKSHOT, bundle) & can_use(Items.IRON_BOOTS, bundle))),
        (Regions.WATER_TEMPLE_BOULDERS_SOUTH,
         lambda bundle: small_keys_scene("SCENE_WATER_TEMPLE", 4, bundle)),
    ])

    # Water Temple Boulders South  (upstream RR_WATER_TEMPLE_BOULDERS_SOUTH, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_BOULDERS_SOUTH, world, [
        (Locations.WATER_TEMPLE_GS_NEAR_BOSS_KEY_CHEST,
         lambda bundle: can_use(Items.LONGSHOT, bundle)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_BOULDERS_SOUTH, world, [
        (Regions.WATER_TEMPLE_BEHIND_SPIKE_MOAT,
         lambda bundle: small_keys_scene("SCENE_WATER_TEMPLE", 4, bundle)),
        (Regions.WATER_TEMPLE_BOULDERS_NORTH,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | (can_do_trick(Tricks.WATER_INVISIBLE_HOOKSHOT_TARGET, bundle) & ((is_adult(bundle)) & can_use(Items.HOOKSHOT, bundle) | (is_child(bundle)) & can_use(Items.LONGSHOT, bundle)) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8))),
        (Regions.WATER_TEMPLE_BOULDER_CANAL,
         lambda bundle: (is_adult(bundle) & (can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle) | can_do_trick(Tricks.WATER_NORTH_BASEMENT_LEDGE_JUMP, bundle))) | (can_middair_ground_jump(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8))),
    ])

    # Water Temple Boulders North  (upstream RR_WATER_TEMPLE_BOULDERS_NORTH, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_BOULDERS_NORTH, world, [
        (Regions.WATER_TEMPLE_BOULDERS_SOUTH,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | (can_do_trick(Tricks.WATER_INVISIBLE_HOOKSHOT_TARGET, bundle) & ((is_adult(bundle)) & can_use(Items.HOOKSHOT, bundle) | (is_child(bundle)) & can_use(Items.LONGSHOT, bundle)) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8))),
        (Regions.WATER_TEMPLE_BLOCK_ROOM_TARGET,
         lambda bundle: True_()),
    ])

    # Water Temple Block Room Target  (upstream RR_WATER_TEMPLE_BLOCK_ROOM_TARGET, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_BLOCK_ROOM_TARGET, world, [
        (Locations.WATER_TEMPLE_BASEMENT_BLOCK_PUZZLE_POT1,
         lambda bundle: can_break_pots(bundle, EnemyDistance.HOOKSHOT, False, True) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8)),
        (Locations.WATER_TEMPLE_BASEMENT_BLOCK_PUZZLE_POT2,
         lambda bundle: can_break_pots(bundle, EnemyDistance.HOOKSHOT, False, True) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_BLOCK_ROOM_TARGET, world, [
        (Regions.WATER_TEMPLE_BOULDERS_NORTH,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_BLOCK_ROOM,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_BLOCK_ROOM_STAIRS,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle)),
    ])

    # Water Temple Block Room  (upstream RR_WATER_TEMPLE_BLOCK_ROOM, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_BLOCK_ROOM, world, [
        (Locations.WATER_TEMPLE_BASEMENT_BLOCK_PUZZLE_POT1,
         lambda bundle: (can_break_pots(bundle, EnemyDistance.LONGSHOT, True, True) & has_item(Items.BRONZE_SCALE, bundle)) | (can_use(Items.IRON_BOOTS, bundle) & can_use(Items.HOOKSHOT, bundle) & water_timer_at_least(bundle, 8))),
        (Locations.WATER_TEMPLE_BASEMENT_BLOCK_PUZZLE_POT2,
         lambda bundle: (can_break_pots(bundle, EnemyDistance.LONGSHOT, True, True) & has_item(Items.BRONZE_SCALE, bundle)) | (can_use(Items.IRON_BOOTS, bundle) & can_use(Items.HOOKSHOT, bundle) & water_timer_at_least(bundle, 8))),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_BLOCK_ROOM, world, [
        (Regions.WATER_TEMPLE_BLOCK_ROOM_TARGET,
         lambda bundle: any_age_time(bundle, lambda bundle: has_item(Items.GORONS_BRACELET, bundle) & has_explosives(bundle)) & has_item(Items.BRONZE_SCALE, bundle)),
        (Regions.WATER_TEMPLE_BLOCK_ROOM_STAIRS,
         lambda bundle: any_age_time(bundle, lambda bundle: has_item(Items.GORONS_BRACELET, bundle) & has_explosives(bundle)) & has_item(Items.BRONZE_SCALE, bundle)),
    ])

    # Water Temple Block Room Stairs  (upstream RR_WATER_TEMPLE_BLOCK_ROOM_STAIRS, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_BLOCK_ROOM_STAIRS, world, [
        (Regions.WATER_TEMPLE_BLOCK_ROOM,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_3_JETS_SWITCH,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_BLOCK_ROOM_TARGET,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle)),
    ])

    # Water Temple 3 Jets Room  (upstream RR_WATER_TEMPLE_3_JETS_SWITCH, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_3_JETS_SWITCH, world, [
        (Regions.WATER_TEMPLE_BLOCK_ROOM_STAIRS,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_3_JETS_NO_SWITCH,
         lambda bundle: True_()),
    ])

    # Water Temple 3 Jets Room No Switch  (upstream RR_WATER_TEMPLE_3_JETS_NO_SWITCH, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_3_JETS_NO_SWITCH, world, [
        (Regions.WATER_TEMPLE_3_JETS_SWITCH,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) | can_recoil_hover(bundle, Recoil.HAMMER_AND_SHIELD)),
        (Regions.WATER_TEMPLE_CANAL_ALCOVE,
         lambda bundle: True_()),
    ])

    # Water Temple Canal Alcove  (upstream RR_WATER_TEMPLE_CANAL_ALCOVE, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_CANAL_ALCOVE, world, [
        (Locations.WATER_TEMPLE_GS_NEAR_BOSS_KEY_CHEST,
         lambda bundle: can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG) | (((is_adult(bundle) & can_use(Items.HOVER_BOOTS, bundle)) | bunny_hovers(bundle) | can_middair_ground_jump(bundle)) & (has_item(Items.BRONZE_SCALE, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle))) & (((has_item(Items.BRONZE_SCALE, bundle) & (is_adult(bundle) | can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle))) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.SHORT_JUMPSLASH) | ((is_adult(bundle)) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOMB_THROW) | (is_child(bundle)) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG)))))),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_CANAL_ALCOVE, world, [
        (Regions.WATER_TEMPLE_3_JETS_NO_SWITCH,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_BOULDER_CANAL,
         lambda bundle: (is_adult(bundle) & (can_jump_slash(bundle) | can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle))) | has_item(Items.BRONZE_SCALE, bundle) | (can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8))),
        (Regions.WATER_TEMPLE_BEHIND_CANAL,
         lambda bundle: is_adult(bundle) & can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & has_item(Items.BRONZE_SCALE, bundle)),
    ])

    # Water Temple Boulder Canal  (upstream RR_WATER_TEMPLE_BOULDER_CANAL, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_BOULDER_CANAL, world, [
        (Locations.WATER_TEMPLE_GS_NEAR_BOSS_KEY_CHEST,
         lambda bundle: (is_adult(bundle) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG)) | (can_use(Items.IRON_BOOTS, bundle) & can_use(Items.HOOKSHOT, bundle))),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_BOULDER_CANAL, world, [
        (Regions.WATER_TEMPLE_BOULDERS_SOUTH,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | (can_do_trick(Tricks.WATER_INVISIBLE_HOOKSHOT_TARGET, bundle) & (((can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8))) & can_use(Items.HOOKSHOT, bundle) | can_use(Items.LONGSHOT, bundle))) | (is_adult(bundle) & (can_jump_slash(bundle) | can_use(Items.HOVER_BOOTS, bundle)))),
        (Regions.WATER_TEMPLE_BOULDERS_NORTH,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | (can_do_trick(Tricks.WATER_INVISIBLE_HOOKSHOT_TARGET, bundle) & ((is_adult(bundle)) & can_use(Items.HOOKSHOT, bundle) | (is_child(bundle)) & can_use(Items.LONGSHOT, bundle)) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8))),
        (Regions.WATER_TEMPLE_CANAL_ALCOVE,
         lambda bundle: is_adult(bundle)),
        (Regions.WATER_TEMPLE_BEHIND_CANAL,
         lambda bundle: can_use(Items.IRON_BOOTS, bundle) & has_item(Items.BRONZE_SCALE, bundle) & water_timer_at_least(bundle, 8)),
    ])

    # Water Temple Behind Canal  (upstream RR_WATER_TEMPLE_BEHIND_CANAL, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_BEHIND_CANAL, world, [
        (Locations.WATER_TEMPLE_GS_NEAR_BOSS_KEY_CHEST,
         lambda bundle: can_use(Items.IRON_BOOTS, bundle) & can_use(Items.HOOKSHOT, bundle) & water_timer_at_least(bundle, 8)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_BEHIND_CANAL, world, [
        (Regions.WATER_TEMPLE_BOULDER_CANAL,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle)),
        (Regions.WATER_TEMPLE_BOSS_KEY_ROOM,
         lambda bundle: small_keys_scene("SCENE_WATER_TEMPLE", 5, bundle)),
    ])

    # Water Temple Boss Key Room  (upstream RR_WATER_TEMPLE_BOSS_KEY_ROOM, SCENE_WATER_TEMPLE)
    # Events
    add_events(Regions.WATER_TEMPLE_BOSS_KEY_ROOM, world, [
        (EventLocations.WATER_TEMPLE_BOSS_KEY_ROOM_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Locations
    add_locations(Regions.WATER_TEMPLE_BOSS_KEY_ROOM, world, [
        (Locations.WATER_TEMPLE_BOSS_KEY_CHEST,
         lambda bundle: can_open_large_chest(bundle)),
        (Locations.WATER_TEMPLE_BOSS_KEY_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.WATER_TEMPLE_BOSS_KEY_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_BOSS_KEY_ROOM, world, [
        (Regions.WATER_TEMPLE_BEHIND_CANAL,
         lambda bundle: small_keys_scene("SCENE_WATER_TEMPLE", 5, bundle)),
    ])

    # Water Temple Near Cage Steps  (upstream RR_WATER_TEMPLE_NEAR_CAGE_STEPS, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_NEAR_CAGE_STEPS, world, [
        (Regions.WATER_TEMPLE_MAIN,
         lambda bundle: can_use(Items.IRON_BOOTS, bundle) & has_item(Items.BRONZE_SCALE, bundle) & water_timer_at_least(bundle, 16)),
        (Regions.WATER_TEMPLE_NEAR_CAGE,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) | (is_adult(bundle) & (can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle))) | can_middair_ground_jump(bundle)),
    ])

    # Water Temple Near Cage  (upstream RR_WATER_TEMPLE_NEAR_CAGE, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_NEAR_CAGE, world, [
        (Regions.WATER_TEMPLE_NEAR_CAGE_STEPS,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_GS_CAGE,
         lambda bundle: can_jump_slash(bundle) | (can_do_trick(Tricks.ITEM_EXTENSION, bundle) & (can_use(Items.FAIRY_BOW, bundle) | can_use(Items.FAIRY_SLINGSHOT, bundle)))),
    ])

    # Water Temple GS Cage  (upstream RR_WATER_TEMPLE_GS_CAGE, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_GS_CAGE, world, [
        (Locations.WATER_TEMPLE_GS_BEHIND_GATE,
         lambda bundle: (is_adult(bundle) & (has_grab(bundle) | can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA))) | can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG) | can_ground_jumpslash(bundle)),
        (Locations.WATER_TEMPLE_BEHIND_GATE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.WATER_TEMPLE_BEHIND_GATE_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.WATER_TEMPLE_BEHIND_GATE_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.WATER_TEMPLE_BEHIND_GATE_POT4,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_GS_CAGE, world, [
        (Regions.WATER_TEMPLE_NEAR_CAGE,
         lambda bundle: can_hit_switch(bundle)),
    ])

    # Water Temple Block U-Bend  (upstream RR_WATER_TEMPLE_BLOCK_U_BEND, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_BLOCK_U_BEND, world, [
        (Regions.WATER_TEMPLE_MAIN,
         lambda bundle: has_item(Events.WATER_PUSHED_1F_BLOCK, bundle) & ((can_use(Items.IRON_BOOTS, bundle) & ((can_use(Items.HOOKSHOT, bundle) & water_level(bundle, WaterLevel.LOW)) | has_item(Items.BRONZE_SCALE, bundle))) | (water_level(bundle, WaterLevel.HIGH_OR_MID) & can_use(Items.SILVER_SCALE, bundle))) & water_timer_at_least(bundle, 8)),
        (Regions.WATER_TEMPLE_OUTSIDE_DRAGON_ROOM,
         lambda bundle: can_hit_switch(bundle) | can_use(Items.HOVER_BOOTS, bundle) | (is_adult(bundle) & bunny_hood(bundle))),
    ])

    # Water Temple Outside Dragon Room  (upstream RR_WATER_TEMPLE_OUTSIDE_DRAGON_ROOM, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_OUTSIDE_DRAGON_ROOM, world, [
        (Regions.WATER_TEMPLE_BLOCK_U_BEND,
         lambda bundle: can_hit_switch(bundle, EnemyDistance.BOOMERANG) | can_use(Items.HOVER_BOOTS, bundle) | can_use(Items.HOOKSHOT, bundle) | (is_adult(bundle) & bunny_hood(bundle))),
        (Regions.WATER_TEMPLE_DRAGON_ROOM,
         lambda bundle: True_()),
    ])

    # Water Temple Dragon Room  (upstream RR_WATER_TEMPLE_DRAGON_ROOM, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_DRAGON_ROOM, world, [
        (Locations.WATER_TEMPLE_DRAGON_CHEST,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) & has_open_chest(bundle) & ((can_use(Items.HOOKSHOT, bundle) & can_use(Items.IRON_BOOTS, bundle)) | (((is_adult(bundle) & can_do_trick(Tricks.WATER_ADULT_DRAGON, bundle)) | (is_child(bundle) & can_do_trick(Tricks.WATER_CHILD_DRAGON, bundle))) & can_hit_switch(bundle, EnemyDistance.BOOMERANG, True) & (has_item(Items.SILVER_SCALE, bundle) | (can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8)))))),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_DRAGON_ROOM, world, [
        (Regions.WATER_TEMPLE_OUTSIDE_DRAGON_ROOM,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_ABOVE_DRAGON,
         lambda bundle: False_()),
    ])

    # Water Temple Pillar 1F  (upstream RR_WATER_TEMPLE_PILLAR_1F, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_PILLAR_1F, world, [
        (Regions.WATER_TEMPLE_MAIN,
         lambda bundle: small_keys_scene("SCENE_WATER_TEMPLE", 5, bundle) & water_level(bundle, WaterLevel.LOW)),
        (Regions.WATER_TEMPLE_PILLAR_2F,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) | (water_level(bundle, WaterLevel.MID) & can_do_trick(Tricks.WATER_FW_CENTRAL_GS, bundle) & can_use(Items.FARORES_WIND, bundle) & has_item(Items.BRONZE_SCALE, bundle))),
        (Regions.WATER_TEMPLE_PILLAR_B1,
         lambda bundle: water_level(bundle, WaterLevel.MID) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 40)),
        (Regions.WATER_TEMPLE_PILLAR_H,
         lambda bundle: can_do_trick(Tricks.WATER_FW_CENTRAL_GS, bundle) & can_use(Items.FARORES_WIND, bundle) & (can_use(Items.IRON_BOOTS, bundle) | has_item(Items.BRONZE_SCALE, bundle))),
    ])

    # Water Temple Pillar 2F  (upstream RR_WATER_TEMPLE_PILLAR_2F, SCENE_WATER_TEMPLE)
    # Events
    add_events(Regions.WATER_TEMPLE_PILLAR_2F, world, [
        (EventLocations.WATER_TEMPLE_PILLAR_2F_WATER_MIDDLE, Events.WATER_MIDDLE,
         lambda bundle: can_use(Items.ZELDAS_LULLABY, bundle)),
        (EventLocations.WATER_TEMPLE_PILLAR_2F_WATER_COULD_MIDDLE, Events.WATER_COULD_MIDDLE,
         lambda bundle: True_()),
    ])
    # Locations
    add_locations(Regions.WATER_TEMPLE_PILLAR_2F, world, [
        (Locations.WATER_TEMPLE_GS_CENTRAL_PILLAR,
         lambda bundle: can_use(Items.LONGSHOT, bundle)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_PILLAR_2F, world, [
        (Regions.WATER_TEMPLE_2F_CENTRAL_LM,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_PILLAR_1F,
         lambda bundle: water_level(bundle, WaterLevel.LOW) | can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8)),
        (Regions.WATER_TEMPLE_PILLAR_H,
         lambda bundle: can_do_trick(Tricks.WATER_FW_CENTRAL_GS, bundle) & can_use(Items.FARORES_WIND, bundle) & (can_use(Items.IRON_BOOTS, bundle) | has_item(Items.BRONZE_SCALE, bundle))),
    ])

    # Water Temple Pillar High Water  (upstream RR_WATER_TEMPLE_PILLAR_H, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_PILLAR_H, world, [
        (Locations.WATER_TEMPLE_GS_CENTRAL_PILLAR,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_PILLAR_H, world, [
        (Regions.WATER_TEMPLE_MAIN,
         lambda bundle: can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8)),
        (Regions.WATER_TEMPLE_2F_CENTRAL_LM,
         lambda bundle: can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8)),
        (Regions.WATER_TEMPLE_PILLAR_B1,
         lambda bundle: can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 40)),
    ])

    # Water Temple Pillar B1  (upstream RR_WATER_TEMPLE_PILLAR_B1, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_PILLAR_B1, world, [
        (Locations.WATER_TEMPLE_CENTRAL_PILLAR_CHEST,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) & has_item(Items.BRONZE_SCALE, bundle) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_PILLAR_B1, world, [
        (Regions.WATER_TEMPLE_MAIN,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle)),
    ])

    # Water Temple Jet Chest Room  (upstream RR_WATER_TEMPLE_JET_CHEST_ROOM, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_JET_CHEST_ROOM, world, [
        (Locations.WATER_TEMPLE_COMPASS_CHEST,
         lambda bundle: can_use_projectile(bundle) & can_open_large_chest(bundle)),
        (Locations.WATER_TEMPLE_NEAR_COMPASS_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.WATER_TEMPLE_NEAR_COMPASS_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.WATER_TEMPLE_NEAR_COMPASS_POT3,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_JET_CHEST_ROOM, world, [
        (Regions.WATER_TEMPLE_MAIN,
         lambda bundle: (can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8)) | water_level(bundle, WaterLevel.LOW_OR_MID)),
    ])

    # Water Temple Outside Jet Lift 2F  (upstream RR_WATER_TEMPLE_OUTSIDE_JET_LIFT_2F, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_OUTSIDE_JET_LIFT_2F, world, [
        (Regions.WATER_TEMPLE_MAIN,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle)),
        (Regions.WATER_TEMPLE_2F_CENTRAL_LM,
         lambda bundle: water_level(bundle, WaterLevel.MID) & (is_adult(bundle) | has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle))),
        (Regions.WATER_TEMPLE_JET_LIFT_2F,
         lambda bundle: water_level(bundle, WaterLevel.MID)),
    ])

    # Water Temple Jet Lift 2F  (upstream RR_WATER_TEMPLE_JET_LIFT_2F, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_JET_LIFT_2F, world, [
        (Regions.WATER_TEMPLE_OUTSIDE_JET_LIFT_2F,
         lambda bundle: water_level(bundle, WaterLevel.LOW_OR_MID) | can_use(Items.IRON_BOOTS, bundle)),
        (Regions.WATER_TEMPLE_JET_LIFT_3F,
         lambda bundle: can_hit_switch(bundle, EnemyDistance.BOMB_THROW)),
    ])

    # Water Temple Jet Lift 3F  (upstream RR_WATER_TEMPLE_JET_LIFT_3F, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_JET_LIFT_3F, world, [
        (Regions.WATER_TEMPLE_JET_LIFT_2F,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_HIGH_EMBLEM,
         lambda bundle: True_()),
    ])

    # Water Temple High Emblem  (upstream RR_WATER_TEMPLE_HIGH_EMBLEM, SCENE_WATER_TEMPLE)
    # Events
    add_events(Regions.WATER_TEMPLE_HIGH_EMBLEM, world, [
        (EventLocations.WATER_TEMPLE_HIGH_EMBLEM_WATER_HIGH, Events.WATER_HIGH,
         lambda bundle: True_()),
        (EventLocations.WATER_TEMPLE_HIGH_EMBLEM_WATER_SCARECROW, Events.WATER_SCARECROW,
         lambda bundle: scarecrows_song(bundle)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_HIGH_EMBLEM, world, [
        (Regions.WATER_TEMPLE_MAIN,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_3F_CENTRAL_A,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_3F_CENTRAL_H,
         lambda bundle: water_level(bundle, WaterLevel.HIGH)),
    ])

    # Water Temple Block Loop  (upstream RR_WATER_TEMPLE_BLOCK_LOOP, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_BLOCK_LOOP, world, [
        (Regions.WATER_TEMPLE_BLOCK_LOOP_BACK,
         lambda bundle: has_item(Items.GORONS_BRACELET, bundle) & water_level(bundle, WaterLevel.LOW_OR_MID)),
        (Regions.WATER_TEMPLE_BLOCK_LOOP_3F_LM,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
    ])

    # Water Temple Block Loop Back  (upstream RR_WATER_TEMPLE_BLOCK_LOOP_BACK, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_BLOCK_LOOP_BACK, world, [
        (Locations.WATER_TEMPLE_CENTRAL_BOW_TARGET_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.WATER_TEMPLE_CENTRAL_BOW_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.WATER_TEMPLE_CENTRAL_BOW_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])

    # Water Temple Block Loop 3F Any Water  (upstream RR_WATER_TEMPLE_BLOCK_LOOP_3F_A, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_BLOCK_LOOP_3F_A, world, [
        (Locations.WATER_TEMPLE_MAIN_LEVEL2_POT1,
         lambda bundle: can_use(Items.BOMBCHUS_5, bundle) & (has_item(Items.GOLDEN_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle))),
        (Locations.WATER_TEMPLE_MAIN_LEVEL2_POT2,
         lambda bundle: can_use(Items.BOMBCHUS_5, bundle) & (has_item(Items.GOLDEN_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle))),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_BLOCK_LOOP_3F_A, world, [
        (Regions.WATER_TEMPLE_MAIN,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_3F_CENTRAL_A,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | (is_adult(bundle) & bunny_hood(bundle))),
    ])

    # Water Temple Block Loop 3F High Water  (upstream RR_WATER_TEMPLE_BLOCK_LOOP_3F_H, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_BLOCK_LOOP_3F_H, world, [
        (Regions.WATER_TEMPLE_BLOCK_LOOP_3F_A,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_3F_CENTRAL_H,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | (is_adult(bundle) & bunny_hood(bundle))),
    ])

    # Water Temple Block Loop 3F Low or Mid Water  (upstream RR_WATER_TEMPLE_BLOCK_LOOP_3F_LM, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_BLOCK_LOOP_3F_LM, world, [
        (Regions.WATER_TEMPLE_BLOCK_LOOP_3F_A,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_3F_CENTRAL_LM,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | (is_adult(bundle) & bunny_hood(bundle))),
        (Regions.WATER_TEMPLE_2F_CENTRAL_LM,
         lambda bundle: True_()),
    ])

    # Water Temple Outside Waterfall  (upstream RR_WATER_TEMPLE_OUTSIDE_WATERFALL, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_OUTSIDE_WATERFALL, world, [
        (Regions.WATER_TEMPLE_MAIN,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_OUTSIDE_JET_LIFT_2F,
         lambda bundle: water_level(bundle, WaterLevel.MID)),
        (Regions.WATER_TEMPLE_WATERFALL,
         lambda bundle: water_level(bundle, WaterLevel.HIGH) & small_keys_scene("SCENE_WATER_TEMPLE", 4, bundle)),
        (Regions.WATER_TEMPLE_3F_CENTRAL_H,
         lambda bundle: water_level(bundle, WaterLevel.HIGH) & (is_adult(bundle) | can_use(Items.HOVER_BOOTS, bundle) | can_use(Items.HOOKSHOT, bundle) | has_item(Items.BRONZE_SCALE, bundle) | bunny_hood(bundle))),
        (Regions.WATER_TEMPLE_2F_CENTRAL_H,
         lambda bundle: water_level(bundle, WaterLevel.HIGH) & can_use(Items.HOOKSHOT, bundle) & can_use(Items.IRON_BOOTS, bundle)),
    ])

    # Water Temple Waterfall  (upstream RR_WATER_TEMPLE_WATERFALL, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_WATERFALL, world, [
        (Locations.WATER_TEMPLE_GS_FALLING_PLATFORM_ROOM,
         lambda bundle: can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.LONGSHOT) | (can_do_trick(Tricks.WATER_RANG_FALLING_PLATFORM_GS, bundle) & can_use(Items.BOOMERANG, bundle)) | (can_do_trick(Tricks.WATER_HOOKSHOT_FALLING_PLATFORM_GS, bundle) & is_adult(bundle) & can_use(Items.HOOKSHOT, bundle))),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_WATERFALL, world, [
        (Regions.WATER_TEMPLE_OUTSIDE_WATERFALL,
         lambda bundle: small_keys_scene("SCENE_WATER_TEMPLE", 4, bundle)),
        (Regions.WATER_TEMPLE_WATERFALL_TOP,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
    ])

    # Water Temple Waterfall Top  (upstream RR_WATER_TEMPLE_WATERFALL_TOP, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_WATERFALL_TOP, world, [
        (Regions.WATER_TEMPLE_WATERFALL,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
        (Regions.WATER_TEMPLE_TOGGLE_SWITCH,
         lambda bundle: small_keys_scene("SCENE_WATER_TEMPLE", 5, bundle)),
    ])

    # Water Temple Toggle Switch  (upstream RR_WATER_TEMPLE_TOGGLE_SWITCH, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_TOGGLE_SWITCH, world, [
        (Regions.WATER_TEMPLE_WATERFALL_TOP,
         lambda bundle: small_keys_scene("SCENE_WATER_TEMPLE", 5, bundle)),
        (Regions.WATER_TEMPLE_LIKE_LIKE_SPIKES,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
    ])

    # Water Temple Like Like Spikes  (upstream RR_WATER_TEMPLE_LIKE_LIKE_SPIKES, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_LIKE_LIKE_SPIKES, world, [
        (Locations.WATER_TEMPLE_LIKE_LIKE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.WATER_TEMPLE_LIKE_LIKE_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_LIKE_LIKE_SPIKES, world, [
        (Regions.WATER_TEMPLE_TOGGLE_SWITCH,
         lambda bundle: (has_item(Items.BRONZE_SCALE, bundle) & can_hit_switch(bundle, EnemyDistance.BOMB_THROW)) | can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle)),
        (Regions.WATER_TEMPLE_DARK_LINK_ROOM,
         lambda bundle: True_()),
    ])

    # Water Temple Dark Link Room  (upstream RR_WATER_TEMPLE_DARK_LINK_ROOM, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_DARK_LINK_ROOM, world, [
        (Regions.WATER_TEMPLE_LIKE_LIKE_SPIKES,
         lambda bundle: can_kill_enemy(bundle, Enemies.DARK_LINK)),
        (Regions.WATER_TEMPLE_SOT_PIT_ROOM,
         lambda bundle: can_kill_enemy(bundle, Enemies.DARK_LINK)),
    ])

    # Water Temple Song Of Time Pit Room  (upstream RR_WATER_TEMPLE_SOT_PIT_ROOM, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_SOT_PIT_ROOM, world, [
        (Locations.WATER_TEMPLE_LONGSHOT_CHEST,
         lambda bundle: can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_SOT_PIT_ROOM, world, [
        (Regions.WATER_TEMPLE_DARK_LINK_ROOM,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_RIVER,
         lambda bundle: is_child(bundle) | can_use(Items.SONG_OF_TIME, bundle)),
    ])

    # Water Temple River  (upstream RR_WATER_TEMPLE_RIVER, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_RIVER, world, [
        (Locations.WATER_TEMPLE_GS_RIVER,
         lambda bundle: (can_use(Items.IRON_BOOTS, bundle) & can_use(Items.HOOKSHOT, bundle) & water_timer_at_least(bundle, 8))),
        (Locations.WATER_TEMPLE_RIVER_HEART1,
         lambda bundle: (can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8)) | has_item(Items.BRONZE_SCALE, bundle)),
        (Locations.WATER_TEMPLE_RIVER_HEART2,
         lambda bundle: (can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8)) | has_item(Items.BRONZE_SCALE, bundle)),
        (Locations.WATER_TEMPLE_RIVER_HEART3,
         lambda bundle: (can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8)) | has_item(Items.BRONZE_SCALE, bundle)),
        (Locations.WATER_TEMPLE_RIVER_HEART4,
         lambda bundle: (can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8)) | has_item(Items.BRONZE_SCALE, bundle)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_RIVER, world, [
        (Regions.WATER_TEMPLE_RIVER_PLATFORM,
         lambda bundle: (can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16) & ((((bunny_hood(bundle)) & can_use(Items.HOOKSHOT, bundle) | can_use(Items.LONGSHOT, bundle))) | (is_adult(bundle) & bunny_hood(bundle)))) | has_item(Items.BRONZE_SCALE, bundle)),
    ])

    # Water Temple River Platform  (upstream RR_WATER_TEMPLE_RIVER_PLATFORM, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_RIVER_PLATFORM, world, [
        (Locations.WATER_TEMPLE_GS_RIVER,
         lambda bundle: can_do_trick(Tricks.WATER_RIVER_GS, bundle) & is_adult(bundle) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.FAR) & can_use(Items.LONGSHOT, bundle)),
        (Locations.WATER_TEMPLE_RIVER_POT1,
         lambda bundle: can_use(Items.BOOMERANG, bundle)),
        (Locations.WATER_TEMPLE_RIVER_POT2,
         lambda bundle: can_use(Items.BOOMERANG, bundle)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_RIVER_PLATFORM, world, [
        (Regions.WATER_TEMPLE_ABOVE_DRAGON,
         lambda bundle: can_hit_eye_targets(bundle) & (is_adult(bundle) | can_use(Items.HOVER_BOOTS, bundle) | can_use(Items.HOOKSHOT, bundle) | bunny_hood(bundle))),
        (Regions.WATER_TEMPLE_RIVER_POTS,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | (is_adult(bundle) & (can_use(Items.IRON_BOOTS, bundle) | can_recoil_hover(bundle, Recoil.SWORD_AND_SHIELD)))),
        (Regions.WATER_TEMPLE_RIVER,
         lambda bundle: can_use(Items.IRON_BOOTS, bundle) & has_item(Items.BRONZE_SCALE, bundle)),
    ])

    # Water Temple River Pots  (upstream RR_WATER_TEMPLE_RIVER_POTS, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_RIVER_POTS, world, [
        (Locations.WATER_TEMPLE_RIVER_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.WATER_TEMPLE_RIVER_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_RIVER_POTS, world, [
        (Regions.WATER_TEMPLE_RIVER_PLATFORM,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | (is_adult(bundle) & (can_use(Items.IRON_BOOTS, bundle) | can_recoil_hover(bundle, Recoil.SWORD_AND_SHIELD) | bunny_hovers(bundle)))),
        (Regions.WATER_TEMPLE_RIVER,
         lambda bundle: can_use(Items.IRON_BOOTS, bundle) & has_item(Items.BRONZE_SCALE, bundle)),
    ])

    # Water Temple Above Dragon  (upstream RR_WATER_TEMPLE_ABOVE_DRAGON, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_ABOVE_DRAGON, world, [
        (Locations.WATER_TEMPLE_RIVER_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.WATER_TEMPLE_DRAGON_CHEST,
         lambda bundle: is_adult(bundle) & can_hit_switch(bundle, EnemyDistance.LONGSHOT) & has_item(Items.BRONZE_SCALE, bundle) & has_open_chest(bundle) & ((can_do_trick(Tricks.WATER_ADULT_DRAGON, bundle) & (has_item(Items.SILVER_SCALE, bundle) | (can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 8)))) | can_do_trick(Tricks.WATER_DRAGON_JUMP_DIVE, bundle))),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_ABOVE_DRAGON, world, [
        (Regions.WATER_TEMPLE_DRAGON_ROOM,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.LONGSHOT, bundle) | (can_use(Items.HOVER_BOOTS, bundle) & (can_jump_slash(bundle) | bunny_hood(bundle)))),
    ])

    # Water Temple Rising Target Ledge  (upstream RR_WATER_TEMPLE_RISING_TARGET_LEDGE, SCENE_WATER_TEMPLE)
    # Events
    add_events(Regions.WATER_TEMPLE_RISING_TARGET_LEDGE, world, [
        (EventLocations.WATER_TEMPLE_RISING_TARGET_LEDGE_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: can_break_pots(bundle)),
        (EventLocations.WATER_TEMPLE_RISING_TARGET_LEDGE_WATER_COULD_MIDDLE, Events.WATER_COULD_MIDDLE,
         lambda bundle: (water_rising_target_to_3f_central(bundle) | bunny_hovers(bundle) | can_recoil_hover(bundle, Recoil.SWORD_AND_SHIELD) | can_use(Items.LONGSHOT, bundle)) & (has_fire_source_with_torch(bundle) | can_use(Items.FAIRY_BOW, bundle))),
        (EventLocations.WATER_TEMPLE_RISING_TARGET_LEDGE_WATER_COULD_HIGH_FROM_MID, Events.WATER_COULD_HIGH_FROM_MID,
         lambda bundle: (bunny_hovers(bundle) | can_recoil_hover(bundle, Recoil.SWORD_AND_SHIELD) | can_use(Items.LONGSHOT, bundle)) & can_hit_switch(bundle, EnemyDistance.BOMB_THROW)),
        (EventLocations.WATER_TEMPLE_RISING_TARGET_LEDGE_WATER_COULD_LOW, Events.WATER_COULD_LOW,
         lambda bundle: can_use(Items.IRON_BOOTS, bundle) & has_item(Items.BRONZE_SCALE, bundle)),
    ])
    # Locations
    add_locations(Regions.WATER_TEMPLE_RISING_TARGET_LEDGE, world, [
        (Locations.WATER_TEMPLE_MAIN_LEVEL1_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.WATER_TEMPLE_MAIN_LEVEL1_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_RISING_TARGET_LEDGE, world, [
        (Regions.WATER_TEMPLE_MAIN,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | (can_use(Items.IRON_BOOTS, bundle) & take_damage(bundle))),
        (Regions.WATER_TEMPLE_3F_CENTRAL_A,
         lambda bundle: water_rising_target_to_3f_central(bundle)),
        (Regions.WATER_TEMPLE_3F_CENTRAL_H,
         lambda bundle: water_rising_target_to_3f_central(bundle) & water_level(bundle, WaterLevel.HIGH)),
        (Regions.WATER_TEMPLE_3F_CENTRAL_LM,
         lambda bundle: water_rising_target_to_3f_central(bundle) & water_level(bundle, WaterLevel.LOW_OR_MID)),
        (Regions.WATER_TEMPLE_2F_CENTRAL_LM,
         lambda bundle: (bunny_hovers(bundle) | can_recoil_hover(bundle, Recoil.SWORD_AND_SHIELD)) & water_level(bundle, WaterLevel.LOW_OR_MID)),
        (Regions.WATER_TEMPLE_PILLAR_H,
         lambda bundle: water_level(bundle, WaterLevel.LOW_OR_MID) & can_do_trick(Tricks.WATER_IRONS_CENTRAL_GS, bundle) & can_use(Items.FIRE_ARROW, bundle) & water_rising_target_to_3f_central(bundle)),
        (Regions.WATER_TEMPLE_TRAPPED_SLOPE,
         lambda bundle: True_()),
    ])

    # Water Temple Trapped Slope  (upstream RR_WATER_TEMPLE_TRAPPED_SLOPE, SCENE_WATER_TEMPLE)
    # Locations
    add_locations(Regions.WATER_TEMPLE_TRAPPED_SLOPE, world, [
        # DEFERRED RC_WATER_BOSS_KEY_HINT: true
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_TRAPPED_SLOPE, world, [
        (Regions.WATER_TEMPLE_RISING_TARGET_LEDGE,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_BOSS_ENTRYWAY,
         lambda bundle: True_()),
    ])

    # Water Temple Boss Entryway  (upstream RR_WATER_TEMPLE_BOSS_ENTRYWAY, SCENE_WATER_TEMPLE)
    # Connections
    connect_regions(Regions.WATER_TEMPLE_BOSS_ENTRYWAY, world, [
        (Regions.WATER_TEMPLE_TRAPPED_SLOPE,
         lambda bundle: True_()),
        (Regions.WATER_TEMPLE_BOSS_ROOM,
         lambda bundle: has_item(Items.WATER_TEMPLE_BOSS_KEY, bundle)),
    ])

    # Water Temple Boss Room  (upstream RR_WATER_TEMPLE_BOSS_ROOM, SCENE_WATER_TEMPLE_BOSS)
    # Events
    add_events(Regions.WATER_TEMPLE_BOSS_ROOM, world, [
        (EventLocations.WATER_TEMPLE_BOSS_ROOM_WATER_TEMPLE_CLEAR, Events.WATER_TEMPLE_COMPLETED,
         lambda bundle: can_kill_enemy(bundle, Enemies.MORPHA)),
    ])
    # Locations
    add_locations(Regions.WATER_TEMPLE_BOSS_ROOM, world, [
        (Locations.WATER_TEMPLE_MORPHA_HEART_CONTAINER,
         lambda bundle: has_item(Events.WATER_TEMPLE_COMPLETED, bundle)),
        (Locations.MORPHA,
         lambda bundle: has_item(Events.WATER_TEMPLE_COMPLETED, bundle)),
    ])
    # Connections
    connect_regions(Regions.WATER_TEMPLE_BOSS_ROOM, world, [
        (Regions.WATER_TEMPLE_BOSS_ENTRYWAY,
         lambda bundle: False_()),
        (Regions.LAKE_HYLIA,
         lambda bundle: has_item(Events.WATER_TEMPLE_COMPLETED, bundle)),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_FAIRIES', 'WATER_COULD_HIGH_FROM_MID', 'WATER_COULD_LOW', 'WATER_COULD_LOW_FROM_HIGH', 'WATER_COULD_MIDDLE', 'WATER_HIGH', 'WATER_LOW', 'WATER_MIDDLE', 'WATER_PUSHED_1F_BLOCK', 'WATER_SCARECROW', 'WATER_TEMPLE_COMPLETED']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (1): ['RC_WATER_BOSS_KEY_HINT']
