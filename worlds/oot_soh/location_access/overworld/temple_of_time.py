"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/temple_of_time.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    TOT_ENTRANCE_FAIRY_ACCESS = "ToT Entrance Fairy Access"


def set_region_rules(world: "SohWorld") -> None:

    # ToT Entrance  (upstream RR_TOT_ENTRANCE, SCENE_TEMPLE_OF_TIME_EXTERIOR_DAY)
    # Events
    add_events(Regions.TOT_ENTRANCE, world, [
        (EventLocations.TOT_ENTRANCE_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
    ])
    # Locations
    add_locations(Regions.TOT_ENTRANCE, world, [
        (Locations.MARKET_TOT_LEFT_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy_except_suns(bundle) | (can_use(Items.SUNS_SONG, bundle) & is_adult(bundle))),
        (Locations.MARKET_TOT_LEFT_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.MARKET_TOT_LEFT_CENTER_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy_except_suns(bundle) | (can_use(Items.SUNS_SONG, bundle) & is_adult(bundle))),
        (Locations.MARKET_TOT_LEFT_CENTER_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.MARKET_TOT_RIGHT_CENTER_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy_except_suns(bundle) | (can_use(Items.SUNS_SONG, bundle) & is_adult(bundle))),
        (Locations.MARKET_TOT_RIGHT_CENTER_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.MARKET_TOT_RIGHT_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy_except_suns(bundle) | (can_use(Items.SUNS_SONG, bundle) & is_adult(bundle))),
        (Locations.MARKET_TOT_RIGHT_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_TOT_LEFTMOST_GOSSIP_STONE: true
        # DEFERRED RC_TOT_LEFT_CENTER_GOSSIP_STONE: true
        # DEFERRED RC_TOT_RIGHT_CENTER_GOSSIP_STONE: true
        # DEFERRED RC_TOT_RIGHTMOST_GOSSIP_STONE: true
    ])
    # Connections
    connect_regions(Regions.TOT_ENTRANCE, world, [
        (Regions.THE_MARKET,
         lambda bundle: True_()),
        (Regions.TEMPLE_OF_TIME,
         lambda bundle: True_()),
    ])

    # Temple of Time  (upstream RR_TEMPLE_OF_TIME, SCENE_TEMPLE_OF_TIME)
    # Locations
    add_locations(Regions.TEMPLE_OF_TIME, world, [
        (Locations.MARKET_TOT_LIGHT_ARROW_CUTSCENE,
         lambda bundle: is_adult(bundle) & has_item(Items.SHADOW_MEDALLION, bundle) & has_item(Items.SPIRIT_MEDALLION, bundle)),
        (Locations.MARKET_TOT_CHILD_ALTAR_HINT,
         lambda bundle: is_child(bundle)),
        (Locations.MARKET_TOT_ADULT_ALTAR_HINT,
         lambda bundle: is_adult(bundle)),
        (Locations.MARKET_OCARINA_OF_TIME_HINT,
         lambda bundle: is_adult(bundle) & has_speak(bundle, "HYLIAN")),
        # DEFERRED RC_TOT_ALTAR: logic->CanRead()
    ])
    # Connections
    connect_regions(Regions.TEMPLE_OF_TIME, world, [
        (Regions.TOT_ENTRANCE,
         lambda bundle: True_()),
        (Regions.TOT_BEYOND_DOOR_OF_TIME,
         lambda bundle: True_(options=[OptionFilter(DoorOfTime, DoorOfTime.option_open)]) | (can_use(Items.SONG_OF_TIME, bundle) & (True_(options=[OptionFilter(DoorOfTime, DoorOfTime.option_song_only)]) | (stone_count_at_least(bundle, 3) & has_item(Items.OCARINA_OF_TIME, bundle))))),
    ])

    # Beyond Door of Time  (upstream RR_TOT_BEYOND_DOOR_OF_TIME, SCENE_TEMPLE_OF_TIME)
    # Locations
    add_locations(Regions.TOT_BEYOND_DOOR_OF_TIME, world, [
        (Locations.MARKET_TOT_MASTER_SWORD,
         lambda bundle: is_adult(bundle)),
        (Locations.GIFT_FROM_RAURU,
         lambda bundle: is_adult(bundle)),
        (Locations.SHEIK_AT_TEMPLE,
         lambda bundle: is_adult(bundle) & has_item(Items.FOREST_MEDALLION, bundle)),
    ])
    # Connections
    connect_regions(Regions.TOT_BEYOND_DOOR_OF_TIME, world, [
        (Regions.TEMPLE_OF_TIME,
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
# deferred locations (5): ['RC_TOT_LEFTMOST_GOSSIP_STONE', 'RC_TOT_LEFT_CENTER_GOSSIP_STONE', 'RC_TOT_RIGHT_CENTER_GOSSIP_STONE', 'RC_TOT_RIGHTMOST_GOSSIP_STONE', 'RC_TOT_ALTAR']
