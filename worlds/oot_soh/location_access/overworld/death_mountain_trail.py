"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/death_mountain_trail.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    DEATH_MOUNTAIN_TRAIL_CHILD_CAN_PASS_TIME = "Death Mountain Trail Child Can Pass Time"
    DEATH_MOUNTAIN_TRAIL_ADULT_CAN_PASS_TIME = "Death Mountain Trail Adult Can Pass Time"
    DEATH_MOUNTAIN_TRAIL_PLANT_DEATH_MOUNTAIN_TRAIL_BEAN = "Death Mountain Trail Plant Death Mountain Trail Bean"
    DEATH_MOUNTAIN_TRAIL_FAIRY_ACCESS = "Death Mountain Trail Fairy Access"
    DEATH_MOUNTAIN_ROCKFALL_CHILD_CAN_PASS_TIME = "Death Mountain Rockfall Child Can Pass Time"
    DEATH_MOUNTAIN_ROCKFALL_ADULT_CAN_PASS_TIME = "Death Mountain Rockfall Adult Can Pass Time"
    DEATH_MOUNTAIN_SUMMIT_CHILD_CAN_PASS_TIME = "Death Mountain Summit Child Can Pass Time"
    DEATH_MOUNTAIN_SUMMIT_ADULT_CAN_PASS_TIME = "Death Mountain Summit Adult Can Pass Time"
    DEATH_MOUNTAIN_SUMMIT_FAIRY_ACCESS = "Death Mountain Summit Fairy Access"
    DEATH_MOUNTAIN_SUMMIT_BUG_ACCESS = "Death Mountain Summit Bug Access"
    DMT_OWL_FLIGHT_CHILD_CAN_PASS_TIME = "DMT Owl Flight Child Can Pass Time"
    DMT_OWL_FLIGHT_ADULT_CAN_PASS_TIME = "DMT Owl Flight Adult Can Pass Time"


