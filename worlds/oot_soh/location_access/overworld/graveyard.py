"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/graveyard.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    THE_GRAVEYARD_PLANT_GRAVEYARD_BEAN = "The Graveyard Plant Graveyard Bean"
    THE_GRAVEYARD_FAIRY_ACCESS = "The Graveyard Fairy Access"
    THE_GRAVEYARD_BUG_ACCESS = "The Graveyard Bug Access"
    THE_GRAVEYARD_SOLD_SPOOKY_MASK = "The Graveyard Sold Spooky Mask"
    GRAVEYARD_DAMPES_GRAVE_NUT_ACCESS = "Graveyard Dampes Grave Nut Access"
    GRAVEYARD_WARP_PAD_REGION_FAIRY_ACCESS = "Graveyard Warp Pad Region Fairy Access"


def set_region_rules(world: "SohWorld") -> None:

    # The Graveyard  (upstream RR_THE_GRAVEYARD, SCENE_GRAVEYARD)
    # Events
    add_events(Regions.THE_GRAVEYARD, world, [
        (EventLocations.THE_GRAVEYARD_PLANT_GRAVEYARD_BEAN, Events.PLANT_GRAVEYARD_BEAN,
         lambda bundle: can_plant_bean(bundle)),
        (EventLocations.THE_GRAVEYARD_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: (at_day(bundle) & can_use(Items.STICKS, bundle)) | (is_child(bundle) & bean_planted(bundle, Events.PLANT_GRAVEYARD_BEAN) & can_use(Items.SONG_OF_STORMS, bundle))),
        (EventLocations.THE_GRAVEYARD_BUG_ACCESS, Events.CAN_ACCESS_BUGS,
         lambda bundle: has_grab(bundle)),
        (EventLocations.THE_GRAVEYARD_SOLD_SPOOKY_MASK, Events.SOLD_SPOOKY_MASK,
         lambda bundle: is_child(bundle) & at_day(bundle) & has_mask(bundle, "SPOOKY_MASK") & has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN")),
    ])
    # Locations
    add_locations(Regions.THE_GRAVEYARD, world, [
        (Locations.GRAVEYARD_FREESTANDING_POH,
         lambda bundle: (((is_adult(bundle) & bean_planted(bundle, Events.PLANT_GRAVEYARD_BEAN)) | can_use(Items.LONGSHOT, bundle)) & can_break_crates(bundle)) | (can_do_trick(Tricks.GY_POH, bundle) & can_use(Items.BOOMERANG, bundle))),
        (Locations.GRAVEYARD_DAMPE_GRAVEDIGGING_TOUR,
         lambda bundle: has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN") & is_child(bundle) & at_night(bundle)),
        (Locations.GRAVEYARD_GS_WALL,
         lambda bundle: is_child(bundle) & hookshot_or_boomerang(bundle) & at_night(bundle) & can_get_nighttime_gs(bundle)),
        (Locations.GRAVEYARD_GS_BEAN_PATCH,
         lambda bundle: can_spawn_soil_skull(bundle) & can_attack(bundle)),
        (Locations.GRAVEYARD_BEAN_SPROUT_FAIRY1,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_GRAVEYARD_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.GRAVEYARD_BEAN_SPROUT_FAIRY2,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_GRAVEYARD_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.GRAVEYARD_BEAN_SPROUT_FAIRY3,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_GRAVEYARD_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.GRAVEYARD_GRASS_1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.GRAVEYARD_GRASS_2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.GRAVEYARD_GRASS_3,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.GRAVEYARD_GRASS_4,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.GRAVEYARD_GRASS_5,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.GRAVEYARD_GRASS_6,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.GRAVEYARD_GRASS_7,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.GRAVEYARD_GRASS_8,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.GRAVEYARD_GRASS_9,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.GRAVEYARD_GRASS_10,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.GRAVEYARD_GRASS_11,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.GRAVEYARD_GRASS_12,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.GRAVEYARD_FREESTANDING_POH_CRATE,
         lambda bundle: ((is_adult(bundle) & bean_planted(bundle, Events.PLANT_GRAVEYARD_BEAN)) | can_use(Items.LONGSHOT, bundle)) & can_break_crates(bundle)),
        # DEFERRED RC_GY_ROCK: logic->CanBreakRocks()
        (Locations.GRAVEYARD_GRAVE_BUTTERFLY_FAIRY,
         lambda bundle: is_child(bundle) & at_day(bundle) & can_use(Items.STICKS, bundle)),
        # DEFERRED RC_GY_ENTRANCE_RECTANGLE_SIGN: logic->CanRead()
        # DEFERRED RC_GY_ENTRANCE_PLINTH: logic->CanRead()
        # DEFERRED RC_GY_RIGHT_OF_ROYAL_TOMB_GRAVE: logic->CanRead()
        # DEFERRED RC_GY_LEFT_OF_ROYAL_TOMB_GRAVE: logic->CanRead()
        # DEFERRED RC_GY_ROYAL_TOMB_GRAVE: logic->CanRead() || logic->CanUse(RG_ZELDAS_LULLABY)
    ])
    # Connections
    connect_regions(Regions.THE_GRAVEYARD, world, [
        (Regions.GRAVEYARD_SHIELD_GRAVE,
         lambda bundle: (is_adult(bundle) | at_night(bundle)) & has_grab(bundle)),
        (Regions.GRAVEYARD_COMPOSERS_GRAVE,
         lambda bundle: can_use(Items.ZELDAS_LULLABY, bundle)),
        (Regions.GRAVEYARD_HEART_PIECE_GRAVE,
         lambda bundle: (is_adult(bundle) | at_night(bundle)) & has_grab(bundle)),
        (Regions.GRAVEYARD_DAMPES_GRAVE,
         lambda bundle: is_adult(bundle) & has_grab(bundle)),
        (Regions.GRAVEYARD_DAMPES_HOUSE,
         lambda bundle: is_adult(bundle) & has_item(Items.DAMPES_HUT_KEY, bundle)),
        (Regions.KAKARIKO_VILLAGE,
         lambda bundle: True_()),
        (Regions.GRAVEYARD_WARP_PAD_REGION,
         lambda bundle: False_()),
    ])

    # Graveyard Shield Grave  (upstream RR_GRAVEYARD_SHIELD_GRAVE, SCENE_GRAVE_WITH_FAIRYS_FOUNTAIN)
    # Locations
    add_locations(Regions.GRAVEYARD_SHIELD_GRAVE, world, [
        (Locations.GRAVEYARD_SHIELD_GRAVE_CHEST,
         lambda bundle: has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.GRAVEYARD_SHIELD_GRAVE, world, [
        (Regions.THE_GRAVEYARD,
         lambda bundle: True_()),
        (Regions.GRAVEYARD_SHIELD_GRAVE_BACK,
         lambda bundle: any_age_time(bundle, lambda bundle: can_break_mud_walls(bundle))),
    ])

    # Graveyard Shield Grave Back  (upstream RR_GRAVEYARD_SHIELD_GRAVE_BACK, SCENE_GRAVE_WITH_FAIRYS_FOUNTAIN)
    # Locations
    add_locations(Regions.GRAVEYARD_SHIELD_GRAVE_BACK, world, [
        (Locations.GRAVEYARD_SHIELD_GRAVE_FAIRY1,
         lambda bundle: True_()),
        (Locations.GRAVEYARD_SHIELD_GRAVE_FAIRY2,
         lambda bundle: True_()),
        (Locations.GRAVEYARD_SHIELD_GRAVE_FAIRY3,
         lambda bundle: True_()),
        (Locations.GRAVEYARD_SHIELD_GRAVE_FAIRY4,
         lambda bundle: True_()),
        (Locations.GRAVEYARD_SHIELD_GRAVE_FAIRY5,
         lambda bundle: True_()),
        (Locations.GRAVEYARD_SHIELD_GRAVE_FAIRY6,
         lambda bundle: True_()),
        (Locations.GRAVEYARD_SHIELD_GRAVE_FAIRY7,
         lambda bundle: True_()),
        (Locations.GRAVEYARD_SHIELD_GRAVE_FAIRY8,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.GRAVEYARD_SHIELD_GRAVE_BACK, world, [
        (Regions.GRAVEYARD_SHIELD_GRAVE,
         lambda bundle: True_()),
    ])

    # Graveyard Heart Piece Grave  (upstream RR_GRAVEYARD_HEART_PIECE_GRAVE, SCENE_REDEAD_GRAVE)
    # Locations
    add_locations(Regions.GRAVEYARD_HEART_PIECE_GRAVE, world, [
        (Locations.GRAVEYARD_HEART_PIECE_GRAVE_CHEST,
         lambda bundle: can_use(Items.SUNS_SONG, bundle) & can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.GRAVEYARD_HEART_PIECE_GRAVE, world, [
        (Regions.THE_GRAVEYARD,
         lambda bundle: True_()),
    ])

    # Graveyard Composers Grave  (upstream RR_GRAVEYARD_COMPOSERS_GRAVE, SCENE_ROYAL_FAMILYS_TOMB)
    # Locations
    add_locations(Regions.GRAVEYARD_COMPOSERS_GRAVE, world, [
        (Locations.GRAVEYARD_ROYAL_FAMILYS_TOMB_CHEST,
         lambda bundle: has_fire_source(bundle) & has_open_chest(bundle)),
        (Locations.SONG_FROM_ROYAL_FAMILYS_TOMB,
         lambda bundle: can_use_projectile(bundle) | can_jump_slash(bundle)),
        (Locations.GRAVEYARD_ROYAL_FAMILYS_TOMB_SUNS_SONG_FAIRY,
         lambda bundle: can_use(Items.SUNS_SONG, bundle)),
    ])
    # Connections
    connect_regions(Regions.GRAVEYARD_COMPOSERS_GRAVE, world, [
        (Regions.THE_GRAVEYARD,
         lambda bundle: True_()),
    ])

    # Graveyard Dampes Grave  (upstream RR_GRAVEYARD_DAMPES_GRAVE, SCENE_WINDMILL_AND_DAMPES_GRAVE)
    # Events
    add_events(Regions.GRAVEYARD_DAMPES_GRAVE, world, [
        (EventLocations.GRAVEYARD_DAMPES_GRAVE_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Locations
    add_locations(Regions.GRAVEYARD_DAMPES_GRAVE, world, [
        (Locations.GRAVEYARD_HOOKSHOT_CHEST,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_open_large_chest(bundle)),
        (Locations.GRAVEYARD_DAMPE_RACE_FREESTANDING_POH,
         lambda bundle: (is_adult(bundle) | can_do_trick(Tricks.GY_CHILD_DAMPE_RACE_POH, bundle) | bunny_hood(bundle)) & has_speak(bundle, "HYLIAN")),
        (Locations.GRAVEYARD_DAMPES_GRAVE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GRAVEYARD_DAMPES_GRAVE_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GRAVEYARD_DAMPES_GRAVE_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GRAVEYARD_DAMPES_GRAVE_POT4,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GRAVEYARD_DAMPES_GRAVE_POT5,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GRAVEYARD_DAMPES_GRAVE_POT6,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GRAVEYARD_DAMPES_GRAVE_RUPEE1,
         lambda bundle: True_()),
        (Locations.GRAVEYARD_DAMPES_GRAVE_RUPEE2,
         lambda bundle: True_()),
        (Locations.GRAVEYARD_DAMPES_GRAVE_RUPEE3,
         lambda bundle: True_()),
        (Locations.GRAVEYARD_DAMPES_GRAVE_RUPEE4,
         lambda bundle: True_()),
        (Locations.GRAVEYARD_DAMPES_GRAVE_RUPEE5,
         lambda bundle: True_()),
        (Locations.GRAVEYARD_DAMPES_GRAVE_RUPEE6,
         lambda bundle: True_()),
        (Locations.GRAVEYARD_DAMPES_GRAVE_RUPEE7,
         lambda bundle: True_()),
        (Locations.GRAVEYARD_DAMPES_GRAVE_RUPEE8,
         lambda bundle: True_()),
        # DEFERRED RC_GY_WONDER_DAMPE_RACE_1: true
        # DEFERRED RC_GY_WONDER_DAMPE_RACE_2: true
        # DEFERRED RC_GY_WONDER_DAMPE_RACE_3: true
        # DEFERRED RC_GY_WONDER_DAMPE_RACE_4: true
        # DEFERRED RC_GY_WONDER_DAMPE_RACE_5: true
        # DEFERRED RC_GY_WONDER_DAMPE_RACE_6: true
        # DEFERRED RC_GY_WONDER_DAMPE_RACE_7: true
        # DEFERRED RC_GY_WONDER_DAMPE_RACE_8: true
        # DEFERRED RC_GY_WONDER_DAMPE_RACE_9: true
        # DEFERRED RC_GY_WONDER_DAMPE_RACE_10: true
        # DEFERRED RC_GY_WONDER_DAMPE_RACE_11: true
        # DEFERRED RC_GY_WONDER_DAMPE_RACE_12: true
        # DEFERRED RC_GY_WONDER_DAMPE_RACE_13: true
        # DEFERRED RC_GY_WONDER_DAMPE_RACE_14: true
        # DEFERRED RC_GY_WONDER_DAMPE_RACE_15: true
    ])
    # Connections
    connect_regions(Regions.GRAVEYARD_DAMPES_GRAVE, world, [
        (Regions.THE_GRAVEYARD,
         lambda bundle: True_()),
        (Regions.KAK_WINDMILL_UPPER,
         lambda bundle: (is_adult(bundle) & can_use(Items.SONG_OF_TIME, bundle)) | (is_child(bundle) & can_ground_jump(bundle))),
    ])

    # Graveyard Dampes House  (upstream RR_GRAVEYARD_DAMPES_HOUSE, SCENE_GRAVEKEEPERS_HUT)
    # Locations
    add_locations(Regions.GRAVEYARD_DAMPES_HOUSE, world, [
        (Locations.GRAVEYARD_DIARY_HINT,
         lambda bundle: is_adult(bundle)),
    ])
    # Connections
    connect_regions(Regions.GRAVEYARD_DAMPES_HOUSE, world, [
        (Regions.THE_GRAVEYARD,
         lambda bundle: True_()),
    ])

    # Graveyard Warp Pad Region  (upstream RR_GRAVEYARD_WARP_PAD_REGION, SCENE_GRAVEYARD)
    # Events
    add_events(Regions.GRAVEYARD_WARP_PAD_REGION, world, [
        (EventLocations.GRAVEYARD_WARP_PAD_REGION_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
    ])
    # Locations
    add_locations(Regions.GRAVEYARD_WARP_PAD_REGION, world, [
        (Locations.GRAVEYARD_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
        (Locations.GRAVEYARD_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_GRAVEYARD_GOSSIP_STONE: true
    ])
    # Connections
    connect_regions(Regions.GRAVEYARD_WARP_PAD_REGION, world, [
        (Regions.THE_GRAVEYARD,
         lambda bundle: True_()),
        (Regions.SHADOW_TEMPLE_ENTRYWAY,
         lambda bundle: can_use(Items.DINS_FIRE, bundle) | (can_do_trick(Tricks.GY_SHADOW_FIRE_ARROWS, bundle) & is_adult(bundle) & can_use(Items.FIRE_ARROW, bundle))),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_BUGS', 'CAN_ACCESS_FAIRIES', 'CAN_FARM_NUTS', 'PLANT_GRAVEYARD_BEAN', 'SOLD_SPOOKY_MASK']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (22): ['RC_GY_ROCK', 'RC_GY_ENTRANCE_RECTANGLE_SIGN', 'RC_GY_ENTRANCE_PLINTH', 'RC_GY_RIGHT_OF_ROYAL_TOMB_GRAVE', 'RC_GY_LEFT_OF_ROYAL_TOMB_GRAVE', 'RC_GY_ROYAL_TOMB_GRAVE', 'RC_GY_WONDER_DAMPE_RACE_1', 'RC_GY_WONDER_DAMPE_RACE_2', 'RC_GY_WONDER_DAMPE_RACE_3', 'RC_GY_WONDER_DAMPE_RACE_4', 'RC_GY_WONDER_DAMPE_RACE_5', 'RC_GY_WONDER_DAMPE_RACE_6', 'RC_GY_WONDER_DAMPE_RACE_7', 'RC_GY_WONDER_DAMPE_RACE_8', 'RC_GY_WONDER_DAMPE_RACE_9', 'RC_GY_WONDER_DAMPE_RACE_10', 'RC_GY_WONDER_DAMPE_RACE_11', 'RC_GY_WONDER_DAMPE_RACE_12', 'RC_GY_WONDER_DAMPE_RACE_13', 'RC_GY_WONDER_DAMPE_RACE_14', 'RC_GY_WONDER_DAMPE_RACE_15', 'RC_GRAVEYARD_GOSSIP_STONE']
