"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/lake_hylia.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    LAKE_HYLIA_CHILD_CAN_PASS_TIME = "Lake Hylia Child Can Pass Time"
    LAKE_HYLIA_ADULT_CAN_PASS_TIME = "Lake Hylia Adult Can Pass Time"
    LAKE_HYLIA_PLANT_LAKE_HYLIA_BEAN = "Lake Hylia Plant Lake Hylia Bean"
    LAKE_HYLIA_FAIRY_ACCESS = "Lake Hylia Fairy Access"
    LAKE_HYLIA_BUG_ACCESS = "Lake Hylia Bug Access"
    LAKE_HYLIA_CHILD_SCARECROW = "Lake Hylia Child Scarecrow"
    LAKE_HYLIA_ADULT_SCARECROW = "Lake Hylia Adult Scarecrow"
    LH_FISHING_ISLAND_CHILD_CAN_PASS_TIME = "LH Fishing Island Child Can Pass Time"
    LH_FISHING_ISLAND_ADULT_CAN_PASS_TIME = "LH Fishing Island Adult Can Pass Time"
    LH_OWL_FLIGHT_CHILD_CAN_PASS_TIME = "LH Owl Flight Child Can Pass Time"
    LH_OWL_FLIGHT_ADULT_CAN_PASS_TIME = "LH Owl Flight Adult Can Pass Time"


