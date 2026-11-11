"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/zoras_river.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    ZR_FRONT_CHILD_CAN_PASS_TIME = "ZR Front Child Can Pass Time"
    ZR_FRONT_ADULT_CAN_PASS_TIME = "ZR Front Adult Can Pass Time"
    ZORAS_RIVER_CHILD_CAN_PASS_TIME = "Zora River Child Can Pass Time"
    ZORAS_RIVER_ADULT_CAN_PASS_TIME = "Zora River Adult Can Pass Time"
    ZORAS_RIVER_PLANT_ZORAS_RIVER_BEAN = "Zora River Plant Zoras River Bean"
    ZORAS_RIVER_FAIRY_ACCESS = "Zora River Fairy Access"
    ZR_ATOP_LADDER_CHILD_CAN_PASS_TIME = "ZR Atop Ladder Child Can Pass Time"
    ZR_ATOP_LADDER_ADULT_CAN_PASS_TIME = "ZR Atop Ladder Adult Can Pass Time"
    ZR_ATOP_LADDER_FAIRY_ACCESS = "ZR Atop Ladder Fairy Access"
    ZR_PILLAR_CHILD_CAN_PASS_TIME = "ZR Pillar Child Can Pass Time"
    ZR_PILLAR_ADULT_CAN_PASS_TIME = "ZR Pillar Adult Can Pass Time"
    ZR_PILLAR_BUG_ACCESS = "ZR Pillar Bug Access"
    ZR_FROM_SHORTCUT_CHILD_CAN_PASS_TIME = "ZR From Shortcut Child Can Pass Time"
    ZR_FROM_SHORTCUT_ADULT_CAN_PASS_TIME = "ZR From Shortcut Adult Can Pass Time"
    ZR_BEHIND_WATERFALL_CHILD_CAN_PASS_TIME = "ZR Behind Waterfall Child Can Pass Time"
    ZR_BEHIND_WATERFALL_ADULT_CAN_PASS_TIME = "ZR Behind Waterfall Adult Can Pass Time"
    ZR_FAIRY_GROTTO_FAIRY_ACCESS = "ZR Fairy Grotto Fairy Access"


