"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/haunted_wasteland.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    HAUNTED_WASTELAND_FAIRY_ACCESS = "Haunted Wasteland Fairy Access"
    HAUNTED_WASTELAND_NUT_ACCESS = "Haunted Wasteland Nut Access"
    HAUNTED_WASTELAND_CARPET_MERCHANT = "Haunted Wasteland Carpet Merchant"


def set_region_rules(world: "SohWorld") -> None:

    # Wasteland Near Fortress  (upstream RR_WASTELAND_NEAR_FORTRESS, SCENE_HAUNTED_WASTELAND)
    # Locations
    add_locations(Regions.WASTELAND_NEAR_FORTRESS, world, [
        (Locations.WASTELAND_BEFORE_QUICKSAND_CRATE,
         lambda bundle: can_break_crates(bundle)),
    ])
    # Connections
    connect_regions(Regions.WASTELAND_NEAR_FORTRESS, world, [
        (Regions.GF_OUTSIDE_GATE,
         lambda bundle: True_()),
        (Regions.HAUNTED_WASTELAND,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle) | can_use(Items.LONGSHOT, bundle) | can_do_trick(Tricks.HW_CROSSING, bundle) | (can_do_trick(Tricks.HW_BUNNY_CROSSING, bundle) & bunny_hood(bundle))),
    ])

    # Haunted Wasteland  (upstream RR_HAUNTED_WASTELAND, SCENE_HAUNTED_WASTELAND)
    # Events
    add_events(Regions.HAUNTED_WASTELAND, world, [
        (EventLocations.HAUNTED_WASTELAND_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: can_break_pots(bundle)),
        (EventLocations.HAUNTED_WASTELAND_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_break_pots(bundle)),
        (EventLocations.HAUNTED_WASTELAND_CARPET_MERCHANT, Events.CARPET_MERCHANT,
         lambda bundle: has_item(Items.ADULT_WALLET, bundle) & can_afford_slot(Locations.WASTELAND_CARPET_SALESMAN, bundle) & (can_jump_slash(bundle) | can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle))),
    ])
    # Locations
    add_locations(Regions.HAUNTED_WASTELAND, world, [
        (Locations.WASTELAND_CHEST,
         lambda bundle: has_fire_source(bundle) & has_open_chest(bundle)),
        (Locations.WASTELAND_CARPET_SALESMAN,
         lambda bundle: (can_jump_slash(bundle) | can_use(Items.HOVER_BOOTS, bundle)) & has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.WASTELAND_CARPET_SALESMAN, bundle)),
        (Locations.WASTELAND_GS,
         lambda bundle: can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG) | (is_adult(bundle) & can_ground_jumpslash(bundle))),
        (Locations.WASTELAND_NEAR_GS_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.WASTELAND_NEAR_GS_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.WASTELAND_NEAR_GS_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.WASTELAND_NEAR_GS_POT4,
         lambda bundle: can_break_pots(bundle)),
        (Locations.WASTELAND_AFTER_QUICKSAND_CRATE1,
         lambda bundle: can_break_crates(bundle)),
        (Locations.WASTELAND_AFTER_QUICKSAND_CRATE2,
         lambda bundle: can_break_crates(bundle)),
        (Locations.WASTELAND_AFTER_QUICKSAND_CRATE3,
         lambda bundle: can_break_crates(bundle)),
        (Locations.HW_CARPET_SALESMAN_ARROW_SIGN,
         lambda bundle: can_read(bundle)),
        (Locations.HW_POE_ALTAR,
         lambda bundle: can_read(bundle)),
    ])
    # Connections
    connect_regions(Regions.HAUNTED_WASTELAND, world, [
        (Regions.WASTELAND_NEAR_COLOSSUS,
         lambda bundle: can_do_trick(Tricks.LENS_HW, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
        (Regions.WASTELAND_NEAR_FORTRESS,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle) | can_use(Items.LONGSHOT, bundle) | can_do_trick(Tricks.HW_CROSSING, bundle) | (can_do_trick(Tricks.HW_BUNNY_CROSSING, bundle) & bunny_hood(bundle))),
    ])

    # Wasteland Near Colossus  (upstream RR_WASTELAND_NEAR_COLOSSUS, SCENE_HAUNTED_WASTELAND)
    # Locations
    add_locations(Regions.WASTELAND_NEAR_COLOSSUS, world, [
        (Locations.WASTELAND_NEAR_COLOSSUS_CRATE,
         lambda bundle: can_break_crates(bundle)),
    ])
    # Connections
    connect_regions(Regions.WASTELAND_NEAR_COLOSSUS, world, [
        (Regions.DESERT_COLOSSUS,
         lambda bundle: True_()),
        (Regions.HAUNTED_WASTELAND,
         lambda bundle: can_do_trick(Tricks.HW_REVERSE, bundle) | False_()),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_FAIRIES', 'CAN_FARM_NUTS', 'CARPET_MERCHANT']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (0): []
