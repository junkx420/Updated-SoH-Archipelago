"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/root.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ..LogicHelpers import *

if TYPE_CHECKING:
    from .. import SohWorld


class EventLocations(StrEnum):
    ROOT_KAKARIKO_GATE_OPEN = "Root Kakariko Gate Open"
    ROOT_TH_COULD_FREE_1_TORCH_CARPENTER = "Root Th Could Free 1 Torch Carpenter"
    ROOT_TH_COULD_FREE_DOUBLE_CELL_CARPENTER = "Root Th Could Free Double Cell Carpenter"
    ROOT_TH_COULD_FREE_DEAD_END_CARPENTER = "Root Th Could Free Dead End Carpenter"
    ROOT_TH_COULD_FREE_SLOPE_CARPENTER = "Root Th Could Free Slope Carpenter"
    ROOT_TH_RESCUED_ALL_CARPENTERS = "Root Th Rescued All Carpenters"
    ROOT_FREED_EPONA = "Root Freed Epona"
    ROOT_SHOWED_MIDO_SWORD_AND_SHIELD = "Root Showed Mido Sword And Shield"
    ROOT_MET_ZELDA = "Root Met Zelda"
    ROOT_MALON_RETURNED_FROM_CASTLE = "Root Malon Returned From Castle"
    ROOT_TALON_RETURNED_FROM_CASTLE = "Root Talon Returned From Castle"


