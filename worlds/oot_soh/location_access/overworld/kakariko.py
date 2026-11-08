"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/kakariko.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    KAKARIKO_VILLAGE_BUG_ACCESS = "Kakariko Village Bug Access"
    KAKARIKO_VILLAGE_KAKARIKO_GATE_OPEN = "Kakariko Village Kakariko Gate Open"
    KAKARIKO_VILLAGE_SOLD_KEATON_MASK = "Kakariko Village Sold Keaton Mask"
    KAK_CARPENTER_BOSS_HOUSE_WAKE_UP_ADULT_TALON = "Kak Carpenter Boss House Wake Up Adult Talon"
    KAK_WINDMILL_LOWER_DRAIN_WELL = "Kak Windmill Lower Drain Well"


def set_region_rules(world: "SohWorld") -> None:

    # Kakariko Village  (upstream RR_KAKARIKO_VILLAGE, SCENE_KAKARIKO_VILLAGE)
    # Events
    add_events(Regions.KAKARIKO_VILLAGE, world, [
        (EventLocations.KAKARIKO_VILLAGE_BUG_ACCESS, Events.CAN_ACCESS_BUGS,
         lambda bundle: has_grab(bundle)),
        (EventLocations.KAKARIKO_VILLAGE_KAKARIKO_GATE_OPEN, Events.KAKARIKO_GATE_OPEN,
         lambda bundle: is_child(bundle) & has_item(Items.ZELDAS_LETTER, bundle)),
        (EventLocations.KAKARIKO_VILLAGE_SOLD_KEATON_MASK, Events.SOLD_KEATON_MASK,
         lambda bundle: is_child(bundle) & has_item(Events.KAKARIKO_GATE_OPEN, bundle) & has_mask(bundle, "KEATON_MASK") & has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN")),
    ])
    # Locations
    add_locations(Regions.KAKARIKO_VILLAGE, world, [
        (Locations.SHEIK_IN_KAKARIKO,
         lambda bundle: is_adult(bundle) & has_item(Items.FOREST_MEDALLION, bundle) & has_item(Items.FIRE_MEDALLION, bundle) & has_item(Items.WATER_MEDALLION, bundle)),
        (Locations.KAK_ANJU_AS_CHILD,
         lambda bundle: is_child(bundle) & at_day(bundle) & has_climb(bundle) & has_grab(bundle) & can_break_crates(bundle) & has_speak(bundle, "HYLIAN")),
        (Locations.KAK_ANJU_AS_ADULT,
         lambda bundle: is_adult(bundle) & at_day(bundle) & has_speak(bundle, "HYLIAN")),
        (Locations.KAK_TRADE_POCKET_CUCCO,
         lambda bundle: is_adult(bundle) & at_day(bundle) & (can_use(Items.POCKET_EGG, bundle) & has_item(Events.WAKE_UP_ADULT_TALON, bundle))),
        (Locations.KAK_GS_HOUSE_UNDER_CONSTRUCTION,
         lambda bundle: is_child(bundle) & can_get_nighttime_gs(bundle) & (has_grab(bundle) | can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA))),
        (Locations.KAK_GS_SKULLTULA_HOUSE,
         lambda bundle: is_child(bundle) & can_get_nighttime_gs(bundle) & (has_grab(bundle) | can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA))),
        (Locations.KAK_GS_GUARDS_HOUSE,
         lambda bundle: is_child(bundle) & can_get_nighttime_gs(bundle) & (has_grab(bundle) | can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA))),
        (Locations.KAK_GS_TREE,
         lambda bundle: is_child(bundle) & can_get_nighttime_gs(bundle) & can_bonk_trees(bundle) & (has_grab(bundle) | can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA))),
        (Locations.KAK_GS_WATCHTOWER,
         lambda bundle: is_child(bundle) & has_climb(bundle) & (can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.LONGSHOT) | (can_do_trick(Tricks.KAK_TOWER_GS, bundle) & can_jump_slash_except_hammer(bundle))) & can_get_nighttime_gs(bundle)),
        (Locations.KAK_NEAR_POTION_SHOP_POT1,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.KAK_NEAR_POTION_SHOP_POT2,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.KAK_NEAR_POTION_SHOP_POT3,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.KAK_NEAR_IMPAS_HOUSE_POT1,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.KAK_NEAR_IMPAS_HOUSE_POT2,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.KAK_NEAR_IMPAS_HOUSE_POT3,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.KAK_NEAR_GUARDS_HOUSE_POT1,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.KAK_NEAR_GUARDS_HOUSE_POT2,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.KAK_NEAR_GUARDS_HOUSE_POT3,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.KAK_NEAR_GRAVEYARD_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_NEAR_GRAVEYARD_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_NEAR_GRAVEYARD_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_TREE_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_TREE_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_TREE_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_TREE_GRASS4,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_TREE_GRASS5,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_NEAR_OPEN_GROTTO_ADULT_CRATE1,
         lambda bundle: is_adult(bundle) & can_break_crates(bundle)),
        (Locations.KAK_NEAR_OPEN_GROTTO_ADULT_CRATE2,
         lambda bundle: is_adult(bundle) & can_break_crates(bundle)),
        (Locations.KAK_NEAR_OPEN_GROTTO_ADULT_CRATE3,
         lambda bundle: is_adult(bundle) & can_break_crates(bundle)),
        (Locations.KAK_NEAR_OPEN_GROTTO_ADULT_CRATE4,
         lambda bundle: is_adult(bundle) & can_break_crates(bundle)),
        (Locations.KAK_NEAR_POTION_SHOP_ADULT_CRATE,
         lambda bundle: is_adult(bundle) & can_break_crates(bundle)),
        (Locations.KAK_NEAR_SHOOTING_GALLERY_ADULT_CRATE,
         lambda bundle: is_adult(bundle) & can_break_crates(bundle)),
        (Locations.KAK_NEAR_BOARDING_HOUSE_ADULT_CRATE1,
         lambda bundle: is_adult(bundle) & can_break_crates(bundle)),
        (Locations.KAK_NEAR_BOARDING_HOUSE_ADULT_CRATE2,
         lambda bundle: is_adult(bundle) & can_break_crates(bundle)),
        (Locations.KAK_NEAR_IMPAS_HOUSE_ADULT_CRATE1,
         lambda bundle: is_adult(bundle) & can_break_crates(bundle)),
        (Locations.KAK_NEAR_IMPAS_HOUSE_ADULT_CRATE2,
         lambda bundle: is_adult(bundle) & can_break_crates(bundle)),
        (Locations.KAK_NEAR_BAZAAR_ADULT_CRATE1,
         lambda bundle: is_adult(bundle) & can_break_crates(bundle)),
        (Locations.KAK_NEAR_BAZAAR_ADULT_CRATE2,
         lambda bundle: is_adult(bundle) & can_break_crates(bundle)),
        (Locations.KAK_BEHIND_GS_HOUSE_ADULT_CRATE,
         lambda bundle: is_adult(bundle) & can_break_crates(bundle)),
        (Locations.KAK_NEAR_GRAVEYARD_CHILD_CRATE,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
        (Locations.KAK_NEAR_WINDMILL_CHILD_CRATE,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
        (Locations.KAK_NEAR_FENCE_CHILD_CRATE,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
        (Locations.KAK_NEAR_BOARDING_HOUSE_CHILD_CRATE,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
        (Locations.KAK_NEAR_BAZAAR_CHILD_CRATE,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
        # DEFERRED RC_KAK_SILVER_BOULDER: logic->IsAdult && logic->CanUse(RG_SILVER_GAUNTLETS) && (logic->HasItem(RG_CLIMB) || logic->CanUse(RG_HOVER_BOOTS) || (logic->HasItem(RG_LONGSHOT) && ((logic->AtDay && logic->HasItem(RG_POWER_BRACELET)) || (ctx->GetTrickOption(RT_UNINTUITIVE_JUMPS) && logic->CanJumpslash() && logic->TakeDamage()))))
        # DEFERRED RC_KAK_ROCK_1: logic->CanBreakRocks()
        # DEFERRED RC_KAK_ROCK_2: logic->CanBreakRocks()
        (Locations.KAK_TREE,
         lambda bundle: can_bonk_trees(bundle)),
        # DEFERRED RC_KAK_GUARD_GATE_RECTANGLE_SIGN: logic->IsChild && logic->CanRead()
        # DEFERRED RC_KAK_WELL_RECTANGLE_SIGN: logic->IsChild && logic->CanRead()
        # DEFERRED RC_KAK_SOUTHEAST_EXIT_ARROW_SIGN: logic->CanRead()
        # DEFERRED RC_KAK_FRONT_GATE_ARROW_SIGN: logic->CanRead()
        # DEFERRED RC_KAK_WONDER_UNDER_CONSTRUCTION: logic->IsChild
        # DEFERRED RC_KAK_BEGGAR_BUGS: logic->IsAdult && logic->CanUse(RG_BOTTLE_WITH_BUGS)
        # DEFERRED RC_KAK_BEGGAR_FISH: logic->IsAdult && logic->CanUse(RG_BOTTLE_WITH_FISH)
        # DEFERRED RC_KAK_BEGGAR_BLUE_FIRE: logic->IsAdult && logic->CanUse(RG_BOTTLE_WITH_BLUE_FIRE)
    ])
    # Connections
    connect_regions(Regions.KAKARIKO_VILLAGE, world, [
        (Regions.HYRULE_FIELD,
         lambda bundle: True_()),
        (Regions.KAK_CARPENTER_BOSS_HOUSE,
         lambda bundle: has_item(Items.BOSS_HOUSE_KEY, bundle)),
        (Regions.KAK_HOUSE_OF_SKULLTULA,
         lambda bundle: has_item(Items.SKULLTULA_HOUSE_KEY, bundle)),
        (Regions.KAK_IMPAS_HOUSE,
         lambda bundle: has_item(Items.IMPAS_HOUSE_KEY, bundle)),
        (Regions.KAK_WINDMILL_LOWER,
         lambda bundle: has_item(Items.WINDMILL_KEY, bundle)),
        (Regions.KAK_BAZAAR,
         lambda bundle: is_adult(bundle) & at_day(bundle) & has_item(Items.KAK_BAZAAR_KEY, bundle)),
        (Regions.KAK_SHOOTING_GALLERY,
         lambda bundle: is_adult(bundle) & at_day(bundle) & has_item(Items.KAK_SHOOTING_GALLERY_KEY, bundle)),
        (Regions.KAK_WELL,
         lambda bundle: is_adult(bundle) | has_item(Events.DRAIN_WELL, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.BOTTOM_OF_THE_WELL_NAVI_DIVE, bundle) & is_child(bundle) & has_item(Items.BRONZE_SCALE, bundle) & can_jump_slash(bundle))),
        (Regions.KAK_POTION_SHOP,
         lambda bundle: (at_day(bundle) | is_child(bundle)) & has_item(Items.KAK_POTION_SHOP_KEY, bundle)),
        (Regions.KAK_REDEAD_GROTTO,
         lambda bundle: can_open_bomb_grotto(bundle)),
        (Regions.KAK_IMPAS_LEDGE,
         lambda bundle: (is_child(bundle) & ((at_day(bundle) & has_grab(bundle)) | (bunny_hovers(bundle) & can_jump_slash(bundle)))) | (is_adult(bundle) & can_do_trick(Tricks.VISIBLE_COLLISION, bundle))),
        (Regions.KAK_WATCHTOWER,
         lambda bundle: has_climb(bundle) & (is_adult(bundle) | at_day(bundle) | can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.LONGSHOT) | (can_do_trick(Tricks.KAK_TOWER_GS, bundle) & can_jump_slash_except_hammer(bundle)))),
        (Regions.KAK_ROOFTOP,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) | (can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & is_adult(bundle))),
        (Regions.KAK_IMPAS_ROOFTOP,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) | (can_do_trick(Tricks.KAK_ROOFTOP_GS, bundle) & can_use(Items.HOVER_BOOTS, bundle))),
        (Regions.THE_GRAVEYARD,
         lambda bundle: True_()),
        (Regions.KAK_BEHIND_GATE,
         lambda bundle: is_adult(bundle) | has_item(Events.KAKARIKO_GATE_OPEN, bundle)),
        (Regions.KAK_BACKYARD,
         lambda bundle: is_adult(bundle) | bunny_hood(bundle) | (at_day(bundle) & has_grab(bundle))),
        (Regions.KAK_BEHIND_POTION_SHOP,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) | (can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & is_adult(bundle))),
    ])

    # Kak Impas Ledge  (upstream RR_KAK_IMPAS_LEDGE, SCENE_KAKARIKO_VILLAGE)
    # Connections
    connect_regions(Regions.KAK_IMPAS_LEDGE, world, [
        (Regions.KAK_IMPAS_HOUSE_BACK,
         lambda bundle: True_()),
        (Regions.KAKARIKO_VILLAGE,
         lambda bundle: True_()),
    ])

    # Kak Impas Rooftop  (upstream RR_KAK_IMPAS_ROOFTOP, SCENE_KAKARIKO_VILLAGE)
    # Locations
    add_locations(Regions.KAK_IMPAS_ROOFTOP, world, [
        (Locations.KAK_GS_ABOVE_IMPAS_HOUSE,
         lambda bundle: is_adult(bundle) & can_get_nighttime_gs(bundle) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA)),
    ])
    # Connections
    connect_regions(Regions.KAK_IMPAS_ROOFTOP, world, [
        (Regions.KAK_IMPAS_LEDGE,
         lambda bundle: True_()),
        (Regions.KAKARIKO_VILLAGE,
         lambda bundle: True_()),
    ])

    # Kak Watchtower  (upstream RR_KAK_WATCHTOWER, SCENE_KAKARIKO_VILLAGE)
    # Locations
    add_locations(Regions.KAK_WATCHTOWER, world, [
        (Locations.KAK_GS_WATCHTOWER,
         lambda bundle: is_child(bundle) & can_use(Items.DINS_FIRE, bundle) & can_get_nighttime_gs(bundle)),
        # DEFERRED RC_KAK_WATCHTOWER_BUTTERFLY_FAIRY: logic->IsChild && logic->AtDay && logic->CanUse(RG_STICKS)
    ])
    # Connections
    connect_regions(Regions.KAK_WATCHTOWER, world, [
        (Regions.KAKARIKO_VILLAGE,
         lambda bundle: True_()),
        (Regions.KAK_ROOFTOP,
         lambda bundle: can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle)),
    ])

    # Kak Rooftop  (upstream RR_KAK_ROOFTOP, SCENE_KAKARIKO_VILLAGE)
    # Locations
    add_locations(Regions.KAK_ROOFTOP, world, [
        (Locations.KAK_MAN_ON_ROOF,
         lambda bundle: has_speak(bundle, "HYLIAN")),
    ])
    # Connections
    connect_regions(Regions.KAK_ROOFTOP, world, [
        (Regions.KAK_BACKYARD,
         lambda bundle: True_()),
        (Regions.KAK_BEHIND_POTION_SHOP,
         lambda bundle: has_item(Items.HOVER_BOOTS, bundle)),
        (Regions.KAKARIKO_VILLAGE,
         lambda bundle: True_()),
    ])

    # Kak Backyard  (upstream RR_KAK_BACKYARD, SCENE_KAKARIKO_VILLAGE)
    # Locations
    add_locations(Regions.KAK_BACKYARD, world, [
        (Locations.KAK_NEAR_MEDICINE_SHOP_POT1,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
        (Locations.KAK_NEAR_MEDICINE_SHOP_POT2,
         lambda bundle: is_child(bundle) & can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.KAK_BACKYARD, world, [
        (Regions.KAKARIKO_VILLAGE,
         lambda bundle: True_()),
        (Regions.KAK_OPEN_GROTTO,
         lambda bundle: True_()),
        (Regions.KAK_ODD_POTION_BUILDING,
         lambda bundle: is_adult(bundle) & has_item(Items.GRANNYS_POTION_SHOP_KEY, bundle)),
        (Regions.KAK_BEHIND_POTION_SHOP,
         lambda bundle: has_climb(bundle)),
    ])

    # Kak Behind Potion Shop  (upstream RR_KAK_BEHIND_POTION_SHOP, SCENE_KAKARIKO_VILLAGE)
    # Connections
    connect_regions(Regions.KAK_BEHIND_POTION_SHOP, world, [
        (Regions.KAK_BACKYARD,
         lambda bundle: True_()),
        (Regions.KAK_POTION_SHOP,
         lambda bundle: is_adult(bundle) & at_day(bundle) & has_item(Items.KAK_POTION_SHOP_KEY, bundle)),
        (Regions.KAK_ROOFTOP,
         lambda bundle: can_do_trick(Tricks.HOVER_BOOST_SIMPLE, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.MEGATON_HAMMER, bundle)),
    ])

    # Kak Carpenter Boss House  (upstream RR_KAK_CARPENTER_BOSS_HOUSE, SCENE_KAKARIKO_CENTER_GUEST_HOUSE)
    # Events
    add_events(Regions.KAK_CARPENTER_BOSS_HOUSE, world, [
        (EventLocations.KAK_CARPENTER_BOSS_HOUSE_WAKE_UP_ADULT_TALON, Events.WAKE_UP_ADULT_TALON,
         lambda bundle: is_adult(bundle) & can_use(Items.POCKET_EGG, bundle)),
    ])
    # Connections
    connect_regions(Regions.KAK_CARPENTER_BOSS_HOUSE, world, [
        (Regions.KAKARIKO_VILLAGE,
         lambda bundle: True_()),
    ])

    # Kak House of Skulltula  (upstream RR_KAK_HOUSE_OF_SKULLTULA, SCENE_HOUSE_OF_SKULLTULA)
    # Locations
    add_locations(Regions.KAK_HOUSE_OF_SKULLTULA, world, [
        (Locations.KAK_10_GOLD_SKULLTULA_REWARD,
         lambda bundle: has_speak(bundle, "HYLIAN") & gs_count_at_least(bundle, 10)),
        (Locations.KAK_20_GOLD_SKULLTULA_REWARD,
         lambda bundle: has_speak(bundle, "HYLIAN") & gs_count_at_least(bundle, 20)),
        (Locations.KAK_30_GOLD_SKULLTULA_REWARD,
         lambda bundle: has_speak(bundle, "HYLIAN") & gs_count_at_least(bundle, 30)),
        (Locations.KAK_40_GOLD_SKULLTULA_REWARD,
         lambda bundle: has_speak(bundle, "HYLIAN") & gs_count_at_least(bundle, 40)),
        (Locations.KAK_50_GOLD_SKULLTULA_REWARD,
         lambda bundle: has_speak(bundle, "HYLIAN") & gs_count_at_least(bundle, 50)),
        (Locations.KAK_100_GOLD_SKULLTULA_REWARD,
         lambda bundle: has_speak(bundle, "HYLIAN") & gs_count_at_least(bundle, 100)),
    ])
    # Connections
    connect_regions(Regions.KAK_HOUSE_OF_SKULLTULA, world, [
        (Regions.KAKARIKO_VILLAGE,
         lambda bundle: True_()),
    ])

    # Kak Impas House  (upstream RR_KAK_IMPAS_HOUSE, SCENE_IMPAS_HOUSE)
    # Locations
    add_locations(Regions.KAK_IMPAS_HOUSE, world, [
        (Locations.KAK_IMPAS_HOUSE_COW,
         lambda bundle: can_use(Items.EPONAS_SONG, bundle)),
        # DEFERRED RC_KAK_WONDER_ABOVE_COW: true
    ])
    # Connections
    connect_regions(Regions.KAK_IMPAS_HOUSE, world, [
        (Regions.KAKARIKO_VILLAGE,
         lambda bundle: True_()),
    ])

    # Kak Impas House Back  (upstream RR_KAK_IMPAS_HOUSE_BACK, SCENE_IMPAS_HOUSE)
    # Locations
    add_locations(Regions.KAK_IMPAS_HOUSE_BACK, world, [
        (Locations.KAK_IMPAS_HOUSE_FREESTANDING_POH,
         lambda bundle: True_()),
        (Locations.KAK_IMPAS_HOUSE_COW,
         lambda bundle: can_use(Items.EPONAS_SONG, bundle)),
    ])
    # Connections
    connect_regions(Regions.KAK_IMPAS_HOUSE_BACK, world, [
        (Regions.KAK_IMPAS_LEDGE,
         lambda bundle: True_()),
    ])

    # Kak Windmill Lower  (upstream RR_KAK_WINDMILL_LOWER, SCENE_WINDMILL_AND_DAMPES_GRAVE)
    # Events
    add_events(Regions.KAK_WINDMILL_LOWER, world, [
        (EventLocations.KAK_WINDMILL_LOWER_DRAIN_WELL, Events.DRAIN_WELL,
         lambda bundle: is_child(bundle) & can_use(Items.SONG_OF_STORMS, bundle)),
    ])
    # Locations
    add_locations(Regions.KAK_WINDMILL_LOWER, world, [
        (Locations.KAK_WINDMILL_FREESTANDING_POH,
         lambda bundle: can_use(Items.BOOMERANG, bundle)),
        (Locations.SONG_FROM_WINDMILL,
         lambda bundle: is_adult(bundle) & can_use(Items.FAIRY_OCARINA, bundle)),
    ])
    # Connections
    connect_regions(Regions.KAK_WINDMILL_LOWER, world, [
        (Regions.KAKARIKO_VILLAGE,
         lambda bundle: True_()),
        (Regions.KAK_WINDMILL_UPPER,
         lambda bundle: (is_adult(bundle) & (can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) | can_ground_jump(bundle))) | (is_child(bundle) & can_jump_slash(bundle) & can_do_trick(Tricks.KAK_CHILD_WINDMILL_POH, bundle))),
    ])

    # Kak Windmill Upper  (upstream RR_KAK_WINDMILL_UPPER, SCENE_WINDMILL_AND_DAMPES_GRAVE)
    # Locations
    add_locations(Regions.KAK_WINDMILL_UPPER, world, [
        (Locations.KAK_WINDMILL_FREESTANDING_POH,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.KAK_WINDMILL_UPPER, world, [
        (Regions.KAK_WINDMILL_LOWER,
         lambda bundle: True_()),
    ])

    # Kak Bazaar  (upstream RR_KAK_BAZAAR, SCENE_BAZAAR)
    # Locations
    add_locations(Regions.KAK_BAZAAR, world, [
        (Locations.KAK_BAZAAR_ITEM1,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.KAK_BAZAAR_ITEM1, bundle)),
        (Locations.KAK_BAZAAR_ITEM2,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.KAK_BAZAAR_ITEM2, bundle)),
        (Locations.KAK_BAZAAR_ITEM3,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.KAK_BAZAAR_ITEM3, bundle)),
        (Locations.KAK_BAZAAR_ITEM4,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.KAK_BAZAAR_ITEM4, bundle)),
        (Locations.KAK_BAZAAR_ITEM5,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.KAK_BAZAAR_ITEM5, bundle)),
        (Locations.KAK_BAZAAR_ITEM6,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.KAK_BAZAAR_ITEM6, bundle)),
        (Locations.KAK_BAZAAR_ITEM7,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.KAK_BAZAAR_ITEM7, bundle)),
        (Locations.KAK_BAZAAR_ITEM8,
         lambda bundle: has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.KAK_BAZAAR_ITEM8, bundle)),
    ])
    # Connections
    connect_regions(Regions.KAK_BAZAAR, world, [
        (Regions.KAKARIKO_VILLAGE,
         lambda bundle: True_()),
    ])

    # Kak Shooting Gallery  (upstream RR_KAK_SHOOTING_GALLERY, SCENE_SHOOTING_GALLERY)
    # Locations
    add_locations(Regions.KAK_SHOOTING_GALLERY, world, [
        (Locations.KAK_SHOOTING_GALLERY_REWARD,
         lambda bundle: is_adult(bundle) & has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN") & has_item(Items.FAIRY_BOW, bundle)),
        # DEFERRED RC_KAK_SHOOTING_GALLERY_RECTANGLE_SIGN: logic->IsAdult && logic->CanRead()
    ])
    # Connections
    connect_regions(Regions.KAK_SHOOTING_GALLERY, world, [
        (Regions.KAKARIKO_VILLAGE,
         lambda bundle: True_()),
    ])

    # Kak Potion Shop  (upstream RR_KAK_POTION_SHOP, SCENE_POTION_SHOP_KAKARIKO)
    # Locations
    add_locations(Regions.KAK_POTION_SHOP, world, [
        (Locations.KAK_POTION_SHOP_ITEM1,
         lambda bundle: is_adult(bundle) & has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.KAK_POTION_SHOP_ITEM1, bundle)),
        (Locations.KAK_POTION_SHOP_ITEM2,
         lambda bundle: is_adult(bundle) & has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.KAK_POTION_SHOP_ITEM2, bundle)),
        (Locations.KAK_POTION_SHOP_ITEM3,
         lambda bundle: is_adult(bundle) & has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.KAK_POTION_SHOP_ITEM3, bundle)),
        (Locations.KAK_POTION_SHOP_ITEM4,
         lambda bundle: is_adult(bundle) & has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.KAK_POTION_SHOP_ITEM4, bundle)),
        (Locations.KAK_POTION_SHOP_ITEM5,
         lambda bundle: is_adult(bundle) & has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.KAK_POTION_SHOP_ITEM5, bundle)),
        (Locations.KAK_POTION_SHOP_ITEM6,
         lambda bundle: is_adult(bundle) & has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.KAK_POTION_SHOP_ITEM6, bundle)),
        (Locations.KAK_POTION_SHOP_ITEM7,
         lambda bundle: is_adult(bundle) & has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.KAK_POTION_SHOP_ITEM7, bundle)),
        (Locations.KAK_POTION_SHOP_ITEM8,
         lambda bundle: is_adult(bundle) & has_speak(bundle, "HYLIAN") & can_afford_slot(Locations.KAK_POTION_SHOP_ITEM8, bundle)),
    ])
    # Connections
    connect_regions(Regions.KAK_POTION_SHOP, world, [
        (Regions.KAKARIKO_VILLAGE,
         lambda bundle: True_()),
        (Regions.KAK_BEHIND_POTION_SHOP,
         lambda bundle: is_adult(bundle)),
    ])

    # Kak Granny's Potion Shop  (upstream RR_KAK_ODD_POTION_BUILDING, SCENE_POTION_SHOP_GRANNY)
    # Locations
    add_locations(Regions.KAK_ODD_POTION_BUILDING, world, [
        (Locations.KAK_TRADE_ODD_MUSHROOM,
         lambda bundle: is_adult(bundle) & can_use(Items.ODD_MUSHROOM, bundle)),
        (Locations.KAK_GRANNYS_SHOP,
         lambda bundle: is_adult(bundle) & has_speak(bundle, "HYLIAN") & (can_use(Items.ODD_MUSHROOM, bundle) | (True_(options=[OptionFilter(ShuffleAdultTradeItems, False)]) & (has_item(Items.CLAIM_CHECK, bundle) | False_())) & can_afford_slot(Locations.KAK_GRANNYS_SHOP, bundle))),
    ])
    # Connections
    connect_regions(Regions.KAK_ODD_POTION_BUILDING, world, [
        (Regions.KAK_BACKYARD,
         lambda bundle: True_()),
    ])

    # Kak Redead Grotto  (upstream RR_KAK_REDEAD_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.KAK_REDEAD_GROTTO, world, [
        (Locations.KAK_REDEAD_GROTTO_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.REDEAD, EnemyDistance.CLOSE, True, 2) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.KAK_REDEAD_GROTTO, world, [
        (Regions.KAKARIKO_VILLAGE,
         lambda bundle: True_()),
    ])

    # Kak Open Grotto  (upstream RR_KAK_OPEN_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.KAK_OPEN_GROTTO, world, [
        (Locations.KAK_OPEN_GROTTO_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.KAK_OPEN_GROTTO_FISH,
         lambda bundle: has_bottle(bundle)),
        (Locations.KAK_OPEN_GROTTO_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.KAK_OPEN_GROTTO_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_KAK_OPEN_GROTTO_GOSSIP_STONE: true
        (Locations.KAK_OPEN_GROTTO_BEEHIVE_LEFT,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.KAK_OPEN_GROTTO_BEEHIVE_RIGHT,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.KAK_OPEN_GROTTO_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_OPEN_GROTTO_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_OPEN_GROTTO_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_OPEN_GROTTO_GRASS4,
         lambda bundle: can_cut_shrubs(bundle)),
        # DEFERRED RC_KAK_OPEN_GROTTO_BUTTERFLY_FAIRY: logic->CanUse(RG_STICKS)
    ])
    # Connections
    connect_regions(Regions.KAK_OPEN_GROTTO, world, [
        (Regions.KAK_BACKYARD,
         lambda bundle: True_()),
    ])

    # Kak Behind Gate  (upstream RR_KAK_BEHIND_GATE, SCENE_KAKARIKO_VILLAGE)
    # Connections
    connect_regions(Regions.KAK_BEHIND_GATE, world, [
        (Regions.KAKARIKO_VILLAGE,
         lambda bundle: is_adult(bundle) | can_do_trick(Tricks.VISIBLE_COLLISION, bundle) | has_item(Events.KAKARIKO_GATE_OPEN, bundle)),
        (Regions.DEATH_MOUNTAIN_TRAIL,
         lambda bundle: True_()),
    ])

    # Kak Well  (upstream RR_KAK_WELL, SCENE_KAKARIKO_VILLAGE)
    # Connections
    connect_regions(Regions.KAK_WELL, world, [
        (Regions.KAKARIKO_VILLAGE,
         lambda bundle: has_climb(bundle) & (is_adult(bundle) | has_item(Items.BRONZE_SCALE, bundle) | has_item(Events.DRAIN_WELL, bundle))),
        (Regions.BOTW_ENTRYWAY,
         lambda bundle: is_child(bundle) | (has_item(Events.DRAIN_WELL, bundle) & False_())),
    ])