def set_region_rules(world: "SohWorld") -> None:

    # Death Mountain Trail  (upstream RR_DEATH_MOUNTAIN_TRAIL, SCENE_DEATH_MOUNTAIN_TRAIL)
    # Events
    add_events(Regions.DEATH_MOUNTAIN_TRAIL, world, [
        (EventLocations.DEATH_MOUNTAIN_TRAIL_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.DEATH_MOUNTAIN_TRAIL_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
        (EventLocations.DEATH_MOUNTAIN_TRAIL_PLANT_DEATH_MOUNTAIN_TRAIL_BEAN, Events.PLANT_DEATH_MOUNTAIN_TRAIL_BEAN,
         lambda bundle: can_plant_bean(bundle) & (has_explosives(bundle) | has_item(Items.GORONS_BRACELET, bundle))),
        (EventLocations.DEATH_MOUNTAIN_TRAIL_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_TRAIL_BEAN) & can_use(Items.SONG_OF_STORMS, bundle) & (has_explosives(bundle) | has_item(Items.GORONS_BRACELET, bundle))),
    ])
    # Locations
    add_locations(Regions.DEATH_MOUNTAIN_TRAIL, world, [
        (Locations.DMT_CHEST,
         lambda bundle: (blast_or_smash(bundle) | (is_child(bundle) & (can_do_trick(Tricks.DMT_BOMBABLE, bundle) | bunny_hood(bundle)) & has_item(Items.GORONS_BRACELET, bundle))) & has_open_chest(bundle)),
        (Locations.DMT_FREESTANDING_POH,
         lambda bundle: is_adult(bundle) | take_damage(bundle) | can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle)),
        (Locations.DMT_GS_BEAN_PATCH,
         lambda bundle: can_spawn_soil_skull(bundle) & (has_explosives(bundle) | has_item(Items.GORONS_BRACELET, bundle) | (can_do_trick(Tricks.DMT_SOIL_GS, bundle) & (take_damage(bundle) | can_use(Items.HOVER_BOOTS, bundle)) & can_use(Items.BOOMERANG, bundle)))),
        (Locations.DMT_GS_NEAR_KAK,
         lambda bundle: blast_or_smash(bundle) & (has_climb(bundle) | can_use(Items.HOOKSHOT, bundle) | can_use(Items.BOOMERANG, bundle))),
        (Locations.DMT_GS_ABOVE_DODONGOS_CAVERN,
         lambda bundle: is_adult(bundle) & can_get_nighttime_gs(bundle) & ((can_use(Items.MEGATON_HAMMER, bundle) | (can_do_trick(Tricks.ITEM_EXTENSION, bundle) & can_use(Items.HOOKSHOT, bundle)) | (can_do_trick(Tricks.BOULDER_COLLISION, bundle) & can_use(Items.LONGSHOT, bundle)) | (can_do_trick(Tricks.DMT_JS_LOWER_GS, bundle) & can_jump_slash(bundle))) | (((can_do_trick(Tricks.DMT_BEAN_LOWER_GS, bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_TRAIL_BEAN)) | (can_do_trick(Tricks.DMT_HOVERS_LOWER_GS, bundle) & can_use(Items.HOVER_BOOTS, bundle))) & (has_explosives(bundle) | can_use(Items.DINS_FIRE, bundle) | ((can_do_trick(Tricks.BOULDER_COLLISION, bundle) | can_do_trick(Tricks.ITEM_EXTENSION, bundle)) & (can_use(Items.FAIRY_BOW, bundle) | can_use(Items.FAIRY_SLINGSHOT, bundle))) | can_jump_slash(bundle))))),
        (Locations.DMT_BLUE_RUPEE_UNDER_BOULDER,
         lambda bundle: is_child(bundle) & blast_or_smash(bundle)),
        (Locations.DMT_RED_RUPEE_UNDER_BOULDER,
         lambda bundle: is_child(bundle) & blast_or_smash(bundle)),
        (Locations.DMT_BEAN_SPROUT_FAIRY1,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_TRAIL_BEAN) & can_use(Items.SONG_OF_STORMS, bundle) & (has_explosives(bundle) | has_item(Items.GORONS_BRACELET, bundle))),
        (Locations.DMT_BEAN_SPROUT_FAIRY2,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_TRAIL_BEAN) & can_use(Items.SONG_OF_STORMS, bundle) & (has_explosives(bundle) | has_item(Items.GORONS_BRACELET, bundle))),
        (Locations.DMT_BEAN_SPROUT_FAIRY3,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_TRAIL_BEAN) & can_use(Items.SONG_OF_STORMS, bundle) & (has_explosives(bundle) | has_item(Items.GORONS_BRACELET, bundle))),
        (Locations.DMT_FLAG_SUNS_SONG_FAIRY,
         lambda bundle: can_use(Items.SUNS_SONG, bundle)),
        # DEFERRED RC_DMT_ROCK_1: logic->CanBreakRocks()
        # DEFERRED RC_DMT_ROCK_2: logic->CanBreakRocks()
        # DEFERRED RC_DMT_ROCK_3: logic->CanBreakRocks()
        # DEFERRED RC_DMT_ROCK_4: logic->CanBreakRocks()
        # DEFERRED RC_DMT_ROCK_5: logic->CanBreakRocks()
        # DEFERRED RC_DMT_CIRCLE_ROCK_1: logic->CanBreakRocks()
        # DEFERRED RC_DMT_CIRCLE_ROCK_2: logic->CanBreakRocks()
        # DEFERRED RC_DMT_CIRCLE_ROCK_3: logic->CanBreakRocks()
        # DEFERRED RC_DMT_CIRCLE_ROCK_4: logic->CanBreakRocks()
        # DEFERRED RC_DMT_CIRCLE_ROCK_5: logic->CanBreakRocks()
        # DEFERRED RC_DMT_CIRCLE_ROCK_6: logic->CanBreakRocks()
        # DEFERRED RC_DMT_CIRCLE_ROCK_7: logic->CanBreakRocks()
        # DEFERRED RC_DMT_CIRCLE_ROCK_8: logic->CanBreakRocks()
        # DEFERRED RC_DMT_CHILD_BOULDER: logic->IsChild && logic->BlastOrSmash()
        # DEFERRED RC_DMT_BOULDER_1: logic->BlastOrSmash()
        # DEFERRED RC_DMT_BOULDER_2: logic->BlastOrSmash()
        # DEFERRED RC_DMT_BRONZE_BOULDER_1: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_DMT_BRONZE_BOULDER_2: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_DMT_BRONZE_BOULDER_3: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_DMT_BRONZE_BOULDER_4: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_DMT_BRONZE_BOULDER_5: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_DMT_BRONZE_BOULDER_6: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_DMT_BRONZE_BOULDER_7: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_DMT_BRONZE_BOULDER_11: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_DMT_ABOVE_DODONGO_RECTANGLE_SIGN: logic->IsChild && logic->CanRead()
        # DEFERRED RC_DMT_ADULT_CENTER_EXIT_ARROW_SIGN: logic->IsAdult && logic->CanRead()
        # DEFERRED RC_DMT_CHILD_CENTER_EXIT_RECTANGLE_SIGN: logic->IsChild && logic->CanRead()
        # DEFERRED RC_DMT_DODONGOS_CAVERN_RECTANGLE_SIGN: logic->CanRead()
        # DEFERRED RC_DMT_CENTER_TRAIL_RECTANGLE_SIGN: logic->CanRead()
        # DEFERRED RC_DMT_TO_UPPER_TRAIL_ARROW_SIGN: logic->CanRead()
        # DEFERRED RC_DMT_TO_CENTER_EXIT_ARROW_SIGN: logic->CanRead()
        # DEFERRED RC_DMT_LOWER_EXIT_ARROW_SIGN: logic->CanRead()
    ])
    # Connections
    connect_regions(Regions.DEATH_MOUNTAIN_TRAIL, world, [
        (Regions.KAK_BEHIND_GATE,
         lambda bundle: True_()),
        (Regions.GORON_CITY,
         lambda bundle: True_()),
        (Regions.DEATH_MOUNTAIN_ROCKFALL,
         lambda bundle: any_age_time(bundle, lambda bundle: blast_or_smash(bundle)) | (is_adult(bundle) & ((bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_TRAIL_BEAN) & has_item(Items.GORONS_BRACELET, bundle)) | (can_use(Items.HOVER_BOOTS, bundle) & can_do_trick(Tricks.DMT_CLIMB_HOVERS, bundle))))),
        (Regions.DODONGOS_CAVERN_ENTRYWAY,
         lambda bundle: has_explosives(bundle) | has_item(Items.GORONS_BRACELET, bundle) | is_adult(bundle)),
        (Regions.DMT_STORMS_GROTTO,
         lambda bundle: can_open_storms_grotto(bundle)),
    ])

    # Death Mountain Rockfall  (upstream RR_DEATH_MOUNTAIN_ROCKFALL, SCENE_DEATH_MOUNTAIN_TRAIL)
    # Events
    add_events(Regions.DEATH_MOUNTAIN_ROCKFALL, world, [
        (EventLocations.DEATH_MOUNTAIN_ROCKFALL_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.DEATH_MOUNTAIN_ROCKFALL_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
    ])
    # Locations
    add_locations(Regions.DEATH_MOUNTAIN_ROCKFALL, world, [
        (Locations.DMT_GS_FALLING_ROCKS_PATH,
         lambda bundle: is_adult(bundle) & can_get_nighttime_gs(bundle) & (can_use(Items.MEGATON_HAMMER, bundle) | (can_do_trick(Tricks.BOULDER_COLLISION, bundle) & can_use(Items.LONGSHOT, bundle)) | (can_do_trick(Tricks.ITEM_EXTENSION, bundle) & can_use(Items.HOOKSHOT, bundle)) | (can_do_trick(Tricks.DMT_UPPER_GS, bundle) & (can_jump_slash(bundle) | can_use(Items.DINS_FIRE, bundle) | has_explosives(bundle) | (can_do_trick(Tricks.ITEM_EXTENSION, bundle) & can_use(Items.FAIRY_SLINGSHOT, bundle)) | (can_do_trick(Tricks.BOULDER_COLLISION, bundle) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.LONGSHOT)))))),
        # DEFERRED RC_DMT_BRONZE_BOULDER_8: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_DMT_BRONZE_BOULDER_9: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_DMT_BRONZE_BOULDER_10: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_DMT_COW_BOULDER: logic->BlastOrSmash()
    ])
    # Connections
    connect_regions(Regions.DEATH_MOUNTAIN_ROCKFALL, world, [
        (Regions.DEATH_MOUNTAIN_TRAIL,
         lambda bundle: True_()),
        (Regions.DEATH_MOUNTAIN_SUMMIT,
         lambda bundle: has_climb(bundle) & (is_adult(bundle) | can_do_trick(Tricks.DMT_SHIELDLESS_CLIMB, bundle) | has_item(Items.HYLIAN_SHIELD, bundle) | can_use(Items.NAYRUS_LOVE, bundle))),
        (Regions.DMT_COW_GROTTO,
         lambda bundle: any_age_time(bundle, lambda bundle: blast_or_smash(bundle))),
    ])

    # Death Mountain Summit  (upstream RR_DEATH_MOUNTAIN_SUMMIT, SCENE_DEATH_MOUNTAIN_TRAIL)
    # Events
    add_events(Regions.DEATH_MOUNTAIN_SUMMIT, world, [
        (EventLocations.DEATH_MOUNTAIN_SUMMIT_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.DEATH_MOUNTAIN_SUMMIT_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
        (EventLocations.DEATH_MOUNTAIN_SUMMIT_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy(bundle)),
        (EventLocations.DEATH_MOUNTAIN_SUMMIT_BUG_ACCESS, Events.CAN_ACCESS_BUGS,
         lambda bundle: is_child(bundle) & has_grab(bundle)),
    ])
    # Locations
    add_locations(Regions.DEATH_MOUNTAIN_SUMMIT, world, [
        (Locations.DMT_TRADE_BROKEN_SWORD,
         lambda bundle: is_adult(bundle) & can_use(Items.BROKEN_GORONS_SWORD, bundle)),
        (Locations.DMT_TRADE_EYEDROPS,
         lambda bundle: is_adult(bundle) & can_use(Items.WORLDS_FINEST_EYEDROPS, bundle)),
        (Locations.DMT_TRADE_CLAIM_CHECK,
         lambda bundle: is_adult(bundle) & can_use(Items.CLAIM_CHECK, bundle)),
        (Locations.DMT_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.DMT_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_DMT_SUMMIT_ROCK: logic->IsChild && logic->CanBreakRocks()
        # DEFERRED RC_DMT_GOSSIP_STONE: true
        # DEFERRED RC_BIGGORON_HINT: logic->IsAdult && logic->HasItem(RG_SPEAK_GORON)
        # DEFERRED RC_DMT_UPPER_EXIT_ARROW_SIGN: logic->CanRead()
    ])
    # Connections
    connect_regions(Regions.DEATH_MOUNTAIN_SUMMIT, world, [
        (Regions.DEATH_MOUNTAIN_ROCKFALL,
         lambda bundle: True_()),
        (Regions.DMC_UPPER_ENTRY,
         lambda bundle: True_()),
        (Regions.DMT_OWL_FLIGHT,
         lambda bundle: is_child(bundle) & (has_speak(bundle, "DEKU") | has_speak(bundle, "GERUDO") | has_speak(bundle, "GORON") | has_speak(bundle, "KOKIRI") | has_speak(bundle, "HYLIAN") | has_speak(bundle, "ZORA"))),
        (Regions.DMT_GREAT_FAIRY_FOUNTAIN,
         lambda bundle: any_age_time(bundle, lambda bundle: blast_or_smash(bundle))),
    ])

    # DMT Owl Flight  (upstream RR_DMT_OWL_FLIGHT, SCENE_DEATH_MOUNTAIN_TRAIL)
    # Events
    add_events(Regions.DMT_OWL_FLIGHT, world, [
        (EventLocations.DMT_OWL_FLIGHT_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.DMT_OWL_FLIGHT_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
    ])
    # Connections
    connect_regions(Regions.DMT_OWL_FLIGHT, world, [
        (Regions.KAK_IMPAS_ROOFTOP,
         lambda bundle: True_()),
    ])

    # DMT Cow Grotto  (upstream RR_DMT_COW_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.DMT_COW_GROTTO, world, [
        (Locations.DMT_COW_GROTTO_COW,
         lambda bundle: can_use(Items.EPONAS_SONG, bundle)),
        (Locations.DMT_COW_GROTTO_BEEHIVE,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.DMT_COW_GROTTO_LEFT_HEART,
         lambda bundle: True_()),
        (Locations.DMT_COW_GROTTO_MIDDLE_LEFT_HEART,
         lambda bundle: True_()),
        (Locations.DMT_COW_GROTTO_MIDDLE_RIGHT_HEART,
         lambda bundle: True_()),
        (Locations.DMT_COW_GROTTO_RIGHT_HEART,
         lambda bundle: True_()),
        (Locations.DMT_COW_GROTTO_RUPEE1,
         lambda bundle: True_()),
        (Locations.DMT_COW_GROTTO_RUPEE2,
         lambda bundle: True_()),
        (Locations.DMT_COW_GROTTO_RUPEE3,
         lambda bundle: True_()),
        (Locations.DMT_COW_GROTTO_RUPEE4,
         lambda bundle: True_()),
        (Locations.DMT_COW_GROTTO_RUPEE5,
         lambda bundle: True_()),
        (Locations.DMT_COW_GROTTO_RUPEE6,
         lambda bundle: True_()),
        (Locations.DMT_COW_GROTTO_RED_RUPEE,
         lambda bundle: True_()),
        (Locations.DMT_COW_GROTTO_SONG_OF_STORMS_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.DMT_COW_GROTTO_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DMT_COW_GROTTO_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
    ])
    # Connections
    connect_regions(Regions.DMT_COW_GROTTO, world, [
        (Regions.DEATH_MOUNTAIN_ROCKFALL,
         lambda bundle: True_()),
    ])

    # DMT Storms Grotto  (upstream RR_DMT_STORMS_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.DMT_STORMS_GROTTO, world, [
        (Locations.DMT_STORMS_GROTTO_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.DMT_STORMS_GROTTO_FISH,
         lambda bundle: has_bottle(bundle)),
        (Locations.DMT_STORMS_GROTTO_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.DMT_STORMS_GROTTO_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_DMT_STORMS_GROTTO_GOSSIP_STONE: true
        (Locations.DMT_STORMS_GROTTO_BEEHIVE_LEFT,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.DMT_STORMS_GROTTO_BEEHIVE_RIGHT,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.DMT_STORMS_GROTTO_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DMT_STORMS_GROTTO_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DMT_STORMS_GROTTO_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DMT_STORMS_GROTTO_GRASS4,
         lambda bundle: can_cut_shrubs(bundle)),
        # DEFERRED RC_DMT_STORMS_GROTTO_BUTTERFLY_FAIRY: logic->CanUse(RG_STICKS)
    ])
    # Connections
    connect_regions(Regions.DMT_STORMS_GROTTO, world, [
        (Regions.DEATH_MOUNTAIN_TRAIL,
         lambda bundle: True_()),
    ])

    # DMT Great Fairy Fountain  (upstream RR_DMT_GREAT_FAIRY_FOUNTAIN, SCENE_GREAT_FAIRYS_FOUNTAIN_MAGIC)
    # Locations
    add_locations(Regions.DMT_GREAT_FAIRY_FOUNTAIN, world, [
        (Locations.DMT_GREAT_FAIRY_REWARD,
         lambda bundle: can_use(Items.ZELDAS_LULLABY, bundle)),
    ])
    # Connections
    connect_regions(Regions.DMT_GREAT_FAIRY_FOUNTAIN, world, [
        (Regions.DEATH_MOUNTAIN_SUMMIT,
         lambda bundle: True_()),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_BUGS', 'CAN_ACCESS_FAIRIES', 'PLANT_DEATH_MOUNTAIN_TRAIL_BEAN']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (42): ['RC_DMT_ROCK_1', 'RC_DMT_ROCK_2', 'RC_DMT_ROCK_3', 'RC_DMT_ROCK_4', 'RC_DMT_ROCK_5', 'RC_DMT_CIRCLE_ROCK_1', 'RC_DMT_CIRCLE_ROCK_2', 'RC_DMT_CIRCLE_ROCK_3', 'RC_DMT_CIRCLE_ROCK_4', 'RC_DMT_CIRCLE_ROCK_5', 'RC_DMT_CIRCLE_ROCK_6', 'RC_DMT_CIRCLE_ROCK_7', 'RC_DMT_CIRCLE_ROCK_8', 'RC_DMT_CHILD_BOULDER', 'RC_DMT_BOULDER_1', 'RC_DMT_BOULDER_2', 'RC_DMT_BRONZE_BOULDER_1', 'RC_DMT_BRONZE_BOULDER_2', 'RC_DMT_BRONZE_BOULDER_3', 'RC_DMT_BRONZE_BOULDER_4', 'RC_DMT_BRONZE_BOULDER_5', 'RC_DMT_BRONZE_BOULDER_6', 'RC_DMT_BRONZE_BOULDER_7', 'RC_DMT_BRONZE_BOULDER_11', 'RC_DMT_ABOVE_DODONGO_RECTANGLE_SIGN', 'RC_DMT_ADULT_CENTER_EXIT_ARROW_SIGN', 'RC_DMT_CHILD_CENTER_EXIT_RECTANGLE_SIGN', 'RC_DMT_DODONGOS_CAVERN_RECTANGLE_SIGN', 'RC_DMT_CENTER_TRAIL_RECTANGLE_SIGN', 'RC_DMT_TO_UPPER_TRAIL_ARROW_SIGN', 'RC_DMT_TO_CENTER_EXIT_ARROW_SIGN', 'RC_DMT_LOWER_EXIT_ARROW_SIGN', 'RC_DMT_BRONZE_BOULDER_8', 'RC_DMT_BRONZE_BOULDER_9', 'RC_DMT_BRONZE_BOULDER_10', 'RC_DMT_COW_BOULDER', 'RC_DMT_SUMMIT_ROCK', 'RC_DMT_GOSSIP_STONE', 'RC_BIGGORON_HINT', 'RC_DMT_UPPER_EXIT_ARROW_SIGN']
