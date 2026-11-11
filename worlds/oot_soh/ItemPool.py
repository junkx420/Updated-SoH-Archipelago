from typing import TYPE_CHECKING

from .Enums import *
from .Items import item_data_table, filler_items, no_rules_bottles, SohItem
from .Regions import dungeon_reward_item_mapping, small_key_vanilla_mapping, dungeon_boss_key_vanilla_mapping
from .LogicHelpers import key_to_ring, GBK_TRIGGER_OPTIONS
from .KeyShuffle import small_key_option_matching
from BaseClasses import ItemClassification
from .SongShuffle import song_vanilla_locations, get_shuffled_songs
from .ShopItems import get_vanilla_shop_pool
from .Options import *

if TYPE_CHECKING:
    from . import SohWorld


BEAN_SOULS = [Items.DEATH_MOUNTAIN_CRATER_BEAN_SOUL, Items.DEATH_MOUNTAIN_TRAIL_BEAN_SOUL, Items.DESERT_COLOSSUS_BEAN_SOUL, Items.GERUDO_VALLEY_BEAN_SOUL, Items.GRAVEYARD_BEAN_SOUL, Items.KOKIRI_FOREST_BEAN_SOUL, Items.LAKE_HYLIA_BEAN_SOUL, Items.LOST_WOODS_BRIDGE_BEAN_SOUL, Items.LOST_WOODS_BEAN_SOUL, Items.ZORAS_RIVER_BEAN_SOUL]


