"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/desert_colossus.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    DESERT_COLOSSUS_CHILD_CAN_PASS_TIME = "Desert Colossus Child Can Pass Time"
    DESERT_COLOSSUS_ADULT_CAN_PASS_TIME = "Desert Colossus Adult Can Pass Time"
    DESERT_COLOSSUS_PLANT_DESERT_COLOSSUS_BEAN = "Desert Colossus Plant Desert Colossus Bean"
    DESERT_COLOSSUS_BUG_ACCESS = "Desert Colossus Bug Access"
    DESERT_COLOSSUS_OASIS_CHILD_CAN_PASS_TIME = "Desert Colossus Oasis Child Can Pass Time"
    DESERT_COLOSSUS_OASIS_ADULT_CAN_PASS_TIME = "Desert Colossus Oasis Adult Can Pass Time"
    DESERT_COLOSSUS_OASIS_FAIRY_ACCESS = "Desert Colossus Oasis Fairy Access"
    DESERT_COLOSSUS_OUTSIDE_TEMPLE_CHILD_CAN_PASS_TIME = "Desert Colossus From Spirit Entryway Child Can Pass Time"
    DESERT_COLOSSUS_OUTSIDE_TEMPLE_ADULT_CAN_PASS_TIME = "Desert Colossus From Spirit Entryway Adult Can Pass Time"


