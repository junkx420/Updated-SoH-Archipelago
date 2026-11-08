"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/lon_lon_ranch.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    LON_LON_RANCH_FREED_EPONA = "Lon Lon Ranch Freed Epona"
    LON_LON_RANCH_LINKS_COW = "Lon Lon Ranch Links Cow"


def set_region_rules(world: "SohWorld") -> None:

    # Lon Lon Ranch  (upstream RR_LON_LON_RANCH, SCENE_LON_LON_RANCH)
    # Events
    add_events(Regions.LON_LON_RANCH, world, [
        (EventLocations.LON_LON_RANCH_FREED_EPONA, Events.FREED_EPONA,
         lambda bundle: has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN") & can_use(Items.EPONAS_SONG, bundle) & is_adult(bundle) & at_day(bundle)),
        (EventLocations.LON_LON_RANCH_LINKS_COW, Events.GOTTEN_LINKS_COW,
         lambda bundle: has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN") & can_use(Items.EPONAS_SONG, bundle) & is_adult(bundle) & at_day(bundle)),
    ])
    # Locations
    add_locations(Regions.LON_LON_RANCH, world, [
        (Locations.SONG_FROM_MALON,
         lambda bundle: is_child(bundle) & has_item(Events.MALON_RETURNED_FROM_CASTLE, bundle) & has_speak(bundle, "HYLIAN") & has_item(Items.FAIRY_OCARINA, bundle) & at_day(bundle)),
        (Locations.LLR_GS_TREE,
         lambda bundle: is_child(bundle) & can_bonk_trees(bundle) & (has_grab(bundle) | can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA))),
        (Locations.LLR_GS_RAIN_SHED,
         lambda bundle: is_child(bundle) & can_get_nighttime_gs(bundle) & (has_grab(bundle) | can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA))),
        (Locations.LLR_GS_HOUSE_WINDOW,
         lambda bundle: is_child(bundle) & hookshot_or_boomerang(bundle) & can_get_nighttime_gs(bundle)),
        (Locations.LLR_GS_BACK_WALL,
         lambda bundle: is_child(bundle) & hookshot_or_boomerang(bundle) & can_get_nighttime_gs(bundle)),
        (Locations.LLR_FRONT_POT1,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.LLR_FRONT_POT2,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.LLR_FRONT_POT3,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.LLR_FRONT_POT4,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.LLR_RAIN_SHED_POT1,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.LLR_RAIN_SHED_POT2,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.LLR_RAIN_SHED_POT3,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.LLR_NEAR_TREE_CRATE,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
        (Locations.LLR_TREE,
         lambda bundle: is_child(bundle) & can_bonk_trees(bundle)),
        # DEFERRED RC_LLR_WONDER_BIG_FENCE: logic->IsAdult && logic->CanUse(RG_EPONAS_SONG) && (logic->HasItem(RG_CHILD_WALLET) || logic->Get(LOGIC_FREED_EPONA))
        # DEFERRED RC_LLR_WONDER_SMALL_FENCE: logic->IsAdult && logic->CanUse(RG_EPONAS_SONG) && (logic->HasItem(RG_CHILD_WALLET) || logic->Get(LOGIC_FREED_EPONA))
    ])
    # Connections
    connect_regions(Regions.LON_LON_RANCH, world, [
        (Regions.HYRULE_FIELD,
         lambda bundle: True_()),
        (Regions.LLR_TALONS_HOUSE,
         lambda bundle: has_item(Items.TALONS_HOUSE_KEY, bundle)),
        (Regions.LLR_STABLES,
         lambda bundle: has_item(Items.STABLES_KEY, bundle)),
        (Regions.LLR_TOWER,
         lambda bundle: has_item(Items.BACK_TOWER_KEY, bundle)),
        (Regions.LLR_GROTTO,
         lambda bundle: is_child(bundle)),
    ])

    # LLR Talons House  (upstream RR_LLR_TALONS_HOUSE, SCENE_LON_LON_BUILDINGS)
    # Locations
    add_locations(Regions.LLR_TALONS_HOUSE, world, [
        (Locations.LLR_TALONS_CHICKENS,
         lambda bundle: has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN") & is_child(bundle) & at_day(bundle) & has_item(Events.TALON_RETURNED_FROM_CASTLE, bundle) & has_grab(bundle)),
        (Locations.LLR_TALONS_HOUSE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.LLR_TALONS_HOUSE_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.LLR_TALONS_HOUSE_POT3,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.LLR_TALONS_HOUSE, world, [
        (Regions.LON_LON_RANCH,
         lambda bundle: True_()),
    ])

    # LLR Stables  (upstream RR_LLR_STABLES, SCENE_STABLE)
    # Locations
    add_locations(Regions.LLR_STABLES, world, [
        (Locations.LLR_STABLES_LEFT_COW,
         lambda bundle: can_use(Items.EPONAS_SONG, bundle)),
        (Locations.LLR_STABLES_RIGHT_COW,
         lambda bundle: can_use(Items.EPONAS_SONG, bundle)),
    ])
    # Connections
    connect_regions(Regions.LLR_STABLES, world, [
        (Regions.LON_LON_RANCH,
         lambda bundle: True_()),
    ])

    # LLR Tower  (upstream RR_LLR_TOWER, SCENE_LON_LON_BUILDINGS)
    # Locations
    add_locations(Regions.LLR_TOWER, world, [
        (Locations.LLR_FREESTANDING_POH,
         lambda bundle: is_child(bundle) & has_grab(bundle) & has_crawl(bundle)),
        (Locations.LLR_TOWER_LEFT_COW,
         lambda bundle: can_use(Items.EPONAS_SONG, bundle)),
        (Locations.LLR_TOWER_RIGHT_COW,
         lambda bundle: can_use(Items.EPONAS_SONG, bundle)),
    ])
    # Connections
    connect_regions(Regions.LLR_TOWER, world, [
        (Regions.LON_LON_RANCH,
         lambda bundle: True_()),
    ])

    # LLR Grotto  (upstream RR_LLR_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.LLR_GROTTO, world, [
        (Locations.LLR_DEKU_SCRUB_GROTTO_LEFT,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.LLR_DEKU_SCRUB_GROTTO_LEFT, bundle)),
        (Locations.LLR_DEKU_SCRUB_GROTTO_RIGHT,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.LLR_DEKU_SCRUB_GROTTO_RIGHT, bundle)),
        (Locations.LLR_DEKU_SCRUB_GROTTO_CENTER,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.LLR_DEKU_SCRUB_GROTTO_CENTER, bundle)),
        (Locations.LLR_DEKU_SCRUB_GROTTO_BEEHIVE,
         lambda bundle: can_break_upper_beehives(bundle)),
    ])
    # Connections
    connect_regions(Regions.LLR_GROTTO, world, [
        (Regions.LON_LON_RANCH,
         lambda bundle: True_()),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['FREED_EPONA', 'GOTTEN_LINKS_COW', 'MALON_RETURNED_FROM_CASTLE', 'TALON_RETURNED_FROM_CASTLE']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (2): ['RC_LLR_WONDER_BIG_FENCE', 'RC_LLR_WONDER_SMALL_FENCE']