def create_item_pool(world: "SohWorld") -> None:
    items_to_create: dict[str, int] = {
        item: data.quantity_in_item_pool for item, data in item_data_table.items()}

    # King Zora
    if world.options.zoras_fountain == "open":
        items_to_create[Items.BOTTLE_WITH_RUTOS_LETTER] = 0

    # Overworld door keys
    if world.options.lock_overworld_doors:
        items_to_create[Items.GUARD_HOUSE_KEY] = 1
        items_to_create[Items.MARKET_BAZAAR_KEY] = 1
        items_to_create[Items.MARKET_POTION_SHOP_KEY] = 1
        items_to_create[Items.MASK_SHOP_KEY] = 1
        items_to_create[Items.MARKET_SHOOTING_GALLERY_KEY] = 1
        items_to_create[Items.BOMBCHU_BOWLING_KEY] = 1
        items_to_create[Items.TREASURE_CHEST_GAME_BUILDING_KEY] = 1
        items_to_create[Items.BOMBCHU_SHOP_KEY] = 1
        items_to_create[Items.RICHARDS_HOUSE_KEY] = 1
        items_to_create[Items.ALLEY_HOUSE_KEY] = 1
        items_to_create[Items.KAK_BAZAAR_KEY] = 1
        items_to_create[Items.KAK_POTION_SHOP_KEY] = 1
        items_to_create[Items.BOSS_HOUSE_KEY] = 1
        items_to_create[Items.GRANNYS_POTION_SHOP_KEY] = 1
        items_to_create[Items.SKULLTULA_HOUSE_KEY] = 1
        items_to_create[Items.IMPAS_HOUSE_KEY] = 1
        items_to_create[Items.WINDMILL_KEY] = 1
        items_to_create[Items.KAK_SHOOTING_GALLERY_KEY] = 1
        items_to_create[Items.DAMPES_HUT_KEY] = 1
        items_to_create[Items.TALONS_HOUSE_KEY] = 1
        items_to_create[Items.STABLES_KEY] = 1
        items_to_create[Items.BACK_TOWER_KEY] = 1
        items_to_create[Items.HYLIA_LAB_KEY] = 1
        items_to_create[Items.FISHING_HOLE_KEY] = 1

    # Gerudo Fortress Keys
    if world.options.fortress_carpenters == "fast":
        items_to_create[Items.GERUDO_FORTRESS_SMALL_KEY] = 1

    if world.options.fortress_carpenters == "free":
        items_to_create[Items.GERUDO_FORTRESS_SMALL_KEY] = 0

    # Tycoon Wallet
    if world.options.shuffle_tycoon_wallet:
        items_to_create[Items.PROGRESSIVE_WALLET] += 1

    # Ocarina Buttons
    if world.options.shuffle_ocarina_buttons:
        items_to_create[Items.OCARINA_A_BUTTON] = 1
        items_to_create[Items.OCARINA_CDOWN_BUTTON] = 1
        items_to_create[Items.OCARINA_CLEFT_BUTTON] = 1
        items_to_create[Items.OCARINA_CRIGHT_BUTTON] = 1
        items_to_create[Items.OCARINA_CUP_BUTTON] = 1

    # Fishing Pole
    if world.options.shuffle_fishing_pole:
        items_to_create[Items.FISHING_POLE] = 1

    # Merchants
    if world.options.shuffle_merchants not in ("all", "bean_merchant_only"):
        items_to_create[Items.MAGIC_BEAN_PACK] = 0

    if world.options.shuffle_merchants in ("all", "all_but_beans"):
        items_to_create[Items.GIANTS_KNIFE] = 1

    # Progressive Goron Sword (9.3.1 item_pool.cpp): two progressive swords instead of Biggoron's Sword and the
    # merchant Giant's Knife
    if world.options.progressive_goron_sword:
        items_to_create[Items.PROGRESSIVE_GORON_SWORD] = 2
        items_to_create[Items.BIGGORONS_SWORD] = 0
        items_to_create[Items.GIANTS_KNIFE] = 0

    # Adult Trade Items
    if world.options.shuffle_adult_trade_items:
        items_to_create[Items.POCKET_EGG] = 1
        items_to_create[Items.COJIRO] = 1
        items_to_create[Items.ODD_MUSHROOM] = 1
        items_to_create[Items.ODD_POTION] = 1
        items_to_create[Items.POACHERS_SAW] = 1
        items_to_create[Items.BROKEN_GORONS_SWORD] = 1
        items_to_create[Items.PRESCRIPTION] = 1
        items_to_create[Items.EYEBALL_FROG] = 1
        items_to_create[Items.WORLDS_FINEST_EYEDROPS] = 1

    # Boss Souls
    if world.options.shuffle_boss_souls:
        items_to_create[Items.GOHMAS_SOUL] = 1
        items_to_create[Items.KING_DODONGOS_SOUL] = 1
        items_to_create[Items.BARINADES_SOUL] = 1
        items_to_create[Items.PHANTOM_GANONS_SOUL] = 1
        items_to_create[Items.VOLVAGIAS_SOUL] = 1
        items_to_create[Items.MORPHAS_SOUL] = 1
        items_to_create[Items.BONGO_BONGOS_SOUL] = 1
        items_to_create[Items.TWINROVAS_SOUL] = 1

    # Win Condition "Anywhere": the Triforce is a multiworld item (9.3.1 RO_WINCON_ANYWHERE)
    if world.options.win_condition == WinCondition.option_anywhere:
        items_to_create[Items.TRIFORCE] = 1

    # Ganon's Soul (own setting since 9.3.1; "On + Ganon" is migrated to "anywhere" in Options.adjust_ganons_soul).
    # any_dungeon / overworld are placed by the dungeon item prefill (KeyShuffle.get_dungeon_item_prefill_items).
    if world.options.ganons_soul in (GanonsSoul.option_any_dungeon, GanonsSoul.option_overworld, GanonsSoul.option_anywhere):
        items_to_create[Items.GANONS_SOUL] = 1

    # Maps and Compasses
    if world.options.maps_and_compasses not in (SmallKeyShuffle.option_start_with, SmallKeyShuffle.option_vanilla):
        items_to_create[Items.GREAT_DEKU_TREE_MAP] = 1
        items_to_create[Items.DODONGOS_CAVERN_MAP] = 1
        items_to_create[Items.JABU_JABUS_BELLY_MAP] = 1
        items_to_create[Items.FOREST_TEMPLE_MAP] = 1
        items_to_create[Items.FIRE_TEMPLE_MAP] = 1
        items_to_create[Items.WATER_TEMPLE_MAP] = 1
        items_to_create[Items.SPIRIT_TEMPLE_MAP] = 1
        items_to_create[Items.SHADOW_TEMPLE_MAP] = 1
        items_to_create[Items.BOTTOM_OF_THE_WELL_MAP] = 1
        items_to_create[Items.ICE_CAVERN_MAP] = 1
        items_to_create[Items.GREAT_DEKU_TREE_COMPASS] = 1
        items_to_create[Items.DODONGOS_CAVERN_COMPASS] = 1
        items_to_create[Items.JABU_JABUS_BELLY_COMPASS] = 1
        items_to_create[Items.FOREST_TEMPLE_COMPASS] = 1
        items_to_create[Items.FIRE_TEMPLE_COMPASS] = 1
        items_to_create[Items.WATER_TEMPLE_COMPASS] = 1
        items_to_create[Items.SPIRIT_TEMPLE_COMPASS] = 1
        items_to_create[Items.SHADOW_TEMPLE_COMPASS] = 1
        items_to_create[Items.BOTTOM_OF_THE_WELL_COMPASS] = 1
        items_to_create[Items.ICE_CAVERN_COMPASS] = 1

    # Ganon's Castle Boss Key; with a trigger option (lacs_*) the client grants it, see location_access/archipelago.py
    # (none with the Triforce Pieces win condition either, as with Triforce Hunt before the Win Condition option)
    if (world.options.win_condition != WinCondition.option_trigger_triforce_pieces
            and world.options.ganons_castle_boss_key.value not in GBK_TRIGGER_OPTIONS):
        items_to_create[Items.GANONS_CASTLE_BOSS_KEY] = 1

    # Keys
    if world.options.forest_temple_key_ring:
        items_to_create[Items.FOREST_TEMPLE_SMALL_KEY] = 0
        items_to_create[Items.FOREST_TEMPLE_KEY_RING] = 1
    if world.options.fire_temple_key_ring:
        items_to_create[Items.FIRE_TEMPLE_SMALL_KEY] = 0
        items_to_create[Items.FIRE_TEMPLE_KEY_RING] = 1
    if world.options.water_temple_key_ring:
        items_to_create[Items.WATER_TEMPLE_SMALL_KEY] = 0
        items_to_create[Items.WATER_TEMPLE_KEY_RING] = 1
    if world.options.spirit_temple_key_ring:
        items_to_create[Items.SPIRIT_TEMPLE_SMALL_KEY] = 0
        items_to_create[Items.SPIRIT_TEMPLE_KEY_RING] = 1
    if world.options.shadow_temple_key_ring:
        items_to_create[Items.SHADOW_TEMPLE_SMALL_KEY] = 0
        items_to_create[Items.SHADOW_TEMPLE_KEY_RING] = 1
    if world.options.bottom_of_the_well_key_ring:
        items_to_create[Items.BOTTOM_OF_THE_WELL_SMALL_KEY] = 0
        items_to_create[Items.BOTTOM_OF_THE_WELL_KEY_RING] = 1
    if world.options.gerudo_training_ground_key_ring:
        items_to_create[Items.TRAINING_GROUND_SMALL_KEY] = 0
        items_to_create[Items.TRAINING_GROUND_KEY_RING] = 1
    if world.options.ganons_castle_key_ring:
        items_to_create[Items.GANONS_CASTLE_SMALL_KEY] = 0
        items_to_create[Items.GANONS_CASTLE_KEY_RING] = 1

    # Gerudo Fortress Keys
    if world.options.gerudo_fortress_key_shuffle != GerudoFortressKeyShuffle.option_vanilla:
        if world.options.gerudo_fortress_key_ring:
            items_to_create[Items.GERUDO_FORTRESS_SMALL_KEY] = 0
            items_to_create[Items.GERUDO_FORTRESS_KEY_RING] = 1
    else:
        items_to_create[Items.GERUDO_FORTRESS_SMALL_KEY] = 0

    # Big Poe Bottle
    if world.options.big_poe_target_count == 0:
        items_to_create[Items.BOTTLE_WITH_BIG_POE] = 0

    # Bombchu bag
    if world.options.bombchu_bag == "single_bag":
        items_to_create[Items.BOMBCHUS_5] = 0
        items_to_create[Items.BOMBCHUS_10] = 0
        items_to_create[Items.BOMBCHUS_20] = 0
        if world.options.shuffle_merchants in ("all_but_beans", "all"):
            items_to_create[Items.BOMBCHU_BAG] = 6
        else:
            items_to_create[Items.BOMBCHU_BAG] = 5
    elif world.options.bombchu_bag == "progressive_bags":
        items_to_create[Items.BOMBCHU_BAG] = 3

    # Infinite Upgrades
    if world.options.infinite_upgrades == "progressive":
        items_to_create[Items.PROGRESSIVE_BOMB_BAG] += 1
        items_to_create[Items.PROGRESSIVE_BOW] += 1
        items_to_create[Items.PROGRESSIVE_NUT_CAPACITY] += 1
        items_to_create[Items.PROGRESSIVE_SLINGSHOT] += 1
        items_to_create[Items.PROGRESSIVE_STICK_CAPACITY] += 1
        items_to_create[Items.PROGRESSIVE_MAGIC_METER] += 1
        items_to_create[Items.PROGRESSIVE_WALLET] += 1
        if world.options.bombchu_bag == "progressive_bags":
            items_to_create[Items.BOMBCHU_BAG] += 1

    # Skeleton Key
    if world.options.skeleton_key:
        items_to_create[Items.SKELETON_KEY] = 1

    # Roc's Feather
    if world.options.rocs_feather:
        items_to_create[Items.ROCS_FEATHER] = 1

    # Shuffle Scarecrow's Song (3drando/item_pool.cpp): unless it's a starting item ("Skip Scarecrow's Song")
    if world.options.shuffle_scarecrows_song and not world.options.skip_scarecrows_song:
        items_to_create[Items.SCARECROWS_SONG] = 1

    # Shuffle Masks (3drando/item_pool.cpp): every mask that isn't a starting mask goes into the pool
    if world.options.shuffle_masks:
        if not world.options.start_with_keaton_mask:
            items_to_create[Items.KEATON_MASK] = 1
        if not world.options.start_with_skull_mask:
            items_to_create[Items.SKULL_MASK] = 1
        if not world.options.start_with_spooky_mask:
            items_to_create[Items.SPOOKY_MASK] = 1
        if not world.options.start_with_bunny_hood:
            items_to_create[Items.BUNNY_HOOD] = 1
        if not world.options.start_with_goron_mask:
            items_to_create[Items.GORON_MASK] = 1
        if not world.options.start_with_zora_mask:
            items_to_create[Items.ZORA_MASK] = 1
        if not world.options.start_with_gerudo_mask:
            items_to_create[Items.GERUDO_MASK] = 1
        if not world.options.start_with_mask_of_truth:
            items_to_create[Items.MASK_OF_TRUTH] = 1

    # Shuffle Bean Souls (3drando/item_pool.cpp): one soul per bean patch (2 each with plentiful, see below)
    if world.options.shuffle_bean_souls:
        for soul in BEAN_SOULS:
            items_to_create[soul] = 1

    # Shuffle Treasure Chest Game (3drando/item_pool.cpp): a key ring or 6 small keys (7 / 2 with plentiful, see below)
    if world.options.shuffle_treasure_chest_game:
        if world.options.chest_game_key_ring:
            items_to_create[Items.TREASURE_GAME_KEY_RING] = 1
        else:
            items_to_create[Items.TREASURE_GAME_SMALL_KEY] = 6

    # Max Hearts logic for Item Pool
    max_hearts: int = 20
    if world.options.item_pool == "scarce":
        max_hearts = 12
    elif world.options.item_pool == "minimal":
        max_hearts = 3

    starting_hearts: int = world.multiworld.state.soh_heart_count[world.player]
    if starting_hearts < max_hearts:
        items_to_create[Items.PIECE_OF_HEART_WINNER] = 1
        items_to_create[Items.PIECE_OF_HEART] = 3
        starting_hearts += 1
        if starting_hearts < max_hearts:
            hearts_to_place: int = max_hearts - starting_hearts
            if world.options.item_pool in ("plentiful", "minimal"):
                items_to_create[Items.HEART_CONTAINER] = hearts_to_place
            elif world.options.item_pool == "balanced":
                half_hearts: int = int(hearts_to_place / 2)
                items_to_create[Items.HEART_CONTAINER] = hearts_to_place - half_hearts
                items_to_create[Items.PIECE_OF_HEART] += half_hearts * 4
            elif world.options.item_pool == "scarce":
                items_to_create[Items.PIECE_OF_HEART] += hearts_to_place * 4

    # Item Pool Modifications
    if world.options.item_pool.value:
        if world.options.item_pool == "plentiful":
            # This plentiful stuff we might want to add to when we check these above. For simplicity I'll recheck stuff here for now
            if world.options.shuffle_ocarinas and not world.options.start_with_ocarina == "ocarina_of_time":
                items_to_create[Items.PROGRESSIVE_OCARINA] += 1

            if world.options.shuffle_merchants in ("all", "bean_merchant_only") and not world.options.start_with_magic_beans:
                items_to_create[Items.MAGIC_BEAN_PACK] += 1

            if world.options.shuffle_skull_tokens:
                items_to_create[Items.GOLD_SKULLTULA_TOKEN] += 10

            if world.options.shuffle_treasure_chest_game:
                if world.options.chest_game_key_ring:
                    items_to_create[Items.TREASURE_GAME_KEY_RING] += 1
                else:
                    items_to_create[Items.TREASURE_GAME_SMALL_KEY] += 1

            if world.options.gerudo_fortress_key_ring and world.options.fortress_carpenters == "normal":
                items_to_create[Items.GERUDO_FORTRESS_KEY_RING] += 1
            else:
                items_to_create[Items.GERUDO_FORTRESS_SMALL_KEY] += 1

            if world.options.shuffle_gerudo_membership_card:
                items_to_create[Items.GERUDO_MEMBERSHIP_CARD] += 1

            if world.options.bombchu_bag in ("single_bag", "progressive_bags"):
                items_to_create[Items.BOMBCHU_BAG] += 1

            items_to_create[Items.BOOMERANG] += 1
            items_to_create[Items.LENS_OF_TRUTH] += 1
            items_to_create[Items.MEGATON_HAMMER] += 1
            items_to_create[Items.IRON_BOOTS] += 1
            items_to_create[Items.GORON_TUNIC] += 1
            items_to_create[Items.ZORA_TUNIC] += 1
            items_to_create[Items.HOVER_BOOTS] += 1
            items_to_create[Items.MIRROR_SHIELD] += 1
            items_to_create[Items.STONE_OF_AGONY] += 1
            items_to_create[Items.FIRE_ARROW] += 1
            items_to_create[Items.ICE_ARROW] += 1
            items_to_create[Items.LIGHT_ARROW] += 1
            items_to_create[Items.DINS_FIRE] += 1
            items_to_create[Items.NAYRUS_LOVE] += 1
            items_to_create[Items.STRENGTH_UPGRADE] += 1
            items_to_create[Items.DOUBLE_DEFENSE] += 1
            items_to_create[Items.PROGRESSIVE_BOW] += 1
            items_to_create[Items.PROGRESSIVE_SLINGSHOT] += 1
            items_to_create[Items.PROGRESSIVE_BOMB_BAG] += 1
            items_to_create[Items.PROGRESSIVE_MAGIC_METER] += 1
            items_to_create[Items.PROGRESSIVE_WALLET] += 1
            items_to_create[Items.PROGRESSIVE_STICK_CAPACITY] += 1
            items_to_create[Items.PROGRESSIVE_NUT_CAPACITY] += 1

            if world.options.shuffle_kokiri_sword and not world.options.start_with_kokiri_sword:
                items_to_create[Items.KOKIRI_SWORD] += 1

            if world.options.shuffle_master_sword and not world.options.start_with_master_sword:
                items_to_create[Items.MASTER_SWORD] += 1

            if world.options.shuffle_weird_egg == ShuffleWeirdEgg.option_on:
                items_to_create[Items.WEIRD_EGG] += 1

            if world.options.shuffle_ocarina_buttons:
                items_to_create[Items.OCARINA_A_BUTTON] += 1
                items_to_create[Items.OCARINA_CUP_BUTTON] += 1
                items_to_create[Items.OCARINA_CDOWN_BUTTON] += 1
                items_to_create[Items.OCARINA_CLEFT_BUTTON] += 1
                items_to_create[Items.OCARINA_CRIGHT_BUTTON] += 1

            items_to_create[Items.PROGRESSIVE_SCALE] += 1

            if world.options.shuffle_fishing_pole:
                items_to_create[Items.FISHING_POLE] += 1

            if world.options.shuffle_adult_trade_items:
                items_to_create[Items.POCKET_EGG] += 1
                items_to_create[Items.COJIRO] += 1
                items_to_create[Items.ODD_MUSHROOM] += 1
                items_to_create[Items.POACHERS_SAW] += 1
                items_to_create[Items.BROKEN_GORONS_SWORD] += 1
                items_to_create[Items.PRESCRIPTION] += 1
                items_to_create[Items.EYEBALL_FROG] += 1
                items_to_create[Items.WORLDS_FINEST_EYEDROPS] += 1

            items_to_create[Items.CLAIM_CHECK] += 1

            if world.options.shuffle_bean_souls:
                for soul in BEAN_SOULS:
                    items_to_create[soul] += 1

            if world.options.shuffle_boss_souls:
                items_to_create[Items.GOHMAS_SOUL] += 1
                items_to_create[Items.KING_DODONGOS_SOUL] += 1
                items_to_create[Items.BARINADES_SOUL] += 1
                items_to_create[Items.PHANTOM_GANONS_SOUL] += 1
                items_to_create[Items.VOLVAGIAS_SOUL] += 1
                items_to_create[Items.MORPHAS_SOUL] += 1
                items_to_create[Items.BONGO_BONGOS_SOUL] += 1
                items_to_create[Items.TWINROVAS_SOUL] += 1
                if world.options.shuffle_boss_souls == "on_plus_ganons":
                    items_to_create[Items.GANONS_SOUL] += 1

            if world.options.lock_overworld_doors:
                items_to_create[Items.GUARD_HOUSE_KEY] += 1
                items_to_create[Items.MARKET_BAZAAR_KEY] += 1
                items_to_create[Items.MARKET_POTION_SHOP_KEY] += 1
                items_to_create[Items.MASK_SHOP_KEY] += 1
                items_to_create[Items.MARKET_SHOOTING_GALLERY_KEY] += 1
                items_to_create[Items.BOMBCHU_BOWLING_KEY] += 1
                items_to_create[Items.TREASURE_CHEST_GAME_BUILDING_KEY] += 1
                items_to_create[Items.BOMBCHU_SHOP_KEY] += 1
                items_to_create[Items.RICHARDS_HOUSE_KEY] += 1
                items_to_create[Items.ALLEY_HOUSE_KEY] += 1
                items_to_create[Items.KAK_BAZAAR_KEY] += 1
                items_to_create[Items.KAK_POTION_SHOP_KEY] += 1
                items_to_create[Items.BOSS_HOUSE_KEY] += 1
                items_to_create[Items.GRANNYS_POTION_SHOP_KEY] += 1
                items_to_create[Items.SKULLTULA_HOUSE_KEY] += 1
                items_to_create[Items.IMPAS_HOUSE_KEY] += 1
                items_to_create[Items.WINDMILL_KEY] += 1
                items_to_create[Items.KAK_SHOOTING_GALLERY_KEY] += 1
                items_to_create[Items.DAMPES_HUT_KEY] += 1
                items_to_create[Items.TALONS_HOUSE_KEY] += 1
                items_to_create[Items.STABLES_KEY] += 1
                items_to_create[Items.BACK_TOWER_KEY] += 1
                items_to_create[Items.HYLIA_LAB_KEY] += 1
                items_to_create[Items.FISHING_HOLE_KEY] += 1

            if world.options.small_key_shuffle not in (SmallKeyShuffle.option_start_with, SmallKeyShuffle.option_vanilla):
                small_key_mapping = small_key_option_matching(world)
                for key in small_key_vanilla_mapping.keys():
                    if small_key_mapping[key].Option:
                        items_to_create[key_to_ring[key]] += 1
                    else:
                        items_to_create[key] += 1

            if world.options.boss_key_shuffle not in (SmallKeyShuffle.option_start_with, SmallKeyShuffle.option_vanilla):
                for key in dungeon_boss_key_vanilla_mapping.values():
                    items_to_create[key] += 1

            if world.options.ganons_castle_boss_key == "anywhere":
                items_to_create[Items.GANONS_CASTLE_BOSS_KEY] += 1

            if world.options.shuffle_songs == "anywhere":
                for song in get_shuffled_songs(world):
                    items_to_create[song] += 1

        elif world.options.item_pool == "scarce":
            if world.options.bombchu_bag == "single_bag":
                items_to_create[Items.BOMBCHU_BAG] = 3
            elif world.options.bombchu_bag == "progressive_bags":
                items_to_create[Items.BOMBCHU_BAG] -= 1

            items_to_create[Items.BOMBCHUS_5] = 1
            items_to_create[Items.BOMBCHUS_10] = 2
            items_to_create[Items.BOMBCHUS_20] = 0
            items_to_create[Items.NAYRUS_LOVE] = 0
            items_to_create[Items.DOUBLE_DEFENSE] = 0

            items_to_create[Items.PROGRESSIVE_BOW] -= 1
            items_to_create[Items.PROGRESSIVE_SLINGSHOT] -= 1
            items_to_create[Items.PROGRESSIVE_BOMB_BAG] -= 1
            items_to_create[Items.PROGRESSIVE_MAGIC_METER] -= 1
            items_to_create[Items.PROGRESSIVE_STICK_CAPACITY] -= 1
            items_to_create[Items.PROGRESSIVE_NUT_CAPACITY] -= 1

        elif world.options.item_pool == "minimal":
            if world.options.bombchu_bag == "single_bag":
                items_to_create[Items.BOMBCHU_BAG] = 1
            elif world.options.bombchu_bag == "progressive_bags":
                items_to_create[Items.BOMBCHU_BAG] -= 2
            items_to_create[Items.BOMBCHUS_5] = 1
            items_to_create[Items.BOMBCHUS_10] = 0
            items_to_create[Items.BOMBCHUS_20] = 0
            items_to_create[Items.NAYRUS_LOVE] = 0
            items_to_create[Items.DOUBLE_DEFENSE] = 0

            items_to_create[Items.PROGRESSIVE_BOW] -= 2
            items_to_create[Items.PROGRESSIVE_SLINGSHOT] -= 2
            items_to_create[Items.PROGRESSIVE_BOMB_BAG] -= 2
            items_to_create[Items.PROGRESSIVE_MAGIC_METER] -= 1
            items_to_create[Items.PROGRESSIVE_STICK_CAPACITY] -= 2
            items_to_create[Items.PROGRESSIVE_NUT_CAPACITY] -= 2

    # It there are more randomized skulltula tokens than required progression, set the excess to useful
    if items_to_create[Items.GOLD_SKULLTULA_TOKEN] > world.randomized_progressive_skulltula_count:
        items_to_create[Items.GOLD_SKULLTULA_TOKEN] -= create_special_progression_item(
            world, Items.GOLD_SKULLTULA_TOKEN, ItemClassification.useful | ItemClassification.deprioritized | ItemClassification.skip_balancing, items_to_create[Items.GOLD_SKULLTULA_TOKEN] - world.randomized_progressive_skulltula_count)

    # If you start with enough hearts to do everything and tricks aren't enabled make the rest of them useful
    if not (world.options.enable_all_tricks or str(Tricks.FEWER_TUNIC_REQUIREMENTS) in world.options.tricks_in_logic.value):
        min_hearts_needed: int = 3
        if world.multiworld.state.soh_heart_count[world.player] >= min_hearts_needed:
            items_to_create[Items.PIECE_OF_HEART] -= create_special_progression_item(world, Items.PIECE_OF_HEART, ItemClassification.useful, items_to_create[Items.PIECE_OF_HEART])
            items_to_create[Items.PIECE_OF_HEART_WINNER] -= create_special_progression_item(world, Items.PIECE_OF_HEART_WINNER, ItemClassification.useful, items_to_create[Items.PIECE_OF_HEART_WINNER])
            items_to_create[Items.HEART_CONTAINER] -= create_special_progression_item(world, Items.HEART_CONTAINER, ItemClassification.useful, items_to_create[Items.HEART_CONTAINER])
        else:
             # starting health is less than min_hearts_needed
            # Get the total number of heart classifications we have to work with
            total_non_progression_hearts: int = max_hearts - min_hearts_needed

            if total_non_progression_hearts > 0:
                # Heart Piece amount to make useful. Convert to actual hearts, then convert back later
                non_progression_piece_amount: int = int((items_to_create[Items.PIECE_OF_HEART] + items_to_create[Items.PIECE_OF_HEART_WINNER]) / 4)
            
                if total_non_progression_hearts >= non_progression_piece_amount: 
                    items_to_create[Items.PIECE_OF_HEART] -= create_special_progression_item(world, Items.PIECE_OF_HEART, ItemClassification.useful, ((non_progression_piece_amount * 4) - 1))
                    items_to_create[Items.PIECE_OF_HEART_WINNER] -= create_special_progression_item(world, Items.PIECE_OF_HEART_WINNER, ItemClassification.useful, 1)

                    total_non_progression_hearts -= non_progression_piece_amount
                elif world.options.item_pool not in ("plentiful", "minimal"):
                    non_progression_piece_amount = total_non_progression_hearts
                    
                    items_to_create[Items.PIECE_OF_HEART] -= create_special_progression_item(world, Items.PIECE_OF_HEART, ItemClassification.useful, ((non_progression_piece_amount * 4) - 1))
                    items_to_create[Items.PIECE_OF_HEART_WINNER] -= create_special_progression_item(world, Items.PIECE_OF_HEART_WINNER, ItemClassification.useful, 1)

                    total_non_progression_hearts = 0

                # Container amount to make useful
                if total_non_progression_hearts >= items_to_create[Items.HEART_CONTAINER]:
                    items_to_create[Items.HEART_CONTAINER] -= create_special_progression_item(world, Items.HEART_CONTAINER, ItemClassification.useful, items_to_create[Items.HEART_CONTAINER])
                else:
                    items_to_create[Items.HEART_CONTAINER] -= create_special_progression_item(world, Items.HEART_CONTAINER, ItemClassification.useful, total_non_progression_hearts)

    # if Greg isn't necessary to win, make him filler
    if not (world.options.rainbow_bridge == "greg" or (world.options.rainbow_bridge and world.options.rainbow_bridge_greg_modifier) or (world.options.ganons_castle_boss_key and world.options.ganons_castle_boss_key_greg_modifier)):
        items_to_create[Items.GREG_THE_GREEN_RUPEE] -= create_special_progression_item(
            world, Items.GREG_THE_GREEN_RUPEE, ItemClassification.filler)

    # Stone of Agony is Progression unless not required for Grottos
    if world.options.enable_all_tricks or str(Tricks.GROTTOS_WITHOUT_AGONY) in world.options.tricks_in_logic:
        items_to_create[Items.STONE_OF_AGONY] -= create_special_progression_item(
            world, Items.STONE_OF_AGONY, ItemClassification.filler)

    # Ice Arrows set to filler if not useful (blue fire arrows enabled)
    if not world.options.blue_fire_arrows:
        items_to_create[Items.ICE_ARROW] -= create_special_progression_item(
            world, Items.ICE_ARROW, ItemClassification.filler)

    items: list[SohItem] = list()
    # Add regular item pool
    for item, quantity in items_to_create.items():
        items.extend([world.create_item(item) for _ in range(quantity)])

    filler_bottle_amount: int = 2
    if world.options.zoras_fountain == "open":
        filler_bottle_amount += 1
    if world.options.big_poe_target_count == 0:
        filler_bottle_amount += 1

    # Add random filler bottles
    items.extend([world.create_item(get_filler_bottle(world)) for _ in range(filler_bottle_amount)])

    world.add_items_to_item_pool_list(items)