def set_region_rules(world: "SohWorld") -> None:

    # Desert Colossus  (upstream RR_DESERT_COLOSSUS, SCENE_DESERT_COLOSSUS)
    # Events
    add_events(Regions.DESERT_COLOSSUS, world, [
        (EventLocations.DESERT_COLOSSUS_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.DESERT_COLOSSUS_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
        (EventLocations.DESERT_COLOSSUS_PLANT_DESERT_COLOSSUS_BEAN, Events.PLANT_DESERT_COLOSSUS_BEAN,
         lambda bundle: can_plant_bean(bundle, Items.DESERT_COLOSSUS_BEAN_SOUL)),
        (EventLocations.DESERT_COLOSSUS_BUG_ACCESS, Events.CAN_ACCESS_BUGS,
         lambda bundle: has_grab(bundle)),
    ])
    # Locations
    add_locations(Regions.DESERT_COLOSSUS, world, [
        (Locations.COLOSSUS_FREESTANDING_POH,
         lambda bundle: is_adult(bundle) & bean_planted(bundle, Events.PLANT_DESERT_COLOSSUS_BEAN)),
        (Locations.COLOSSUS_GS_BEAN_PATCH,
         lambda bundle: can_spawn_soil_skull(bundle, Items.DESERT_COLOSSUS_BEAN_SOUL) & can_attack(bundle)),
        (Locations.COLOSSUS_GS_TREE,
         lambda bundle: is_adult(bundle) & hookshot_or_boomerang(bundle) & can_get_nighttime_gs(bundle)),
        (Locations.COLOSSUS_GS_HILL,
         lambda bundle: is_adult(bundle) & ((bean_planted(bundle, Events.PLANT_DESERT_COLOSSUS_BEAN) & can_attack(bundle)) | can_use(Items.LONGSHOT, bundle) | (can_do_trick(Tricks.COLOSSUS_GS, bundle) & can_use(Items.HOOKSHOT, bundle))) & can_get_nighttime_gs(bundle)),
        (Locations.COLOSSUS_BEAN_SPROUT_FAIRY1,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_DESERT_COLOSSUS_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.COLOSSUS_BEAN_SPROUT_FAIRY2,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_DESERT_COLOSSUS_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.COLOSSUS_BEAN_SPROUT_FAIRY3,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_DESERT_COLOSSUS_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.COLOSSUS_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.COLOSSUS_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.COLOSSUS_SILVER_BOULDER,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.COLOSSUS_ROCK,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.COLOSSUS_CIRCLE_1_ROCK_1,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.COLOSSUS_CIRCLE_1_ROCK_2,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.COLOSSUS_CIRCLE_1_ROCK_3,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.COLOSSUS_CIRCLE_1_ROCK_4,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.COLOSSUS_CIRCLE_1_ROCK_5,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.COLOSSUS_CIRCLE_1_ROCK_6,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.COLOSSUS_CIRCLE_1_ROCK_7,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.COLOSSUS_CIRCLE_1_ROCK_8,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.COLOSSUS_CIRCLE_2_ROCK_1,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.COLOSSUS_CIRCLE_2_ROCK_2,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.COLOSSUS_CIRCLE_2_ROCK_3,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.COLOSSUS_CIRCLE_2_ROCK_4,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.COLOSSUS_CIRCLE_2_ROCK_5,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.COLOSSUS_CIRCLE_2_ROCK_6,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.COLOSSUS_CIRCLE_2_ROCK_7,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.COLOSSUS_CIRCLE_2_ROCK_8,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.COLOSSUS_WONDER_OASIS_TREE_1,
         lambda bundle: (is_adult(bundle) & can_use(Items.FAIRY_BOW, bundle)) | (is_child(bundle) & can_use(Items.FAIRY_SLINGSHOT, bundle))),
        (Locations.COLOSSUS_WONDER_OASIS_TREE_2,
         lambda bundle: (is_adult(bundle) & can_use(Items.FAIRY_BOW, bundle)) | (is_child(bundle) & can_use(Items.FAIRY_SLINGSHOT, bundle))),
        (Locations.COLOSSUS_WONDER_OASIS_CHILD_TREE,
         lambda bundle: is_child(bundle) & can_use(Items.FAIRY_SLINGSHOT, bundle)),
        (Locations.COLOSSUS_WONDER_GF_TREE_1,
         lambda bundle: (is_adult(bundle) & can_use(Items.FAIRY_BOW, bundle)) | (is_child(bundle) & can_use(Items.FAIRY_SLINGSHOT, bundle))),
        (Locations.COLOSSUS_WONDER_GF_TREE_2,
         lambda bundle: (is_adult(bundle) & can_use(Items.FAIRY_BOW, bundle)) | (is_child(bundle) & can_use(Items.FAIRY_SLINGSHOT, bundle))),
        # DEFERRED RC_COLOSSUS_GOSSIP_STONE: true
    ])
    # Connections
    connect_regions(Regions.DESERT_COLOSSUS, world, [
        (Regions.DESERT_COLOSSUS_OASIS,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | has_bottle(bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Regions.COLOSSUS_GREAT_FAIRY_FOUNTAIN,
         lambda bundle: has_explosives(bundle)),
        (Regions.SPIRIT_TEMPLE_ENTRYWAY,
         lambda bundle: True_()),
        (Regions.WASTELAND_NEAR_COLOSSUS,
         lambda bundle: True_()),
        (Regions.COLOSSUS_GROTTO,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
    ])

    # Desert Colossus Oasis  (upstream RR_DESERT_COLOSSUS_OASIS, SCENE_DESERT_COLOSSUS)
    # Events
    add_events(Regions.DESERT_COLOSSUS_OASIS, world, [
        (EventLocations.DESERT_COLOSSUS_OASIS_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.DESERT_COLOSSUS_OASIS_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
        (EventLocations.DESERT_COLOSSUS_OASIS_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: True_()),
    ])
    # Locations
    add_locations(Regions.DESERT_COLOSSUS_OASIS, world, [
        (Locations.COLOSSUS_OASIS_FAIRY1,
         lambda bundle: True_()),
        (Locations.COLOSSUS_OASIS_FAIRY2,
         lambda bundle: True_()),
        (Locations.COLOSSUS_OASIS_FAIRY3,
         lambda bundle: True_()),
        (Locations.COLOSSUS_OASIS_FAIRY4,
         lambda bundle: True_()),
        (Locations.COLOSSUS_OASIS_FAIRY5,
         lambda bundle: True_()),
        (Locations.COLOSSUS_OASIS_FAIRY6,
         lambda bundle: True_()),
        (Locations.COLOSSUS_OASIS_FAIRY7,
         lambda bundle: True_()),
        (Locations.COLOSSUS_OASIS_FAIRY8,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.DESERT_COLOSSUS_OASIS, world, [
        (Regions.DESERT_COLOSSUS,
         lambda bundle: True_()),
    ])

    # Desert Colossus From Spirit Entryway  (upstream RR_DESERT_COLOSSUS_OUTSIDE_TEMPLE, SCENE_DESERT_COLOSSUS)
    # Events
    add_events(Regions.DESERT_COLOSSUS_OUTSIDE_TEMPLE, world, [
        (EventLocations.DESERT_COLOSSUS_OUTSIDE_TEMPLE_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.DESERT_COLOSSUS_OUTSIDE_TEMPLE_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
    ])
    # Locations
    add_locations(Regions.DESERT_COLOSSUS_OUTSIDE_TEMPLE, world, [
        (Locations.SHEIK_AT_COLOSSUS,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.DESERT_COLOSSUS_OUTSIDE_TEMPLE, world, [
        (Regions.DESERT_COLOSSUS,
         lambda bundle: True_()),
    ])

    # Colossus Great Fairy Fountain  (upstream RR_COLOSSUS_GREAT_FAIRY_FOUNTAIN, SCENE_GREAT_FAIRYS_FOUNTAIN_SPELLS)
    # Locations
    add_locations(Regions.COLOSSUS_GREAT_FAIRY_FOUNTAIN, world, [
        (Locations.COLOSSUS_GREAT_FAIRY_REWARD,
         lambda bundle: can_use(Items.ZELDAS_LULLABY, bundle)),
    ])
    # Connections
    connect_regions(Regions.COLOSSUS_GREAT_FAIRY_FOUNTAIN, world, [
        (Regions.DESERT_COLOSSUS,
         lambda bundle: True_()),
    ])

    # Colossus Grotto  (upstream RR_COLOSSUS_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.COLOSSUS_GROTTO, world, [
        (Locations.COLOSSUS_DEKU_SCRUB_GROTTO_REAR,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.COLOSSUS_DEKU_SCRUB_GROTTO_REAR, bundle)),
        (Locations.COLOSSUS_DEKU_SCRUB_GROTTO_FRONT,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.COLOSSUS_DEKU_SCRUB_GROTTO_FRONT, bundle)),
        (Locations.COLOSSUS_DEKU_SCRUB_GROTTO_BEEHIVE,
         lambda bundle: can_break_upper_beehives(bundle)),
    ])
    # Connections
    connect_regions(Regions.COLOSSUS_GROTTO, world, [
        (Regions.DESERT_COLOSSUS,
         lambda bundle: True_()),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_BUGS', 'CAN_ACCESS_FAIRIES', 'PLANT_DESERT_COLOSSUS_BEAN']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (1): ['RC_COLOSSUS_GOSSIP_STONE']
