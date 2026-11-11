import orjson
import pkgutil

from typing import Any, ClassVar, Callable

from BaseClasses import CollectionState, Item, Tutorial, ItemClassification, Location
from rule_builder.cached_world import CachedRuleBuilderWorld
from rule_builder.rules import Has
from worlds.AutoWorld import WebWorld, World
from Fill import fill_restrictive
from .Items import SohItem, item_data_table, item_table, SohItemData, progressive_items
from .Locations import location_table, token_amounts, SohLocData, location_data_table
from .Options import (SohOptions, soh_option_groups, wallet_capacities, LEGACY_TRICKS, GanonsSoul,
                      RainbowBridge, GanonsCastleBossKey)
from .Regions import create_regions_and_locations, place_locked_items
from .Enums import *
from .ItemPool import create_item_pool, create_filler_item_pool, create_triforce_pieces, get_filler_item, give_starting_items
from . import RegionAgeAccess
from .DungeonRewardShuffle import pre_fill_dungeon_rewards, get_pre_fill_rewards
from .KeyShuffle import pre_fill_own_dungeon_items, pre_fill_any_dungeon_keys, pre_fill_overworld_items, get_own_dungeon_prefill_items, get_dungeon_item_prefill_items
from .SongShuffle import pre_fill_songs, get_prefill_songs
from .ShopItems import fill_shop_items, generate_prices
from .Presets import oot_soh_options_presets
from .UniversalTracker import setup_options_from_slot_data
from settings import Group, Bool
from Options import OptionError
from rule_builder.rules import Has, CanReachLocation, Rule, True_
from .Hints import CreateNonlocalHints, StaticHint
from worlds.LauncherComponents import Component, components, Type, launch as launch_component

import logging
logger = logging.getLogger("SOH_OOT")


class SohWebWorld(WebWorld):
    theme = "ice"
    options_presets = oot_soh_options_presets

    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to playing Ship of Harkinian.",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["aMannus"]
    )

    tutorials = [setup_en]
    game_info_languages = ["en"]
    option_groups = soh_option_groups


class SohSettings(Group):
    class AllowTrueNoLogic(Bool):
        """
        Allows SoH players to enable the true_no_logic hidden option, which makes every region and logically accessible.
        Do not enable this if you are not ready to use /send, !getitem, or similar commands.
        Do not enable this if you don't trust the players using it to play responsibly.
        """

    class DisableFillOverflow(Bool):
        """
        A debugging option for disabling our fill overflow for prefills. Typical users likely shouldn't enable this as it allows for generation failures.
        By default when an item can't be placed in prefill it will be added to the item pool as a backup. This disables that behavoir.
        """

    class SOHExecutablePath(str):
        """
        Where the game executable is installed. Used for opening the game through the AP launcher or Webhost
        """

    class SOHSettingsFolder(str):
        """
        Where game files and configuration is contained. Used to change shipofharkinian.json settings
        """

    allow_true_no_logic: AllowTrueNoLogic | bool = False
    disable_fill_overflow: DisableFillOverflow | bool = False
    executable_path: SOHExecutablePath | None = None
    soh_settings_folder: SOHSettingsFolder | None = None


@staticmethod
def create_groups(obj: dict[Items, SohItemData] | dict[str, SohLocData]) -> dict[str, set[str]]:
    groups: dict[str, set[str]] = dict()
    for key, data in obj.items():
        if data.tags is None:
            continue
        for tag in data.tags:
            tag_name = tag.name.replace('_', ' ')
            if tag_name not in groups:
                groups[tag_name] = set()
            groups[tag_name].add(str(key))
    return groups