def create_special_progression_item(world: "SohWorld", item: Items, classification: ItemClassification, amount: int = 1) -> int:
    if amount < 1:
        return 0

    items = [world.create_item(item, classification=classification)
             for _ in range(amount)]

    world.add_items_to_item_pool_list(items)

    return amount


def create_triforce_pieces(world: "SohWorld") -> None:
    total_triforce_pieces: int = min(
        get_open_location_count(world), world.options.triforce_hunt_pieces_total.value)

    triforce_pieces_to_win: int = max(1, round(
        total_triforce_pieces * (world.options.triforce_hunt_pieces_required_percentage.value * .01)))

    # Triforce Piece counts of the other triggers, capped at the pieces in the pool
    world.ganons_soul_triforce_pieces_required = min(world.options.ganons_soul_triforce_pieces_required.value,
                                                     total_triforce_pieces)
    world.rainbow_bridge_triforce_pieces_required = min(world.options.rainbow_bridge_triforce_pieces_required.value,
                                                        total_triforce_pieces)
    world.gbk_triforce_pieces_required = min(world.options.ganons_castle_boss_key_triforce_pieces_required.value,
                                             total_triforce_pieces)

    # pieces the logic needs: the win condition, or more if a trigger asks for more
    needed = []
    if world.options.win_condition == WinCondition.option_trigger_triforce_pieces:
        needed.append(triforce_pieces_to_win)
    if world.options.ganons_soul == GanonsSoul.option_trigger_triforce_pieces:
        needed.append(world.ganons_soul_triforce_pieces_required)
    if world.options.rainbow_bridge == RainbowBridge.option_triforce_pieces:
        needed.append(world.rainbow_bridge_triforce_pieces_required)
    if world.options.ganons_castle_boss_key == GanonsCastleBossKey.option_lacs_triforce_pieces:
        needed.append(world.gbk_triforce_pieces_required)
    progression_pieces = max(needed, default=0)

    triforce_pieces_made = [world.create_item(Items.TRIFORCE_PIECE) 
                            for _ in range(progression_pieces)]
    triforce_pieces_made += [world.create_item(Items.TRIFORCE_PIECE, classification=ItemClassification.useful | ItemClassification.skip_balancing) 
                             for _ in range(total_triforce_pieces - progression_pieces)]

    world.add_items_to_item_pool_list(triforce_pieces_made)

    world.options.triforce_hunt_pieces_total.value = total_triforce_pieces
    world.triforce_pieces_required = triforce_pieces_to_win

    if world.using_ut:
        world.triforce_pieces_required = world.passthrough["triforce_hunt_pieces_required"]
        world.ganons_soul_triforce_pieces_required = world.passthrough.get("ganons_soul_triforce_pieces_required", 0)
        world.rainbow_bridge_triforce_pieces_required = world.passthrough.get("rainbow_bridge_triforce_pieces_required", 0)
        world.gbk_triforce_pieces_required = world.passthrough.get("ganons_castle_boss_key_triforce_pieces_required", 0)


