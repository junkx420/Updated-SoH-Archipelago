"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/zoras_domain.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    ZORAS_DOMAIN_FAIRY_ACCESS = "Zoras Domain Fairy Access"
    ZORAS_DOMAIN_NUT_ACCESS = "Zoras Domain Nut Access"
    ZORAS_DOMAIN_STICK_ACCESS = "Zoras Domain Stick Access"
    ZORAS_DOMAIN_FISH_ACCESS = "Zoras Domain Fish Access"
    ZORAS_DOMAIN_KING_ZORA_THAWED = "Zoras Domain King Zora Thawed"
    ZORAS_DOMAIN_DELIVER_RUTOS_LETTER = "Zoras Domain Deliver Rutos Letter"
    ZD_BEHIND_KING_ZORA_KING_ZORA_THAWED = "ZD Behind King Zora King Zora Thawed"
    ZD_STORMS_GROTTO_FAIRY_ACCESS = "ZD Storms Grotto Fairy Access"


def set_region_rules(world: "SohWorld") -> None:

    # Zoras Domain  (upstream RR_ZORAS_DOMAIN, SCENE_ZORAS_DOMAIN)
    # Events
    add_events(Regions.ZORAS_DOMAIN, world, [
        (EventLocations.ZORAS_DOMAIN_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
        (EventLocations.ZORAS_DOMAIN_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_break_pots(bundle)),
        (EventLocations.ZORAS_DOMAIN_STICK_ACCESS, Events.CAN_FARM_STICKS,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (EventLocations.ZORAS_DOMAIN_FISH_ACCESS, Events.CAN_ACCESS_FISH,
         lambda bundle: is_child(bundle)),
        (EventLocations.ZORAS_DOMAIN_KING_ZORA_THAWED, Events.KING_ZORA_THAWED,
         lambda bundle: is_adult(bundle) & blue_fire(bundle)),
        (EventLocations.ZORAS_DOMAIN_DELIVER_RUTOS_LETTER, Events.DELIVER_RUTOS_LETTER,
         lambda bundle: can_use(Items.BOTTLE_WITH_RUTOS_LETTER, bundle) & is_child(bundle) & True_(options=[OptionFilter(ZorasFountain, ZorasFountain.option_open, "ne")])),
    ])
    # Locations
    add_locations(Regions.ZORAS_DOMAIN, world, [
        (Locations.ZD_DIVING_MINIGAME,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) & has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "ZORA") & is_child(bundle)),
        (Locations.ZD_CHEST,
         lambda bundle: is_child(bundle) & can_use(Items.STICKS, bundle) & can_open_large_chest(bundle)),
        (Locations.ZD_KING_ZORA_THAWED,
         lambda bundle: is_adult(bundle) & has_item(Events.KING_ZORA_THAWED, bundle) & has_speak(bundle, "ZORA")),
        (Locations.ZD_TRADE_PRESCRIPTION,
         lambda bundle: is_adult(bundle) & has_item(Events.KING_ZORA_THAWED, bundle) & can_use(Items.PRESCRIPTION, bundle)),
        (Locations.ZD_GS_FROZEN_WATERFALL,
         lambda bundle: is_adult(bundle) & ((can_use(Items.MAGIC_SINGLE, bundle) | can_do_trick(Tricks.ZD_GS, bundle)) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.SHORT_JUMPSLASH, True, 1, False, True) | can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG, True, 1, False, True)) & can_get_nighttime_gs(bundle)),
        (Locations.ZD_FISH1,
         lambda bundle: is_child(bundle) & has_bottle(bundle)),
        (Locations.ZD_FISH2,
         lambda bundle: is_child(bundle) & has_bottle(bundle)),
        (Locations.ZD_FISH3,
         lambda bundle: is_child(bundle) & has_bottle(bundle)),
        (Locations.ZD_FISH4,
         lambda bundle: is_child(bundle) & has_bottle(bundle)),
        (Locations.ZD_FISH5,
         lambda bundle: is_child(bundle) & has_bottle(bundle)),
        (Locations.ZD_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
        (Locations.ZD_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.ZD_IN_FRONT_OF_KING_ZORA_BEEHIVE_LEFT,
         lambda bundle: is_child(bundle) & can_break_upper_beehives(bundle)),
        (Locations.ZD_IN_FRONT_OF_KING_ZORA_BEEHIVE_RIGHT,
         lambda bundle: is_child(bundle) & can_break_upper_beehives(bundle)),
        (Locations.ZD_NEAR_SHOP_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.ZD_NEAR_SHOP_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.ZD_NEAR_SHOP_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.ZD_NEAR_SHOP_POT4,
         lambda bundle: can_break_pots(bundle)),
        (Locations.ZD_NEAR_SHOP_POT5,
         lambda bundle: can_break_pots(bundle)),
        # DEFERRED RC_ZD_CIRCLE_ROCK_1: logic->CanBreakRocks()
        # DEFERRED RC_ZD_CIRCLE_ROCK_2: logic->CanBreakRocks()
        # DEFERRED RC_ZD_CIRCLE_ROCK_3: logic->CanBreakRocks()
        # DEFERRED RC_ZD_CIRCLE_ROCK_4: logic->CanBreakRocks()
        # DEFERRED RC_ZD_CIRCLE_ROCK_5: logic->CanBreakRocks()
        # DEFERRED RC_ZD_CIRCLE_ROCK_6: logic->CanBreakRocks()
        # DEFERRED RC_ZD_CIRCLE_ROCK_7: logic->CanBreakRocks()
        # DEFERRED RC_ZD_CIRCLE_ROCK_8: logic->CanBreakRocks()
        # DEFERRED RC_ZD_SHOP_RECTANGLE_SIGN: logic->CanRead()
        # DEFERRED RC_ZD_ENTRANCE_RECTANGLE_SIGN: logic->CanRead()
        # DEFERRED RC_ZD_KING_ZORA_PATH_ARROW_SIGN: logic->CanRead()
        # DEFERRED RC_ZD_NEAR_KING_ZORA_RECTANGLE_SIGN: logic->CanRead()
        # DEFERRED RC_ZD_NEAR_KING_ZORA_ARROW_SIGN: logic->CanRead()
        # DEFERRED RC_ZD_KING_ZORA_RED_ICE: logic->IsAdult && logic->Get(LOGIC_KING_ZORA_THAWED)
        # DEFERRED RC_ZD_ZORA_SHOP_RED_ICE: logic->IsAdult && logic->BlueFire()
        # DEFERRED RC_ZD_GOSSIP_STONE: true
    ])
    # Connections
    connect_regions(Regions.ZORAS_DOMAIN, world, [
        (Regions.ZR_BEHIND_WATERFALL,
         lambda bundle: True_()),
        (Regions.LH_FROM_SHORTCUT,
         lambda bundle: is_child(bundle) & (has_item(Items.SILVER_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle))),
        (Regions.ZD_BEHIND_KING_ZORA,
         lambda bundle: has_item(Events.DELIVER_RUTOS_LETTER, bundle) | True_(options=[OptionFilter(ZorasFountain, ZorasFountain.option_open)]) | (True_(options=[OptionFilter(ZorasFountain, ZorasFountain.option_closed_as_child)]) & is_adult(bundle)) | (can_do_trick(Tricks.ZD_KING_ZORA_SKIP, bundle) & is_adult(bundle))),
        (Regions.ZD_SHOP,
         lambda bundle: is_child(bundle) | blue_fire(bundle)),
        (Regions.ZORAS_DOMAIN_ISLAND,
         lambda bundle: True_()),
    ])

    # Zoras Domain Island  (upstream RR_ZORAS_DOMAIN_ISLAND, SCENE_ZORAS_DOMAIN)
    # Connections
    connect_regions(Regions.ZORAS_DOMAIN_ISLAND, world, [
        (Regions.ZORAS_DOMAIN,
         lambda bundle: is_adult(bundle) | has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.LONGSHOT, bundle) | (can_use(Items.HOOKSHOT, bundle) & can_do_trick(Tricks.HOOKSHOT_LADDERS, bundle)) | can_use(Items.IRON_BOOTS, bundle) | ((can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle)) & has_climb(bundle))),
        (Regions.ZD_STORMS_GROTTO,
         lambda bundle: can_open_storms_grotto(bundle)),
    ])

    # ZD Behind King Zora  (upstream RR_ZD_BEHIND_KING_ZORA, SCENE_ZORAS_DOMAIN)
    # Events
    add_events(Regions.ZD_BEHIND_KING_ZORA, world, [
        (EventLocations.ZD_BEHIND_KING_ZORA_KING_ZORA_THAWED, Events.KING_ZORA_THAWED,
         lambda bundle: is_adult(bundle) & blue_fire(bundle)),
    ])
    # Locations
    add_locations(Regions.ZD_BEHIND_KING_ZORA, world, [
        (Locations.ZD_BEHIND_KING_ZORA_BEEHIVE,
         lambda bundle: is_child(bundle) & can_break_upper_beehives(bundle)),
        # DEFERRED RC_ZD_KING_ZORA_RED_ICE: logic->IsAdult && logic->Get(LOGIC_KING_ZORA_THAWED)
    ])
    # Connections
    connect_regions(Regions.ZD_BEHIND_KING_ZORA, world, [
        (Regions.ZORAS_DOMAIN,
         lambda bundle: has_item(Events.DELIVER_RUTOS_LETTER, bundle) | True_(options=[OptionFilter(ZorasFountain, ZorasFountain.option_open)]) | (True_(options=[OptionFilter(ZorasFountain, ZorasFountain.option_closed_as_child)]) & is_adult(bundle))),
        (Regions.ZORAS_FOUNTAIN,
         lambda bundle: True_()),
    ])

    # ZD Shop  (upstream RR_ZD_SHOP, SCENE_ZORA_SHOP)
    # Locations
    add_locations(Regions.ZD_SHOP, world, [
        (Locations.ZD_SHOP_ITEM1,
         lambda bundle: has_speak(bundle, "ZORA") & can_afford_slot(Locations.ZD_SHOP_ITEM1, bundle)),
        (Locations.ZD_SHOP_ITEM2,
         lambda bundle: has_speak(bundle, "ZORA") & can_afford_slot(Locations.ZD_SHOP_ITEM2, bundle)),
        (Locations.ZD_SHOP_ITEM3,
         lambda bundle: has_speak(bundle, "ZORA") & can_afford_slot(Locations.ZD_SHOP_ITEM3, bundle)),
        (Locations.ZD_SHOP_ITEM4,
         lambda bundle: has_speak(bundle, "ZORA") & can_afford_slot(Locations.ZD_SHOP_ITEM4, bundle)),
        (Locations.ZD_SHOP_ITEM5,
         lambda bundle: has_speak(bundle, "ZORA") & can_afford_slot(Locations.ZD_SHOP_ITEM5, bundle)),
        (Locations.ZD_SHOP_ITEM6,
         lambda bundle: has_speak(bundle, "ZORA") & can_afford_slot(Locations.ZD_SHOP_ITEM6, bundle)),
        (Locations.ZD_SHOP_ITEM7,
         lambda bundle: has_speak(bundle, "ZORA") & can_afford_slot(Locations.ZD_SHOP_ITEM7, bundle)),
        (Locations.ZD_SHOP_ITEM8,
         lambda bundle: has_speak(bundle, "ZORA") & can_afford_slot(Locations.ZD_SHOP_ITEM8, bundle)),
    ])
    # Connections
    connect_regions(Regions.ZD_SHOP, world, [
        (Regions.ZORAS_DOMAIN,
         lambda bundle: True_()),
    ])

    # ZD Storms Grotto  (upstream RR_ZD_STORMS_GROTTO, SCENE_GROTTOS)
    # Events
    add_events(Regions.ZD_STORMS_GROTTO, world, [
        (EventLocations.ZD_STORMS_GROTTO_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: True_()),
    ])
    # Locations
    add_locations(Regions.ZD_STORMS_GROTTO, world, [
        (Locations.ZD_FAIRY_GROTTO_FAIRY1,
         lambda bundle: True_()),
        (Locations.ZD_FAIRY_GROTTO_FAIRY2,
         lambda bundle: True_()),
        (Locations.ZD_FAIRY_GROTTO_FAIRY3,
         lambda bundle: True_()),
        (Locations.ZD_FAIRY_GROTTO_FAIRY4,
         lambda bundle: True_()),
        (Locations.ZD_FAIRY_GROTTO_FAIRY5,
         lambda bundle: True_()),
        (Locations.ZD_FAIRY_GROTTO_FAIRY6,
         lambda bundle: True_()),
        (Locations.ZD_FAIRY_GROTTO_FAIRY7,
         lambda bundle: True_()),
        (Locations.ZD_FAIRY_GROTTO_FAIRY8,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.ZD_STORMS_GROTTO, world, [
        (Regions.ZORAS_DOMAIN_ISLAND,
         lambda bundle: True_()),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_FAIRIES', 'CAN_ACCESS_FISH', 'CAN_FARM_NUTS', 'CAN_FARM_STICKS', 'DELIVER_RUTOS_LETTER', 'KING_ZORA_THAWED']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (17): ['RC_ZD_CIRCLE_ROCK_1', 'RC_ZD_CIRCLE_ROCK_2', 'RC_ZD_CIRCLE_ROCK_3', 'RC_ZD_CIRCLE_ROCK_4', 'RC_ZD_CIRCLE_ROCK_5', 'RC_ZD_CIRCLE_ROCK_6', 'RC_ZD_CIRCLE_ROCK_7', 'RC_ZD_CIRCLE_ROCK_8', 'RC_ZD_SHOP_RECTANGLE_SIGN', 'RC_ZD_ENTRANCE_RECTANGLE_SIGN', 'RC_ZD_KING_ZORA_PATH_ARROW_SIGN', 'RC_ZD_NEAR_KING_ZORA_RECTANGLE_SIGN', 'RC_ZD_NEAR_KING_ZORA_ARROW_SIGN', 'RC_ZD_KING_ZORA_RED_ICE', 'RC_ZD_ZORA_SHOP_RED_ICE', 'RC_ZD_GOSSIP_STONE', 'RC_ZD_KING_ZORA_RED_ICE']
