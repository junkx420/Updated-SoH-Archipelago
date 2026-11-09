"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/goron_city.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    GORON_CITY_FAIRY_ACCESS = "Goron City Fairy Access"
    GORON_CITY_STICK_ACCESS = "Goron City Stick Access"
    GORON_CITY_BUG_ACCESS = "Goron City Bug Access"
    GORON_CITY_GORON_CITY_CHILD_FIRE = "Goron City Goron City Child Fire"
    GORON_CITY_GORON_CITY_WOODS_WARP_OPEN = "Goron City Goron City Woods Warp Open"
    GORON_CITY_GORON_CITY_DARUNIAS_DOOR_OPEN_CHILD = "Goron City Goron City Darunias Door Open Child"
    GORON_CITY_GORON_CITY_STOP_ROLLING_GORON_AS_ADULT = "Goron City Goron City Stop Rolling Goron As Adult"
    GC_MEDIGORON_MEDIGORON = "GC Medigoron Medigoron"
    GC_WOODS_WARP_GORON_CITY_WOODS_WARP_OPEN = "GC Woods Warp Goron City Woods Warp Open"
    GC_DARUNIAS_CHAMBER_GORON_CITY_CHILD_FIRE = "GC Darunias Chamber Goron City Child Fire"


def set_region_rules(world: "SohWorld") -> None:

    # Goron City  (upstream RR_GORON_CITY, SCENE_GORON_CITY)
    # Events
    add_events(Regions.GORON_CITY, world, [
        (EventLocations.GORON_CITY_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
        (EventLocations.GORON_CITY_STICK_ACCESS, Events.CAN_FARM_STICKS,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (EventLocations.GORON_CITY_BUG_ACCESS, Events.CAN_ACCESS_BUGS,
         lambda bundle: (blast_or_smash(bundle) & has_grab(bundle)) | can_use(Items.SILVER_GAUNTLETS, bundle)),
        (EventLocations.GORON_CITY_GORON_CITY_CHILD_FIRE, Events.GORON_CITY_CHILD_FIRE,
         lambda bundle: is_child(bundle) & can_use(Items.DINS_FIRE, bundle)),
        (EventLocations.GORON_CITY_GORON_CITY_WOODS_WARP_OPEN, Events.GORON_CITY_WOODS_WARP_OPEN,
         lambda bundle: can_detonate_upright_bomb_flower(bundle) | can_use(Items.MEGATON_HAMMER, bundle) | (is_child(bundle) & has_item(Events.GORON_CITY_CHILD_FIRE, bundle) & can_use(Items.STICKS, bundle))),
        (EventLocations.GORON_CITY_GORON_CITY_DARUNIAS_DOOR_OPEN_CHILD, Events.GORON_CITY_DARUNIAS_DOOR_OPEN_CHILD,
         lambda bundle: is_child(bundle) & can_use(Items.ZELDAS_LULLABY, bundle)),
        (EventLocations.GORON_CITY_GORON_CITY_STOP_ROLLING_GORON_AS_ADULT, Events.GORON_CITY_STOP_ROLLING_GORON_AS_ADULT,
         lambda bundle: is_adult(bundle) & has_speak(bundle, "GORON") & (has_item(Items.GORONS_BRACELET, bundle) | has_explosives(bundle) | can_use(Items.FAIRY_BOW, bundle) | (can_do_trick(Tricks.GC_LINK_GORON_DINS, bundle) & (can_use(Items.DINS_FIRE, bundle) | (can_do_trick(Tricks.BLUE_FIRE_MUD_WALLS, bundle) & can_use(Items.BOTTLE_WITH_BLUE_FIRE, bundle)))))),
    ])
    # Locations
    add_locations(Regions.GORON_CITY, world, [
        (Locations.GC_MAZE_LEFT_CHEST,
         lambda bundle: (can_use(Items.MEGATON_HAMMER, bundle) | can_use(Items.SILVER_GAUNTLETS, bundle) | (can_do_trick(Tricks.GC_LEFTMOST, bundle) & has_explosives(bundle) & can_use(Items.HOVER_BOOTS, bundle))) & has_open_chest(bundle)),
        (Locations.GC_MAZE_CENTER_CHEST,
         lambda bundle: (blast_or_smash(bundle) | can_use(Items.SILVER_GAUNTLETS, bundle)) & has_open_chest(bundle)),
        (Locations.GC_MAZE_RIGHT_CHEST,
         lambda bundle: (blast_or_smash(bundle) | can_use(Items.SILVER_GAUNTLETS, bundle)) & has_open_chest(bundle)),
        (Locations.GC_POT_FREESTANDING_POH,
         lambda bundle: is_child(bundle) & has_item(Events.GORON_CITY_CHILD_FIRE, bundle) & (can_use(Items.BOMB_BAG, bundle) | (has_item(Items.GORONS_BRACELET, bundle) & can_do_trick(Tricks.GC_POT_STRENGTH, bundle)) | (can_use(Items.BOMBCHUS_5, bundle) & can_do_trick(Tricks.GC_POT, bundle)))),
        (Locations.GC_ROLLING_GORON_AS_CHILD,
         lambda bundle: is_child(bundle) & has_speak(bundle, "GORON") & (has_explosives(bundle) | (has_item(Items.GORONS_BRACELET, bundle) & can_do_trick(Tricks.GC_ROLLING_STRENGTH, bundle)))),
        (Locations.GC_ROLLING_GORON_AS_ADULT,
         lambda bundle: has_item(Events.GORON_CITY_STOP_ROLLING_GORON_AS_ADULT, bundle)),
        (Locations.GC_GS_BOULDER_MAZE,
         lambda bundle: is_child(bundle) & blast_or_smash(bundle)),
        (Locations.GC_GS_CENTER_PLATFORM,
         lambda bundle: is_adult(bundle) & can_attack(bundle)),
        (Locations.GC_MAZE_GOSSIP_STONE_FAIRY,
         lambda bundle: (blast_or_smash(bundle) | can_use(Items.SILVER_GAUNTLETS, bundle)) & call_gossip_fairy_except_suns(bundle)),
        (Locations.GC_MAZE_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: (blast_or_smash(bundle) | can_use(Items.SILVER_GAUNTLETS, bundle)) & can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_GC_MAZE_GOSSIP_STONE: logic->BlastOrSmash() || logic->CanUse(RG_SILVER_GAUNTLETS)
        (Locations.GC_LOWER_STAIRCASE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GC_LOWER_STAIRCASE_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GC_UPPER_STAIRCASE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GC_UPPER_STAIRCASE_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GC_UPPER_STAIRCASE_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GC_MAZE_CRATE,
         lambda bundle: blast_or_smash(bundle) | (can_use(Items.SILVER_GAUNTLETS, bundle) & can_break_crates(bundle))),
        (Locations.GC_ENTRANCE_BOULDER_1,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.GC_ENTRANCE_BOULDER_2,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.GC_ENTRANCE_BOULDER_3,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.GC_LW_BOULDER_1,
         lambda bundle: has_item(Events.GORON_CITY_WOODS_WARP_OPEN, bundle)),
        (Locations.GC_LW_BOULDER_2,
         lambda bundle: has_item(Events.GORON_CITY_WOODS_WARP_OPEN, bundle)),
        (Locations.GC_LW_BOULDER_3,
         lambda bundle: has_item(Events.GORON_CITY_WOODS_WARP_OPEN, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_1,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_2,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_3,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_4,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_5,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_6,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_7,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_8,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_9,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_10,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_11,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_12,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_13,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_14,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_15,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_16,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_17,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_18,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_19,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_20,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_21,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_22,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_23,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_24,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_25,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_26,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_27,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_28,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_SILVER_BOULDER_29,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_MAZE_BOULDER_1,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.GC_MAZE_BOULDER_2,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.GC_MAZE_BOULDER_3,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.GC_MAZE_BOULDER_4,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.GC_MAZE_BOULDER_5,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.GC_MAZE_BOULDER_6,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.GC_MAZE_BOULDER_7,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.GC_MAZE_BOULDER_8,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.GC_MAZE_BOULDER_9,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.GC_MAZE_BOULDER_10,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.GC_MAZE_BRONZE_BOULDER_1,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
        (Locations.GC_MAZE_BRONZE_BOULDER_2,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
        (Locations.GC_MAZE_BRONZE_BOULDER_3,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
        (Locations.GC_MAZE_BRONZE_BOULDER_4,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
        (Locations.GC_MAZE_BRONZE_BOULDER_5,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
        (Locations.GC_MAZE_ROCK,
         lambda bundle: blast_or_smash(bundle) | can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.GC_CHILD_ROLLING_GORON_RECTANGLE_SIGN,
         lambda bundle: is_child(bundle) & can_read(bundle)),
    ])
    # Connections
    connect_regions(Regions.GORON_CITY, world, [
        (Regions.DEATH_MOUNTAIN_TRAIL,
         lambda bundle: True_()),
        (Regions.GC_MEDIGORON,
         lambda bundle: can_break_mud_walls(bundle) | has_item(Items.GORONS_BRACELET, bundle)),
        (Regions.GC_WOODS_WARP,
         lambda bundle: has_item(Events.GORON_CITY_WOODS_WARP_OPEN, bundle)),
        (Regions.GC_SHOP,
         lambda bundle: (is_adult(bundle) & has_item(Events.GORON_CITY_STOP_ROLLING_GORON_AS_ADULT, bundle)) | (is_child(bundle) & (blast_or_smash(bundle) | has_item(Items.GORONS_BRACELET, bundle) | has_item(Events.GORON_CITY_CHILD_FIRE, bundle) | can_use(Items.FAIRY_BOW, bundle)))),
        (Regions.GC_DARUNIAS_CHAMBER,
         lambda bundle: (is_adult(bundle) & has_item(Events.GORON_CITY_STOP_ROLLING_GORON_AS_ADULT, bundle)) | (is_child(bundle) & has_item(Events.GORON_CITY_DARUNIAS_DOOR_OPEN_CHILD, bundle))),
        (Regions.GC_GROTTO_PLATFORM,
         lambda bundle: is_adult(bundle) & ((can_use(Items.SONG_OF_TIME, bundle) & ((effective_health_at_least(bundle, 17)) | can_use(Items.GORON_TUNIC, bundle) | can_use(Items.LONGSHOT, bundle) | can_use(Items.NAYRUS_LOVE, bundle))) | (effective_health_at_least(bundle, 9) & can_use(Items.GORON_TUNIC, bundle) & can_use(Items.HOOKSHOT, bundle)) | (can_use(Items.NAYRUS_LOVE, bundle) & can_use(Items.HOOKSHOT, bundle)) | (effective_health_at_least(bundle, 17) & can_use(Items.HOOKSHOT, bundle) & can_do_trick(Tricks.GC_GROTTO, bundle)))),
    ])

    # GC Medigoron  (upstream RR_GC_MEDIGORON, SCENE_GORON_CITY)
    # Events
    add_events(Regions.GC_MEDIGORON, world, [
        (EventLocations.GC_MEDIGORON_MEDIGORON, Events.MEDIGORON,
         lambda bundle: is_adult(bundle) & has_item(Items.ADULT_WALLET, bundle) & can_afford_slot(Locations.GC_MEDIGORON, bundle) & has_speak(bundle, "GORON")),
    ])
    # Locations
    add_locations(Regions.GC_MEDIGORON, world, [
        (Locations.GC_MEDIGORON,
         lambda bundle: is_adult(bundle) & has_speak(bundle, "GORON") & can_afford_slot(Locations.GC_MEDIGORON, bundle)),
        (Locations.GC_MEDIGORON_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
        (Locations.GC_MEDIGORON_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_GC_MEDIGORON_GOSSIP_STONE: true
        (Locations.GC_MEDIGORON_POT1,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.GC_MEDIGORON, world, [
        (Regions.GORON_CITY,
         lambda bundle: True_()),
    ])

    # GC Woods Warp  (upstream RR_GC_WOODS_WARP, SCENE_GORON_CITY)
    # Events
    add_events(Regions.GC_WOODS_WARP, world, [
        (EventLocations.GC_WOODS_WARP_GORON_CITY_WOODS_WARP_OPEN, Events.GORON_CITY_WOODS_WARP_OPEN,
         lambda bundle: blast_or_smash(bundle) | can_use(Items.DINS_FIRE, bundle)),
    ])
    # Connections
    connect_regions(Regions.GC_WOODS_WARP, world, [
        (Regions.GORON_CITY,
         lambda bundle: has_item(Events.GORON_CITY_WOODS_WARP_OPEN, bundle)),
        (Regions.THE_LOST_WOODS,
         lambda bundle: True_()),
    ])

    # GC Darunias Chamber  (upstream RR_GC_DARUNIAS_CHAMBER, SCENE_GORON_CITY)
    # Events
    add_events(Regions.GC_DARUNIAS_CHAMBER, world, [
        (EventLocations.GC_DARUNIAS_CHAMBER_GORON_CITY_CHILD_FIRE, Events.GORON_CITY_CHILD_FIRE,
         lambda bundle: is_child(bundle) & can_use(Items.STICKS, bundle)),
    ])
    # Locations
    add_locations(Regions.GC_DARUNIAS_CHAMBER, world, [
        (Locations.GC_DARUNIAS_JOY,
         lambda bundle: is_child(bundle) & can_use(Items.SARIAS_SONG, bundle)),
        (Locations.GC_DARUNIA_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GC_DARUNIA_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GC_DARUNIA_POT3,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.GC_DARUNIAS_CHAMBER, world, [
        (Regions.GORON_CITY,
         lambda bundle: True_()),
        (Regions.DMC_POTS_ENTRY,
         lambda bundle: is_adult(bundle) & has_grab(bundle)),
    ])

    # GC Grotto Platform  (upstream RR_GC_GROTTO_PLATFORM, SCENE_GORON_CITY)
    # Connections
    connect_regions(Regions.GC_GROTTO_PLATFORM, world, [
        (Regions.GC_GROTTO,
         lambda bundle: True_()),
        (Regions.GORON_CITY,
         lambda bundle: effective_health_at_least(bundle, 17) | can_use(Items.GORON_TUNIC, bundle) | can_use(Items.NAYRUS_LOVE, bundle) | ((is_child(bundle) | can_use(Items.SONG_OF_TIME, bundle)) & can_use(Items.LONGSHOT, bundle))),
    ])

    # GC Shop  (upstream RR_GC_SHOP, SCENE_GORON_SHOP)
    # Locations
    add_locations(Regions.GC_SHOP, world, [
        (Locations.GC_SHOP_ITEM1,
         lambda bundle: has_speak(bundle, "GORON") & can_afford_slot(Locations.GC_SHOP_ITEM1, bundle)),
        (Locations.GC_SHOP_ITEM2,
         lambda bundle: has_speak(bundle, "GORON") & can_afford_slot(Locations.GC_SHOP_ITEM2, bundle)),
        (Locations.GC_SHOP_ITEM3,
         lambda bundle: has_speak(bundle, "GORON") & can_afford_slot(Locations.GC_SHOP_ITEM3, bundle)),
        (Locations.GC_SHOP_ITEM4,
         lambda bundle: has_speak(bundle, "GORON") & can_afford_slot(Locations.GC_SHOP_ITEM4, bundle)),
        (Locations.GC_SHOP_ITEM5,
         lambda bundle: has_speak(bundle, "GORON") & can_afford_slot(Locations.GC_SHOP_ITEM5, bundle)),
        (Locations.GC_SHOP_ITEM6,
         lambda bundle: has_speak(bundle, "GORON") & can_afford_slot(Locations.GC_SHOP_ITEM6, bundle)),
        (Locations.GC_SHOP_ITEM7,
         lambda bundle: has_speak(bundle, "GORON") & can_afford_slot(Locations.GC_SHOP_ITEM7, bundle)),
        (Locations.GC_SHOP_ITEM8,
         lambda bundle: has_speak(bundle, "GORON") & can_afford_slot(Locations.GC_SHOP_ITEM8, bundle)),
    ])
    # Connections
    connect_regions(Regions.GC_SHOP, world, [
        (Regions.GORON_CITY,
         lambda bundle: True_()),
    ])

    # GC Grotto  (upstream RR_GC_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.GC_GROTTO, world, [
        (Locations.GC_DEKU_SCRUB_GROTTO_LEFT,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.GC_DEKU_SCRUB_GROTTO_LEFT, bundle)),
        (Locations.GC_DEKU_SCRUB_GROTTO_RIGHT,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.GC_DEKU_SCRUB_GROTTO_RIGHT, bundle)),
        (Locations.GC_DEKU_SCRUB_GROTTO_CENTER,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.GC_DEKU_SCRUB_GROTTO_CENTER, bundle)),
        (Locations.GC_GROTTO_BEEHIVE,
         lambda bundle: can_break_upper_beehives(bundle)),
    ])
    # Connections
    connect_regions(Regions.GC_GROTTO, world, [
        (Regions.GC_GROTTO_PLATFORM,
         lambda bundle: True_()),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_BUGS', 'CAN_ACCESS_FAIRIES', 'CAN_FARM_STICKS', 'GORON_CITY_CHILD_FIRE', 'GORON_CITY_DARUNIAS_DOOR_OPEN_CHILD', 'GORON_CITY_STOP_ROLLING_GORON_AS_ADULT', 'GORON_CITY_WOODS_WARP_OPEN', 'MEDIGORON']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (2): ['RC_GC_MAZE_GOSSIP_STONE', 'RC_GC_MEDIGORON_GOSSIP_STONE']