def create_filler_item_pool(world: "SohWorld") -> None:
    filler_item_count = get_open_location_count(world)

    # Ice Trap Count
    ice_trap_count = min(filler_item_count, world.options.ice_trap_count.value)
    world.multiworld.itempool += [world.create_item(
        Items.ICE_TRAP) for _ in range(ice_trap_count)]

    filler_item_count -= ice_trap_count

    # Ice Trap Filler Replacement
    ice_traps_to_place: int = int(
        filler_item_count * (world.options.ice_trap_filler_replacement.value * .01))
    world.multiworld.itempool += [world.create_item(
        Items.ICE_TRAP) for _ in range(ice_traps_to_place)]

    filler_item_count -= ice_traps_to_place

    # Add junk items to fill remaining locations
    world.multiworld.itempool += [world.create_item(
        get_filler_item(world)) for _ in range(filler_item_count)]


def get_open_location_count(world: "SohWorld") -> int:
    open_location_count = len(world.multiworld.get_unfilled_locations(
        world.player)) - len(world.item_pool) - len(world.pre_fill_pool) + len(get_vanilla_shop_pool(world))

    return open_location_count


def get_filler_item(world: "SohWorld") -> str:
    return world.random.choice(filler_items)


def get_filler_bottle(world: "SohWorld") -> str:
    return world.random.choice(no_rules_bottles)


