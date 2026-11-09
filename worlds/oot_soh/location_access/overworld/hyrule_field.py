"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/hyrule_field.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    HYRULE_FIELD_CHILD_CAN_PASS_TIME = "Hyrule Field Child Can Pass Time"
    HYRULE_FIELD_ADULT_CAN_PASS_TIME = "Hyrule Field Adult Can Pass Time"
    HYRULE_FIELD_BIG_POE_KILL = "Hyrule Field Big Poe Kill"
    HYRULE_FIELD_SOLD_BUNNY_HOOD = "Hyrule Field Sold Bunny Hood"
    HF_TO_LAKE_HYLIA_CHILD_CAN_PASS_TIME = "HF to Lake Hylia Child Can Pass Time"
    HF_TO_LAKE_HYLIA_ADULT_CAN_PASS_TIME = "HF to Lake Hylia Adult Can Pass Time"
    HF_COW_GROTTO_BEHIND_WEBS_BUG_ACCESS = "HF Cow Grotto Behind Webs Bug Access"
    HF_COW_GROTTO_BEHIND_WEBS_FAIRY_ACCESS = "HF Cow Grotto Behind Webs Fairy Access"
    HF_FAIRY_GROTTO_FAIRY_ACCESS = "HF Fairy Grotto Fairy Access"