def set_region_rules(world: "SohWorld") -> None:

    # Lake Hylia  (upstream RR_LAKE_HYLIA, SCENE_LAKE_HYLIA)
    # Events
    add_events(Regions.LAKE_HYLIA, world, [
        (EventLocations.LAKE_HYLIA_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.LAKE_HYLIA_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
        (EventLocations.LAKE_HYLIA_PLANT_LAKE_HYLIA_BEAN, Events.PLANT_LAKE_HYLIA_BEAN,
         lambda bundle: can_plant_bean(bundle)),
        (EventLocations.LAKE_HYLIA_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy(bundle) | can_use(Items.STICKS, bundle) | (is_child(bundle) & bean_planted(bundle, Events.PLANT_LAKE_HYLIA_BEAN) & can_use(Items.SONG_OF_STORMS, bundle))),
        (EventLocations.LAKE_HYLIA_BUG_ACCESS, Events.CAN_ACCESS_BUGS,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (EventLocations.LAKE_HYLIA_CHILD_SCARECROW, Events.CHILD_SCARECROW_UNLOCKED,
         lambda bundle: is_child(bundle) & has_item(Items.FAIRY_OCARINA, bundle) & has_enough_ocarina_buttons(bundle, 2)),
        (EventLocations.LAKE_HYLIA_ADULT_SCARECROW, Events.ADULT_SCARECROW_UNLOCKED,
         lambda bundle: is_adult(bundle) & has_item(Items.FAIRY_OCARINA, bundle) & has_enough_ocarina_buttons(bundle, 2)),
    ])
    # Locations
    add_locations(Regions.LAKE_HYLIA, world, [
        (Locations.LH_UNDERWATER_ITEM,
         lambda bundle: is_child(bundle) & has_item(Items.SILVER_SCALE, bundle)),
        # DEFERRED RC_LH_SCARECROWS_SONG: logic->Get(LOGIC_CHILD_SCARECROW) && logic->Get(LOGIC_ADULT_SCARECROW)
        (Locations.LH_SUN,
         lambda bundle: is_adult(bundle) & ((has_item(Events.WATER_TEMPLE_COMPLETED, bundle) & has_item(Items.BRONZE_SCALE, bundle)) | reach_distant_scarecrow(bundle)) & can_use(Items.FAIRY_BOW, bundle)),
        (Locations.LH_FREESTANDING_POH,
         lambda bundle: is_adult(bundle) & (reach_scarecrow(bundle) | bean_planted(bundle, Events.PLANT_LAKE_HYLIA_BEAN)) & can_avoid_enemy(bundle, Enemies.GUAY, EnemyDistance.CLOSE, False) & has_climb(bundle)),
        (Locations.LH_GS_BEAN_PATCH,
         lambda bundle: can_spawn_soil_skull(bundle) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA)),
        (Locations.LH_GS_LAB_WALL,
         lambda bundle: is_child(bundle) & (can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG) | (can_do_trick(Tricks.LH_LAB_WALL_GS, bundle) & can_jump_slash_except_hammer(bundle))) & can_get_nighttime_gs(bundle)),
        (Locations.LH_GS_SMALL_ISLAND,
         lambda bundle: is_child(bundle) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA) & can_get_nighttime_gs(bundle) & has_item(Items.BRONZE_SCALE, bundle)),
        (Locations.LH_GS_TREE,
         lambda bundle: is_adult(bundle) & can_use(Items.LONGSHOT, bundle) & can_get_nighttime_gs(bundle)),
        (Locations.LH_UNDERWATER_FRONT_RUPEE,
         lambda bundle: is_child(bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle))),
        (Locations.LH_UNDERWATER_MIDDLE_RUPEE,
         lambda bundle: is_child(bundle) & (has_item(Items.SILVER_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle))),
        (Locations.LH_UNDERWATER_BACK_RUPEE,
         lambda bundle: is_child(bundle) & (has_item(Items.SILVER_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle))),
        (Locations.LH_BEAN_SPROUT_FAIRY1,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_LAKE_HYLIA_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.LH_BEAN_SPROUT_FAIRY2,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_LAKE_HYLIA_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.LH_BEAN_SPROUT_FAIRY3,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_LAKE_HYLIA_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.LH_LAB_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.LH_LAB_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.LH_SOUTHEAST_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.LH_SOUTHEAST_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.LH_SOUTHWEST_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.LH_SOUTHWEST_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.LH_ISLAND_SUNS_SONG_FAIRY,
         lambda bundle: can_use(Items.SUNS_SONG, bundle) & ((has_item(Items.BRONZE_SCALE, bundle) & (is_child(bundle) | has_item(Events.WATER_TEMPLE_COMPLETED, bundle))) | reach_distant_scarecrow(bundle))),
        # DEFERRED RC_LH_LAB_GOSSIP_STONE: true
        # DEFERRED RC_LH_SOUTHEAST_GOSSIP_STONE: true
        # DEFERRED RC_LH_SOUTHWEST_GOSSIP_STONE: true
        (Locations.LH_GRASS_1,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_2,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_3,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_4,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_5,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_6,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_7,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_8,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_9,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_10,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_11,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_12,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_13,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_14,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_15,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_16,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_17,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_18,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_19,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_20,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_21,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_22,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_23,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_24,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_25,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_26,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_27,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_28,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_29,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_30,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_31,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_32,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_33,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_34,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_35,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_GRASS_36,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_CHILD_GRASS_1,
         lambda bundle: is_child(bundle) & (can_cut_shrubs(bundle) | summon_epona(bundle))),
        (Locations.LH_CHILD_GRASS_2,
         lambda bundle: is_child(bundle) & (can_cut_shrubs(bundle) | summon_epona(bundle))),
        (Locations.LH_CHILD_GRASS_3,
         lambda bundle: is_child(bundle) & (can_cut_shrubs(bundle) | summon_epona(bundle))),
        (Locations.LH_CHILD_GRASS_4,
         lambda bundle: is_child(bundle) & (can_cut_shrubs(bundle) | summon_epona(bundle))),
        (Locations.LH_WARP_PAD_GRASS_1,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.LH_WARP_PAD_GRASS_2,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        # DEFERRED RC_LH_SCARECROW_BUTTERFLY_FAIRY: logic->IsChild && logic->CanUse(RG_STICKS)
        # DEFERRED RC_LH_LAB_RECTANGLE_SIGN: logic->CanRead()
        # DEFERRED RC_LH_NORTH_EXIT_ARROW_SIGN: logic->CanRead()
        # DEFERRED RC_LH_ISLAND_PEDESTAL: logic->CanRead()
        # DEFERRED RC_LH_WATER_SWITCH_SIGN: logic->IsAdult && logic->CanRead()
    ])
    # Connections
    connect_regions(Regions.LAKE_HYLIA, world, [
        (Regions.HF_TO_LAKE_HYLIA,
         lambda bundle: True_()),
        (Regions.LH_FROM_SHORTCUT,
         lambda bundle: True_()),
        (Regions.LH_OWL_FLIGHT,
         lambda bundle: is_child(bundle) & (has_speak(bundle, "DEKU") | has_speak(bundle, "GERUDO") | has_speak(bundle, "GORON") | has_speak(bundle, "KOKIRI") | has_speak(bundle, "HYLIAN") | has_speak(bundle, "ZORA"))),
        (Regions.LH_FISHING_ISLAND,
         lambda bundle: ((is_child(bundle) | has_item(Events.WATER_TEMPLE_COMPLETED, bundle)) & has_item(Items.BRONZE_SCALE, bundle)) | (is_adult(bundle) & (reach_scarecrow(bundle) | bean_planted(bundle, Events.PLANT_LAKE_HYLIA_BEAN)))),
        (Regions.LH_LAB,
         lambda bundle: has_item(Items.HYLIA_LAB_KEY, bundle)),
        (Regions.LH_FROM_WATER_TEMPLE,
         lambda bundle: True_()),
        (Regions.LH_GROTTO,
         lambda bundle: has_grab(bundle) & (is_adult(bundle) | has_speak(bundle, "DEKU") | has_speak(bundle, "GERUDO") | has_speak(bundle, "GORON") | has_speak(bundle, "KOKIRI") | has_speak(bundle, "HYLIAN") | has_speak(bundle, "ZORA"))),
    ])

    # LH From Shortcut  (upstream RR_LH_FROM_SHORTCUT, SCENE_LAKE_HYLIA)
    # Connections
    connect_regions(Regions.LH_FROM_SHORTCUT, world, [
        (Regions.LAKE_HYLIA,
         lambda bundle: can_void(bundle) | has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle)),
        (Regions.ZORAS_DOMAIN,
         lambda bundle: is_child(bundle) & (has_item(Items.SILVER_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle))),
    ])

    # LH From Water Temple  (upstream RR_LH_FROM_WATER_TEMPLE, SCENE_LAKE_HYLIA)
    # Connections
    connect_regions(Regions.LH_FROM_WATER_TEMPLE, world, [
        (Regions.LAKE_HYLIA,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | has_item(Items.BOTTLE_WITH_FAIRY, bundle) | can_use(Items.IRON_BOOTS, bundle)),
        (Regions.WATER_TEMPLE_ENTRYWAY,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) & ((can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.LH_WATER_HOOKSHOT, bundle) & has_item(Items.GOLDEN_SCALE, bundle))) | (is_adult(bundle) & can_use(Items.LONGSHOT, bundle) & has_item(Items.GOLDEN_SCALE, bundle)))),
    ])

    # LH Fishing Island  (upstream RR_LH_FISHING_ISLAND, SCENE_LAKE_HYLIA)
    # Events
    add_events(Regions.LH_FISHING_ISLAND, world, [
        (EventLocations.LH_FISHING_ISLAND_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.LH_FISHING_ISLAND_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
    ])
    # Locations
    add_locations(Regions.LH_FISHING_ISLAND, world, [
        # DEFERRED RC_LH_ROCK: logic->CanBreakRocks()
        # DEFERRED RC_LH_FISHING_SIGN: logic->CanRead()
        # DEFERRED RC_LH_FISHING_ISLAND_WATER_SWITCH_SIGN: logic->IsAdult && logic->CanRead()
    ])
    # Connections
    connect_regions(Regions.LH_FISHING_ISLAND, world, [
        (Regions.LAKE_HYLIA,
         lambda bundle: is_adult(bundle) | has_item(Items.BRONZE_SCALE, bundle)),
        (Regions.LH_FISHING_POND,
         lambda bundle: has_item(Items.FISHING_HOLE_KEY, bundle)),
    ])

    # LH Owl Flight  (upstream RR_LH_OWL_FLIGHT, SCENE_LAKE_HYLIA)
    # Events
    add_events(Regions.LH_OWL_FLIGHT, world, [
        (EventLocations.LH_OWL_FLIGHT_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.LH_OWL_FLIGHT_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
    ])
    # Connections
    connect_regions(Regions.LH_OWL_FLIGHT, world, [
        (Regions.HYRULE_FIELD,
         lambda bundle: True_()),
    ])

    # LH Lab  (upstream RR_LH_LAB, SCENE_LAKESIDE_LABORATORY)
    # Locations
    add_locations(Regions.LH_LAB, world, [
        (Locations.LH_LAB_DIVE,
         lambda bundle: has_item(Items.GOLDEN_SCALE, bundle) & has_speak(bundle, "HYLIAN")),
        (Locations.LH_LAB_TRADE_EYEBALL_FROG,
         lambda bundle: is_adult(bundle) & can_use(Items.EYEBALL_FROG, bundle)),
        (Locations.LH_LAB_FRONT_RUPEE,
         lambda bundle: has_item(Items.GOLDEN_SCALE, bundle)),
        (Locations.LH_LAB_LEFT_RUPEE,
         lambda bundle: has_item(Items.GOLDEN_SCALE, bundle)),
        (Locations.LH_LAB_RIGHT_RUPEE,
         lambda bundle: has_item(Items.GOLDEN_SCALE, bundle)),
    ])
    # Connections
    connect_regions(Regions.LH_LAB, world, [
        (Regions.LAKE_HYLIA,
         lambda bundle: True_()),
        (Regions.LH_LAB_UNDERWATER,
         lambda bundle: can_use(Items.IRON_BOOTS, bundle)),
    ])

    # LH Lab Underwater  (upstream RR_LH_LAB_UNDERWATER, SCENE_LAKESIDE_LABORATORY)
    # Locations
    add_locations(Regions.LH_LAB_UNDERWATER, world, [
        (Locations.LH_LAB_DIVE,
         lambda bundle: (can_do_trick(Tricks.LH_LAB_DIVING, bundle) & can_use(Items.HOOKSHOT, bundle) & has_item(Items.BRONZE_SCALE, bundle)) & has_speak(bundle, "HYLIAN")),
        (Locations.LH_GS_LAB_CRATE,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) & can_break_crates(bundle)),
        (Locations.LH_LAB_FRONT_RUPEE,
         lambda bundle: True_()),
        (Locations.LH_LAB_LEFT_RUPEE,
         lambda bundle: True_()),
        (Locations.LH_LAB_RIGHT_RUPEE,
         lambda bundle: True_()),
        (Locations.LH_LAB_CRATE,
         lambda bundle: can_break_crates(bundle)),
    ])
    # Connections
    connect_regions(Regions.LH_LAB_UNDERWATER, world, [
        (Regions.LH_LAB,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle)),
    ])

    # LH Fishing Hole  (upstream RR_LH_FISHING_POND, SCENE_FISHING_POND)
    # Locations
    add_locations(Regions.LH_FISHING_POND, world, [
        (Locations.LH_CHILD_FISHING,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & is_child(bundle)),
        (Locations.LH_CHILD_POND_FISH1,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & (is_child(bundle) | Not(True_(options=[OptionFilter(FishsanityAgeSplit, True)])))),
        (Locations.LH_CHILD_POND_FISH2,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & (is_child(bundle) | Not(True_(options=[OptionFilter(FishsanityAgeSplit, True)])))),
        (Locations.LH_CHILD_POND_FISH3,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & (is_child(bundle) | Not(True_(options=[OptionFilter(FishsanityAgeSplit, True)])))),
        (Locations.LH_CHILD_POND_FISH4,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & (is_child(bundle) | Not(True_(options=[OptionFilter(FishsanityAgeSplit, True)])))),
        (Locations.LH_CHILD_POND_FISH5,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & (is_child(bundle) | Not(True_(options=[OptionFilter(FishsanityAgeSplit, True)])))),
        (Locations.LH_CHILD_POND_FISH6,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & (is_child(bundle) | Not(True_(options=[OptionFilter(FishsanityAgeSplit, True)])))),
        (Locations.LH_CHILD_POND_FISH7,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & (is_child(bundle) | Not(True_(options=[OptionFilter(FishsanityAgeSplit, True)])))),
        (Locations.LH_CHILD_POND_FISH8,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & (is_child(bundle) | Not(True_(options=[OptionFilter(FishsanityAgeSplit, True)])))),
        (Locations.LH_CHILD_POND_FISH9,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & (is_child(bundle) | Not(True_(options=[OptionFilter(FishsanityAgeSplit, True)])))),
        (Locations.LH_CHILD_POND_FISH10,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & (is_child(bundle) | Not(True_(options=[OptionFilter(FishsanityAgeSplit, True)])))),
        (Locations.LH_CHILD_POND_FISH11,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & (is_child(bundle) | Not(True_(options=[OptionFilter(FishsanityAgeSplit, True)])))),
        (Locations.LH_CHILD_POND_FISH12,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & (is_child(bundle) | Not(True_(options=[OptionFilter(FishsanityAgeSplit, True)])))),
        (Locations.LH_CHILD_POND_FISH13,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & (is_child(bundle) | Not(True_(options=[OptionFilter(FishsanityAgeSplit, True)])))),
        (Locations.LH_CHILD_POND_FISH14,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & (is_child(bundle) | Not(True_(options=[OptionFilter(FishsanityAgeSplit, True)])))),
        (Locations.LH_CHILD_POND_FISH15,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & (is_child(bundle) | Not(True_(options=[OptionFilter(FishsanityAgeSplit, True)])))),
        (Locations.LH_CHILD_POND_LOACH1,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & (is_child(bundle) | Not(True_(options=[OptionFilter(FishsanityAgeSplit, True)])))),
        (Locations.LH_CHILD_POND_LOACH2,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & (is_child(bundle) | Not(True_(options=[OptionFilter(FishsanityAgeSplit, True)])))),
        (Locations.LH_ADULT_FISHING,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & is_adult(bundle)),
        (Locations.LH_ADULT_POND_FISH1,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & is_adult(bundle) & True_(options=[OptionFilter(FishsanityAgeSplit, True)])),
        (Locations.LH_ADULT_POND_FISH2,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & is_adult(bundle) & True_(options=[OptionFilter(FishsanityAgeSplit, True)])),
        (Locations.LH_ADULT_POND_FISH3,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & is_adult(bundle) & True_(options=[OptionFilter(FishsanityAgeSplit, True)])),
        (Locations.LH_ADULT_POND_FISH4,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & is_adult(bundle) & True_(options=[OptionFilter(FishsanityAgeSplit, True)])),
        (Locations.LH_ADULT_POND_FISH5,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & is_adult(bundle) & True_(options=[OptionFilter(FishsanityAgeSplit, True)])),
        (Locations.LH_ADULT_POND_FISH6,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & is_adult(bundle) & True_(options=[OptionFilter(FishsanityAgeSplit, True)])),
        (Locations.LH_ADULT_POND_FISH7,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & is_adult(bundle) & True_(options=[OptionFilter(FishsanityAgeSplit, True)])),
        (Locations.LH_ADULT_POND_FISH8,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & is_adult(bundle) & True_(options=[OptionFilter(FishsanityAgeSplit, True)])),
        (Locations.LH_ADULT_POND_FISH9,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & is_adult(bundle) & True_(options=[OptionFilter(FishsanityAgeSplit, True)])),
        (Locations.LH_ADULT_POND_FISH10,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & is_adult(bundle) & True_(options=[OptionFilter(FishsanityAgeSplit, True)])),
        (Locations.LH_ADULT_POND_FISH11,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & is_adult(bundle) & True_(options=[OptionFilter(FishsanityAgeSplit, True)])),
        (Locations.LH_ADULT_POND_FISH12,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & is_adult(bundle) & True_(options=[OptionFilter(FishsanityAgeSplit, True)])),
        (Locations.LH_ADULT_POND_FISH13,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & is_adult(bundle) & True_(options=[OptionFilter(FishsanityAgeSplit, True)])),
        (Locations.LH_ADULT_POND_FISH14,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & is_adult(bundle) & True_(options=[OptionFilter(FishsanityAgeSplit, True)])),
        (Locations.LH_ADULT_POND_FISH15,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & is_adult(bundle) & True_(options=[OptionFilter(FishsanityAgeSplit, True)])),
        (Locations.LH_ADULT_POND_LOACH,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN") & is_adult(bundle) & True_(options=[OptionFilter(FishsanityAgeSplit, True)])),
        (Locations.LH_HYRULE_LOACH_REWARD,
         lambda bundle: can_use(Items.FISHING_POLE, bundle) & has_speak(bundle, "HYLIAN")),
        (Locations.LH_FISHING_POLE_HINT,
         lambda bundle: has_speak(bundle, "HYLIAN")),
        # DEFERRED RC_LH_FISHING_POND_RECTANGLE_SIGN: logic->CanRead()
    ])
    # Connections
    connect_regions(Regions.LH_FISHING_POND, world, [
        (Regions.LH_FISHING_ISLAND,
         lambda bundle: True_()),
    ])

    # LH Grotto  (upstream RR_LH_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.LH_GROTTO, world, [
        (Locations.LH_DEKU_SCRUB_GROTTO_LEFT,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.LH_DEKU_SCRUB_GROTTO_LEFT, bundle)),
        (Locations.LH_DEKU_SCRUB_GROTTO_RIGHT,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.LH_DEKU_SCRUB_GROTTO_RIGHT, bundle)),
        (Locations.LH_DEKU_SCRUB_GROTTO_CENTER,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.LH_DEKU_SCRUB_GROTTO_CENTER, bundle)),
        (Locations.LH_DEKU_SCRUB_GROTTO_BEEHIVE,
         lambda bundle: can_break_upper_beehives(bundle)),
    ])
    # Connections
    connect_regions(Regions.LH_GROTTO, world, [
        (Regions.LAKE_HYLIA,
         lambda bundle: True_()),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['ADULT_SCARECROW_UNLOCKED', 'CAN_ACCESS_BUGS', 'CAN_ACCESS_FAIRIES', 'CHILD_SCARECROW_UNLOCKED', 'PLANT_LAKE_HYLIA_BEAN', 'WATER_TEMPLE_COMPLETED']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (13): ['RC_LH_SCARECROWS_SONG', 'RC_LH_LAB_GOSSIP_STONE', 'RC_LH_SOUTHEAST_GOSSIP_STONE', 'RC_LH_SOUTHWEST_GOSSIP_STONE', 'RC_LH_SCARECROW_BUTTERFLY_FAIRY', 'RC_LH_LAB_RECTANGLE_SIGN', 'RC_LH_NORTH_EXIT_ARROW_SIGN', 'RC_LH_ISLAND_PEDESTAL', 'RC_LH_WATER_SWITCH_SIGN', 'RC_LH_ROCK', 'RC_LH_FISHING_SIGN', 'RC_LH_FISHING_ISLAND_WATER_SWITCH_SIGN', 'RC_LH_FISHING_POND_RECTANGLE_SIGN']