def give_starting_items(world: "SohWorld") -> None:
    # these are for making the progressive items collect/remove work properly
    if not world.options.shuffle_swim:
        world.precollect_from_pool(Items.PROGRESSIVE_SCALE)
    if not world.options.shuffle_deku_stick_bag:
        world.precollect_from_pool(Items.PROGRESSIVE_STICK_CAPACITY)
    if not world.options.shuffle_deku_nut_bag:
        world.precollect_from_pool(Items.PROGRESSIVE_NUT_CAPACITY)
    if not world.options.shuffle_childs_wallet:
        world.precollect_from_pool(Items.PROGRESSIVE_WALLET)

    # Pre-Collect Extra Fire Temple Small Key
    if world.options.small_key_shuffle in ("vanilla", "own_dungeon"):
        world.multiworld.push_precollected(
            world.create_item(str(Items.FIRE_TEMPLE_SMALL_KEY), True))


    if world.options.start_with_kokiri_sword:
        world.precollect_from_pool(Items.KOKIRI_SWORD)

    if world.options.start_with_master_sword and world.options.shuffle_master_sword:
        world.precollect_from_pool(Items.MASTER_SWORD)

    # doesn't actually do anything logically since deku shields can be lost
    if world.options.start_with_deku_shield:
        world.push_precollected(world.create_item(Items.DEKU_SHIELD, True))

    if world.options.start_with_ocarina == "fairy_ocarina":
        world.precollect_from_pool(Items.PROGRESSIVE_OCARINA)

    if world.options.start_with_ocarina == "ocarina_of_time":
        world.precollect_from_pool(Items.PROGRESSIVE_OCARINA)
        world.precollect_from_pool(Items.PROGRESSIVE_OCARINA)
    
    if world.options.start_with_magic_beans:
        world.precollect_from_pool(Items.MAGIC_BEAN_PACK)
    
    if world.options.fortress_carpenters == "free":
        world.precollect_from_pool(Items.GERUDO_MEMBERSHIP_CARD)

    shuffled_songs = get_shuffled_songs(world)
    for song in song_vanilla_locations.values():
        if song not in shuffled_songs:
            world.precollect_from_pool(song)

    if world.options.small_key_shuffle == "start_with":
        for key_ring in key_to_ring.values():
            world.precollect_from_pool(key_ring)
        
    if world.options.boss_key_shuffle == "start_with":
        for boss_key in dungeon_boss_key_vanilla_mapping.values():
            world.precollect_from_pool(boss_key)

    # Starting items from SoH 9.3.1 (RSK_STARTING_*): taken out of the pool like upstream item_pool.cpp
    if world.options.start_with_megaton_hammer:
        world.precollect_from_pool(Items.MEGATON_HAMMER)
    if world.options.start_with_boomerang:
        world.precollect_from_pool(Items.BOOMERANG)
    if world.options.start_with_lens_of_truth:
        world.precollect_from_pool(Items.LENS_OF_TRUTH)
    if world.options.start_with_dins_fire:
        world.precollect_from_pool(Items.DINS_FIRE)
    if world.options.start_with_farores_wind:
        world.precollect_from_pool(Items.FARORES_WIND)
    if world.options.start_with_nayrus_love:
        world.precollect_from_pool(Items.NAYRUS_LOVE)
    if world.options.start_with_fire_arrows:
        world.precollect_from_pool(Items.FIRE_ARROW)
    if world.options.start_with_ice_arrows:
        world.precollect_from_pool(Items.ICE_ARROW)
    if world.options.start_with_light_arrows:
        world.precollect_from_pool(Items.LIGHT_ARROW)
    if world.options.start_with_iron_boots:
        world.precollect_from_pool(Items.IRON_BOOTS)
    if world.options.start_with_hover_boots:
        world.precollect_from_pool(Items.HOVER_BOOTS)
    if world.options.start_with_hylian_shield:
        world.precollect_from_pool(Items.HYLIAN_SHIELD)
    if world.options.start_with_mirror_shield:
        world.precollect_from_pool(Items.MIRROR_SHIELD)
    if world.options.start_with_goron_tunic:
        world.precollect_from_pool(Items.GORON_TUNIC)
    if world.options.start_with_zora_tunic:
        world.precollect_from_pool(Items.ZORA_TUNIC)
    if world.options.start_with_stone_of_agony:
        world.precollect_from_pool(Items.STONE_OF_AGONY)
    if world.options.start_with_weird_egg:
        world.precollect_from_pool(Items.WEIRD_EGG)
    if world.options.start_with_claim_check:
        world.precollect_from_pool(Items.CLAIM_CHECK)
    if world.options.start_with_gerudo_card:
        world.precollect_from_pool(Items.GERUDO_MEMBERSHIP_CARD)
    if world.options.start_with_hookshot:
        for _ in range(world.options.start_with_hookshot.value):
            world.precollect_from_pool(Items.PROGRESSIVE_HOOKSHOT)
    if world.options.start_with_bow:
        for _ in range(world.options.start_with_bow.value):
            world.precollect_from_pool(Items.PROGRESSIVE_BOW)
    if world.options.start_with_slingshot:
        for _ in range(world.options.start_with_slingshot.value):
            world.precollect_from_pool(Items.PROGRESSIVE_SLINGSHOT)
    if world.options.start_with_bomb_bag:
        for _ in range(world.options.start_with_bomb_bag.value):
            world.precollect_from_pool(Items.PROGRESSIVE_BOMB_BAG)
    if world.options.start_with_strength:
        for _ in range(world.options.start_with_strength.value):
            world.precollect_from_pool(Items.STRENGTH_UPGRADE)
    if world.options.start_with_scale:
        for _ in range(world.options.start_with_scale.value):  # Shuffle Swim turns the starting scale off
            world.precollect_from_pool(Items.PROGRESSIVE_SCALE)
    if world.options.start_with_wallet:
        for _ in range(world.options.start_with_wallet.value + (1 if world.options.shuffle_childs_wallet else 0)):
            world.precollect_from_pool(Items.PROGRESSIVE_WALLET)
    if world.options.start_with_magic_meter:
        for _ in range(world.options.start_with_magic_meter.value):
            world.precollect_from_pool(Items.PROGRESSIVE_MAGIC_METER)
    if world.options.start_with_bombchu_bag and world.options.bombchu_bag == BombchuBag.option_single_bag:
        world.precollect_from_pool(Items.BOMBCHU_BAG)
    if world.options.start_with_biggorons_sword:
        if world.options.progressive_goron_sword:
            for _ in range(world.options.start_with_biggorons_sword.value):
                world.precollect_from_pool(Items.PROGRESSIVE_GORON_SWORD)
        elif world.options.start_with_biggorons_sword.value == 2:
            world.precollect_from_pool(Items.BIGGORONS_SWORD)
        elif not in_pool(world, Items.GIANTS_KNIFE):
            # without merchant shuffle the knife isn't in the pool (Medigoron sells it)
            world.push_precollected(world.create_item(Items.GIANTS_KNIFE, True))
        else:
            world.precollect_from_pool(Items.GIANTS_KNIFE)
    for bottle in (world.options.start_with_bottle_1, world.options.start_with_bottle_2,
                   world.options.start_with_bottle_3, world.options.start_with_bottle_4):
        if bottle.value == 0:
            continue
        wanted = {1: list(no_rules_bottles), 2: [Items.BOTTLE_WITH_BIG_POE], 3: [Items.BOTTLE_WITH_RUTOS_LETTER]}[bottle.value]
        # a bottle from the pool makes room for it (upstream: starting bottles are removed from the pool)
        pool_bottle = next((b for b in list(wanted) + list(no_rules_bottles)
                            if in_pool(world, b)), None)
        if pool_bottle is not None:
            world.get_item_from_pool(pool_bottle, world.item_pool)
        # as an event item (no ID), like precollect_from_pool: the client gives it at the start, not the server
        world.push_precollected(world.create_item(wanted[0] if bottle.value != 1 else (pool_bottle or wanted[0]), True))
    give_starting_skulltula_tokens(world)