def set_region_rules(world: "SohWorld") -> None:

    # Hyrule Field  (upstream RR_HYRULE_FIELD, SCENE_HYRULE_FIELD)
    # Events
    add_events(Regions.HYRULE_FIELD, world, [
        (EventLocations.HYRULE_FIELD_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.HYRULE_FIELD_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
        (EventLocations.HYRULE_FIELD_BIG_POE_KILL, Events.CAN_DEFEAT_BIG_POE,
         lambda bundle: has_bottle(bundle) & can_use(Items.FAIRY_BOW, bundle) & (summon_epona(bundle) | can_do_trick(Tricks.HF_BIG_POE_WITHOUT_EPONA, bundle))),
        (EventLocations.HYRULE_FIELD_SOLD_BUNNY_HOOD, Events.SOLD_BUNNY_HOOD,
         lambda bundle: is_child(bundle) & has_mask(bundle, "BUNNY_HOOD") & has_item(Items.KOKIRIS_EMERALD, bundle) & has_item(Items.GORONS_RUBY, bundle) & has_item(Items.ZORAS_SAPPHIRE, bundle) & has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN")),
    ])
    # Locations
    add_locations(Regions.HYRULE_FIELD, world, [
        (Locations.HF_OCARINA_OF_TIME_ITEM,
         lambda bundle: is_child(bundle) & stone_count_at_least(bundle, 3) & has_item(Items.BRONZE_SCALE, bundle)),
        (Locations.SONG_FROM_OCARINA_OF_TIME,
         lambda bundle: is_child(bundle) & stone_count_at_least(bundle, 3) & has_item(Items.BRONZE_SCALE, bundle)),
        (Locations.HF_POND_SONG_OF_STORMS_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.HF_CENTRAL_GRASS1,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_CENTRAL_GRASS2,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_CENTRAL_GRASS3,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_CENTRAL_GRASS4,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_CENTRAL_GRASS5,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_CENTRAL_GRASS6,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_CENTRAL_GRASS7,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_CENTRAL_GRASS8,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_CENTRAL_GRASS9,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_CENTRAL_GRASS10,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_CENTRAL_GRASS11,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_CENTRAL_GRASS12,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_SOUTH_GRASS1,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_SOUTH_GRASS2,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_SOUTH_GRASS3,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_SOUTH_GRASS4,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_SOUTH_GRASS5,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_SOUTH_GRASS6,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_SOUTH_GRASS7,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_SOUTH_GRASS8,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_SOUTH_GRASS9,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_SOUTH_GRASS10,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_SOUTH_GRASS11,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_SOUTH_GRASS12,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_MARKET_GRASS1,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_MARKET_GRASS2,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_MARKET_GRASS3,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_MARKET_GRASS4,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_MARKET_GRASS5,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_MARKET_GRASS6,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_MARKET_GRASS7,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_MARKET_GRASS8,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_MARKET_GRASS9,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_MARKET_GRASS10,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_MARKET_GRASS11,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_MARKET_GRASS12,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_KFGRASS1,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_KFGRASS2,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_KFGRASS3,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_KFGRASS4,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_KFGRASS5,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_KFGRASS6,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_KFGRASS7,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_KFGRASS8,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_KFGRASS9,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_KFGRASS10,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_KFGRASS11,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        (Locations.HF_NEAR_KFGRASS12,
         lambda bundle: can_cut_shrubs(bundle) | summon_epona(bundle)),
        # DEFERRED RC_HF_SILVER_BOULDER: logic->CanUse(RG_SILVER_GAUNTLETS)
        # DEFERRED RC_HF_ROCK_1: logic->CanBreakRocks()
        # DEFERRED RC_HF_ROCK_2: logic->CanBreakRocks()
        # DEFERRED RC_HF_ROCK_3: logic->CanBreakRocks()
        # DEFERRED RC_HF_ROCK_4: logic->CanBreakRocks()
        # DEFERRED RC_HF_ROCK_5: logic->CanBreakRocks()
        # DEFERRED RC_HF_ROCK_6: logic->CanBreakRocks()
        # DEFERRED RC_HF_ROCK_7: logic->CanBreakRocks()
        # DEFERRED RC_HF_ROCK_8: logic->CanBreakRocks()
        # DEFERRED RC_HF_BOULDER_NORTH: logic->BlastOrSmash()
        # DEFERRED RC_HF_BOULDER_BY_MARKET: logic->BlastOrSmash()
        # DEFERRED RC_HF_BOULDER_SOUTH: logic->BlastOrSmash()
        # DEFERRED RC_HF_BRONZE_BOULDER_1: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_HF_BRONZE_BOULDER_2: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_HF_BRONZE_BOULDER_3: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_HF_BRONZE_BOULDER_4: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        (Locations.HF_NEAR_LLR_TREE,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_NEAR_LH_TREE,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_CHILD_NEAR_GV_TREE,
         lambda bundle: is_child(bundle) & can_bonk_trees(bundle)),
        (Locations.HF_ADULT_NEAR_GV_TREE,
         lambda bundle: is_adult(bundle) & can_bonk_trees(bundle)),
        (Locations.HF_NEAR_ZR_TREE,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_NEAR_KAK_TREE,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_NEAR_KAK_SMALL_TREE,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_NEAR_MARKET_TREE_1,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_NEAR_MARKET_TREE_2,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_NEAR_MARKET_TREE_3,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_NORTHWEST_TREE_1,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_NORTHWEST_TREE_2,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_NORTHWEST_TREE_3,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_NORTHWEST_TREE_4,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_NORTHWEST_TREE_5,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_NORTHWEST_TREE_6,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_EAST_TREE_1,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_EAST_TREE_2,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_EAST_TREE_3,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_EAST_TREE_4,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_EAST_TREE_5,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_EAST_TREE_6,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_SOUTHEAST_TREE_1,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_SOUTHEAST_TREE_2,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_SOUTHEAST_TREE_3,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_SOUTHEAST_TREE_4,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_SOUTHEAST_TREE_5,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_SOUTHEAST_TREE_6,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_SOUTHEAST_TREE_7,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_SOUTHEAST_TREE_8,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_SOUTHEAST_TREE_9,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_SOUTHEAST_TREE_10,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_SOUTHEAST_TREE_11,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_SOUTHEAST_TREE_12,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_SOUTHEAST_TREE_13,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_SOUTHEAST_TREE_14,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_SOUTHEAST_TREE_15,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_SOUTHEAST_TREE_16,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_SOUTHEAST_TREE_17,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_SOUTHEAST_TREE_18,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_SOUTHEAST_TREE_19,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HF_CHILD_SOUTHEAST_TREE_1,
         lambda bundle: is_child(bundle) & can_bonk_trees(bundle)),
        (Locations.HF_CHILD_SOUTHEAST_TREE_2,
         lambda bundle: is_child(bundle) & can_bonk_trees(bundle)),
        (Locations.HF_CHILD_SOUTHEAST_TREE_3,
         lambda bundle: is_child(bundle) & can_bonk_trees(bundle)),
        (Locations.HF_CHILD_SOUTHEAST_TREE_4,
         lambda bundle: is_child(bundle) & can_bonk_trees(bundle)),
        (Locations.HF_CHILD_SOUTHEAST_TREE_5,
         lambda bundle: is_child(bundle) & can_bonk_trees(bundle)),
        (Locations.HF_CHILD_SOUTHEAST_TREE_6,
         lambda bundle: is_child(bundle) & can_bonk_trees(bundle)),
        (Locations.HF_TEKTITE_GROTTO_TREE,
         lambda bundle: can_bonk_trees(bundle)),
        # DEFERRED RC_HF_BUSH_NEAR_LAKE_1: true
        # DEFERRED RC_HF_BUSH_NEAR_LAKE_2: true
        # DEFERRED RC_HF_BUSH_NEAR_LAKE_3: true
        # DEFERRED RC_HF_BUSH_NEAR_LAKE_4: true
        # DEFERRED RC_HF_BUSH_NEAR_LAKE_5: true
        # DEFERRED RC_HF_BUSH_NEAR_LAKE_6: true
        # DEFERRED RC_HF_BUSH_NEAR_LAKE_7: true
        # DEFERRED RC_HF_BUSH_NEAR_LAKE_8: true
        # DEFERRED RC_HF_BUSH_NEAR_LAKE_9: true
        # DEFERRED RC_HF_BUSH_NEAR_LAKE_10: true
        # DEFERRED RC_HF_BUSH_NEAR_LAKE_11: true
        # DEFERRED RC_HF_NORTHERN_BUSH_1: true
        # DEFERRED RC_HF_NORTHERN_BUSH_2: true
        # DEFERRED RC_HF_NORTHERN_BUSH_3: true
        # DEFERRED RC_HF_NORTHERN_BUSH_4: true
        # DEFERRED RC_HF_NORTHERN_BUSH_5: true
        # DEFERRED RC_HF_NORTHERN_BUSH_6: true
        # DEFERRED RC_HF_CHILD_NORTHERN_BUSH_1: logic->IsChild
        # DEFERRED RC_HF_CHILD_NORTHERN_BUSH_2: logic->IsChild
        # DEFERRED RC_HF_CHILD_NORTHERN_BUSH_3: logic->IsChild
        # DEFERRED RC_HF_CHILD_NORTHERN_BUSH_4: logic->IsChild
        # DEFERRED RC_HF_CHILD_NORTHERN_BUSH_5: logic->IsChild
        # DEFERRED RC_HF_CHILD_NORTHERN_BUSH_6: logic->IsChild
        # DEFERRED RC_HF_CHILD_NORTHERN_BUSH_7: logic->IsChild
        # DEFERRED RC_HF_CHILD_NORTHERN_BUSH_8: logic->IsChild
        # DEFERRED RC_HF_CHILD_NORTHERN_BUSH_9: logic->IsChild
        # DEFERRED RC_HF_CHILD_NORTHERN_BUSH_10: logic->IsChild
        # DEFERRED RC_HF_CHILD_NORTHERN_BUSH_11: logic->IsChild
        # DEFERRED RC_HF_BUSH_BY_ROCKY_PATH_1: true
        # DEFERRED RC_HF_BUSH_BY_ROCKY_PATH_2: true
        # DEFERRED RC_HF_BUSH_BY_ROCKY_PATH_3: true
        # DEFERRED RC_HF_BUSH_BY_ROCKY_PATH_4: true
        # DEFERRED RC_HF_BUSH_BY_ROCKY_PATH_5: true
        # DEFERRED RC_HF_BUSH_BY_ROCKY_PATH_6: true
        # DEFERRED RC_HF_SOUTHERN_BUSH_1: true
        # DEFERRED RC_HF_SOUTHERN_BUSH_2: true
        # DEFERRED RC_HF_SOUTHERN_BUSH_3: true
        # DEFERRED RC_HF_SOUTHERN_BUSH_4: true
        # DEFERRED RC_HF_SOUTHERN_BUSH_5: true
        # DEFERRED RC_HF_SOUTHERN_BUSH_6: true
        # DEFERRED RC_HF_SOUTHERN_BUSH_7: true
        # DEFERRED RC_HF_SOUTHERN_BUSH_8: true
        # DEFERRED RC_HF_SOUTHERN_BUSH_9: true
        # DEFERRED RC_HF_SOUTHERN_BUSH_10: true
        # DEFERRED RC_HF_SOUTHERN_BUSH_11: true
        # DEFERRED RC_HF_SOUTHERN_BUSH_12: true
        # DEFERRED RC_HF_CHILD_SOUTHERN_BUSH_1: logic->IsChild
        # DEFERRED RC_HF_CHILD_SOUTHERN_BUSH_2: logic->IsChild
        # DEFERRED RC_HF_CHILD_SOUTHERN_BUSH_3: logic->IsChild
        # DEFERRED RC_HF_CHILD_SOUTHERN_BUSH_4: logic->IsChild
        # DEFERRED RC_HF_CHILD_SOUTHERN_BUSH_5: logic->IsChild
        # DEFERRED RC_HF_CHILD_SOUTHERN_BUSH_6: logic->IsChild
        # DEFERRED RC_HF_CHILD_SOUTHERN_BUSH_7: logic->IsChild
        # DEFERRED RC_HF_CHILD_SOUTHERN_BUSH_8: logic->IsChild
        # DEFERRED RC_HF_CHILD_SOUTHERN_BUSH_9: logic->IsChild
        # DEFERRED RC_HF_CHILD_SOUTHERN_BUSH_10: logic->IsChild
        # DEFERRED RC_HF_CHILD_SOUTHERN_BUSH_11: logic->IsChild
        # DEFERRED RC_HF_CHILD_SOUTHERN_BUSH_12: logic->IsChild
        (Locations.HF_CASTLE_EXIT_ARROW_SIGN,
         lambda bundle: can_read(bundle)),
        (Locations.HF_WOODED_EXIT_ARROW_SIGN,
         lambda bundle: can_read(bundle)),
        (Locations.HF_ROCKY_PATH_EXIT_ARROW_SIGN,
         lambda bundle: can_read(bundle)),
        (Locations.HF_FENCED_ARROW_SIGN,
         lambda bundle: can_read(bundle)),
        (Locations.HF_CENTER_EXIT_ARROW_SIGN,
         lambda bundle: can_read(bundle)),
        (Locations.HF_RIVER_EXIT_ARROW_SIGN,
         lambda bundle: can_read(bundle)),
        (Locations.HF_STAIRS_EXIT_ARROW_SIGN,
         lambda bundle: can_read(bundle)),
        # DEFERRED RC_HF_WONDER_BRIDGE_1: logic->IsChild
        # DEFERRED RC_HF_WONDER_BRIDGE_2: logic->IsChild
        # DEFERRED RC_HF_WONDER_BRIDGE_3: logic->IsChild
    ])
    # Connections
    connect_regions(Regions.HYRULE_FIELD, world, [
        (Regions.LW_BRIDGE,
         lambda bundle: True_()),
        (Regions.GERUDO_VALLEY,
         lambda bundle: True_()),
        (Regions.MARKET_ENTRANCE,
         lambda bundle: True_()),
        (Regions.KAKARIKO_VILLAGE,
         lambda bundle: True_()),
        (Regions.ZR_FRONT,
         lambda bundle: True_()),
        (Regions.LON_LON_RANCH,
         lambda bundle: True_()),
        (Regions.HF_SOUTHEAST_GROTTO,
         lambda bundle: any_age_time(bundle, lambda bundle: blast_or_smash(bundle))),
        (Regions.HF_TO_LAKE_HYLIA,
         lambda bundle: can_climb_ladder(bundle) | summon_epona(bundle)),
        (Regions.HF_OPEN_GROTTO,
         lambda bundle: True_()),
        (Regions.HF_INSIDE_FENCE_GROTTO,
         lambda bundle: can_open_bomb_grotto(bundle)),
        (Regions.HF_COW_GROTTO,
         lambda bundle: (can_use(Items.MEGATON_HAMMER, bundle) | is_child(bundle)) & can_open_bomb_grotto(bundle)),
        (Regions.HF_NEAR_MARKET_GROTTO,
         lambda bundle: any_age_time(bundle, lambda bundle: blast_or_smash(bundle))),
        (Regions.HF_FAIRY_GROTTO,
         lambda bundle: any_age_time(bundle, lambda bundle: blast_or_smash(bundle))),
        (Regions.HF_NEAR_KAK_GROTTO,
         lambda bundle: can_open_bomb_grotto(bundle)),
        (Regions.HF_TEKTITE_GROTTO,
         lambda bundle: can_open_bomb_grotto(bundle)),
    ])

    # HF to Lake Hylia  (upstream RR_HF_TO_LAKE_HYLIA, SCENE_HYRULE_FIELD)
    # Events
    add_events(Regions.HF_TO_LAKE_HYLIA, world, [
        (EventLocations.HF_TO_LAKE_HYLIA_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.HF_TO_LAKE_HYLIA_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
    ])
    # Connections
    connect_regions(Regions.HF_TO_LAKE_HYLIA, world, [
        (Regions.LAKE_HYLIA,
         lambda bundle: True_()),
        (Regions.HYRULE_FIELD,
         lambda bundle: can_climb_ladder(bundle) | summon_epona(bundle)),
    ])

    # HF Southeast Grotto  (upstream RR_HF_SOUTHEAST_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.HF_SOUTHEAST_GROTTO, world, [
        (Locations.HF_SOUTHEAST_GROTTO_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.HF_SOUTHEAST_GROTTO_FISH,
         lambda bundle: has_bottle(bundle)),
        (Locations.HF_SOUTHEAST_GROTTO_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.HF_SOUTHEAST_GROTTO_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_HF_SOUTHEAST_GROTTO_GOSSIP_STONE: true
        (Locations.HF_SOUTHEAST_GROTTO_BEEHIVE_LEFT,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.HF_SOUTHEAST_GROTTO_BEEHIVE_RIGHT,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.HF_SOUTHEAST_GROTTO_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.HF_SOUTHEAST_GROTTO_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.HF_SOUTHEAST_GROTTO_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.HF_SOUTHEAST_GROTTO_GRASS4,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.HF_SOUTHEAST_BOULDER_GROTTO_BUTTERFLY_FAIRY,
         lambda bundle: can_use(Items.STICKS, bundle)),
    ])
    # Connections
    connect_regions(Regions.HF_SOUTHEAST_GROTTO, world, [
        (Regions.HYRULE_FIELD,
         lambda bundle: True_()),
    ])

    # HF Open Grotto  (upstream RR_HF_OPEN_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.HF_OPEN_GROTTO, world, [
        (Locations.HF_OPEN_GROTTO_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.HF_OPEN_GROTTO_FISH,
         lambda bundle: has_bottle(bundle)),
        (Locations.HF_OPEN_GROTTO_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.HF_OPEN_GROTTO_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_HF_OPEN_GROTTO_GOSSIP_STONE: true
        (Locations.HF_OPEN_GROTTO_BEEHIVE_LEFT,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.HF_OPEN_GROTTO_BEEHIVE_RIGHT,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.HF_OPEN_GROTTO_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.HF_OPEN_GROTTO_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.HF_OPEN_GROTTO_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.HF_OPEN_GROTTO_GRASS4,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.HF_OPEN_GROTTO_BUTTERFLY_FAIRY,
         lambda bundle: can_use(Items.STICKS, bundle)),
    ])
    # Connections
    connect_regions(Regions.HF_OPEN_GROTTO, world, [
        (Regions.HYRULE_FIELD,
         lambda bundle: True_()),
    ])

    # HF Inside Fence Grotto  (upstream RR_HF_INSIDE_FENCE_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.HF_INSIDE_FENCE_GROTTO, world, [
        (Locations.HF_DEKU_SCRUB_GROTTO,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.HF_DEKU_SCRUB_GROTTO, bundle)),
        (Locations.HF_DEKU_SCRUB_GROTTO_BEEHIVE,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.HF_FENCE_GROTTO_STORMS_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
    ])
    # Connections
    connect_regions(Regions.HF_INSIDE_FENCE_GROTTO, world, [
        (Regions.HYRULE_FIELD,
         lambda bundle: True_()),
    ])

    # HF Cow Grotto  (upstream RR_HF_COW_GROTTO, SCENE_GROTTOS)
    # Connections
    connect_regions(Regions.HF_COW_GROTTO, world, [
        (Regions.HYRULE_FIELD,
         lambda bundle: True_()),
        (Regions.HF_COW_GROTTO_BEHIND_WEBS,
         lambda bundle: has_fire_source(bundle)),
    ])

    # HF Cow Grotto Behind Webs  (upstream RR_HF_COW_GROTTO_BEHIND_WEBS, SCENE_GROTTOS)
    # Events
    add_events(Regions.HF_COW_GROTTO_BEHIND_WEBS, world, [
        (EventLocations.HF_COW_GROTTO_BEHIND_WEBS_BUG_ACCESS, Events.CAN_ACCESS_BUGS,
         lambda bundle: can_cut_shrubs(bundle)),
        (EventLocations.HF_COW_GROTTO_BEHIND_WEBS_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy(bundle)),
    ])
    # Locations
    add_locations(Regions.HF_COW_GROTTO_BEHIND_WEBS, world, [
        (Locations.HF_GS_COW_GROTTO,
         lambda bundle: can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG)),
        (Locations.HF_COW_GROTTO_COW,
         lambda bundle: can_use(Items.EPONAS_SONG, bundle)),
        (Locations.HF_COW_GROTTO_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.HF_COW_GROTTO_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_HF_COW_GROTTO_GOSSIP_STONE: true
        (Locations.HF_COW_GROTTO_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.HF_COW_GROTTO_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.HF_COW_GROTTO_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.HF_COW_GROTTO_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
    ])
    # Connections
    connect_regions(Regions.HF_COW_GROTTO_BEHIND_WEBS, world, [
        (Regions.HF_COW_GROTTO,
         lambda bundle: True_()),
    ])

    # HF Near Market Grotto  (upstream RR_HF_NEAR_MARKET_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.HF_NEAR_MARKET_GROTTO, world, [
        (Locations.HF_NEAR_MARKET_GROTTO_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.HF_NEAR_MARKET_GROTTO_FISH,
         lambda bundle: has_bottle(bundle)),
        (Locations.HF_NEAR_MARKET_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.HF_NEAR_MARKET_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_HF_NEAR_MARKET_GROTTO_GOSSIP_STONE: true
        (Locations.HF_NEAR_MARKET_GROTTO_BEEHIVE_LEFT,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.HF_NEAR_MARKET_GROTTO_BEEHIVE_RIGHT,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.HF_NEAR_MARKET_GROTTO_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.HF_NEAR_MARKET_GROTTO_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.HF_NEAR_MARKET_GROTTO_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.HF_NEAR_MARKET_GROTTO_GRASS4,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.HF_NEAR_MARKET_GROTTO_BUTTERFLY_FAIRY,
         lambda bundle: can_use(Items.STICKS, bundle)),
    ])
    # Connections
    connect_regions(Regions.HF_NEAR_MARKET_GROTTO, world, [
        (Regions.HYRULE_FIELD,
         lambda bundle: True_()),
    ])

    # HF Fairy Grotto  (upstream RR_HF_FAIRY_GROTTO, SCENE_GROTTOS)
    # Events
    add_events(Regions.HF_FAIRY_GROTTO, world, [
        (EventLocations.HF_FAIRY_GROTTO_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: True_()),
    ])
    # Locations
    add_locations(Regions.HF_FAIRY_GROTTO, world, [
        (Locations.HF_FAIRY_GROTTO_FAIRY1,
         lambda bundle: True_()),
        (Locations.HF_FAIRY_GROTTO_FAIRY2,
         lambda bundle: True_()),
        (Locations.HF_FAIRY_GROTTO_FAIRY3,
         lambda bundle: True_()),
        (Locations.HF_FAIRY_GROTTO_FAIRY4,
         lambda bundle: True_()),
        (Locations.HF_FAIRY_GROTTO_FAIRY5,
         lambda bundle: True_()),
        (Locations.HF_FAIRY_GROTTO_FAIRY6,
         lambda bundle: True_()),
        (Locations.HF_FAIRY_GROTTO_FAIRY7,
         lambda bundle: True_()),
        (Locations.HF_FAIRY_GROTTO_FAIRY8,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.HF_FAIRY_GROTTO, world, [
        (Regions.HYRULE_FIELD,
         lambda bundle: True_()),
    ])

    # HF Near Kak Grotto  (upstream RR_HF_NEAR_KAK_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.HF_NEAR_KAK_GROTTO, world, [
        (Locations.HF_GS_STONE_BRIDGE_TREE_GROTTO,
         lambda bundle: hookshot_or_boomerang(bundle)),
    ])
    # Connections
    connect_regions(Regions.HF_NEAR_KAK_GROTTO, world, [
        (Regions.HYRULE_FIELD,
         lambda bundle: True_()),
    ])

    # HF Tektite Grotto  (upstream RR_HF_TEKTITE_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.HF_TEKTITE_GROTTO, world, [
        (Locations.HF_TEKTITE_GROTTO_FREESTANDING_POH,
         lambda bundle: has_item(Items.GOLDEN_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle)),
    ])
    # Connections
    connect_regions(Regions.HF_TEKTITE_GROTTO, world, [
        (Regions.HYRULE_FIELD,
         lambda bundle: True_()),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_BUGS', 'CAN_ACCESS_FAIRIES', 'CAN_DEFEAT_BIG_POE', 'SOLD_BUNNY_HOOD']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (81): ['RC_HF_SILVER_BOULDER', 'RC_HF_ROCK_1', 'RC_HF_ROCK_2', 'RC_HF_ROCK_3', 'RC_HF_ROCK_4', 'RC_HF_ROCK_5', 'RC_HF_ROCK_6', 'RC_HF_ROCK_7', 'RC_HF_ROCK_8', 'RC_HF_BOULDER_NORTH', 'RC_HF_BOULDER_BY_MARKET', 'RC_HF_BOULDER_SOUTH', 'RC_HF_BRONZE_BOULDER_1', 'RC_HF_BRONZE_BOULDER_2', 'RC_HF_BRONZE_BOULDER_3', 'RC_HF_BRONZE_BOULDER_4', 'RC_HF_BUSH_NEAR_LAKE_1', 'RC_HF_BUSH_NEAR_LAKE_2', 'RC_HF_BUSH_NEAR_LAKE_3', 'RC_HF_BUSH_NEAR_LAKE_4', 'RC_HF_BUSH_NEAR_LAKE_5', 'RC_HF_BUSH_NEAR_LAKE_6', 'RC_HF_BUSH_NEAR_LAKE_7', 'RC_HF_BUSH_NEAR_LAKE_8', 'RC_HF_BUSH_NEAR_LAKE_9', 'RC_HF_BUSH_NEAR_LAKE_10', 'RC_HF_BUSH_NEAR_LAKE_11', 'RC_HF_NORTHERN_BUSH_1', 'RC_HF_NORTHERN_BUSH_2', 'RC_HF_NORTHERN_BUSH_3', 'RC_HF_NORTHERN_BUSH_4', 'RC_HF_NORTHERN_BUSH_5', 'RC_HF_NORTHERN_BUSH_6', 'RC_HF_CHILD_NORTHERN_BUSH_1', 'RC_HF_CHILD_NORTHERN_BUSH_2', 'RC_HF_CHILD_NORTHERN_BUSH_3', 'RC_HF_CHILD_NORTHERN_BUSH_4', 'RC_HF_CHILD_NORTHERN_BUSH_5', 'RC_HF_CHILD_NORTHERN_BUSH_6', 'RC_HF_CHILD_NORTHERN_BUSH_7']
