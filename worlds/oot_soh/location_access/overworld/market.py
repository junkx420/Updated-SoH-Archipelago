"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/market.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    MARKET_GUARD_HOUSE_CAN_EMPTY_BIG_POES = "Market Guard House Can Empty Big Poes"
    MARKET_MASK_SHOP_CAN_BORROW_MASKS = "Market Mask Shop Can Borrow Masks"
    MARKET_BOMBCHU_BOWLING_COULD_PLAY_BOWLING = "Market Bombchu Bowling Could Play Bowling"


def set_region_rules(world: "SohWorld") -> None:

    # Market Entrance  (upstream RR_MARKET_ENTRANCE, SCENE_MARKET_ENTRANCE_DAY)
    # Connections
    connect_regions(Regions.MARKET_ENTRANCE, world, [
        (Regions.HYRULE_FIELD,
         lambda bundle: is_adult(bundle) | at_day(bundle)),
        (Regions.THE_MARKET,
         lambda bundle: True_()),
        (Regions.MARKET_GUARD_HOUSE,
         lambda bundle: has_item(Items.GUARD_HOUSE_KEY, bundle)),
    ])

    # Market  (upstream RR_THE_MARKET, SCENE_MARKET_DAY)
    # Locations
    add_locations(Regions.THE_MARKET, world, [
        (Locations.MARKET_MARKET_GRASS1,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.MARKET_MARKET_GRASS2,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.MARKET_MARKET_GRASS3,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.MARKET_MARKET_GRASS4,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.MARKET_MARKET_GRASS5,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.MARKET_MARKET_GRASS6,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.MARKET_MARKET_GRASS7,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.MARKET_MARKET_GRASS8,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.MARKET_NEAR_BAZAAR_CRATE1,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
        (Locations.MARKET_NEAR_BAZAAR_CRATE2,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
        (Locations.MARKET_SHOOTING_GALLERY_CRATE1,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
        (Locations.MARKET_SHOOTING_GALLERY_CRATE2,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
        (Locations.MARKET_TREE,
         lambda bundle: is_child(bundle) & can_bonk_trees(bundle)),
        # DEFERRED RC_MKT_WONDER_DAY_1: logic->IsChild && logic->AtDay
        # DEFERRED RC_MKT_WONDER_DAY_2: logic->IsChild && logic->AtDay
        # DEFERRED RC_MKT_WONDER_DAY_3: logic->IsChild && logic->AtDay
        # DEFERRED RC_MKT_WONDER_DAY_4: logic->IsChild && logic->AtDay
        # DEFERRED RC_MKT_WONDER_DAY_5: logic->IsChild && logic->AtDay
        # DEFERRED RC_MKT_WONDER_NIGHT_1: logic->IsChild && logic->AtNight
        # DEFERRED RC_MKT_WONDER_NIGHT_2: logic->IsChild && logic->AtNight
        (Locations.MARKET_BEGGAR_BUGS,
         lambda bundle: is_child(bundle) & at_day(bundle) & can_use(Items.BOTTLE_WITH_BUGS, bundle)),
        (Locations.MARKET_BEGGAR_FISH,
         lambda bundle: is_child(bundle) & at_day(bundle) & can_use(Items.BOTTLE_WITH_FISH, bundle)),
        (Locations.MARKET_BEGGAR_BLUE_FIRE,
         lambda bundle: is_child(bundle) & at_day(bundle) & can_use(Items.BOTTLE_WITH_BLUE_FIRE, bundle)),
    ])
    # Connections
    connect_regions(Regions.THE_MARKET, world, [
        (Regions.MARKET_ENTRANCE,
         lambda bundle: True_()),
        (Regions.TOT_ENTRANCE,
         lambda bundle: True_()),
        (Regions.CASTLE_GROUNDS,
         lambda bundle: True_()),
        (Regions.MARKET_BAZAAR,
         lambda bundle: is_child(bundle) & at_day(bundle) & has_item(Items.MARKET_BAZAAR_KEY, bundle)),
        (Regions.MARKET_MASK_SHOP,
         lambda bundle: is_child(bundle) & at_day(bundle) & has_item(Items.MASK_SHOP_KEY, bundle)),
        (Regions.MARKET_SHOOTING_GALLERY,
         lambda bundle: is_child(bundle) & at_day(bundle) & has_item(Items.MARKET_SHOOTING_GALLERY_KEY, bundle)),
        (Regions.MARKET_BOMBCHU_BOWLING,
         lambda bundle: is_child(bundle) & has_item(Items.BOMBCHU_BOWLING_KEY, bundle)),
        (Regions.MARKET_TREASURE_CHEST_GAME,
         lambda bundle: is_child(bundle) & at_night(bundle) & has_item(Items.TREASURE_CHEST_GAME_BUILDING_KEY, bundle)),
        (Regions.MARKET_POTION_SHOP,
         lambda bundle: is_child(bundle) & at_day(bundle) & has_item(Items.MARKET_POTION_SHOP_KEY, bundle)),
        (Regions.MARKET_BACK_ALLEY,
         lambda bundle: is_child(bundle)),
    ])

    # Market Back Alley  (upstream RR_MARKET_BACK_ALLEY, SCENE_BACK_ALLEY_DAY)
    # Connections
    connect_regions(Regions.MARKET_BACK_ALLEY, world, [
        (Regions.THE_MARKET,
         lambda bundle: True_()),
        (Regions.MARKET_BOMBCHU_SHOP,
         lambda bundle: at_night(bundle) & has_item(Items.BOMBCHU_SHOP_KEY, bundle)),
        (Regions.MARKET_DOG_LADY_HOUSE,
         lambda bundle: has_item(Items.RICHARDS_HOUSE_KEY, bundle)),
        (Regions.MARKET_MAN_IN_GREEN_HOUSE,
         lambda bundle: at_night(bundle) & has_item(Items.ALLEY_HOUSE_KEY, bundle)),
    ])

    # Market Guard House  (upstream RR_MARKET_GUARD_HOUSE, SCENE_MARKET_GUARD_HOUSE)
    # Events
    add_events(Regions.MARKET_GUARD_HOUSE, world, [
        (EventLocations.MARKET_GUARD_HOUSE_CAN_EMPTY_BIG_POES, Events.CAN_EMPTY_BIG_POES,
         lambda bundle: is_adult(bundle)),
    ])
    # Locations
    add_locations(Regions.MARKET_GUARD_HOUSE, world, [
        (Locations.MARKET_10_BIG_POES,
         lambda bundle: is_adult(bundle) & has_speak(bundle, "HYLIAN") & (has_item(Events.CAN_DEFEAT_BIG_POE, bundle) | big_poes_at_least_target(bundle))),
        (Locations.MARKET_MARKET_GS_GUARD_HOUSE,
         lambda bundle: is_child(bundle) & can_break_crates(bundle) & (has_grab(bundle) | can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA))),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT1,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT2,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT3,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT4,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT5,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT6,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT7,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT8,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT9,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT10,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT11,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT12,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT13,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT14,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT15,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT16,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT17,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT18,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT19,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT20,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT21,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT22,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT23,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT24,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT25,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT26,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT27,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT28,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT29,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT30,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT31,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT32,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT33,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT34,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT35,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT36,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT37,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT38,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT39,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT40,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT41,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT42,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT43,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CHILD_POT44,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_ADULT_POT1,
         lambda bundle: is_adult(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_ADULT_POT2,
         lambda bundle: is_adult(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_ADULT_POT3,
         lambda bundle: is_adult(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_ADULT_POT4,
         lambda bundle: is_adult(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_ADULT_POT5,
         lambda bundle: is_adult(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_ADULT_POT6,
         lambda bundle: is_adult(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_ADULT_POT7,
         lambda bundle: is_adult(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_ADULT_POT8,
         lambda bundle: is_adult(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_ADULT_POT9,
         lambda bundle: is_adult(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_ADULT_POT10,
         lambda bundle: is_adult(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_ADULT_POT11,
         lambda bundle: is_adult(bundle) & can_break_pots(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CRATE1,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CRATE2,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CRATE3,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CRATE4,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
        (Locations.MARKET_GUARD_HOUSE_CRATE5,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
    ])
    # Connections
    connect_regions(Regions.MARKET_GUARD_HOUSE, world, [
        (Regions.MARKET_ENTRANCE,
         lambda bundle: True_()),
    ])

    # Market Bazaar  (upstream RR_MARKET_BAZAAR, SCENE_BAZAAR)
    # Locations
    add_locations(Regions.MARKET_BAZAAR, world, [
        (Locations.MARKET_BAZAAR_ITEM1,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_BAZAAR_ITEM1, bundle)),
        (Locations.MARKET_BAZAAR_ITEM2,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_BAZAAR_ITEM2, bundle)),
        (Locations.MARKET_BAZAAR_ITEM3,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_BAZAAR_ITEM3, bundle)),
        (Locations.MARKET_BAZAAR_ITEM4,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_BAZAAR_ITEM4, bundle)),
        (Locations.MARKET_BAZAAR_ITEM5,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_BAZAAR_ITEM5, bundle)),
        (Locations.MARKET_BAZAAR_ITEM6,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_BAZAAR_ITEM6, bundle)),
        (Locations.MARKET_BAZAAR_ITEM7,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_BAZAAR_ITEM7, bundle)),
        (Locations.MARKET_BAZAAR_ITEM8,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_BAZAAR_ITEM8, bundle)),
    ])
    # Connections
    connect_regions(Regions.MARKET_BAZAAR, world, [
        (Regions.THE_MARKET,
         lambda bundle: True_()),
    ])

    # Market Mask Shop  (upstream RR_MARKET_MASK_SHOP, SCENE_HAPPY_MASK_SHOP)
    # Events
    add_events(Regions.MARKET_MASK_SHOP, world, [
        (EventLocations.MARKET_MASK_SHOP_CAN_BORROW_MASKS, Events.CAN_BORROW_MASKS,
         lambda bundle: has_speak(bundle, "HYLIAN") & has_item(Events.KAKARIKO_GATE_OPEN, bundle)),
    ])
    # Locations
    add_locations(Regions.MARKET_MASK_SHOP, world, [
        (Locations.MARKET_MASK_SHOP_HINT,
         lambda bundle: True_()),
        # DEFERRED RC_MK_MASK_SHOP_SIGN: logic->CanRead()
    ])
    # Connections
    connect_regions(Regions.MARKET_MASK_SHOP, world, [
        (Regions.THE_MARKET,
         lambda bundle: True_()),
    ])

    # Market Shooting Gallery  (upstream RR_MARKET_SHOOTING_GALLERY, SCENE_SHOOTING_GALLERY)
    # Locations
    add_locations(Regions.MARKET_SHOOTING_GALLERY, world, [
        (Locations.MARKET_SHOOTING_GALLERY,
         lambda bundle: is_child(bundle) & has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN")),
        # DEFERRED RC_MK_SHOOTING_GALLERY_RECTANGLE_SIGN: logic->IsChild && logic->CanRead()
    ])
    # Connections
    connect_regions(Regions.MARKET_SHOOTING_GALLERY, world, [
        (Regions.THE_MARKET,
         lambda bundle: True_()),
    ])

    # Market Bombchu Bowling  (upstream RR_MARKET_BOMBCHU_BOWLING, SCENE_BOMBCHU_BOWLING_ALLEY)
    # Events
    add_events(Regions.MARKET_BOMBCHU_BOWLING, world, [
        (EventLocations.MARKET_BOMBCHU_BOWLING_COULD_PLAY_BOWLING, Events.COULD_PLAY_BOWLING,
         lambda bundle: has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN")),
    ])
    # Locations
    add_locations(Regions.MARKET_BOMBCHU_BOWLING, world, [
        (Locations.MARKET_BOMBCHU_BOWLING_FIRST_PRIZE,
         lambda bundle: has_item(Events.COULD_PLAY_BOWLING, bundle) & bombchus_enabled(bundle)),
        (Locations.MARKET_BOMBCHU_BOWLING_SECOND_PRIZE,
         lambda bundle: has_item(Events.COULD_PLAY_BOWLING, bundle) & bombchus_enabled(bundle)),
    ])
    # Connections
    connect_regions(Regions.MARKET_BOMBCHU_BOWLING, world, [
        (Regions.THE_MARKET,
         lambda bundle: True_()),
    ])

    # Market Potion Shop  (upstream RR_MARKET_POTION_SHOP, SCENE_POTION_SHOP_MARKET)
    # Locations
    add_locations(Regions.MARKET_POTION_SHOP, world, [
        (Locations.MARKET_POTION_SHOP_ITEM1,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_POTION_SHOP_ITEM1, bundle)),
        (Locations.MARKET_POTION_SHOP_ITEM2,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_POTION_SHOP_ITEM2, bundle)),
        (Locations.MARKET_POTION_SHOP_ITEM3,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_POTION_SHOP_ITEM3, bundle)),
        (Locations.MARKET_POTION_SHOP_ITEM4,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_POTION_SHOP_ITEM4, bundle)),
        (Locations.MARKET_POTION_SHOP_ITEM5,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_POTION_SHOP_ITEM5, bundle)),
        (Locations.MARKET_POTION_SHOP_ITEM6,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_POTION_SHOP_ITEM6, bundle)),
        (Locations.MARKET_POTION_SHOP_ITEM7,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_POTION_SHOP_ITEM7, bundle)),
        (Locations.MARKET_POTION_SHOP_ITEM8,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_POTION_SHOP_ITEM8, bundle)),
    ])
    # Connections
    connect_regions(Regions.MARKET_POTION_SHOP, world, [
        (Regions.THE_MARKET,
         lambda bundle: True_()),
    ])

    # Market Treasure Chest Game  (upstream RR_MARKET_TREASURE_CHEST_GAME, SCENE_TREASURE_BOX_SHOP)
    # Locations
    add_locations(Regions.MARKET_TREASURE_CHEST_GAME, world, [
        (Locations.MARKET_GREG_HINT,
         lambda bundle: has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN")),
        # DEFERRED RC_MARKET_TREASURE_CHEST_GAME_SHOPKEEPER: logic->HasItem(RG_CHILD_WALLET) && logic->HasItem(RG_SPEAK_HYLIAN) && ctx->GetOption(RSK_SHUFFLE_CHEST_MINIGAME)
        (Locations.MARKET_CHEST_GAME_FIRST_ROOM_KEY,
         lambda bundle: can_open_large_chest(bundle) & (((False_()) & small_keys_scene("SCENE_TREASURE_BOX_SHOP", 1, bundle) | (Not(False_())) & (has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN") & can_use(Items.LENS_OF_TRUTH, bundle))))),
        (Locations.MARKET_CHEST_GAME_FIRST_ROOM_ITEM,
         lambda bundle: can_open_large_chest(bundle) & (((False_()) & small_keys_scene("SCENE_TREASURE_BOX_SHOP", 1, bundle) | (Not(False_())) & (has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN") & can_use(Items.LENS_OF_TRUTH, bundle))))),
        (Locations.MARKET_CHEST_GAME_SECOND_ROOM_KEY,
         lambda bundle: can_open_large_chest(bundle) & (((False_()) & small_keys_scene("SCENE_TREASURE_BOX_SHOP", 2, bundle) | (Not(False_())) & (has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN") & can_use(Items.LENS_OF_TRUTH, bundle))))),
        (Locations.MARKET_CHEST_GAME_SECOND_ROOM_ITEM,
         lambda bundle: can_open_large_chest(bundle) & (((False_()) & small_keys_scene("SCENE_TREASURE_BOX_SHOP", 2, bundle) | (Not(False_())) & (has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN") & can_use(Items.LENS_OF_TRUTH, bundle))))),
        (Locations.MARKET_CHEST_GAME_THIRD_ROOM_KEY,
         lambda bundle: can_open_large_chest(bundle) & (((False_()) & small_keys_scene("SCENE_TREASURE_BOX_SHOP", 3, bundle) | (Not(False_())) & (has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN") & can_use(Items.LENS_OF_TRUTH, bundle))))),
        (Locations.MARKET_CHEST_GAME_THIRD_ROOM_ITEM,
         lambda bundle: can_open_large_chest(bundle) & (((False_()) & small_keys_scene("SCENE_TREASURE_BOX_SHOP", 3, bundle) | (Not(False_())) & (has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN") & can_use(Items.LENS_OF_TRUTH, bundle))))),
        (Locations.MARKET_CHEST_GAME_FOURTH_ROOM_KEY,
         lambda bundle: can_open_large_chest(bundle) & (((False_()) & small_keys_scene("SCENE_TREASURE_BOX_SHOP", 4, bundle) | (Not(False_())) & (has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN") & can_use(Items.LENS_OF_TRUTH, bundle))))),
        (Locations.MARKET_CHEST_GAME_FOURTH_ROOM_ITEM,
         lambda bundle: can_open_large_chest(bundle) & (((False_()) & small_keys_scene("SCENE_TREASURE_BOX_SHOP", 4, bundle) | (Not(False_())) & (has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN") & can_use(Items.LENS_OF_TRUTH, bundle))))),
        (Locations.MARKET_CHEST_GAME_FIFTH_ROOM_KEY,
         lambda bundle: can_open_large_chest(bundle) & (((False_()) & small_keys_scene("SCENE_TREASURE_BOX_SHOP", 5, bundle) | (Not(False_())) & (has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN") & can_use(Items.LENS_OF_TRUTH, bundle))))),
        (Locations.MARKET_CHEST_GAME_FIFTH_ROOM_ITEM,
         lambda bundle: can_open_large_chest(bundle) & (((False_()) & small_keys_scene("SCENE_TREASURE_BOX_SHOP", 5, bundle) | (Not(False_())) & (has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN") & can_use(Items.LENS_OF_TRUTH, bundle))))),
        (Locations.MARKET_TREASURE_CHEST_GAME_REWARD,
         lambda bundle: can_open_large_chest(bundle) & (((False_()) & small_keys_scene("SCENE_TREASURE_BOX_SHOP", 6, bundle) | (Not(False_())) & (has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN") & can_use(Items.LENS_OF_TRUTH, bundle))))),
    ])
    # Connections
    connect_regions(Regions.MARKET_TREASURE_CHEST_GAME, world, [
        (Regions.THE_MARKET,
         lambda bundle: True_()),
    ])

    # Market Bombchu Shop  (upstream RR_MARKET_BOMBCHU_SHOP, SCENE_BOMBCHU_SHOP)
    # Locations
    add_locations(Regions.MARKET_BOMBCHU_SHOP, world, [
        (Locations.MARKET_BOMBCHU_SHOP_ITEM1,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_BOMBCHU_SHOP_ITEM1, bundle)),
        (Locations.MARKET_BOMBCHU_SHOP_ITEM2,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_BOMBCHU_SHOP_ITEM2, bundle)),
        (Locations.MARKET_BOMBCHU_SHOP_ITEM3,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_BOMBCHU_SHOP_ITEM3, bundle)),
        (Locations.MARKET_BOMBCHU_SHOP_ITEM4,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_BOMBCHU_SHOP_ITEM4, bundle)),
        (Locations.MARKET_BOMBCHU_SHOP_ITEM5,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_BOMBCHU_SHOP_ITEM5, bundle)),
        (Locations.MARKET_BOMBCHU_SHOP_ITEM6,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_BOMBCHU_SHOP_ITEM6, bundle)),
        (Locations.MARKET_BOMBCHU_SHOP_ITEM7,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_BOMBCHU_SHOP_ITEM7, bundle)),
        (Locations.MARKET_BOMBCHU_SHOP_ITEM8,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.MARKET_BOMBCHU_SHOP_ITEM8, bundle)),
    ])
    # Connections
    connect_regions(Regions.MARKET_BOMBCHU_SHOP, world, [
        (Regions.MARKET_BACK_ALLEY,
         lambda bundle: True_()),
    ])

    # Market Dog Lady House  (upstream RR_MARKET_DOG_LADY_HOUSE, SCENE_DOG_LADY_HOUSE)
    # Locations
    add_locations(Regions.MARKET_DOG_LADY_HOUSE, world, [
        (Locations.MARKET_LOST_DOG,
         lambda bundle: is_child(bundle) & at_night(bundle) & has_speak(bundle, "HYLIAN")),
        (Locations.MARKET_LOST_DOG_HOUSE_CRATE,
         lambda bundle: can_break_crates(bundle)),
    ])
    # Connections
    connect_regions(Regions.MARKET_DOG_LADY_HOUSE, world, [
        (Regions.MARKET_BACK_ALLEY,
         lambda bundle: True_()),
    ])

    # Market Man in Green House  (upstream RR_MARKET_MAN_IN_GREEN_HOUSE, SCENE_BACK_ALLEY_HOUSE)
    # Locations
    add_locations(Regions.MARKET_MAN_IN_GREEN_HOUSE, world, [
        (Locations.MARKET_BACK_ALLEY_HOUSE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.MARKET_BACK_ALLEY_HOUSE_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.MARKET_BACK_ALLEY_HOUSE_POT3,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.MARKET_MAN_IN_GREEN_HOUSE, world, [
        (Regions.MARKET_BACK_ALLEY,
         lambda bundle: True_()),
    ])

# ---- summary
# notes: ['TODO feature 3.10']
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_BORROW_MASKS', 'CAN_DEFEAT_BIG_POE', 'CAN_EMPTY_BIG_POES', 'COULD_PLAY_BOWLING', 'KAKARIKO_GATE_OPEN']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (10): ['RC_MKT_WONDER_DAY_1', 'RC_MKT_WONDER_DAY_2', 'RC_MKT_WONDER_DAY_3', 'RC_MKT_WONDER_DAY_4', 'RC_MKT_WONDER_DAY_5', 'RC_MKT_WONDER_NIGHT_1', 'RC_MKT_WONDER_NIGHT_2', 'RC_MK_MASK_SHOP_SIGN', 'RC_MK_SHOOTING_GALLERY_RECTANGLE_SIGN', 'RC_MARKET_TREASURE_CHEST_GAME_SHOPKEEPER']