class SohWorld(CachedRuleBuilderWorld):
    """A PC Port of Ocarina of Time"""

    game = "Ship of Harkinian"
    web = SohWebWorld()
    options: SohOptions
    options_dataclass = SohOptions
    settings: ClassVar[SohSettings]
    location_name_to_id = location_table
    item_name_to_id = item_table
    item_name_groups = create_groups(item_data_table)
    location_name_groups = create_groups(location_data_table)

    # Universal Tracker stuff, does not do anything in normal gen
    glitches_item_name = Items.GLITCHED
    using_ut: bool  # so we can check if we're using UT only once
    passthrough: dict[str, Any]  # slot data that got passed through
    ut_can_gen_without_yaml = True  # class var that tells it to ignore the player yaml

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)
        self.item_pool = list[SohItem]()
        self.preplaced_items = list[SohItem]()
        self.included_locations = dict[str, SohLocData]()
        # location name -> [(region, rule)] for every region that lists it (see LogicHelpers.add_location_source)
        self.soh_location_sources: dict[str, list] = {}
        self.shop_prices = dict[Locations, int]()
        self.shop_vanilla_items = dict[str, str]()
        self.triforce_pieces_required: int = 0
        self.ganons_soul_triforce_pieces_required: int = 0
        self.rainbow_bridge_triforce_pieces_required: int = 0
        self.gbk_triforce_pieces_required: int = 0
        self.randomized_progressive_skulltula_count: int = 0
        self.ganons_trials = list[GanonsTrials]()
        self.pre_fill_pool = list[SohItem]()
        self.reserved_pre_fill_locations = list[Locations]()

        apworld_manifest = orjson.loads(pkgutil.get_data(
            __name__, "archipelago.json").decode("utf-8"))
        self.apworld_version: str = apworld_manifest["world_version"]
        # The version is stored on Worlds, so when we're ready to bump our min AP version to 0.6.4, we can use this directly in our slot data:
        # slot_data["apworld_version"] = self.world_version

    def generate_early(self) -> None:
        # for use with Universal Tracker, doesn't do anything otherwise
        setup_options_from_slot_data(self)

        if self.options.true_no_logic and not self.settings.allow_true_no_logic:
            raise OptionError(f"Player {self.player_name} enabled True No Logic, but the corresponding host.yaml "
                              "setting has not been enabled. Either have them disable that option, or enable it in "
                              "your host.yaml settings.")

        self.options.apply_any_required_option_adjustments()
        self.apply_legacy_tricks()
     
        self.randomized_progressive_skulltula_count = self.options.calculate_progression_skulltula_count(token_reward_counts=token_amounts)

        # Figure out Keyring Situation
        key_ring_options: list = [self.options.gerudo_fortress_key_ring, self.options.forest_temple_key_ring, self.options.fire_temple_key_ring, self.options.water_temple_key_ring,
                                  self.options.spirit_temple_key_ring, self.options.shadow_temple_key_ring, self.options.bottom_of_the_well_key_ring, self.options.gerudo_training_ground_key_ring, self.options.ganons_castle_key_ring,
                                  self.options.chest_game_key_ring]

        if self.options.key_rings != "selection":
            for option in key_ring_options:
                option.value = False

        # settings.cpp: the Gerudo Fortress key ring only counts with normal carpenters and shuffled Gerudo keys, the
        # Treasure Chest Game key ring only with the Treasure Chest Game shuffle
        fortress_keys_shuffled = not (self.options.fortress_carpenters == "normal" and self.options.gerudo_fortress_key_shuffle == "vanilla")
        if self.options.key_rings == "count":
            if not fortress_keys_shuffled:
                key_ring_options.remove(self.options.gerudo_fortress_key_ring)
            if not self.options.shuffle_treasure_chest_game:
                key_ring_options.remove(self.options.chest_game_key_ring)
            if self.options.key_rings_count.value > len(key_ring_options):
                self.options.key_rings_count.value = len(key_ring_options)

            self.random.shuffle(key_ring_options)

            # Set only the chosen
            for index in range(self.options.key_rings_count.value):
                key_ring_options[index].value = True
        elif self.options.key_rings == "selection":
            if self.options.fortress_carpenters == "normal" and self.options.gerudo_fortress_key_shuffle == "vanilla":
                self.options.gerudo_fortress_key_ring.value = False
            if not self.options.shuffle_treasure_chest_game:
                self.options.chest_game_key_ring.value = False

        if self.options.ganons_trials == "set_number" and self.options.ganons_trials_count.value > 0:
            self.ganons_trials = [str(trial) for trial in GanonsTrials]
            if self.options.ganons_trials_count.value < 6:
                self.random.shuffle(self.ganons_trials)
                self.ganons_trials = self.ganons_trials[:self.options.ganons_trials_count.value]

        # These things get modified after we call setup_options_from_slot_data, so we need to set them here.
        if self.using_ut:
            self.ganons_trials = self.passthrough.get("required_trials", 6)
            self.options.gerudo_fortress_key_ring.value = self.passthrough.get("gerudo_fortress_key_ring", False)
            self.options.chest_game_key_ring.value = self.passthrough.get("chest_game_key_ring", False)  # apworld 1.5+
            self.options.forest_temple_key_ring.value = self.passthrough.get("forest_temple_key_ring", False)
            self.options.fire_temple_key_ring.value = self.passthrough.get("fire_temple_key_ring", False)
            self.options.water_temple_key_ring.value = self.passthrough.get("water_temple_key_ring", False)
            self.options.spirit_temple_key_ring.value = self.passthrough.get("spirit_temple_key_ring", False)
            self.options.shadow_temple_key_ring.value = self.passthrough.get("shadow_temple_key_ring", False)
            self.options.bottom_of_the_well_key_ring.value = self.passthrough.get("bottom_of_the_well_key_ring", False)
            self.options.gerudo_training_ground_key_ring.value = self.passthrough.get("gerudo_training_ground_key_ring", False)
            self.options.ganons_castle_key_ring.value = self.passthrough.get("ganons_castle_key_ring", False)

    def get_item_from_pool(self, item: Items, item_pool: list[SohItem]) -> SohItem|None:
        item_id = item_data_table[item].item_id
        found_item = None
        for soh_item in item_pool:
            if soh_item.code == item_id:
                found_item = soh_item
                break
        if found_item:
            item_pool.remove(found_item)
        return found_item
    
    def precollect_from_pool(self, item: Items):
        world_item = self.get_item_from_pool(item, self.item_pool)
        if not world_item:
            return

        world_item.code = None
        self.push_precollected(world_item)

    def create_regions(self) -> None:
        create_regions_and_locations(self)
        self.reserve_prefill_locations()
        for location in self.get_locations():
            location.name = str(location.name)
        for region in self.get_regions():
            region.name = str(region.name)

        if self.using_ut:
            # Put vanilla items in shop
            fill_shop_items(self)

    def reserve_prefill_locations(self) -> None:
        # songs and medalion locations get a soft reservation, by adding them to the reserved location list
        # pre-fill is not allowed to place items there, but plando is allowed
        DungeonRewardShuffle.reserve_dungeon_reward_locations(self)
        SongShuffle.reserve_song_locations(self)

        # vanilla shop locations get a hard reservation, by placing a RESERVATION item there
        # pre-fill and plando are not allowed to place items there
        ShopItems.reserve_vanilla_shop_locations(self)

    def create_item(self, name: str, create_as_event: bool = False, classification: ItemClassification = None) -> SohItem:
        item_entry = Items(name)
        # "Gate Shop Shields & Tunics": found shields and tunics unlock their shop slots, so the logic needs them
        if (classification is None and self.options.shop_shields_and_tunics_only_refill
                and item_entry in (Items.DEKU_SHIELD, Items.HYLIAN_SHIELD, Items.GORON_TUNIC, Items.ZORA_TUNIC)):
            classification = item_data_table[item_entry].classification | ItemClassification.progression
        return SohItem(str(name), item_data_table[item_entry].classification if classification == None else classification,
                       None if create_as_event else item_data_table[item_entry].item_id, self.player)

    def get_pre_fill_items(self) -> list[Item]:
        return self.pre_fill_pool

    def get_filler_item_name(self) -> str:
        return get_filler_item(self)

    def set_completion_rule(self, goal: Rule = None) -> None:
        if not self.options.true_no_logic:
            # Actual completion condition.
            if goal == None:
                super().set_completion_rule(Has(str(Events.GAME_COMPLETED)))
            else:
                super().set_completion_rule(goal)

    def get_empty_locations_from_list_shuffled(self, location_list: list[Locations]) -> list[Location]:
        locations = []
        for location in location_list:
            loc = self.get_location(str(location))
            if loc.item != None or loc.locked or location in self.reserved_pre_fill_locations:
                continue
            locations.append(loc)
        self.random.shuffle(locations)

        return locations

    def get_pre_fill_state(self) -> CollectionState:
        my_locations = list(self.multiworld.get_locations(self.player))
        prefill_state = CollectionState(self.multiworld)
        for item in self.item_pool:
            prefill_state.collect(item, True)
        for item in self.pre_fill_pool:
            prefill_state.collect(item, True)
        prefill_state.sweep_for_advancements(my_locations)
        return prefill_state
    
    def set_rules(self) -> None:
        # Set price rules in advance
        generate_prices(self)


    def create_items(self) -> None:
        # generate the prefill pool
        pre_fill_items = list()
        pre_fill_items += get_pre_fill_rewards(self)
        pre_fill_items += get_prefill_songs(self)
        for key_shuffle in get_own_dungeon_prefill_items(self).values():
            pre_fill_items += key_shuffle
        pre_fill_items += get_dungeon_item_prefill_items(self, False)
        pre_fill_items += get_dungeon_item_prefill_items(self, True)

        vanilla_shop_pool = ShopItems.get_vanilla_shop_pool(self)
        pre_fill_items += vanilla_shop_pool
        self.item_pool += [self.create_item(item) for item in vanilla_shop_pool]

        # Generate the item pool
        create_item_pool(self)

        # Pre-place items from the pool
        give_starting_items(self)
        place_locked_items(self)

        if self.options.triforce_hunt:
            create_triforce_pieces(self)

        create_filler_item_pool(self)

        # Extract pre fill items from the pool
        for item in pre_fill_items:
            if (pre_fill_item := self.get_item_from_pool(item, self.item_pool)):
                self.pre_fill_pool.append(pre_fill_item)

        # Send items to the multiworld
        self.multiworld.itempool.extend(self.item_pool)

        self.set_completion_rule()

    def apply_legacy_tricks(self) -> None:
        """Tricks that SoH 9.3.1 renamed or dropped (Options.LEGACY_TRICKS): a 1:1 rename turns the new trick on,
        the others stay without effect and get a warning."""
        tricks = self.options.tricks_in_logic.value
        for old, target in LEGACY_TRICKS.items():
            if old.value not in tricks:
                continue
            if isinstance(target, Tricks):
                tricks.add(target.value)
            else:
                replacement = f" Its replacement is the broader trick \"{target}\"." if target else ""
                logger.warning(f"Ship of Harkinian (player {self.player_name}): the trick \"{old.value}\" no longer "
                               f"exists in SoH 9.3.1 and has no effect.{replacement}")

    def slot_data_tricks(self) -> list[str]:
        """Enabled tricks as upstream enum names ("RT_LW_BRIDGE"): the client looks these up independent of the
        UI language. Legacy tricks are left out; the client doesn't know them."""
        return sorted(f"RT_{trick.name}" for trick in Tricks
                      if trick.value in self.options.tricks_in_logic.value and trick not in LEGACY_TRICKS)

    def remove_unreachable_events(self) -> None:
        """Drop event locations that stay unreachable even with every item of this world.

        The 9.3.1 region logic (ported 1:1) has events that only trigger with tricks or settings the seed doesn't use,
        e.g. the Forest Temple NE courtyard scarecrow without the hover boost trick. Upstream simply never triggers them;
        in Archipelago an unreachable event fails the accessibility check, so they are removed. This doesn't change what
        is reachable: the event could never be collected."""
        state = self.get_pre_fill_state()
        removed = []
        for region in self.multiworld.get_regions(self.player):
            for location in list(region.locations):
                if location.address is None and location.item is not None and not location.can_reach(state):
                    region.locations.remove(location)
                    self.multiworld.regions.location_cache[self.player].pop(location.name, None)
                    removed.append(location.name)
        if removed:
            logger.debug(f"Ship of Harkinian (player {self.player}): removed {len(removed)} unreachable events: {removed}")
        self.removed_unreachable_events = removed

    def pre_fill(self) -> None:
        self.remove_unreachable_events()
        pre_fill_own_dungeon_items(self)
        pre_fill_dungeon_rewards(self)
        pre_fill_songs(self)
        pre_fill_any_dungeon_keys(self)
        pre_fill_overworld_items(self)
        fill_shop_items(self)

        self.set_completion_rule()

    def run_prefill(self, item_pool: list[Items], locations: list[Locations], original_goal: Callable[[CollectionState], bool] | None = None):
        def create_new_goal(empty_locations: list[Location]):
            goal = True_()
            # set region accessability of locations as the goal
            for reg in empty_locations:
                goal &= CanReachLocation(str(reg.name))
            return goal

        # Get the items from the prefill pool
        items = list()
        for item in item_pool:
            if (pre_fill_item := self.get_item_from_pool(item, self.pre_fill_pool)):
                items.append(pre_fill_item)

        prefill_state = self.get_pre_fill_state()

        # get empty, non reserved locations
        empty_locations_all = self.get_empty_locations_from_list_shuffled(locations)
        count_empty_locations_all = len(empty_locations_all)
        chunk = min(len(item_pool) + 100, count_empty_locations_all)

        # If fill overflow is disabled or the chunk is as large as the original list, use all locations
        if self.settings.disable_fill_overflow or chunk == count_empty_locations_all:
            empty_locations = empty_locations_all
        else:
            empty_locations = empty_locations_all[:chunk]

        self.preplaced_items.extend(items)
        
        if original_goal is None:
            self.set_completion_rule(create_new_goal(empty_locations))
        else:
            self.set_completion_rule(original_goal)

        # Determines if a partial or full fill is occuring
        fill_restrictive(self.multiworld, prefill_state, empty_locations, items, single_player_placement=True, lock=True, allow_partial=(not self.settings.disable_fill_overflow), name="SOH_Prefill_Initial")

        # Check if any items and locations are left. If so try again once more with the rest of the locations
        if len(items) > 0 and chunk != count_empty_locations_all:
            empty_locations = empty_locations_all[chunk:]

            if original_goal is None:
                self.set_completion_rule(create_new_goal(empty_locations))

            fill_restrictive(self.multiworld, prefill_state, empty_locations, items, single_player_placement=True, lock=True, allow_partial=True, name="SOH_Prefill_Secondary")
        
        # Add any unplaced items to the item pool
        if len(items) > 0:
            self.item_pool.extend(items)
            self.multiworld.itempool.extend(items)

        for item in items:
            self.preplaced_items.remove(item)


    def collect(self, state: CollectionState, item: Item) -> bool:
        changed = super().collect(state, item)
        state._soh_stale[self.player] = True  # type: ignore

        if item.name == Items.HEART_CONTAINER:
            state.soh_heart_count[self.player] += 1  # type: ignore

        if item.name in (Items.PIECE_OF_HEART, Items.PIECE_OF_HEART_WINNER):
            state.soh_piece_of_heart_count[self.player] += 1  # type: ignore
            # type: ignore
            if state.soh_piece_of_heart_count[self.player] == 4:
                state.soh_piece_of_heart_count[self.player] = 0  # type: ignore
                state.soh_heart_count[self.player] += 1  # type: ignore

        return changed
    
    def add_items_to_item_pool_list(self, items: list[SohItem]) -> None:
        if len(items) > 0:
            self.item_pool.extend(items)

    def remove(self, state: CollectionState, item: Item) -> bool:
        changed = super().remove(state, item)
        if changed:
            state._soh_invalidate(self.player)  # type: ignore

        if item.name == Items.HEART_CONTAINER:
            state.soh_heart_count[self.player] -= 1  # type: ignore

        if item.name in (Items.PIECE_OF_HEART, Items.PIECE_OF_HEART_WINNER):
            state.soh_piece_of_heart_count[self.player] -= 1  # type: ignore
            # type: ignore
            if state.soh_piece_of_heart_count[self.player] == -1:
                state.soh_piece_of_heart_count[self.player] = 3  # type: ignore
                state.soh_heart_count[self.player] -= 1  # type: ignore

        return changed

    # For debugging purposes
    # def generate_output(self, output_directory: str):
    #    from Utils import visualize_regions
    #    visualize_regions(self.get_region(self.origin_region_name), f"SOH-Player{self.player}.puml",
    #                      show_entrance_names=True,
    #                      regions_to_highlight=self.multiworld.get_all_state().reachable_regions[self.player])

    def fill_slot_data(self) -> dict[str, Any]:
        # Create the relevant foreign hints
        hints = CreateNonlocalHints(self)
        static_hints = dict[str, list[list[int, int]]]()
        for hint in hints:
            static_hints.update(hint.serialize())

        return {
            "closed_forest": self.options.closed_forest.value,
            "kakariko_gate": self.options.kakariko_gate.value,
            "door_of_time": self.options.door_of_time.value,
            "zoras_fountain": self.options.zoras_fountain.value,
            "sleeping_waterfall": self.options.sleeping_waterfall.value,
            "jabu_jabu": self.options.jabu_jabu.value,
            "lock_overworld_doors": self.options.lock_overworld_doors.value,
            "fortress_carpenters": self.options.fortress_carpenters.value,
            "rainbow_bridge": self.options.rainbow_bridge.value,
            "rainbow_bridge_greg_modifier": self.options.rainbow_bridge_greg_modifier.value,
            "rainbow_bridge_stones_required": self.options.rainbow_bridge_stones_required.value,
            "rainbow_bridge_medallions_required": self.options.rainbow_bridge_medallions_required.value,
            "rainbow_bridge_dungeon_rewards_required": self.options.rainbow_bridge_dungeon_rewards_required.value,
            "rainbow_bridge_dungeons_required": self.options.rainbow_bridge_dungeons_required.value,
            "rainbow_bridge_skull_tokens_required": self.options.rainbow_bridge_skull_tokens_required.value,
            "ganons_trials": self.options.ganons_trials.value,
            "ganons_trials_count": self.options.ganons_trials_count.value,
            "required_trials": self.ganons_trials,
            "triforce_hunt": self.options.triforce_hunt.value,
            "triforce_hunt_pieces_total": self.options.triforce_hunt_pieces_total.value,
            "triforce_hunt_pieces_required": self.triforce_pieces_required,
            "shuffle_songs": self.options.shuffle_songs.value,
            "shuffle_skull_tokens": self.options.shuffle_skull_tokens.value,
            "skulls_sun_song": self.options.skulls_sun_song.value,
            "shuffle_kokiri_sword": self.options.shuffle_kokiri_sword.value,
            "shuffle_master_sword": self.options.shuffle_master_sword.value,
            "shuffle_childs_wallet": self.options.shuffle_childs_wallet.value,
            "shuffle_tycoon_wallet": self.options.shuffle_tycoon_wallet.value,
            "shuffle_ocarinas": self.options.shuffle_ocarinas.value,
            "shuffle_ocarina_buttons": self.options.shuffle_ocarina_buttons.value,
            "shuffle_swim": self.options.shuffle_swim.value,
            "shuffle_gerudo_membership_card": self.options.shuffle_gerudo_membership_card.value,
            "shuffle_weird_egg": self.options.shuffle_weird_egg.value,
            "shuffle_fishing_pole": self.options.shuffle_fishing_pole.value,
            "shuffle_deku_stick_bag": self.options.shuffle_deku_stick_bag.value,
            "shuffle_deku_nut_bag": self.options.shuffle_deku_nut_bag.value,
            "shuffle_freestanding_items": self.options.shuffle_freestanding_items.value,
            "shuffle_shops": self.options.shuffle_shops.value,
            "shuffle_shops_item_amount": self.options.shuffle_shops_item_amount.value,
            "shop_prices": self.shop_prices,
            "shop_vanilla_items": self.shop_vanilla_items,
            "shuffle_fish": self.options.shuffle_fish.value,
            "fishsanity_pond_count": self.options.fishsanity_pond_count.value,
            "fishsanity_age_split": self.options.fishsanity_age_split.value,
            "shuffle_scrubs": self.options.shuffle_scrubs.value,
            "shuffle_beehives": self.options.shuffle_beehives.value,
            "shuffle_cows": self.options.shuffle_cows.value,
            "shuffle_pots": self.options.shuffle_pots.value,
            "shuffle_signs": self.options.shuffle_signs.value,
            "shuffle_wonder_items": self.options.shuffle_wonder_items.value,
            "shuffle_icicles": self.options.shuffle_icicles.value,
            "shuffle_red_ice": self.options.shuffle_red_ice.value,
            "shuffle_rocks": self.options.shuffle_rocks.value,
            "shuffle_boulders": self.options.shuffle_boulders.value,
            "shuffle_crates": self.options.shuffle_crates.value,
            "shuffle_trees": self.options.shuffle_trees.value,
            "shuffle_merchants": self.options.shuffle_merchants.value,
            "shuffle_frog_song_rupees": self.options.shuffle_frog_song_rupees.value,
            "shuffle_beggar": self.options.shuffle_beggar.value,
            "shuffle_treasure_chest_game": self.options.shuffle_treasure_chest_game.value,
            "shuffle_bushes": self.options.shuffle_bushes.value,
            "shuffle_bean_souls": self.options.shuffle_bean_souls.value,
            "shuffle_adult_trade_items": self.options.shuffle_adult_trade_items.value,
            "shuffle_boss_souls": self.options.shuffle_boss_souls.value,
            "shuffle_fountain_fairies": self.options.shuffle_fountain_fairies.value,
            "shuffle_stone_fairies": self.options.shuffle_stone_fairies.value,
            "shuffle_bean_fairies": self.options.shuffle_bean_fairies.value,
            "shuffle_song_fairies": self.options.shuffle_song_fairies.value,
            "shuffle_butterfly_fairies": self.options.shuffle_butterfly_fairies.value,
            "shuffle_grass": self.options.shuffle_grass.value,
            "shuffle_dungeon_rewards": self.options.shuffle_dungeon_rewards.value,
            "maps_and_compasses": self.options.maps_and_compasses.value,
            "ganons_castle_boss_key": self.options.ganons_castle_boss_key.value,
            "ganons_castle_boss_key_greg_modifier": self.options.ganons_castle_boss_key_greg_modifier.value,
            "ganons_castle_boss_key_stones_required": self.options.ganons_castle_boss_key_stones_required.value,
            "ganons_castle_boss_key_medallions_required": self.options.ganons_castle_boss_key_medallions_required.value,
            "ganons_castle_boss_key_dungeon_rewards_required": self.options.ganons_castle_boss_key_dungeon_rewards_required.value,
            "ganons_castle_boss_key_dungeons_required": self.options.ganons_castle_boss_key_dungeons_required.value,
            "ganons_castle_boss_key_skull_tokens_required": self.options.ganons_castle_boss_key_skull_tokens_required.value,
            "small_key_shuffle": self.options.small_key_shuffle.value,
            "gerudo_fortress_key_shuffle": self.options.gerudo_fortress_key_shuffle.value,
            "boss_key_shuffle": self.options.boss_key_shuffle.value,
            "key_rings": self.options.key_rings.value,
            "key_rings_count": self.options.key_rings_count.value,
            "gerudo_fortress_key_ring": self.options.gerudo_fortress_key_ring.value,
            "chest_game_key_ring": self.options.chest_game_key_ring.value,
            "forest_temple_key_ring": self.options.forest_temple_key_ring.value,
            "fire_temple_key_ring": self.options.fire_temple_key_ring.value,
            "water_temple_key_ring": self.options.water_temple_key_ring.value,
            "spirit_temple_key_ring": self.options.spirit_temple_key_ring.value,
            "shadow_temple_key_ring": self.options.shadow_temple_key_ring.value,
            "bottom_of_the_well_key_ring": self.options.bottom_of_the_well_key_ring.value,
            "gerudo_training_ground_key_ring": self.options.gerudo_training_ground_key_ring.value,
            "ganons_castle_key_ring": self.options.ganons_castle_key_ring.value,
            "big_poe_target_count": self.options.big_poe_target_count.value,
            "skip_child_zelda": self.options.skip_child_zelda.value,
            "shuffle_zeldas_letter": self.options.shuffle_zeldas_letter.value,
            "skip_epona_race": self.options.skip_epona_race.value,
            "skip_child_stealth": self.options.skip_child_stealth.value,
            "skip_planting_beans": self.options.skip_planting_beans.value,
            "complete_mask_quest": self.options.complete_mask_quest.value,
            "shuffle_masks": self.options.shuffle_masks.value,
            "skip_scarecrows_song": self.options.skip_scarecrows_song.value,
            "shuffle_scarecrows_song": self.options.shuffle_scarecrows_song.value,
            "start_with_links_pocket": self.options.start_with_links_pocket.value,
            "links_pocket_reward": self.options.links_pocket_reward.value,
            "bunny_hood_effect": self.options.bunny_hood_effect.value,
            "progressive_goron_sword": self.options.progressive_goron_sword.value,
            "masks_as_adult": self.options.masks_as_adult.value,
            "early_grannys_shop": self.options.early_grannys_shop.value,
            "swordless_epona_items": self.options.swordless_epona_items.value,
            "shop_shields_and_tunics_only_refill": self.options.shop_shields_and_tunics_only_refill.value,
            "start_with_kokiri_sword": self.options.start_with_kokiri_sword.value,
            "start_with_deku_shield": self.options.start_with_deku_shield.value,
            "start_with_master_sword": self.options.start_with_master_sword.value,
            "start_with_ocarina": self.options.start_with_ocarina.value,
            "start_with_stick_ammo": self.options.start_with_stick_ammo.value,
            "start_with_nut_ammo": self.options.start_with_nut_ammo.value,
            "start_with_magic_beans": self.options.start_with_magic_beans.value,
            "start_with_zeldas_lullaby": self.options.start_with_zeldas_lullaby.value,
            "start_with_eponas_song": self.options.start_with_eponas_song.value,
            "start_with_sarias_song": self.options.start_with_sarias_song.value,
            "start_with_suns_song": self.options.start_with_suns_song.value,
            "start_with_song_of_time": self.options.start_with_song_of_time.value,
            "start_with_song_of_storms": self.options.start_with_song_of_storms.value,
            "start_with_minuet": self.options.start_with_minuet.value,
            "start_with_bolero": self.options.start_with_bolero.value,
            "start_with_serenade": self.options.start_with_serenade.value,
            "start_with_requiem": self.options.start_with_requiem.value,
            "start_with_nocturne": self.options.start_with_nocturne.value,
            "start_with_prelude": self.options.start_with_prelude.value,
            "start_with_megaton_hammer": self.options.start_with_megaton_hammer.value,
            "start_with_boomerang": self.options.start_with_boomerang.value,
            "start_with_lens_of_truth": self.options.start_with_lens_of_truth.value,
            "start_with_dins_fire": self.options.start_with_dins_fire.value,
            "start_with_farores_wind": self.options.start_with_farores_wind.value,
            "start_with_nayrus_love": self.options.start_with_nayrus_love.value,
            "start_with_fire_arrows": self.options.start_with_fire_arrows.value,
            "start_with_ice_arrows": self.options.start_with_ice_arrows.value,
            "start_with_light_arrows": self.options.start_with_light_arrows.value,
            "start_with_iron_boots": self.options.start_with_iron_boots.value,
            "start_with_hover_boots": self.options.start_with_hover_boots.value,
            "start_with_hylian_shield": self.options.start_with_hylian_shield.value,
            "start_with_mirror_shield": self.options.start_with_mirror_shield.value,
            "start_with_goron_tunic": self.options.start_with_goron_tunic.value,
            "start_with_zora_tunic": self.options.start_with_zora_tunic.value,
            "start_with_stone_of_agony": self.options.start_with_stone_of_agony.value,
            "start_with_weird_egg": self.options.start_with_weird_egg.value,
            "start_with_claim_check": self.options.start_with_claim_check.value,
            "start_with_gerudo_card": self.options.start_with_gerudo_card.value,
            "start_with_keaton_mask": self.options.start_with_keaton_mask.value,
            "start_with_skull_mask": self.options.start_with_skull_mask.value,
            "start_with_spooky_mask": self.options.start_with_spooky_mask.value,
            "start_with_bunny_hood": self.options.start_with_bunny_hood.value,
            "start_with_goron_mask": self.options.start_with_goron_mask.value,
            "start_with_zora_mask": self.options.start_with_zora_mask.value,
            "start_with_gerudo_mask": self.options.start_with_gerudo_mask.value,
            "start_with_mask_of_truth": self.options.start_with_mask_of_truth.value,
            "start_with_hookshot": self.options.start_with_hookshot.value,
            "start_with_bow": self.options.start_with_bow.value,
            "start_with_slingshot": self.options.start_with_slingshot.value,
            "start_with_bomb_bag": self.options.start_with_bomb_bag.value,
            "start_with_strength": self.options.start_with_strength.value,
            "start_with_scale": self.options.start_with_scale.value,
            "start_with_wallet": self.options.start_with_wallet.value,
            "start_with_magic_meter": self.options.start_with_magic_meter.value,
            "start_with_bombchu_bag": self.options.start_with_bombchu_bag.value,
            "start_with_biggorons_sword": self.options.start_with_biggorons_sword.value,
            "start_with_bottle_1": self.options.start_with_bottle_1.value,
            "start_with_bottle_2": self.options.start_with_bottle_2.value,
            "start_with_bottle_3": self.options.start_with_bottle_3.value,
            "start_with_bottle_4": self.options.start_with_bottle_4.value,
            "starting_skulltula_tokens": self.options.starting_skulltula_tokens.value,
            "full_wallets": self.options.full_wallets.value,
            "bombchu_bag": self.options.bombchu_bag.value,
            "bombchu_drops": self.options.bombchu_drops.value,
            "blue_fire_arrows": self.options.blue_fire_arrows.value,
            "sunlight_arrows": self.options.sunlight_arrows.value,
            "rocs_feather": self.options.rocs_feather.value,
            "infinite_upgrades": self.options.infinite_upgrades.value,
            "skeleton_key": self.options.skeleton_key.value,
            "slingbow_break_beehives": self.options.slingbow_break_beehives.value,
            "starting_age": self.options.starting_age.value,
            "shuffle_100_gs_reward": self.options.shuffle_100_gs_reward.value,
            "ice_trap_count": self.options.ice_trap_count.value,
            "ice_trap_filler_replacement": self.options.ice_trap_filler_replacement.value,
            "ice_trap_names": self.options.ice_trap_names.value,
            "no_logic": self.options.true_no_logic.value,
            "apworld_version": self.apworld_version,
            "enable_all_tricks": self.options.enable_all_tricks.value,
            "tricks_in_logic": self.slot_data_tricks(),
            # Win Condition (9.3.1 RSK_WINCON); "default" is already resolved to defeat_ganon / trigger_triforce_pieces
            "win_condition": self.options.win_condition.value,
            "win_condition_greg_modifier": self.options.win_condition_greg_modifier.value,
            "win_condition_stones_required": self.options.win_condition_stones_required.value,
            "win_condition_medallions_required": self.options.win_condition_medallions_required.value,
            "win_condition_dungeon_rewards_required": self.options.win_condition_dungeon_rewards_required.value,
            "win_condition_dungeons_required": self.options.win_condition_dungeons_required.value,
            "win_condition_skull_tokens_required": self.options.win_condition_skull_tokens_required.value,
            "triforce_hunt_pieces_location": self.options.triforce_hunt_pieces_location.value,
            "rainbow_bridge_triforce_pieces_required": self.rainbow_bridge_triforce_pieces_required
            if self.options.rainbow_bridge == RainbowBridge.option_triforce_pieces else 0,
            "ganons_castle_boss_key_triforce_pieces_required": self.gbk_triforce_pieces_required
            if self.options.ganons_castle_boss_key == GanonsCastleBossKey.option_lacs_triforce_pieces else 0,
            # Ganon's Soul (9.3.1 RSK_GANONS_SOUL); values follow the upstream order Start With ... Trigger-Triforce
            "ganons_soul": self.options.ganons_soul.value,
            "ganons_soul_greg_modifier": self.options.ganons_soul_greg_modifier.value,
            "ganons_soul_stones_required": self.options.ganons_soul_stones_required.value,
            "ganons_soul_medallions_required": self.options.ganons_soul_medallions_required.value,
            "ganons_soul_dungeon_rewards_required": self.options.ganons_soul_dungeon_rewards_required.value,
            "ganons_soul_dungeons_required": self.options.ganons_soul_dungeons_required.value,
            "ganons_soul_skull_tokens_required": self.options.ganons_soul_skull_tokens_required.value,
            "ganons_soul_triforce_pieces_required": self.ganons_soul_triforce_pieces_required
            if self.options.ganons_soul == GanonsSoul.option_trigger_triforce_pieces else 0,
            "medallion_locked_trials": self.options.medallion_locked_trials.value,
            "starting_hearts": self.options.starting_hearts.value,
            "hint_clarity": self.options.hint_clarity.value,
            "gossip_stone_hints": self.options.gossip_stone_hints.value,
            "tot_altar_hint": self.options.tot_altar_hint.value,
            "ganondorf_hint": self.options.ganondorf_hint.value,
            "sheik_la_hint": self.options.sheik_la_hint.value,
            "boss_key_hint": self.options.boss_key_hint.value,
            "dampe_diary_hint": self.options.dampe_diary_hint.value,
            "greg_hint": self.options.greg_hint.value,
            "hyrule_loach_hint": self.options.hyrule_loach_hint.value,
            "saria_hint": self.options.saria_hint.value,
            "mido_hint": self.options.mido_hint.value,
            "frog_game_hint": self.options.frog_game_hint.value,
            "ocarina_of_time_hint": self.options.ocarina_of_time_hint.value,
            "big_goron_hint": self.options.big_goron_hint.value,
            "big_poe_hint": self.options.big_poe_hint.value,
            "chicken_hint": self.options.chicken_hint.value,
            "malon_hint": self.options.malon_hint.value,
            "horseback_archery_hint": self.options.horseback_archery_hint.value,
            "fishing_pole_hint": self.options.fishing_pole_hint.value,
            #"warp_song_hint": self.options.warp_song_hint.value,
            "scrub_hints": self.options.scrub_hints.value,
            "merchant_hints": self.options.merchant_hints.value,
            "gs_10_hint": self.options.gs_10_hint.value,
            "gs_20_hint": self.options.gs_20_hint.value,
            "gs_30_hint": self.options.gs_30_hint.value,
            "gs_40_hint": self.options.gs_40_hint.value,
            "gs_50_hint": self.options.gs_50_hint.value,
            "gs_100_hint": self.options.gs_100_hint.value,
            "mask_shop_hint": self.options.mask_shop_hint.value,
            "static_hints": static_hints,
            "hintable_items": {item.code for item in self.item_pool + self.preplaced_items if item.code is not None},
            "starting_hearts": self.options.starting_hearts.value,
            "archipelago_seed": self.random.randint(0, 4294967295) #This is a uint32_t in ship
        }

def launch_client(*args: str):
    from .Client import launch
    launch_component(launch, name="Ship of Harkinian Client", args=args)

components.append(Component("Ship Of Harkinian Client", game_name="Ship of Harkinian", func=launch_client, component_type=Type.CLIENT, supports_uri=True))