def set_region_rules(world: "SohWorld") -> None:

    # ZR Front  (upstream RR_ZR_FRONT, SCENE_ZORAS_RIVER)
    # Events
    add_events(Regions.ZR_FRONT, world, [
        (EventLocations.ZR_FRONT_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.ZR_FRONT_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
    ])
    # Locations
    add_locations(Regions.ZR_FRONT, world, [
        (Locations.ZR_GS_TREE,
         lambda bundle: is_child(bundle) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.CLOSE) & can_bonk_trees(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS4,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS5,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS6,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS7,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS8,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS9,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS10,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS11,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS12,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_BOULDER_1,
         lambda bundle: is_child(bundle) & blast_or_smash(bundle)),
        (Locations.ZR_BOULDER_2,
         lambda bundle: is_child(bundle) & blast_or_smash(bundle)),
        (Locations.ZR_BOULDER_3,
         lambda bundle: is_child(bundle) & blast_or_smash(bundle)),
        (Locations.ZR_BOULDER_4,
         lambda bundle: is_child(bundle) & blast_or_smash(bundle)),
        (Locations.ZR_TREE,
         lambda bundle: is_child(bundle) & can_bonk_trees(bundle)),
        (Locations.ZR_WONDER_LOWER_RIVER_1,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_LOWER_RIVER_2,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_LOWER_RIVER_3,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_LOWER_RIVER_4,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
    ])
    # Connections
    connect_regions(Regions.ZR_FRONT, world, [
        (Regions.ZORAS_RIVER,
         lambda bundle: is_adult(bundle) | blast_or_smash(bundle) | can_use(Items.HOVER_BOOTS, bundle)),
        (Regions.HYRULE_FIELD,
         lambda bundle: True_()),
    ])

    # Zora River  (upstream RR_ZORAS_RIVER, SCENE_ZORAS_RIVER)
    # Events
    add_events(Regions.ZORAS_RIVER, world, [
        (EventLocations.ZORAS_RIVER_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.ZORAS_RIVER_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
        (EventLocations.ZORAS_RIVER_PLANT_ZORAS_RIVER_BEAN, Events.PLANT_ZORAS_RIVER_BEAN,
         lambda bundle: can_plant_bean(bundle, Items.ZORAS_RIVER_BEAN_SOUL)),
        (EventLocations.ZORAS_RIVER_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy(bundle) | (is_child(bundle) & can_use(Items.STICKS, bundle)) | (is_child(bundle) & bean_planted(bundle, Events.PLANT_ZORAS_RIVER_BEAN) & can_use(Items.SONG_OF_STORMS, bundle))),
    ])
    # Locations
    add_locations(Regions.ZORAS_RIVER, world, [
        (Locations.ZR_MAGIC_BEAN_SALESMAN,
         lambda bundle: is_child(bundle) & has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.ZR_MAGIC_BEAN_SALESMAN, bundle)),
        (Locations.ZR_FROGS_OCARINA_GAME,
         lambda bundle: is_child(bundle) & can_use(Items.ZELDAS_LULLABY, bundle) & can_use(Items.SARIAS_SONG, bundle) & can_use(Items.SUNS_SONG, bundle) & can_use(Items.EPONAS_SONG, bundle) & can_use(Items.SONG_OF_TIME, bundle) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.ZR_FROGS_IN_THE_RAIN,
         lambda bundle: is_child(bundle) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.ZR_FROGS_ZELDAS_LULLABY,
         lambda bundle: is_child(bundle) & can_use(Items.ZELDAS_LULLABY, bundle)),
        (Locations.ZR_FROGS_EPONAS_SONG,
         lambda bundle: is_child(bundle) & can_use(Items.EPONAS_SONG, bundle)),
        (Locations.ZR_FROGS_SARIAS_SONG,
         lambda bundle: is_child(bundle) & can_use(Items.SARIAS_SONG, bundle)),
        (Locations.ZR_FROGS_SUNS_SONG,
         lambda bundle: is_child(bundle) & can_use(Items.SUNS_SONG, bundle)),
        (Locations.ZR_FROGS_SONG_OF_TIME,
         lambda bundle: is_child(bundle) & can_use(Items.SONG_OF_TIME, bundle)),
        (Locations.ZR_NEAR_OPEN_GROTTO_FREESTANDING_POH,
         lambda bundle: can_use(Items.BOOMERANG, bundle)),
        (Locations.ZR_NEAR_DOMAIN_FREESTANDING_POH,
         lambda bundle: (is_child(bundle) & has_grab(bundle)) | can_use(Items.BOOMERANG, bundle) | can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle) | (is_adult(bundle) & can_do_trick(Tricks.ZR_UPPER, bundle))),
        (Locations.ZR_GS_LADDER,
         lambda bundle: is_child(bundle) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.SHORT_JUMPSLASH) & can_get_nighttime_gs(bundle)),
        (Locations.ZR_GS_NEAR_RAISED_GROTTOS,
         lambda bundle: is_adult(bundle) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.LONGSHOT) & can_get_nighttime_gs(bundle)),
        (Locations.ZR_GS_ABOVE_BRIDGE,
         lambda bundle: is_adult(bundle) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.HOOKSHOT) & can_get_nighttime_gs(bundle)),
        (Locations.ZR_BEAN_SPROUT_FAIRY1,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_ZORAS_RIVER_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.ZR_BEAN_SPROUT_FAIRY2,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_ZORAS_RIVER_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.ZR_BEAN_SPROUT_FAIRY3,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_ZORAS_RIVER_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.ZR_NEAR_DOMAIN_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.ZR_NEAR_DOMAIN_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.ZR_BENEATH_DOMAIN_RED_LEFT_RUPEE,
         lambda bundle: is_adult(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_BENEATH_DOMAIN_RED_MIDDLE_LEFT_RUPEE,
         lambda bundle: is_adult(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_BENEATH_DOMAIN_RED_MIDDLE_RIGHT_RUPEE,
         lambda bundle: is_adult(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_BENEATH_DOMAIN_RED_RIGHT_RUPEE,
         lambda bundle: is_adult(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_CIRCLE_ROCK_1,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.ZR_CIRCLE_ROCK_2,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.ZR_CIRCLE_ROCK_3,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.ZR_CIRCLE_ROCK_4,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.ZR_CIRCLE_ROCK_5,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.ZR_CIRCLE_ROCK_6,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.ZR_CIRCLE_ROCK_7,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.ZR_CIRCLE_ROCK_8,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.ZR_ROCK,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.ZR_UNDERWATER_ROCK_1,
         lambda bundle: (can_use(Items.BOMBCHUS_5, bundle) | (can_use(Items.BOMB_BAG, bundle) & can_do_trick(Tricks.BOMB_DETONATION, bundle)) | (is_adult(bundle) & has_grab(bundle))) & (is_adult(bundle) | has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.BOOMERANG, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_UNDERWATER_ROCK_2,
         lambda bundle: (can_use(Items.BOMBCHUS_5, bundle) | (can_use(Items.BOMB_BAG, bundle) & can_do_trick(Tricks.BOMB_DETONATION, bundle)) | (is_adult(bundle) & has_grab(bundle))) & (is_adult(bundle) | has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.BOOMERANG, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_UNDERWATER_ROCK_3,
         lambda bundle: (can_use(Items.BOMBCHUS_5, bundle) | (can_use(Items.BOMB_BAG, bundle) & can_do_trick(Tricks.BOMB_DETONATION, bundle)) | (is_adult(bundle) & has_grab(bundle))) & (is_adult(bundle) | has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.BOOMERANG, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_UNDERWATER_ROCK_4,
         lambda bundle: (can_use(Items.BOMBCHUS_5, bundle) | (can_use(Items.BOMB_BAG, bundle) & can_do_trick(Tricks.BOMB_DETONATION, bundle)) | (is_adult(bundle) & has_grab(bundle))) & (is_adult(bundle) | has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.BOOMERANG, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_NEAR_FREESTANDING_POH_GRASS,
         lambda bundle: can_use(Items.BOOMERANG, bundle)),
        (Locations.ZR_NEAR_ROCK_CIRCLE_BUTTERFLY_FAIRY,
         lambda bundle: is_child(bundle) & can_use(Items.STICKS, bundle)),
        (Locations.ZR_WATERFALL_BUTTERFLY_FAIRY,
         lambda bundle: is_child(bundle) & can_use(Items.STICKS, bundle)),
        (Locations.ZR_SLEEPLESS_WATERFALL_PLAQUE,
         lambda bundle: can_read(bundle)),
        (Locations.ZR_WONDER_NEAR_DOMAIN_1,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_NEAR_DOMAIN_2,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_NEAR_DOMAIN_3,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_NEAR_DOMAIN_4,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_BEFORE_LADDER_1,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_BEFORE_LADDER_2,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_BEFORE_LADDER_3,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_BEFORE_LADDER_4,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_BEFORE_LADDER_5,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_BEFORE_LADDER_6,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_AFTER_LADDER_1,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_AFTER_LADDER_2,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_AFTER_LADDER_3,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_FROG_BRIDGE_1,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_FROG_BRIDGE_2,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_FROG_BRIDGE_3,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_PILLARS_1,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_PILLARS_2,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_PILLARS_3,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_PILLARS_4,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_LOWER_LAND_BRIDGE_1,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_LOWER_LAND_BRIDGE_2,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_LOWER_LAND_BRIDGE_3,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_LOWER_LAND_BRIDGE_4,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_NEAR_CUCCO_1,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_NEAR_CUCCO_2,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.ZR_WONDER_NEAR_CUCCO_3,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        # DEFERRED RC_ZR_NEAR_DOMAIN_GOSSIP_STONE: true
    ])
    # Connections
    connect_regions(Regions.ZORAS_RIVER, world, [
        (Regions.ZR_FRONT,
         lambda bundle: is_adult(bundle) | has_item(Items.BRONZE_SCALE, bundle) | has_grab(bundle) | blast_or_smash(bundle) | has_item(Items.HOVER_BOOTS, bundle)),
        (Regions.ZR_ATOP_LADDER,
         lambda bundle: ((is_adult(bundle) | has_grab(bundle) | can_use(Items.HOVER_BOOTS, bundle)) & can_climb_ladder(bundle)) | (is_adult(bundle) & bean_planted(bundle, Events.PLANT_ZORAS_RIVER_BEAN))),
        (Regions.ZR_PILLAR,
         lambda bundle: (is_child(bundle) & has_grab(bundle)) | can_use(Items.HOVER_BOOTS, bundle) | (is_adult(bundle) & (can_do_trick(Tricks.ZR_LOWER, bundle) | bunny_hood(bundle)))),
        (Regions.ZR_FROM_SHORTCUT,
         lambda bundle: has_item(Items.SILVER_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle)),
        (Regions.ZR_STORMS_GROTTO,
         lambda bundle: can_open_storms_grotto(bundle)),
        (Regions.ZR_BEHIND_WATERFALL,
         lambda bundle: True_(options=[OptionFilter(SleepingWaterfall, SleepingWaterfall.option_open)]) | any_age_time(bundle, lambda bundle: can_use(Items.ZELDAS_LULLABY, bundle)) | (is_child(bundle) & can_do_trick(Tricks.ZR_CUCCO, bundle) & has_grab(bundle)) | (is_adult(bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_do_trick(Tricks.ZR_HOVERS, bundle))),
    ])

    # ZR Atop Ladder  (upstream RR_ZR_ATOP_LADDER, SCENE_ZORAS_RIVER)
    # Events
    add_events(Regions.ZR_ATOP_LADDER, world, [
        (EventLocations.ZR_ATOP_LADDER_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.ZR_ATOP_LADDER_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
        (EventLocations.ZR_ATOP_LADDER_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy(bundle)),
    ])
    # Locations
    add_locations(Regions.ZR_ATOP_LADDER, world, [
        (Locations.ZR_GS_NEAR_RAISED_GROTTOS,
         lambda bundle: is_adult(bundle) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG) & can_get_nighttime_gs(bundle)),
        (Locations.ZR_NEAR_GROTTOS_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.ZR_NEAR_GROTTOS_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.ZR_UPPER_CIRCLE_BOULDER,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.ZR_UPPER_CIRCLE_ROCK_1,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.ZR_UPPER_CIRCLE_ROCK_2,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.ZR_UPPER_CIRCLE_ROCK_3,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.ZR_UPPER_CIRCLE_ROCK_4,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.ZR_UPPER_CIRCLE_ROCK_5,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.ZR_UPPER_CIRCLE_ROCK_6,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.ZR_UPPER_CIRCLE_ROCK_7,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.ZR_UPPER_CIRCLE_ROCK_8,
         lambda bundle: can_break_rocks(bundle)),
        # DEFERRED RC_ZR_NEAR_GROTTOS_GOSSIP_STONE: true
    ])
    # Connections
    connect_regions(Regions.ZR_ATOP_LADDER, world, [
        (Regions.ZORAS_RIVER,
         lambda bundle: True_()),
        (Regions.ZR_PILLAR,
         lambda bundle: (is_child(bundle) & has_grab(bundle)) | can_use(Items.HOVER_BOOTS, bundle) | (bunny_hood(bundle) & (is_adult(bundle) | can_jump_slash(bundle)))),
        (Regions.ZR_OPEN_GROTTO,
         lambda bundle: True_()),
        (Regions.ZR_FAIRY_GROTTO,
         lambda bundle: any_age_time(bundle, lambda bundle: blast_or_smash(bundle))),
    ])

    # ZR Pillar  (upstream RR_ZR_PILLAR, SCENE_ZORAS_RIVER)
    # Events
    add_events(Regions.ZR_PILLAR, world, [
        (EventLocations.ZR_PILLAR_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.ZR_PILLAR_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
        (EventLocations.ZR_PILLAR_BUG_ACCESS, Events.CAN_ACCESS_BUGS,
         lambda bundle: can_cut_shrubs(bundle)),
    ])
    # Locations
    add_locations(Regions.ZR_PILLAR, world, [
        (Locations.ZR_NEAR_OPEN_GROTTO_FREESTANDING_POH,
         lambda bundle: True_()),
        (Locations.ZR_NEAR_FREESTANDING_POH_GRASS,
         lambda bundle: can_cut_shrubs(bundle)),
    ])
    # Connections
    connect_regions(Regions.ZR_PILLAR, world, [
        (Regions.ZORAS_RIVER,
         lambda bundle: True_()),
    ])

    # ZR From Shortcut  (upstream RR_ZR_FROM_SHORTCUT, SCENE_ZORAS_RIVER)
    # Events
    add_events(Regions.ZR_FROM_SHORTCUT, world, [
        (EventLocations.ZR_FROM_SHORTCUT_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.ZR_FROM_SHORTCUT_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
    ])
    # Connections
    connect_regions(Regions.ZR_FROM_SHORTCUT, world, [
        (Regions.ZORAS_RIVER,
         lambda bundle: can_void(bundle) | has_item(Items.BRONZE_SCALE, bundle)),
        (Regions.THE_LOST_WOODS,
         lambda bundle: has_item(Items.SILVER_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle)),
    ])

    # ZR Behind Waterfall  (upstream RR_ZR_BEHIND_WATERFALL, SCENE_ZORAS_RIVER)
    # Events
    add_events(Regions.ZR_BEHIND_WATERFALL, world, [
        (EventLocations.ZR_BEHIND_WATERFALL_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.ZR_BEHIND_WATERFALL_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
    ])
    # Connections
    connect_regions(Regions.ZR_BEHIND_WATERFALL, world, [
        (Regions.ZORAS_RIVER,
         lambda bundle: True_()),
        (Regions.ZORAS_DOMAIN,
         lambda bundle: True_()),
    ])

    # ZR Open Grotto  (upstream RR_ZR_OPEN_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.ZR_OPEN_GROTTO, world, [
        (Locations.ZR_OPEN_GROTTO_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.ZR_OPEN_GROTTO_FISH,
         lambda bundle: has_bottle(bundle)),
        (Locations.ZR_OPEN_GROTTO_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.ZR_OPEN_GROTTO_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_ZR_OPEN_GROTTO_GOSSIP_STONE: true
        (Locations.ZR_OPEN_GROTTO_BEEHIVE_LEFT,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.ZR_OPEN_GROTTO_BEEHIVE_RIGHT,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.ZR_OPEN_GROTTO_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_OPEN_GROTTO_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_OPEN_GROTTO_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_OPEN_GROTTO_GRASS4,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_OPEN_GROTTO_BUTTERFLY_FAIRY,
         lambda bundle: can_use(Items.STICKS, bundle)),
    ])
    # Connections
    connect_regions(Regions.ZR_OPEN_GROTTO, world, [
        (Regions.ZR_ATOP_LADDER,
         lambda bundle: True_()),
    ])

    # ZR Fairy Grotto  (upstream RR_ZR_FAIRY_GROTTO, SCENE_GROTTOS)
    # Events
    add_events(Regions.ZR_FAIRY_GROTTO, world, [
        (EventLocations.ZR_FAIRY_GROTTO_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: True_()),
    ])
    # Locations
    add_locations(Regions.ZR_FAIRY_GROTTO, world, [
        (Locations.ZR_FAIRY_GROTTO_FAIRY1,
         lambda bundle: True_()),
        (Locations.ZR_FAIRY_GROTTO_FAIRY2,
         lambda bundle: True_()),
        (Locations.ZR_FAIRY_GROTTO_FAIRY3,
         lambda bundle: True_()),
        (Locations.ZR_FAIRY_GROTTO_FAIRY4,
         lambda bundle: True_()),
        (Locations.ZR_FAIRY_GROTTO_FAIRY5,
         lambda bundle: True_()),
        (Locations.ZR_FAIRY_GROTTO_FAIRY6,
         lambda bundle: True_()),
        (Locations.ZR_FAIRY_GROTTO_FAIRY7,
         lambda bundle: True_()),
        (Locations.ZR_FAIRY_GROTTO_FAIRY8,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.ZR_FAIRY_GROTTO, world, [
        (Regions.ZR_ATOP_LADDER,
         lambda bundle: True_()),
    ])

    # ZR Storms Grotto  (upstream RR_ZR_STORMS_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.ZR_STORMS_GROTTO, world, [
        (Locations.ZR_DEKU_SCRUB_GROTTO_REAR,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.ZR_DEKU_SCRUB_GROTTO_REAR, bundle)),
        (Locations.ZR_DEKU_SCRUB_GROTTO_FRONT,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.ZR_DEKU_SCRUB_GROTTO_FRONT, bundle)),
        (Locations.ZR_DEKU_SCRUB_GROTTO_BEEHIVE,
         lambda bundle: can_break_upper_beehives(bundle)),
    ])
    # Connections
    connect_regions(Regions.ZR_STORMS_GROTTO, world, [
        (Regions.ZORAS_RIVER,
         lambda bundle: True_()),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_BUGS', 'CAN_ACCESS_FAIRIES', 'PLANT_ZORAS_RIVER_BEAN']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (3): ['RC_ZR_NEAR_DOMAIN_GOSSIP_STONE', 'RC_ZR_NEAR_GROTTOS_GOSSIP_STONE', 'RC_ZR_OPEN_GROTTO_GOSSIP_STONE']
