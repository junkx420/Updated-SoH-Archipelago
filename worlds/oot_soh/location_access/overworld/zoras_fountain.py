"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/zoras_fountain.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    ZORAS_FOUNTAIN_FAIRY_ACCESS = "Zoras Fountain Fairy Access"


def set_region_rules(world: "SohWorld") -> None:

    # Zoras Fountain  (upstream RR_ZORAS_FOUNTAIN, SCENE_ZORAS_FOUNTAIN)
    # Events
    add_events(Regions.ZORAS_FOUNTAIN, world, [
        (EventLocations.ZORAS_FOUNTAIN_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy_except_suns(bundle) | (can_use(Items.STICKS, bundle) & at_day(bundle))),
    ])
    # Locations
    add_locations(Regions.ZORAS_FOUNTAIN, world, [
        (Locations.ZF_GS_TREE,
         lambda bundle: is_child(bundle) & can_bonk_trees(bundle) & (has_grab(bundle) | can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA))),
        (Locations.ZF_GS_ABOVE_THE_LOG,
         lambda bundle: is_child(bundle) & hookshot_or_boomerang(bundle) & can_get_nighttime_gs(bundle)),
        (Locations.ZF_FAIRY_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
        (Locations.ZF_FAIRY_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.ZF_JABU_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
        (Locations.ZF_JABU_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_ZF_FAIRY_GOSSIP_STONE: true
        # DEFERRED RC_ZF_JABU_GOSSIP_STONE: true
        (Locations.ZF_NEAR_JABU_POT1,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.ZF_NEAR_JABU_POT2,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.ZF_NEAR_JABU_POT3,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.ZF_NEAR_JABU_POT4,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        # DEFERRED RC_ZF_BOULDER: logic->BlastOrSmash()
        # DEFERRED RC_ZF_SILVER_BOULDER: logic->CanUse(RG_SILVER_GAUNTLETS)
        # DEFERRED RC_ZF_UNDERGROUND_BOULDER: logic->CanUse(RG_SILVER_GAUNTLETS) && logic->BlastOrSmash()
        (Locations.ZF_TREE,
         lambda bundle: is_child(bundle) & can_bonk_trees(bundle)),
        # DEFERRED RC_ZF_BUSH_1: logic->IsChild
        # DEFERRED RC_ZF_BUSH_2: logic->IsChild
        # DEFERRED RC_ZF_BUSH_3: logic->IsChild
        # DEFERRED RC_ZF_BUSH_4: logic->IsChild
        # DEFERRED RC_ZF_BUSH_5: logic->IsChild
        # DEFERRED RC_ZF_BUSH_6: logic->IsChild
        # DEFERRED RC_ZF_LOG_BUTTERFLY_FAIRY: logic->IsChild && logic->AtDay && logic->CanUse(RG_STICKS)
        # DEFERRED RC_ZF_JABU_JABU_PLATFORM_RECTANGLE_SIGN: logic->IsChild && logic->CanRead()
        # DEFERRED RC_ZF_ENTRANCE_ARROW_SIGN: logic->CanRead()
        # DEFERRED RC_ZF_WONDER_ROCK: logic->IsAdult && logic->ReachScarecrow()
    ])
    # Connections
    connect_regions(Regions.ZORAS_FOUNTAIN, world, [
        (Regions.ZD_BEHIND_KING_ZORA,
         lambda bundle: True_()),
        (Regions.ZF_ICEBERGS,
         lambda bundle: is_adult(bundle)),
        (Regions.ZF_LAKEBED,
         lambda bundle: can_use(Items.IRON_BOOTS, bundle)),
        (Regions.ZF_HIDDEN_CAVE,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle) & blast_or_smash(bundle)),
        (Regions.ZF_ROCK,
         lambda bundle: is_adult(bundle) & reach_scarecrow(bundle)),
        (Regions.JABU_JABUS_BELLY_ENTRYWAY,
         lambda bundle: is_child(bundle) & (True_(options=[OptionFilter(JabuJabu, JabuJabu.option_open)]) | can_use(Items.BOTTLE_WITH_FISH, bundle))),
        (Regions.ZF_GREAT_FAIRY_FOUNTAIN,
         lambda bundle: has_explosives(bundle) | (can_do_trick(Tricks.ZF_GREAT_FAIRY_WITHOUT_EXPLOSIVES, bundle) & can_use(Items.MEGATON_HAMMER, bundle) & can_use(Items.SILVER_GAUNTLETS, bundle))),
    ])

    # ZF Icebergs  (upstream RR_ZF_ICEBERGS, SCENE_ZORAS_FOUNTAIN)
    # Locations
    add_locations(Regions.ZF_ICEBERGS, world, [
        (Locations.ZF_ICEBERG_FREESTANDING_POH,
         lambda bundle: is_adult(bundle)),
    ])
    # Connections
    connect_regions(Regions.ZF_ICEBERGS, world, [
        (Regions.ZORAS_FOUNTAIN,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.HOVER_BOOTS, bundle)),
        (Regions.ZF_LAKEBED,
         lambda bundle: can_use(Items.IRON_BOOTS, bundle)),
        (Regions.ZF_LEDGE,
         lambda bundle: True_()),
    ])

    # ZF Lakebed  (upstream RR_ZF_LAKEBED, SCENE_ZORAS_FOUNTAIN)
    # Locations
    add_locations(Regions.ZF_LAKEBED, world, [
        (Locations.ZF_BOTTOM_FREESTANDING_POH,
         lambda bundle: is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
        (Locations.ZF_BOTTOM_NORTH_INNER_RUPEE,
         lambda bundle: is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
        (Locations.ZF_BOTTOM_NORTHEAST_INNER_RUPEE,
         lambda bundle: is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
        (Locations.ZF_BOTTOM_SOUTHEAST_INNER_RUPEE,
         lambda bundle: is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
        (Locations.ZF_BOTTOM_SOUTH_INNER_RUPEE,
         lambda bundle: is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
        (Locations.ZF_BOTTOM_SOUTHWEST_INNER_RUPEE,
         lambda bundle: is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
        (Locations.ZF_BOTTOM_NORTHWEST_INNER_RUPEE,
         lambda bundle: is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
        (Locations.ZF_BOTTOM_NORTH_MIDDLE_RUPEE,
         lambda bundle: is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
        (Locations.ZF_BOTTOM_NORTHEAST_MIDDLE_RUPEE,
         lambda bundle: is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
        (Locations.ZF_BOTTOM_SOUTHEAST_MIDDLE_RUPEE,
         lambda bundle: is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
        (Locations.ZF_BOTTOM_SOUTH_MIDDLE_RUPEE,
         lambda bundle: is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
        (Locations.ZF_BOTTOM_SOUTHWEST_MIDDLE_RUPEE,
         lambda bundle: is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
        (Locations.ZF_BOTTOM_NORTHWEST_MIDDLE_RUPEE,
         lambda bundle: is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
        (Locations.ZF_BOTTOM_NORTH_OUTER_RUPEE,
         lambda bundle: is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
        (Locations.ZF_BOTTOM_NORTHEAST_OUTER_RUPEE,
         lambda bundle: is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
        (Locations.ZF_BOTTOM_SOUTHEAST_OUTER_RUPEE,
         lambda bundle: is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
        (Locations.ZF_BOTTOM_SOUTH_OUTER_RUPEE,
         lambda bundle: is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
        (Locations.ZF_BOTTOM_SOUTHWEST_OUTER_RUPEE,
         lambda bundle: is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
        (Locations.ZF_BOTTOM_NORTHWEST_OUTER_RUPEE,
         lambda bundle: is_adult(bundle) & can_use(Items.IRON_BOOTS, bundle) & water_timer_at_least(bundle, 16)),
    ])
    # Connections
    connect_regions(Regions.ZF_LAKEBED, world, [
        (Regions.ZORAS_FOUNTAIN,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle)),
    ])

    # ZF Ledge  (upstream RR_ZF_LEDGE, SCENE_ZORAS_FOUNTAIN)
    # Connections
    connect_regions(Regions.ZF_LEDGE, world, [
        (Regions.ZORAS_FOUNTAIN,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle)),
        (Regions.ZF_ICEBERGS,
         lambda bundle: is_adult(bundle)),
        (Regions.ZF_LAKEBED,
         lambda bundle: can_use(Items.IRON_BOOTS, bundle)),
        (Regions.ICE_CAVERN_ENTRYWAY,
         lambda bundle: True_()),
    ])

    # ZF Hidden Cave  (upstream RR_ZF_HIDDEN_CAVE, SCENE_ZORAS_FOUNTAIN)
    # Locations
    add_locations(Regions.ZF_HIDDEN_CAVE, world, [
        (Locations.ZF_HIDDEN_CAVE_POT1,
         lambda bundle: is_adult(bundle) & can_break_pots(bundle)),
        (Locations.ZF_HIDDEN_CAVE_POT2,
         lambda bundle: is_adult(bundle) & can_break_pots(bundle)),
        (Locations.ZF_HIDDEN_CAVE_POT3,
         lambda bundle: is_adult(bundle) & can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.ZF_HIDDEN_CAVE, world, [
        (Regions.ZF_HIDDEN_LEDGE,
         lambda bundle: has_climb(bundle) | can_use(Items.LONGSHOT, bundle)),
    ])

    # ZF Hidden Ledge  (upstream RR_ZF_HIDDEN_LEDGE, SCENE_ZORAS_FOUNTAIN)
    # Locations
    add_locations(Regions.ZF_HIDDEN_LEDGE, world, [
        (Locations.ZF_GS_HIDDEN_CAVE,
         lambda bundle: is_adult(bundle) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOMB_THROW) & can_get_nighttime_gs(bundle)),
    ])
    # Connections
    connect_regions(Regions.ZF_HIDDEN_LEDGE, world, [
        (Regions.ZORAS_FOUNTAIN,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | take_damage(bundle)),
        (Regions.ZF_HIDDEN_CAVE,
         lambda bundle: True_()),
    ])

    # ZF Rock  (upstream RR_ZF_ROCK, SCENE_ZORAS_FOUNTAIN)
    # Connections
    connect_regions(Regions.ZF_ROCK, world, [
        (Regions.ZORAS_FOUNTAIN,
         lambda bundle: True_()),
    ])

    # ZF Great Fairy Fountain  (upstream RR_ZF_GREAT_FAIRY_FOUNTAIN, SCENE_GREAT_FAIRYS_FOUNTAIN_SPELLS)
    # Locations
    add_locations(Regions.ZF_GREAT_FAIRY_FOUNTAIN, world, [
        (Locations.ZF_GREAT_FAIRY_REWARD,
         lambda bundle: can_use(Items.ZELDAS_LULLABY, bundle)),
    ])
    # Connections
    connect_regions(Regions.ZF_GREAT_FAIRY_FOUNTAIN, world, [
        (Regions.ZORAS_FOUNTAIN,
         lambda bundle: True_()),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_FAIRIES']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (15): ['RC_ZF_FAIRY_GOSSIP_STONE', 'RC_ZF_JABU_GOSSIP_STONE', 'RC_ZF_BOULDER', 'RC_ZF_SILVER_BOULDER', 'RC_ZF_UNDERGROUND_BOULDER', 'RC_ZF_BUSH_1', 'RC_ZF_BUSH_2', 'RC_ZF_BUSH_3', 'RC_ZF_BUSH_4', 'RC_ZF_BUSH_5', 'RC_ZF_BUSH_6', 'RC_ZF_LOG_BUTTERFLY_FAIRY', 'RC_ZF_JABU_JABU_PLATFORM_RECTANGLE_SIGN', 'RC_ZF_ENTRANCE_ARROW_SIGN', 'RC_ZF_WONDER_ROCK']