def give_starting_skulltula_tokens(world: "SohWorld") -> None:
    # SoH 9.3.1 RSK_STARTING_SKULLTULA_TOKEN: 3drando/item_pool.cpp only adds (shuffled tokens - starting tokens) to the
    # pool, vanilla-placed tokens stay; 3drando/starting_inventory.cpp gives all starting tokens
    starting_tokens = world.options.starting_skulltula_tokens.value
    if not starting_tokens:
        return
    vanilla_tokens = {ShuffleTokens.option_off: TokenCounts.TOTAL, ShuffleTokens.option_dungeon: TokenCounts.OVERWORLD,
                      ShuffleTokens.option_overworld: TokenCounts.DUNGEON}.get(world.options.shuffle_skull_tokens.value, 0)
    pool_tokens = [item for item in world.item_pool if item.name == Items.GOLD_SKULLTULA_TOKEN.value]
    # the tokens not needed for progression go first, so the pool keeps its progression tokens
    pool_tokens.sort(key=lambda item: item.advancement)
    for item in pool_tokens[:max(0, min(starting_tokens, len(pool_tokens) - vanilla_tokens))]:
        world.item_pool.remove(item)
    # as event items (no ID) and progression, so they count in logic and the server doesn't send them
    for _ in range(starting_tokens):
        world.push_precollected(world.create_item(Items.GOLD_SKULLTULA_TOKEN, True))


def in_pool(world: "SohWorld", item: Items) -> bool:
    item_id = item_data_table[item].item_id
    return any(pool_item.code == item_id for pool_item in world.item_pool)