# ---- summary
# notes: ['TODO feature 2.4', 'TODO feature 4.1']
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_BUGS', 'DRAIN_WELL', 'KAKARIKO_GATE_OPEN', 'SOLD_KEATON_MASK', 'WAKE_UP_ADULT_TALON']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (16): ['RC_KAK_SILVER_BOULDER', 'RC_KAK_ROCK_1', 'RC_KAK_ROCK_2', 'RC_KAK_GUARD_GATE_RECTANGLE_SIGN', 'RC_KAK_WELL_RECTANGLE_SIGN', 'RC_KAK_SOUTHEAST_EXIT_ARROW_SIGN', 'RC_KAK_FRONT_GATE_ARROW_SIGN', 'RC_KAK_WONDER_UNDER_CONSTRUCTION', 'RC_KAK_BEGGAR_BUGS', 'RC_KAK_BEGGAR_FISH', 'RC_KAK_BEGGAR_BLUE_FIRE', 'RC_KAK_WATCHTOWER_BUTTERFLY_FAIRY', 'RC_KAK_WONDER_ABOVE_COW', 'RC_KAK_SHOOTING_GALLERY_RECTANGLE_SIGN', 'RC_KAK_OPEN_GROTTO_GOSSIP_STONE', 'RC_KAK_OPEN_GROTTO_BUTTERFLY_FAIRY']