def set_region_rules(world: "SohWorld") -> None:

    # Root  (upstream RR_ROOT, SCENE_ID_MAX)
    # Events
    add_events(Regions.ROOT, world, [
        (EventLocations.ROOT_KAKARIKO_GATE_OPEN, Events.KAKARIKO_GATE_OPEN,
         lambda bundle: starting_zeldas_letter(bundle)),
        (EventLocations.ROOT_TH_COULD_FREE_1_TORCH_CARPENTER, Events.TH_COULD_FREE_1_TORCH_CARPENTER,
         lambda bundle: True_(options=[OptionFilter(FortressCarpenters, FortressCarpenters.option_free)])),
        (EventLocations.ROOT_TH_COULD_FREE_DOUBLE_CELL_CARPENTER, Events.TH_COULD_FREE_DOUBLE_CELL_CARPENTER,
         lambda bundle: True_(options=[OptionFilter(FortressCarpenters, FortressCarpenters.option_free)]) | True_(options=[OptionFilter(FortressCarpenters, FortressCarpenters.option_fast)])),
        (EventLocations.ROOT_TH_COULD_FREE_DEAD_END_CARPENTER, Events.TH_COULD_FREE_DEAD_END_CARPENTER,
         lambda bundle: True_(options=[OptionFilter(FortressCarpenters, FortressCarpenters.option_free)]) | True_(options=[OptionFilter(FortressCarpenters, FortressCarpenters.option_fast)])),
        (EventLocations.ROOT_TH_COULD_FREE_SLOPE_CARPENTER, Events.TH_COULD_FREE_SLOPE_CARPENTER,
         lambda bundle: True_(options=[OptionFilter(FortressCarpenters, FortressCarpenters.option_free)]) | True_(options=[OptionFilter(FortressCarpenters, FortressCarpenters.option_fast)])),
        (EventLocations.ROOT_TH_RESCUED_ALL_CARPENTERS, Events.TH_RESCUED_ALL_CARPENTERS,
         lambda bundle: True_(options=[OptionFilter(FortressCarpenters, FortressCarpenters.option_free)])),
        (EventLocations.ROOT_FREED_EPONA, Events.FREED_EPONA,
         lambda bundle: True_(options=[OptionFilter(SkipEponaRace, True)])),
        (EventLocations.ROOT_SHOWED_MIDO_SWORD_AND_SHIELD, Events.SHOWED_MIDO_SWORD_AND_SHIELD,
         lambda bundle: True_(options=[OptionFilter(ClosedForest, ClosedForest.option_off)])),
        (EventLocations.ROOT_MET_ZELDA, Events.MET_ZELDA,
         lambda bundle: starting_zeldas_letter(bundle) & Not(False_())),
        (EventLocations.ROOT_MALON_RETURNED_FROM_CASTLE, Events.MALON_RETURNED_FROM_CASTLE,
         lambda bundle: True_(options=[OptionFilter(ShuffleWeirdEgg, ShuffleWeirdEgg.option_skip_waking_talon)])),
        (EventLocations.ROOT_TALON_RETURNED_FROM_CASTLE, Events.TALON_RETURNED_FROM_CASTLE,
         lambda bundle: True_(options=[OptionFilter(ShuffleWeirdEgg, ShuffleWeirdEgg.option_skip_waking_talon)])),
    ])
    # Locations
    add_locations(Regions.ROOT, world, [
        (Locations.LINKS_POCKET,
         lambda bundle: True_()),
        # DEFERRED RC_GANONS_BOSS_KEY: logic->CanTriggerGBK()
        # DEFERRED RC_GANON_SOUL: logic->CanTriggerGanonsSoul()
        # DEFERRED RC_WINCON: logic->CanTriggerWincon()
        (Locations.MAGIC_HINT_VIA_SARIAS_SONG,
         lambda bundle: can_use(Items.SARIAS_SONG, bundle)),
        (Locations.SONG_FROM_IMPA,
         lambda bundle: starting_zeldas_letter(bundle) & Not(False_())),
        (Locations.HC_MALON_EGG,
         lambda bundle: True_(options=[OptionFilter(ShuffleWeirdEgg, ShuffleWeirdEgg.option_skip_waking_talon)])),
        (Locations.HC_ZELDAS_LETTER,
         lambda bundle: starting_zeldas_letter(bundle) & Not(False_())),
        (Locations.MARKET_TOT_MASTER_SWORD,
         lambda bundle: True_(options=[OptionFilter(StartingAge, StartingAge.option_adult)])),
    ])
    # Connections
    connect_regions(Regions.ROOT, world, [
        (Regions.ROOT_EXITS,
         lambda bundle: True_()),
    ])

    # Root Exits  (upstream RR_ROOT_EXITS, SCENE_ID_MAX)
    # Connections
    connect_regions(Regions.ROOT_EXITS, world, [
        (Regions.CHILD_SPAWN,
         lambda bundle: is_child(bundle)),
        (Regions.ADULT_SPAWN,
         lambda bundle: is_adult(bundle)),
        (Regions.MINUET_OF_FOREST_WARP,
         lambda bundle: can_use(Items.MINUET_OF_FOREST, bundle)),
        (Regions.BOLERO_OF_FIRE_WARP,
         lambda bundle: can_use(Items.BOLERO_OF_FIRE, bundle)),
        (Regions.SERENADE_OF_WATER_WARP,
         lambda bundle: can_use(Items.SERENADE_OF_WATER, bundle)),
        (Regions.NOCTURNE_OF_SHADOW_WARP,
         lambda bundle: can_use(Items.NOCTURNE_OF_SHADOW, bundle)),
        (Regions.REQUIEM_OF_SPIRIT_WARP,
         lambda bundle: can_use(Items.REQUIEM_OF_SPIRIT, bundle)),
        (Regions.PRELUDE_OF_LIGHT_WARP,
         lambda bundle: can_use(Items.PRELUDE_OF_LIGHT, bundle)),
    ])

    # Child Spawn  (upstream RR_CHILD_SPAWN, SCENE_ID_MAX)
    # Connections
    connect_regions(Regions.CHILD_SPAWN, world, [
        (Regions.KF_LINKS_HOUSE,
         lambda bundle: True_()),
    ])

    # Adult Spawn  (upstream RR_ADULT_SPAWN, SCENE_ID_MAX)
    # Connections
    connect_regions(Regions.ADULT_SPAWN, world, [
        (Regions.TEMPLE_OF_TIME,
         lambda bundle: True_()),
    ])

    # Minuet of Forest Warp  (upstream RR_MINUET_OF_FOREST_WARP, SCENE_ID_MAX)
    # Connections
    connect_regions(Regions.MINUET_OF_FOREST_WARP, world, [
        (Regions.SACRED_FOREST_MEADOW,
         lambda bundle: True_()),
    ])

    # Bolero of Fire Warp  (upstream RR_BOLERO_OF_FIRE_WARP, SCENE_ID_MAX)
    # Connections
    connect_regions(Regions.BOLERO_OF_FIRE_WARP, world, [
        (Regions.DMC_PAD_ENTRY,
         lambda bundle: True_()),
    ])

    # Serenade of Water Warp  (upstream RR_SERENADE_OF_WATER_WARP, SCENE_ID_MAX)
    # Connections
    connect_regions(Regions.SERENADE_OF_WATER_WARP, world, [
        (Regions.LAKE_HYLIA,
         lambda bundle: True_()),
    ])

    # Requiem of Spirit Warp  (upstream RR_REQUIEM_OF_SPIRIT_WARP, SCENE_ID_MAX)
    # Connections
    connect_regions(Regions.REQUIEM_OF_SPIRIT_WARP, world, [
        (Regions.DESERT_COLOSSUS,
         lambda bundle: True_()),
    ])

    # Nocturne of Shadow Warp  (upstream RR_NOCTURNE_OF_SHADOW_WARP, SCENE_ID_MAX)
    # Connections
    connect_regions(Regions.NOCTURNE_OF_SHADOW_WARP, world, [
        (Regions.GRAVEYARD_WARP_PAD_REGION,
         lambda bundle: True_()),
    ])

    # Prelude of Light Warp  (upstream RR_PRELUDE_OF_LIGHT_WARP, SCENE_ID_MAX)
    # Connections
    connect_regions(Regions.PRELUDE_OF_LIGHT_WARP, world, [
        (Regions.TEMPLE_OF_TIME,
         lambda bundle: True_()),
    ])

# ---- summary
# notes: ['TODO feature 3.9']
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['FREED_EPONA', 'KAKARIKO_GATE_OPEN', 'MALON_RETURNED_FROM_CASTLE', 'MET_ZELDA', 'SHOWED_MIDO_SWORD_AND_SHIELD', 'TALON_RETURNED_FROM_CASTLE', 'TH_COULD_FREE_1_TORCH_CARPENTER', 'TH_COULD_FREE_DEAD_END_CARPENTER', 'TH_COULD_FREE_DOUBLE_CELL_CARPENTER', 'TH_COULD_FREE_SLOPE_CARPENTER', 'TH_RESCUED_ALL_CARPENTERS']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (3): ['RC_GANONS_BOSS_KEY', 'RC_GANON_SOUL', 'RC_WINCON']
