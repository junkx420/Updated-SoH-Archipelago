from collections import Counter
import math
from typing import TYPE_CHECKING, Callable
from collections import Counter

from BaseClasses import CollectionState, ItemClassification as IC, MultiWorld, Location, Region
from .Locations import SohLocation
from worlds.AutoWorld import LogicMixin, World
from .Enums import *
from .Items import SohItem, item_data_table, ItemType, no_rules_bottles, GroupTag, progressive_items
from rule_builder.rules import *
from rule_builder.field_resolvers import *
from .Options import *
from .RegionScenes import REGION_SCENE

if TYPE_CHECKING:
    from . import SohWorld

import logging
logger = logging.getLogger("SOH_OOT.Logic")

child_age_dependent_rules: dict[Regions, list[Rule.Resolved]] = {}
adult_age_dependent_rules: dict[Regions, list[Rule.Resolved]] = {}

class rule_wrapper:
    def __init__(self, parent_region: Regions, rule: Callable[[tuple[Regions, "SohWorld"]], Rule], world: "SohWorld"):
        self.parent_region = parent_region
        self.world = world
        self.rule = rule

    @staticmethod
    def wrap(parent_region: Regions, rule: Callable[[tuple[Regions, "SohWorld"]], Rule], world: "SohWorld") -> Rule:
        wrapper = rule_wrapper(parent_region, rule, world)
        return wrapper.evaluate()

    def evaluate(self) -> Rule:
        rule = self.rule((self.parent_region, self.world))
        return rule 


def test_for_age_check(rule: Rule, parent_region: Regions, world: "SohWorld") -> set[Ages]:
        ages: set[Ages] = set()
        if isinstance(rule, IsChild):
            ages.add(Ages.CHILD)
        elif isinstance(rule, IsAdult):
            ages.add(Ages.ADULT)
        elif isinstance(rule, WrapperRule):
            ages = test_for_age_check(rule.child, parent_region, world)
        elif isinstance(rule, NestedRule):
            ages = set()
            for sub_rule in rule.children:
                ages.update(test_for_age_check(sub_rule, parent_region, world))
        if Ages.CHILD in ages:
            if parent_region in child_age_dependent_rules:
                child_age_dependent_rules[parent_region].append(rule.resolve(world))
            else:
                child_age_dependent_rules[parent_region] = [rule.resolve(world)]
        if Ages.ADULT in ages:
            if parent_region in adult_age_dependent_rules:
                adult_age_dependent_rules[parent_region].append(rule.resolve(world))
            else:
                adult_age_dependent_rules[parent_region] = [rule.resolve(world)]
        return ages

def add_locations(parent_region: Regions, world: "SohWorld", locations: list[tuple[Locations, Rule | Callable[[tuple[Regions, "SohWorld"]], Rule]]]) -> None:
    mLocations : list[tuple[str, int | None, Rule | Callable[[CollectionState], bool]]] = list()
    for loc in locations:
        locationName = str(loc[0])
        if locationName not in world.included_locations and locationName not in world.soh_location_sources:
            continue
        if len(loc) > 1 and not world.options.true_no_logic:
            locationRule = loc[1]((parent_region, world)) if callable(loc[1]) else loc[1]
        else:
            locationRule = True_()
        if locationName in world.included_locations:
            locationAddress = world.included_locations.pop(loc[0]).loc_id
            mLocations.append((locationName, locationAddress, locationRule))
            world.soh_location_sources[locationName] = [(parent_region, locationRule)]
        else:
            add_location_source(locationName, parent_region, locationRule, world)

    if len(mLocations) > 0:
        # Create the whole batch of locations at once
        world.get_region(str(parent_region)).add_locations({mLoc[0]: mLoc[1] for mLoc in mLocations}, SohLocation)

        # Set rules
        for mLocation in mLocations:
            locationRule = mLocation[2]
            location: Location = world.get_location(mLocation[0])
            world.set_rule(location, locationRule)


def add_location_source(location_name: str, parent_region: Regions, rule: Rule, world: "SohWorld") -> None:
    """A location that upstream lists in more than one region (LOCATION() in several areaTable entries) can be
    collected from any of them. The location moves into its own small region, entered from every listing region with
    that region's rule; entering keeps the age the region was reached with, so IsChild/IsAdult checks still hold."""
    from .Regions import SohRegion
    sources = world.soh_location_sources[location_name]
    hub_name = f"{location_name} (shared access)"
    if len(sources) == 1:
        location: Location = world.get_location(location_name)
        first_region, first_rule = sources[0]
        hub = SohRegion(hub_name, world.player, world.multiworld)
        world.multiworld.regions.append(hub)
        location.parent_region.locations.remove(location)
        location.parent_region = hub
        hub.locations.append(location)
        world.set_rule(location, True_())
        world.create_entrance(world.get_region(str(first_region)), hub, first_rule)
    sources.append((parent_region, rule))
    world.create_entrance(world.get_region(str(parent_region)), world.get_region(hub_name), rule)


def connect_regions(parent_region: Regions, world: "SohWorld", child_regions: list[tuple[Regions, Rule | Callable[[tuple[Regions, "SohWorld"]], Rule]]]) -> None:
    parentRegion: Region = world.get_region(str(parent_region))

    for region in child_regions:
        childRegion = world.get_region(region[0])
        
        if len(region) > 1 and not world.options.true_no_logic:
            regionRule = region[1]((parent_region, world)) if callable(region[1]) else region[1]  # type: ignore # noqa
        else:
            regionRule = True_()
        world.create_entrance(parentRegion, childRegion, regionRule)


def add_events(parent_region: Regions, world: "SohWorld", events: list[tuple[StrEnum, Events | StrEnum, Rule | Callable[[tuple[Regions, "SohWorld"]], Rule]]]) -> None:
    parentRegion: Region = world.get_region(str(parent_region))

    for event in events:
        eventName = str(event[0])
        eventItemName = str(event[1])
        eventRule = event[2]((parent_region, world)) if callable(event[2]) else event[2]
        # test_for_age_check(eventRule, parent_region, world)
        parentRegion.add_event(eventName, eventItemName, eventRule, SohLocation, SohItem)


def can_use(item: Items, bundle: tuple[Regions, "SohWorld"]) -> Rule:
    # 9.3.1 Logic::CanUse: HasItem && ItemUseAllowed (items that can't be used in the region's scene)
    if not item_use_allowed(item, bundle[0]):
        return False_()
    rule : Rule = has_item(item, bundle)
    data = item_data_table

    if item in data:
        if data[item].adult_only:
            rule &= is_adult(bundle)

        if data[item].child_only:
            rule &= is_child(bundle)

        if data[item].item_type == ItemType.magic:
            rule &= has_item(Items.MAGIC_SINGLE, bundle)

        if data[item].item_type == ItemType.song:
            rule &= can_play_song(item, bundle)
            # 9.3.1 Logic::CanUse: every song but Song of Storms checks CanUse(RG_FAIRY_OCARINA), so the scene's
            # ocarina restriction applies (Song of Storms only checks HasItem)
            if item != Items.SONG_OF_STORMS and not item_use_allowed(Items.FAIRY_OCARINA, bundle[0]):
                return False_()

    if item in (Items.FIRE_ARROW, Items.ICE_ARROW, Items.LIGHT_ARROW):
        rule &= can_use(Items.FAIRY_BOW, bundle)

    if item in (Items.BOMBCHU_BAG, Items.BOMBCHUS_5, Items.BOMBCHUS_10, Items.BOMBCHUS_20):
        rule &= bombchu_refill(bundle)

    if item == Items.FISHING_POLE:
        rule &= has_item(Items.CHILD_WALLET, bundle)

    if item == Items.EPONA:
        rule &= is_adult(bundle) & can_use(Items.EPONAS_SONG, bundle)
    
    return rule

# --- per-scene item restrictions (9.3.1 logic.cpp Logic::ItemUseAllowed / Logic::BAllowed, StaticData sets) -----------
_SWORDS = {Items.KOKIRI_SWORD, Items.MASTER_SWORD, Items.GIANTS_KNIFE, Items.BIGGORONS_SWORD}
_ALWAYS_ALLOWED = {Items.DEKU_SHIELD, Items.HYLIAN_SHIELD, Items.MIRROR_SHIELD, Items.GORON_TUNIC, Items.ZORA_TUNIC,
                   Items.IRON_BOOTS, Items.HOVER_BOOTS, Items.MAGIC_SINGLE, Items.SILVER_GAUNTLETS,
                   Items.GOLDEN_GAUNTLETS, Items.ZELDAS_LULLABY, Items.EPONAS_SONG, Items.PRELUDE_OF_LIGHT,
                   Items.SARIAS_SONG, Items.SONG_OF_TIME, Items.BOLERO_OF_FIRE, Items.REQUIEM_OF_SPIRIT,
                   Items.SONG_OF_STORMS, Items.MINUET_OF_FOREST, Items.SERENADE_OF_WATER, Items.NOCTURNE_OF_SHADOW}
_RESTRICT_SPELLS = {Items.FARORES_WIND, Items.DINS_FIRE, Items.NAYRUS_LOVE}
_RESTRICT_TRADE = {Items.POCKET_EGG, Items.COJIRO, Items.ODD_MUSHROOM, Items.ODD_POTION, Items.POACHERS_SAW,
                   Items.BROKEN_GORONS_SWORD, Items.PRESCRIPTION, Items.EYEBALL_FROG, Items.WORLDS_FINEST_EYEDROPS,
                   Items.CLAIM_CHECK}
# allowMasks / allowBottleMaskTrade without the masks (the apworld handles masks in can_use_mask)
_ALLOW_MASKS = {Items.WEIRD_EGG, Items.ZELDAS_LETTER}
_ALLOW_BOTTLE_MASK_TRADE = _ALLOW_MASKS | _RESTRICT_TRADE | {
    Items.EMPTY_BOTTLE, Items.BOTTLE_WITH_MILK, Items.BOTTLE_WITH_RED_POTION, Items.BOTTLE_WITH_GREEN_POTION,
    Items.BOTTLE_WITH_BLUE_POTION, Items.BOTTLE_WITH_FAIRY, Items.BOTTLE_WITH_FISH, Items.BOTTLE_WITH_BLUE_FIRE,
    Items.BOTTLE_WITH_BUGS, Items.BOTTLE_WITH_POE, Items.BOTTLE_WITH_RUTOS_LETTER, Items.BOTTLE_WITH_BIG_POE}
_OCARINAS = {Items.FAIRY_OCARINA, Items.OCARINA_OF_TIME}

_SCENES_ALL_ALLOWED = {"SCENE_DEKU_TREE", "SCENE_DODONGOS_CAVERN", "SCENE_JABU_JABU", "SCENE_FOREST_TEMPLE",
                       "SCENE_FIRE_TEMPLE", "SCENE_WATER_TEMPLE", "SCENE_SPIRIT_TEMPLE", "SCENE_SHADOW_TEMPLE",
                       "SCENE_BOTTOM_OF_THE_WELL", "SCENE_ICE_CAVERN", "SCENE_ID_MAX"}
_SCENES_NO_FARORE = {"SCENE_HYRULE_FIELD", "SCENE_GANONS_TOWER", "SCENE_GERUDO_TRAINING_GROUND",
                     "SCENE_THIEVES_HIDEOUT", "SCENE_INSIDE_GANONS_CASTLE", "SCENE_GREAT_FAIRYS_FOUNTAIN_MAGIC",
                     "SCENE_FAIRYS_FOUNTAIN", "SCENE_GREAT_FAIRYS_FOUNTAIN_SPELLS", "SCENE_GROTTOS",
                     "SCENE_GRAVE_WITH_FAIRYS_FOUNTAIN", "SCENE_REDEAD_GRAVE", "SCENE_ROYAL_FAMILYS_TOMB",
                     "SCENE_KAKARIKO_VILLAGE", "SCENE_GRAVEYARD", "SCENE_ZORAS_RIVER", "SCENE_KOKIRI_FOREST",
                     "SCENE_SACRED_FOREST_MEADOW", "SCENE_LAKE_HYLIA", "SCENE_ZORAS_DOMAIN", "SCENE_ZORAS_FOUNTAIN",
                     "SCENE_GERUDO_VALLEY", "SCENE_LOST_WOODS", "SCENE_DESERT_COLOSSUS", "SCENE_GERUDOS_FORTRESS",
                     "SCENE_HAUNTED_WASTELAND", "SCENE_HYRULE_CASTLE", "SCENE_DEATH_MOUNTAIN_TRAIL",
                     "SCENE_DEATH_MOUNTAIN_CRATER", "SCENE_GORON_CITY", "SCENE_LON_LON_RANCH",
                     "SCENE_OUTSIDE_GANONS_CASTLE"}
_SCENES_COLLAPSE = {"SCENE_GANONS_TOWER_COLLAPSE_INTERIOR", "SCENE_INSIDE_GANONS_CASTLE_COLLAPSE",
                    "SCENE_GANONS_TOWER_COLLAPSE_EXTERIOR"}
_SCENES_BOSS = {"SCENE_DEKU_TREE_BOSS", "SCENE_DODONGOS_CAVERN_BOSS", "SCENE_JABU_JABU_BOSS",
                "SCENE_FOREST_TEMPLE_BOSS", "SCENE_FIRE_TEMPLE_BOSS", "SCENE_WATER_TEMPLE_BOSS",
                "SCENE_SPIRIT_TEMPLE_BOSS", "SCENE_SHADOW_TEMPLE_BOSS", "SCENE_GANONDORF_BOSS", "SCENE_GANON_BOSS"}
_SCENES_TOWN_AND_HOUSES = {"SCENE_MARKET_ENTRANCE_DAY", "SCENE_MARKET_ENTRANCE_NIGHT", "SCENE_MARKET_ENTRANCE_RUINS",
                           "SCENE_BACK_ALLEY_DAY", "SCENE_BACK_ALLEY_NIGHT", "SCENE_MARKET_DAY", "SCENE_MARKET_NIGHT",
                           "SCENE_MARKET_RUINS", "SCENE_TEMPLE_OF_TIME_EXTERIOR_DAY",
                           "SCENE_TEMPLE_OF_TIME_EXTERIOR_NIGHT", "SCENE_TEMPLE_OF_TIME_EXTERIOR_RUINS",
                           "SCENE_KNOW_IT_ALL_BROS_HOUSE", "SCENE_TWINS_HOUSE", "SCENE_MIDOS_HOUSE",
                           "SCENE_SARIAS_HOUSE", "SCENE_KAKARIKO_CENTER_GUEST_HOUSE", "SCENE_BACK_ALLEY_HOUSE",
                           "SCENE_BAZAAR", "SCENE_KOKIRI_SHOP", "SCENE_GORON_SHOP", "SCENE_ZORA_SHOP",
                           "SCENE_POTION_SHOP_KAKARIKO", "SCENE_BOMBCHU_SHOP", "SCENE_HAPPY_MASK_SHOP",
                           "SCENE_LINKS_HOUSE", "SCENE_DOG_LADY_HOUSE", "SCENE_STABLE", "SCENE_IMPAS_HOUSE",
                           "SCENE_LAKESIDE_LABORATORY", "SCENE_CARPENTERS_TENT", "SCENE_GRAVEKEEPERS_HUT",
                           "SCENE_TEMPLE_OF_TIME", "SCENE_LON_LON_BUILDINGS", "SCENE_HOUSE_OF_SKULLTULA"}
_SCENES_MASKS_ONLY = {"SCENE_SHOOTING_GALLERY", "SCENE_CASTLE_COURTYARD_GUARDS_DAY",
                      "SCENE_CASTLE_COURTYARD_GUARDS_NIGHT", "SCENE_BOMBCHU_BOWLING_ALLEY"}
_SCENES_NO_SWORD = {"SCENE_TREASURE_BOX_SHOP", "SCENE_KNOW_IT_ALL_BROS_HOUSE", "SCENE_TWINS_HOUSE", "SCENE_MIDOS_HOUSE",
                    "SCENE_SARIAS_HOUSE", "SCENE_KAKARIKO_CENTER_GUEST_HOUSE", "SCENE_BACK_ALLEY_HOUSE",
                    "SCENE_BAZAAR", "SCENE_KOKIRI_SHOP", "SCENE_GORON_SHOP", "SCENE_ZORA_SHOP",
                    "SCENE_POTION_SHOP_KAKARIKO", "SCENE_BOMBCHU_SHOP", "SCENE_HAPPY_MASK_SHOP", "SCENE_LINKS_HOUSE",
                    "SCENE_DOG_LADY_HOUSE", "SCENE_STABLE", "SCENE_IMPAS_HOUSE", "SCENE_LAKESIDE_LABORATORY",
                    "SCENE_CARPENTERS_TENT", "SCENE_GRAVEKEEPERS_HUT", "SCENE_SHOOTING_GALLERY",
                    "SCENE_BOMBCHU_BOWLING_ALLEY", "SCENE_POTION_SHOP_GRANNY", "SCENE_CASTLE_COURTYARD_GUARDS_DAY",
                    "SCENE_CASTLE_COURTYARD_GUARDS_NIGHT", "SCENE_FISHING_POND"}


def b_allowed(region: Regions) -> bool:
    """Logic::BAllowed: can the B button (swords) be used in this region's scene."""
    if region == Regions.LH_LAB_UNDERWATER:  # upstream: "hacky fix for underwater sections"
        return False
    return REGION_SCENE.get(region, "SCENE_ID_MAX") not in _SCENES_NO_SWORD


def item_use_allowed(item, region: Regions) -> bool:
    """Logic::ItemUseAllowed for the region a rule belongs to (upstream CurrentRegionKey: the parent region of an
    entrance, or the region of an event/location). Fixed per region, so it is decided while building the rules."""
    if item in _SWORDS:
        return b_allowed(region)
    if item in _ALWAYS_ALLOWED:
        return True
    if region == Regions.LH_LAB_UNDERWATER:
        return item in (Items.HOOKSHOT, Items.LONGSHOT)
    scene = REGION_SCENE.get(region, "SCENE_ID_MAX")
    if scene in _SCENES_ALL_ALLOWED:
        return True
    if scene in _SCENES_NO_FARORE:
        return item != Items.FARORES_WIND
    if scene in _SCENES_COLLAPSE:
        return item != Items.FARORES_WIND and item not in _OCARINAS
    if scene == "SCENE_CASTLE_COURTYARD_ZELDA":
        return item not in _RESTRICT_SPELLS and item not in _OCARINAS
    if scene in _SCENES_BOSS:
        return item not in _RESTRICT_TRADE and item != Items.FARORES_WIND and item not in _OCARINAS
    if scene == "SCENE_WINDMILL_AND_DAMPES_GRAVE":
        return item not in _RESTRICT_SPELLS
    if scene == "SCENE_MARKET_GUARD_HOUSE":
        return item not in _RESTRICT_SPELLS and item not in (Items.HOOKSHOT, Items.LONGSHOT)
    if scene in _SCENES_TOWN_AND_HOUSES:
        return item in _ALLOW_BOTTLE_MASK_TRADE or item in _OCARINAS
    if scene == "SCENE_TREASURE_BOX_SHOP":
        return item in _ALLOW_BOTTLE_MASK_TRADE or item == Items.LENS_OF_TRUTH
    if scene == "SCENE_POTION_SHOP_GRANNY":
        return item in _ALLOW_BOTTLE_MASK_TRADE
    if scene in _SCENES_MASKS_ONLY:
        return item in _ALLOW_MASKS
    if scene == "SCENE_FISHING_POND":
        return item == Items.FISHING_POLE
    return True  # upstream default: SPDLOG_INFO + true


def mask_use_allowed(region: Regions) -> bool:
    """Logic::ItemUseAllowed for masks: all masks are in allowMasks/allowBottleMaskTrade, so only the fishing pond
    (fishing pole only) and the Lakeside Lab underwater spot (hookshots only) forbid them."""
    if region == Regions.LH_LAB_UNDERWATER:
        return False
    return REGION_SCENE.get(region, "SCENE_ID_MAX") != "SCENE_FISHING_POND"


def can_use_any(names: list[Items], bundle: tuple[Regions, "SohWorld"]) -> Rule:
    rule: Rule
    for i in range(len(names)):
        if i == 0:
            rule = can_use(names[i], bundle)
        else:
            rule |= can_use(names[i], bundle) # type: ignore
    return rule # type: ignore


def has_item(item: Items | Events | StrEnum, bundle: tuple[Regions, "SohWorld"], count: int = 1) -> Rule:
    if (item != Items.SKELETON_KEY and item in item_data_table and item_data_table[item].tags
            and item_data_table[item].tags & GroupTag.Overworld_Key):
        # 9.3.1 Logic::HasItem: overworld keys count as owned unless Lock Overworld Doors is on
        return can_open_overworld_door(item, bundle)

    if item in BOSS_SOULS:
        # 9.3.1 Logic::HasItem: boss souls count as owned while they aren't shuffled
        return has_boss_soul(item, bundle)

    if item == Items.STICKS:
        return has_item(Events.CAN_FARM_STICKS, bundle) & has_item(Items.DEKU_STICK_BAG, bundle)

    if item in (Items.BOMBCHU_BAG, Items.BOMBCHUS_5, Items.BOMBCHUS_10, Items.BOMBCHUS_20):
        return bombchus_enabled(bundle)

    if item == Items.NUTS:
        return has_item(Events.CAN_FARM_NUTS, bundle) & has_item(Items.DEKU_NUT_BAG, bundle)

    if item == Items.MAGIC_BEAN:
        return HasAny(Items.MAGIC_BEAN_PACK, Events.CAN_BUY_BEANS)

    # 9.3.1 Logic::HasItem: the knife is found, the first Progressive Goron Sword, or bought from Medigoron (not with
    # progressive swords, Medigoron then only replaces broken knives); Biggoron's Sword is found or the second one
    if item == Items.GIANTS_KNIFE:
        return (Has(Items.GIANTS_KNIFE) | Has(Items.PROGRESSIVE_GORON_SWORD)
                | (Has(Events.MEDIGORON) & True_(options=[OptionFilter(ProgressiveGoronSword, False)])))

    if item == Items.BIGGORONS_SWORD:
        return Has(Items.BIGGORONS_SWORD) | Has(Items.PROGRESSIVE_GORON_SWORD, 2)

    # apworld rule: found shields can be lost (fire, Like-Likes), so only buyable ones count. With "Gate Shop Shields &
    # Tunics" the found shield is what unlocks buying it (CanAffordSlot).
    if item == Items.DEKU_SHIELD:
        return Has(Items.BUY_DEKU_SHIELD)

    if item == Items.HYLIAN_SHIELD:
        return Has(Items.BUY_HYLIAN_SHIELD)

    if item == Items.GORON_TUNIC:
        return HasAny(Items.BUY_GORON_TUNIC, Items.GORON_TUNIC)

    if item == Items.ZORA_TUNIC:
        return HasAny(Items.BUY_ZORA_TUNIC, Items.ZORA_TUNIC)

    if item == Items.SCARECROW:
        return scarecrows_song(bundle) & can_use(Items.HOOKSHOT, bundle)

    if item == Items.DISTANT_SCARECROW:
        return scarecrows_song(bundle) & can_use(Items.LONGSHOT, bundle)

    if item == Items.FISHING_POLE:
        return OptionFilter(ShuffleFishingPole, False) | Has(Items.FISHING_POLE)

    if item == Items.EPONA:
        return Has(Events.FREED_EPONA)

    if item in {Items.POCKET_EGG, Items.COJIRO, Items.ODD_MUSHROOM, Items.ODD_POTION, Items.POACHERS_SAW,
                Items.BROKEN_GORONS_SWORD, Items.PRESCRIPTION, Items.EYEBALL_FROG, Items.WORLDS_FINEST_EYEDROPS}:
        return OptionFilter(ShuffleAdultTradeItems, False) | Has(item)

    if item == Items.BOTTLE_WITH_BLUE_FIRE:
        return has_bottle(bundle) & (Has(Events.CAN_ACCESS_BLUE_FIRE) | Has(Items.BUY_BLUE_FIRE))

    if item == Items.BOTTLE_WITH_BLUE_POTION:
        return has_bottle(bundle) & Has(Items.BUY_BLUE_POTION)

    if item == Items.BOTTLE_WITH_BUGS:
        return has_bottle(bundle) & (Has(Events.CAN_ACCESS_BUGS) | Has(Items.BUY_BOTTLE_BUG))

    if item == Items.BOTTLE_WITH_FAIRY:
        return has_bottle(bundle) & (Has(Events.CAN_ACCESS_FAIRIES) | Has(Items.BUY_FAIRYS_SPIRIT))

    if item == Items.BOTTLE_WITH_FISH:
        return has_bottle(bundle) & (Has(Events.CAN_ACCESS_FISH) | Has(Items.BUY_FISH))

    if item == Items.BOTTLE_WITH_GREEN_POTION:
        return has_bottle(bundle) & Has(Items.BUY_GREEN_POTION)

    if item in (Items.BOTTLE_WITH_MILK, Items.BOTTLE_WITH_POE, Items.BOTTLE_WITH_RED_POTION, Items.EMPTY_BOTTLE):
        return has_bottle(bundle)

    for prog,non_progs in progressive_items.items():
        if item in non_progs:
            return Has(prog, non_progs.index(item) + 1)

    return Has(item, count)



# shop item -> item that has to be found first with "Gate Shop Shields & Tunics" (9.3.1 Logic::ShopItemNotForSale)
SHOP_GATED_ITEMS: dict[str, str] = {
    str(Items.BUY_DEKU_SHIELD): str(Items.DEKU_SHIELD),
    str(Items.BUY_HYLIAN_SHIELD): str(Items.HYLIAN_SHIELD),
    str(Items.BUY_GORON_TUNIC): str(Items.GORON_TUNIC),
    str(Items.BUY_ZORA_TUNIC): str(Items.ZORA_TUNIC),
}


@dataclasses.dataclass
class CanAffordSlot(Rule, game="Ship of Harkinian"):
    location: Locations

    def _instantiate(self, world: "SohWorld") -> Rule.Resolved: # type: ignore
        return self.Resolved(location = self.location, player = world.player,
                             caching_enabled=getattr(world, "rule_caching_enabled", False))

    class Resolved(Rule.Resolved):
        location: Locations
        #player: int
        
        def _evaluate(self, state: CollectionState) -> bool:
            world = state.multiworld.worlds[self.player]
            wallet = get_wallet_for_shop_slot(self.location, world)[0] #type: ignore
            prog_wallet_count = progressive_items[Items.PROGRESSIVE_WALLET].index(wallet) + 1
            if not state.has(Items.PROGRESSIVE_WALLET, self.player, prog_wallet_count):
                return False
            # 9.3.1 Logic::ShopItemNotForSale ("Gate Shop Shields & Tunics"): a non-randomized shield or tunic in a
            # shop slot can't be bought before the same item has been found elsewhere
            if world.options.shop_shields_and_tunics_only_refill:  # type: ignore
                location = state.multiworld.regions.location_cache[self.player].get(str(self.location))
                item = location.item if location is not None else None  # events use slots that aren't locations
                if item is not None and item.player == self.player and item.name in SHOP_GATED_ITEMS:
                    return state.has(SHOP_GATED_ITEMS[item.name], self.player)
            return True

        def item_dependencies(self) -> dict[str, set[int]]:
            deps = {str(Items.PROGRESSIVE_WALLET): {id(self)}}
            for found in SHOP_GATED_ITEMS.values():
                deps[found] = {id(self)}
            return deps
        
        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            data = get_wallet_for_shop_slot(self.location, state.multiworld.worlds[self.player])
            verb = "Missing " if state and not self(state) else "Has "
            messages: list[JSONMessagePart] = [{"type": "text", "text": verb}]
            if state:
                color = "green" if self(state) else "salmon"
                messages.append({"type": "color", "color": color, "text": data[0]})
                messages.append({"type": "text", "text": f" to buy item for "})
                messages.append({"type": "color", "color": "cyan", "text": str(data[1])})
                messages.append({"type": "text", "text": f" rupees"})
            else:
                messages.append({"type": "item_name", "flags": 0b001, "text": data[0], "player": self.player})
            return messages

        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            data = get_wallet_for_shop_slot(self.location, state.multiworld.worlds[self.player])
            if state is None:
                return str(self)
            prefix = "Has" if self(state) else "Missing"
            return f"{prefix} {data[0]} to buy item for {str(data[1])} rupees"

        @override
        def __str__(self) -> str:
            return f"Has wallet large enough to buy the item at {str(self.location)}"


def get_wallet_for_shop_slot(location: Locations, world: "SohWorld") -> tuple[str, int]:
    price = world.shop_prices.get(location, 500)
    for wallet, amount in wallet_capacities.items():
        if amount >= price:
            return str(wallet), price

def can_afford_slot(slot: Locations, bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return CanAffordSlot(slot)


def scarecrows_song(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return ((OptionFilter(SkipScarecrowsSong, True) & has_item(Items.FAIRY_OCARINA, bundle)
            & has_enough_ocarina_buttons(bundle, 2))
            | (has_item(Events.CHILD_SCARECROW_UNLOCKED, bundle) & has_item(Events.ADULT_SCARECROW_UNLOCKED, bundle)))


def has_bottle(bundle: tuple[Regions, "SohWorld"]) -> Rule:  # soup
    return has_bottle_count(1)

#Exists just to make the bottle rule somewhat more understandable in explains
@dataclasses.dataclass()
class HasBottleCount(WrapperRule, game="Ship of Harkinian"):
    count: int

    def _instantiate(self, world: World) -> Rule.Resolved:
        return self.Resolved(
            self.child.resolve(world),
            player=world.player,
            caching_enabled=getattr(world, "rule_caching_enabled", False),
            count = self.count
        )

    class Resolved(WrapperRule.Resolved):
        count: int
        
        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            verb = "Does not have " if state and not self(state) else "Has "
            messages: list[JSONMessagePart] = [{"type": "text", "text": verb}]
            bottles = "bottles" if self.count > 1 else "bottle"
            if state:
                messages.append({"type": "color", "color": "cyan", "text": f"{self.count} "})
                messages.append({"type": "text", "text": f"emptiable {bottles}"})
            else:
                messages.append({"type": "text", "text": f"at least {self.count} emptiable {bottles}"})
            return messages

        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            return f"{"Has" if self(state) else "Does not have"} {self.count} emptiable bottle{"s" if self.count > 1 else ""}"

        @override
        def __str__(self) -> str:
            return f"Has {self.count} bottle{"s" if self.count>1 else ""}"


def has_bottle_count(target_count: int) -> Rule:
    return HasBottleCount( \
        (HasAll(Events.DELIVER_RUTOS_LETTER, Events.CAN_EMPTY_BIG_POES) & HasFromList(*no_rules_bottles, Items.BOTTLE_WITH_BIG_POE, Items.BOTTLE_WITH_RUTOS_LETTER, count=target_count)) \
            | (Has(Events.DELIVER_RUTOS_LETTER) & HasFromList(*no_rules_bottles, Items.BOTTLE_WITH_RUTOS_LETTER, count=target_count)) \
            | (Has(Events.CAN_EMPTY_BIG_POES) & HasFromList(*no_rules_bottles, Items.BOTTLE_WITH_BIG_POE, count=target_count)) \
            | HasFromList(*no_rules_bottles, count=target_count) \
        , count = target_count)


def bombchu_refill(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return OptionFilter(BombchuDrops, True) | HasAny(Items.BUY_BOMBCHUS10, Items.BUY_BOMBCHUS20, Events.COULD_PLAY_BOWLING, Events.CARPET_MERCHANT)


def bombchus_enabled(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return Has(Items.BOMBCHU_BAG) | Has(Items.PROGRESSIVE_BOMB_BAG, options=[OptionFilter(BombchuBag, False)])


ocarina_buttons_required: dict[str, list[str]] = {
    Items.ZELDAS_LULLABY: [Items.OCARINA_CLEFT_BUTTON, Items.OCARINA_CRIGHT_BUTTON, Items.OCARINA_CUP_BUTTON],
    Items.EPONAS_SONG: [Items.OCARINA_CLEFT_BUTTON, Items.OCARINA_CRIGHT_BUTTON, Items.OCARINA_CUP_BUTTON],
    Items.PRELUDE_OF_LIGHT: [Items.OCARINA_CLEFT_BUTTON, Items.OCARINA_CRIGHT_BUTTON, Items.OCARINA_CUP_BUTTON],
    Items.SARIAS_SONG: [Items.OCARINA_CLEFT_BUTTON, Items.OCARINA_CRIGHT_BUTTON, Items.OCARINA_CDOWN_BUTTON],
    Items.SUNS_SONG: [Items.OCARINA_CRIGHT_BUTTON, Items.OCARINA_CUP_BUTTON, Items.OCARINA_CDOWN_BUTTON],
    Items.SONG_OF_TIME: [Items.OCARINA_A_BUTTON, Items.OCARINA_CRIGHT_BUTTON, Items.OCARINA_CDOWN_BUTTON],
    Items.BOLERO_OF_FIRE: [Items.OCARINA_A_BUTTON, Items.OCARINA_CRIGHT_BUTTON, Items.OCARINA_CDOWN_BUTTON],
    Items.REQUIEM_OF_SPIRIT: [Items.OCARINA_A_BUTTON, Items.OCARINA_CRIGHT_BUTTON, Items.OCARINA_CDOWN_BUTTON],
    Items.SONG_OF_STORMS: [Items.OCARINA_A_BUTTON, Items.OCARINA_CUP_BUTTON, Items.OCARINA_CDOWN_BUTTON],
    Items.MINUET_OF_FOREST: [Items.OCARINA_A_BUTTON, Items.OCARINA_CLEFT_BUTTON, Items.OCARINA_CRIGHT_BUTTON, Items.OCARINA_CUP_BUTTON],
    Items.SERENADE_OF_WATER: [Items.OCARINA_A_BUTTON, Items.OCARINA_CLEFT_BUTTON, Items.OCARINA_CRIGHT_BUTTON, Items.OCARINA_CDOWN_BUTTON],
    Items.NOCTURNE_OF_SHADOW: [Items.OCARINA_A_BUTTON, Items.OCARINA_CLEFT_BUTTON, Items.OCARINA_CRIGHT_BUTTON, Items.OCARINA_CDOWN_BUTTON],
}


def can_play_song(song: StrEnum, bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return has_item(Items.FAIRY_OCARINA, bundle) & has_item(song, bundle) & (OptionFilter(ShuffleOcarinaButtons, False) | HasAll(*ocarina_buttons_required[song]))


def has_explosives(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """Check if Link has access to explosives (bombs or bombchus)."""
    return can_use_any([Items.BOMB_BAG, Items.BOMBCHU_BAG], bundle)


def blast_or_smash(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """Check if Link can blast or smash obstacles."""
    return has_explosives(bundle) | can_use(Items.MEGATON_HAMMER, bundle)


def blue_fire(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """Check if Link has access to blue fire."""
    return ((has_bottle(bundle) &
             (has_item(Events.CAN_ACCESS_BLUE_FIRE, bundle) |
              has_item(Items.BUY_BLUE_FIRE, bundle))) |
            (can_use(Items.ICE_ARROW, bundle) &
             OptionFilter(BlueFireArrows, True)))


def can_use_sword(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """Check if Link can use any sword."""
    return can_use_any([Items.KOKIRI_SWORD, Items.MASTER_SWORD, Items.BIGGORONS_SWORD], bundle)


def has_projectile(bundle: tuple[Regions, "SohWorld"], age: Ages = Ages.null) -> Rule:
    """Check if Link has access to projectiles."""
    if age == Ages.CHILD:
        return has_explosives(bundle) | can_use_any([Items.FAIRY_SLINGSHOT, Items.BOOMERANG], bundle)
    elif age == Ages.ADULT:
        return has_explosives(bundle) | can_use_any([Items.HOOKSHOT, Items.FAIRY_BOW], bundle)
    else:  # "either"
        return has_explosives(bundle) | can_use_any([Items.FAIRY_SLINGSHOT, Items.BOOMERANG, Items.HOOKSHOT, Items.FAIRY_BOW], bundle)


def can_use_projectile(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return has_projectile(bundle)


def can_break_mud_walls(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return blast_or_smash(bundle) | (can_do_trick(Tricks.BLUE_FIRE_MUD_WALLS, bundle) & blue_fire(bundle))


def can_get_deku_baba_sticks(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return can_use_sword(bundle) | can_use(Items.BOOMERANG, bundle)


def can_get_deku_baba_nuts(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return can_use_any([Items.FAIRY_SLINGSHOT, Items.FAIRY_BOW, Items.DINS_FIRE], bundle) | can_jump_slash(bundle) | has_explosives(bundle)


@dataclasses.dataclass
class IsAdult(Rule, game="Ship of Harkinian"):
    parent_region: Regions

    def _instantiate(self, world: "SohWorld") -> Rule.Resolved: # type: ignore
        return self.Resolved(parent_region = self.parent_region, player = world.player, caching_enabled=getattr(world, "rule_caching_enabled", False))

    class Resolved(Rule.Resolved):
        parent_region: Regions
        force_recalculate = True
        def _evaluate(self, state: CollectionState) -> bool:
            return state._soh_can_reach_as_age(self.parent_region, Ages.ADULT, self.player) # type: ignore

        def item_dependencies(self) -> dict[str, set[int]]:
            return {}
        
        def region_dependencies(self) -> dict[str, set[int]]:
            return {self.parent_region.value: {id(self)}}
        
        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            verb = "Can not " if state and not self(state) else "Can "
            messages: list[JSONMessagePart] = [{"type": "text", "text": verb}]
            if state:
                color = "green" if self(state) else "salmon"
                messages.append({"type": "text", "text": "reach "})
                messages.append({"type": "color", "color": "cyan", "text": f"{self.parent_region} "})
                messages.append({"type": "text", "text": "as "})
                messages.append({"type": "color", "color": color, "text": "Adult Link"})
            return messages
        
        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            prefix = "Can" if self(state) else "Can not"
            return f"{prefix} reach {str(self.parent_region)} as Adult Link"

        @override
        def __str__(self) -> str:
            return f"Can reach {str(self.parent_region)} as Adult Link"

@dataclasses.dataclass
class IsChild(Rule, game="Ship of Harkinian"):
    parent_region: Regions

    def _instantiate(self, world: "SohWorld") -> Rule.Resolved: # type: ignore
        return self.Resolved(parent_region = self.parent_region, player = world.player, caching_enabled=getattr(world, "rule_caching_enabled", False))

    class Resolved(Rule.Resolved):
        parent_region: Regions
        force_recalculate = True
        def _evaluate(self, state: CollectionState) -> bool:
            return state._soh_can_reach_as_age(self.parent_region, Ages.CHILD, self.player) # type: ignore

        def item_dependencies(self) -> dict[str, set[int]]:
            return {}
        
        def region_dependencies(self) -> dict[str, set[int]]:
            return {self.parent_region.value: {id(self)}}
        
        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            verb = "Can not " if state and not self(state) else "Can "
            messages: list[JSONMessagePart] = [{"type": "text", "text": verb}]
            if state:
                color = "green" if self(state) else "salmon"
                messages.append({"type": "text", "text": "reach "})
                messages.append({"type": "color", "color": "cyan", "text": f"{self.parent_region} "})
                messages.append({"type": "text", "text": "as "})
                messages.append({"type": "color", "color": color, "text": "Child Link"})
            return messages
        
        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            prefix = "Can" if self(state) else "Can not"
            return f"{prefix} reach {self.parent_region} as Child Link"

        @override
        def __str__(self) -> str:
            return f"Can reach {self.parent_region} as Child Link"

#Build the rules
def is_child(bundle: tuple[Regions, "SohWorld"]):
    return IsChild(bundle[0])

def is_adult(bundle: tuple[Regions, "SohWorld"]):
    return IsAdult(bundle[0])

def at_day(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return ((is_child(bundle) & has_item(Events.CHILD_CAN_PASS_TIME, bundle))
            | (is_adult(bundle) & has_item(Events.ADULT_CAN_PASS_TIME, bundle)))
    # TODO: Implement starting time of day if that ever gets added


def at_night(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return ((is_child(bundle) & has_item(Events.CHILD_CAN_PASS_TIME, bundle))
            | (is_adult(bundle) & has_item(Events.ADULT_CAN_PASS_TIME, bundle)))
    # TODO: Implement starting time of day if that ever gets added

def starting_age(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return IsChild(bundle[0], options=[OptionFilter(StartingAge, StartingAge.option_child)]) | IsAdult(bundle[0], options=[OptionFilter(StartingAge, StartingAge.option_adult)])


def can_damage(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """Check if Link can deal damage to enemies."""
    return (can_jump_slash(bundle) |
            has_explosives(bundle) |
            can_use_any([Items.FAIRY_SLINGSHOT, Items.FAIRY_BOW, Items.DINS_FIRE], bundle))


def can_attack(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """Check if Link can attack enemies (damage or stun)."""
    return (can_damage(bundle) |
            can_use_any([Items.BOOMERANG, Items.HOOKSHOT], bundle))


def can_standing_shield(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """Check if Link can use a shield for standing blocks."""
    return (can_use_any([Items.MIRROR_SHIELD, Items.DEKU_SHIELD], bundle) |
            (is_adult(bundle) & has_item(Items.HYLIAN_SHIELD, bundle)))  # upstream: HasItem


def can_shield(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """Check if Link can use a shield for blocking or stunning."""
    # upstream 9.3.1 Logic::CanShield: Hylian Shield via HasItem (any age)
    return can_use_any([Items.MIRROR_SHIELD, Items.DEKU_SHIELD], bundle) | has_item(Items.HYLIAN_SHIELD, bundle)


def can_do_trick(trick: Tricks, bundle: tuple[Regions, "SohWorld"]) -> Rule:
    # check if we have the trick enabled, the GLITCHED item is for Universal Tracker purposes.
    return OptionFilter(EnableAllTricks, True) | Has(Items.GLITCHED) | OptionFilter(TricksInLogic, trick.value, "contains")


def can_get_nighttime_gs(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return at_night(bundle) & (OptionFilter(SkullsSunSong, False) | can_use(Items.SUNS_SONG, bundle))


def can_read(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """logic.cpp Logic::CanRead: always true in 9.3.1 (signs)."""
    return True_()


def can_break_rocks(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """logic.cpp Logic::CanBreakRocks: BlastOrSmash() || HasItem(RG_POWER_BRACELET) (= the grab ability)."""
    return blast_or_smash(bundle) | has_grab(bundle)


def can_bonk_trees(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """Check if Link can bonk trees."""
    return True_()


def can_hit_eye_targets(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """Check if Link can hit eye switches/targets."""
    return can_use_any([Items.FAIRY_BOW, Items.FAIRY_SLINGSHOT], bundle)


def can_stun_deku(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """Check if Link can stun Deku Scrubs."""
    return can_attack(bundle) | can_use(Items.NUTS, bundle) | can_reflect_nuts(bundle)


def can_reflect_nuts(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """Check if Link can reflect Deku Nuts back at enemies."""
    return can_use(Items.DEKU_SHIELD, bundle) | (is_adult(bundle) & has_item(Items.HYLIAN_SHIELD, bundle))


def has_fire_source_with_torch(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """Check if Link has a fire source that can be used with a torch."""
    return has_fire_source(bundle) | can_use(Items.STICKS, bundle)


def has_fire_source(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """Check if Link has any fire source."""
    return can_use_any([Items.DINS_FIRE, Items.FIRE_ARROW], bundle)


def can_jump_slash_except_hammer(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """Check if Link can perform a jump slash with any sword."""
    return can_use(Items.STICKS, bundle) | can_use_sword(bundle)


def can_jump_slash(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """Check if Link can perform a jump slash at all"""
    return can_jump_slash_except_hammer(bundle) | can_use(Items.MEGATON_HAMMER, bundle)


def call_gossip_fairy_except_suns(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return can_use_any([Items.ZELDAS_LULLABY, Items.EPONAS_SONG, Items.SONG_OF_TIME], bundle)


def call_gossip_fairy(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return (call_gossip_fairy_except_suns(bundle) | can_use(Items.SUNS_SONG, bundle))


def can_break_lower_hives(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return can_break_upper_beehives(bundle) | can_use(Items.BOMB_BAG, bundle)


def can_break_upper_beehives(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return (hookshot_or_boomerang(bundle) | 
            (can_do_trick(Tricks.BOMBCHU_BEEHIVES, bundle) & can_use(Items.BOMBCHU_BAG, bundle)) |
            (OptionFilter(SlingbowBreakBeehives, True) & (can_use_any([Items.FAIRY_BOW, Items.FAIRY_SLINGSHOT], bundle))))


def can_open_storms_grotto(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return (can_use(Items.SONG_OF_STORMS, bundle) & (has_item(Items.STONE_OF_AGONY, bundle) | can_do_trick(Tricks.GROTTOS_WITHOUT_AGONY, bundle)))


def can_hit_at_range(bundle: tuple[Regions, "SohWorld"],
                     distance: EnemyDistance = EnemyDistance.CLOSE,
                     wall_or_floor: bool = True, in_water: bool = False) -> Rule:
    rule = False_()
    if distance == EnemyDistance.CLOSE:
        rule |= can_use(Items.MEGATON_HAMMER, bundle)
    if distance <= EnemyDistance.SHORT_JUMPSLASH:
        rule |= can_use(Items.KOKIRI_SWORD, bundle)
    if distance <= EnemyDistance.MASTER_SWORD_JUMPSLASH:
        rule |= can_use(Items.MASTER_SWORD, bundle)
    if distance <= EnemyDistance.LONG_JUMPSLASH:
        rule |= can_use_any([Items.BIGGORONS_SWORD, Items.STICKS], bundle)
    if distance <= EnemyDistance.BOMB_THROW and not in_water:
        rule |= can_use(Items.BOMB_BAG, bundle)
    if distance <= EnemyDistance.HOOKSHOT:
        wof = True_() if wall_or_floor else False_()
        rule |= can_use(Items.HOOKSHOT, bundle) | (wof & can_use(Items.BOMBCHUS_5, bundle))
    if distance <= EnemyDistance.LONGSHOT:
        rule |= can_use(Items.LONGSHOT, bundle)
    if distance <= EnemyDistance.FAR:
        rule |= can_use_any([Items.FAIRY_SLINGSHOT, Items.FAIRY_BOW], bundle)
    return rule

def can_kill_enemy(bundle: tuple[Regions, "SohWorld"], enemy: Enemies, distance: EnemyDistance = EnemyDistance.CLOSE,
                   wall_or_floor: bool = True, quantity: int = 1, timer: bool = False, in_water: bool = False) -> Rule:
    """Port of upstream 9.3.1 Logic::CanKillEnemy (soh/soh/Enhancements/randomizer/logic.cpp).

    The C++ switch(distance) falls through from the given distance to ED_FAR, so a weapon listed under
    `case ED_X` counts whenever distance <= ED_X.
    """
    def at(case: EnemyDistance) -> bool:
        return distance <= case

    if enemy in (Enemies.GERUDO_GUARD, Enemies.BREAK_ROOM_GUARD):
        return False_()

    if enemy == Enemies.GOLD_SKULLTULA:
        rule: Rule = False_()
        if at(EnemyDistance.CLOSE):
            rule |= can_use(Items.MEGATON_HAMMER, bundle)
        if at(EnemyDistance.SHORT_JUMPSLASH):
            rule |= can_use(Items.KOKIRI_SWORD, bundle)
        if at(EnemyDistance.MASTER_SWORD_JUMPSLASH):
            rule |= can_use(Items.MASTER_SWORD, bundle)
        if at(EnemyDistance.LONG_JUMPSLASH):
            rule |= can_use_any([Items.BIGGORONS_SWORD, Items.STICKS], bundle)
        if at(EnemyDistance.BOMB_THROW):
            rule |= can_use(Items.BOMB_BAG, bundle)
        if at(EnemyDistance.BOOMERANG):
            rule |= can_use_any([Items.BOOMERANG, Items.DINS_FIRE], bundle)
        if at(EnemyDistance.HOOKSHOT):
            rule |= can_use(Items.HOOKSHOT, bundle)
        if at(EnemyDistance.LONGSHOT):
            rule |= can_use(Items.LONGSHOT, bundle)
            if wall_or_floor:
                rule |= can_use(Items.BOMBCHUS_5, bundle)
        rule |= can_use_any([Items.FAIRY_SLINGSHOT, Items.FAIRY_BOW], bundle)
        return rule

    if enemy in (Enemies.GOHMA_LARVA, Enemies.MAD_SCRUB, Enemies.DEKU_BABA, Enemies.POE):
        return can_attack(bundle)

    if enemy == Enemies.BIG_SKULLTULA:
        rule = False_()
        if at(EnemyDistance.CLOSE):
            rule |= can_use(Items.MEGATON_HAMMER, bundle)
        if at(EnemyDistance.SHORT_JUMPSLASH):
            rule |= can_use(Items.KOKIRI_SWORD, bundle)
        if at(EnemyDistance.MASTER_SWORD_JUMPSLASH):
            rule |= can_use(Items.MASTER_SWORD, bundle)
        if at(EnemyDistance.LONG_JUMPSLASH):
            rule |= can_use_any([Items.BIGGORONS_SWORD, Items.STICKS], bundle)
        if at(EnemyDistance.BOMB_THROW):
            rule |= can_use_any([Items.BOMB_BAG, Items.DINS_FIRE], bundle)
        if at(EnemyDistance.HOOKSHOT):  # ED_BOOMERANG falls into ED_HOOKSHOT
            rule |= can_use(Items.HOOKSHOT, bundle)
            if wall_or_floor:
                rule |= can_use(Items.BOMBCHUS_5, bundle)
        if at(EnemyDistance.LONGSHOT):
            rule |= can_use(Items.LONGSHOT, bundle)
        rule |= can_use_any([Items.FAIRY_SLINGSHOT, Items.FAIRY_BOW], bundle)
        return rule

    if enemy == Enemies.DODONGO:
        rule = (can_use_sword(bundle) | can_use(Items.MEGATON_HAMMER, bundle) | has_explosives(bundle)
                | can_use_any([Items.FAIRY_SLINGSHOT, Items.FAIRY_BOW], bundle))
        if quantity <= 5:
            rule |= can_use(Items.STICKS, bundle)
        return rule

    if enemy == Enemies.LIZALFOS:
        return (can_jump_slash(bundle) | has_explosives(bundle)
                | can_use_any([Items.FAIRY_SLINGSHOT, Items.FAIRY_BOW], bundle))

    if enemy in (Enemies.KEESE, Enemies.FIRE_KEESE, Enemies.GUAY):
        rule = False_()
        if at(EnemyDistance.SHORT_JUMPSLASH):
            rule |= can_use_any([Items.MEGATON_HAMMER, Items.KOKIRI_SWORD], bundle)
        if at(EnemyDistance.MASTER_SWORD_JUMPSLASH):
            rule |= can_use(Items.MASTER_SWORD, bundle)
        if at(EnemyDistance.LONG_JUMPSLASH):
            rule |= can_use_any([Items.BIGGORONS_SWORD, Items.STICKS], bundle)
        if at(EnemyDistance.BOMB_THROW):
            if not in_water:
                rule |= can_use(Items.BOMB_BAG, bundle)
            if enemy == Enemies.GUAY:
                rule |= can_use(Items.DINS_FIRE, bundle)
        if at(EnemyDistance.BOOMERANG):
            rule |= can_use(Items.BOOMERANG, bundle)
        if at(EnemyDistance.HOOKSHOT):
            rule |= can_use(Items.HOOKSHOT, bundle)
            if wall_or_floor:
                rule |= can_use(Items.BOMBCHUS_5, bundle)
        if at(EnemyDistance.LONGSHOT):
            rule |= can_use(Items.LONGSHOT, bundle)
        rule |= can_use_any([Items.FAIRY_SLINGSHOT, Items.FAIRY_BOW], bundle)
        return rule

    if enemy == Enemies.BLUE_BUBBLE:
        return (blast_or_smash(bundle) | can_use(Items.FAIRY_BOW, bundle)
                | ((can_jump_slash_except_hammer(bundle) | can_use(Items.FAIRY_SLINGSHOT, bundle))
                   & (can_use(Items.NUTS, bundle) | hookshot_or_boomerang(bundle) | can_standing_shield(bundle))))

    if enemy == Enemies.DEAD_HAND:
        return (can_use_sword(bundle)
                | (can_use(Items.STICKS, bundle) & can_do_trick(Tricks.BOTW_CHILD_DEADHAND, bundle)))

    if enemy == Enemies.WITHERED_DEKU_BABA:
        return can_use_sword(bundle) | can_use(Items.BOOMERANG, bundle)

    if enemy in (Enemies.LIKE_LIKE, Enemies.FLOORMASTER):
        return can_damage(bundle)

    if enemy == Enemies.STALFOS:
        rule = False_()
        if at(EnemyDistance.SHORT_JUMPSLASH):
            rule |= can_use_any([Items.MEGATON_HAMMER, Items.KOKIRI_SWORD], bundle)
        if at(EnemyDistance.MASTER_SWORD_JUMPSLASH):
            rule |= can_use(Items.MASTER_SWORD, bundle)
        if at(EnemyDistance.LONG_JUMPSLASH):
            rule |= can_use(Items.BIGGORONS_SWORD, bundle)
            if quantity <= 1:
                rule |= can_use(Items.STICKS, bundle)
        if at(EnemyDistance.BOMB_THROW) and quantity <= 2 and not timer and not in_water:
            rule |= ((can_use(Items.NUTS, bundle) | hookshot_or_boomerang(bundle))
                     & can_use(Items.BOMB_BAG, bundle))
        if at(EnemyDistance.HOOKSHOT) and wall_or_floor:
            rule |= can_use(Items.BOMBCHUS_5, bundle)
        rule |= can_use(Items.FAIRY_BOW, bundle)
        return rule

    if enemy == Enemies.IRON_KNUCKLE:
        return can_use_sword(bundle) | can_use(Items.MEGATON_HAMMER, bundle) | has_explosives(bundle)

    if enemy == Enemies.FLARE_DANCER:
        return (can_use_any([Items.MEGATON_HAMMER, Items.HOOKSHOT], bundle)
                | (has_explosives(bundle)
                   & (can_jump_slash_except_hammer(bundle)
                      | can_use_any([Items.FAIRY_BOW, Items.FAIRY_SLINGSHOT, Items.BOOMERANG], bundle))))

    if enemy in (Enemies.WOLFOS, Enemies.WHITE_WOLFOS, Enemies.WALLMASTER):
        return (can_jump_slash(bundle)
                | can_use_any([Items.FAIRY_BOW, Items.FAIRY_SLINGSHOT, Items.BOMBCHUS_5, Items.DINS_FIRE], bundle)
                | (can_use(Items.BOMB_BAG, bundle)
                   & can_use_any([Items.NUTS, Items.HOOKSHOT, Items.BOOMERANG], bundle)))

    if enemy == Enemies.GERUDO_WARRIOR:
        return (can_jump_slash(bundle) | can_use(Items.FAIRY_BOW, bundle)
                | (can_do_trick(Tricks.GF_WARRIOR_WITH_DIFFICULT_WEAPON, bundle)
                   & can_use_any([Items.FAIRY_SLINGSHOT, Items.BOMBCHUS_5], bundle)))

    if enemy in (Enemies.GIBDO, Enemies.REDEAD):
        return can_jump_slash(bundle) | can_use(Items.DINS_FIRE, bundle)

    if enemy == Enemies.MEG:
        return can_use_any([Items.FAIRY_BOW, Items.HOOKSHOT], bundle) | has_explosives(bundle)

    if enemy == Enemies.ARMOS:
        return (blast_or_smash(bundle)
                | can_use_any([Items.MASTER_SWORD, Items.BIGGORONS_SWORD, Items.STICKS, Items.FAIRY_BOW], bundle)
                | (can_use_any([Items.NUTS, Items.HOOKSHOT, Items.BOOMERANG], bundle)
                   & can_use_any([Items.KOKIRI_SWORD, Items.FAIRY_SLINGSHOT], bundle)))

    if enemy == Enemies.GREEN_BUBBLE:
        return (can_jump_slash(bundle) | can_use_any([Items.FAIRY_BOW, Items.FAIRY_SLINGSHOT], bundle)
                | has_explosives(bundle))

    if enemy == Enemies.DINOLFOS:
        rule = can_jump_slash(bundle) | can_use_any([Items.FAIRY_BOW, Items.FAIRY_SLINGSHOT], bundle)
        if not timer:
            rule |= can_use(Items.BOMBCHUS_5, bundle)
        return rule

    if enemy == Enemies.TORCH_SLUG:
        return can_jump_slash(bundle) | has_explosives(bundle) | can_use(Items.FAIRY_BOW, bundle)

    if enemy == Enemies.FREEZARD:
        return (can_use_any([Items.MASTER_SWORD, Items.BIGGORONS_SWORD, Items.MEGATON_HAMMER, Items.STICKS,
                             Items.HOOKSHOT, Items.DINS_FIRE, Items.FIRE_ARROW], bundle)
                | has_explosives(bundle))

    if enemy == Enemies.SHELL_BLADE:
        return (can_jump_slash(bundle) | has_explosives(bundle)
                | can_use_any([Items.HOOKSHOT, Items.FAIRY_BOW, Items.DINS_FIRE], bundle))

    if enemy == Enemies.SPIKE:
        return (can_use_any([Items.MASTER_SWORD, Items.BIGGORONS_SWORD, Items.MEGATON_HAMMER, Items.STICKS,
                             Items.HOOKSHOT, Items.FAIRY_BOW, Items.DINS_FIRE], bundle)
                | has_explosives(bundle))

    if enemy == Enemies.STINGER:
        rule = False_()
        if at(EnemyDistance.SHORT_JUMPSLASH):
            rule |= can_use_any([Items.MEGATON_HAMMER, Items.KOKIRI_SWORD], bundle)
        if at(EnemyDistance.MASTER_SWORD_JUMPSLASH):
            rule |= can_use(Items.MASTER_SWORD, bundle)
        if at(EnemyDistance.LONG_JUMPSLASH):
            rule |= can_use_any([Items.BIGGORONS_SWORD, Items.STICKS], bundle)
        if at(EnemyDistance.BOMB_THROW) and not in_water:
            rule |= can_use(Items.BOMB_BAG, bundle)
        if at(EnemyDistance.HOOKSHOT):  # ED_BOOMERANG falls into ED_HOOKSHOT
            rule |= can_use(Items.HOOKSHOT, bundle)
            if wall_or_floor:
                rule |= can_use(Items.BOMBCHUS_5, bundle)
        if at(EnemyDistance.LONGSHOT):
            rule |= can_use(Items.LONGSHOT, bundle)
        rule |= can_use_any([Items.FAIRY_SLINGSHOT, Items.FAIRY_BOW], bundle)
        return rule

    if enemy == Enemies.BIG_OCTO:
        return can_use_any([Items.KOKIRI_SWORD, Items.STICKS, Items.MASTER_SWORD], bundle)

    if enemy == Enemies.GOHMA:
        return (has_boss_soul(Items.GOHMAS_SOUL, bundle) & can_jump_slash(bundle)
                & (can_use_any([Items.NUTS, Items.FAIRY_SLINGSHOT, Items.FAIRY_BOW], bundle)
                   | hookshot_or_boomerang(bundle)))

    if enemy == Enemies.KING_DODONGO:
        return (has_boss_soul(Items.KING_DODONGOS_SOUL, bundle) & can_jump_slash(bundle)
                & (can_use(Items.BOMB_BAG, bundle) | has_item(Items.GORONS_BRACELET, bundle)
                   | (can_do_trick(Tricks.DC_DODONGO_CHU, bundle) & is_adult(bundle)
                      & can_use(Items.BOMBCHUS_5, bundle))))

    if enemy == Enemies.BARINADE:
        return (has_boss_soul(Items.BARINADES_SOUL, bundle) & can_use(Items.BOOMERANG, bundle)
                & (can_jump_slash_except_hammer(bundle)
                   | (can_do_trick(Tricks.JABU_BARINADE_POTS, bundle) & has_grab(bundle))))

    if enemy == Enemies.PHANTOM_GANON:
        return (has_boss_soul(Items.PHANTOM_GANONS_SOUL, bundle) & can_use_sword(bundle)
                & can_use_any([Items.HOOKSHOT, Items.FAIRY_BOW, Items.FAIRY_SLINGSHOT], bundle))

    if enemy == Enemies.VOLVAGIA:
        return has_boss_soul(Items.VOLVAGIAS_SOUL, bundle) & can_use(Items.MEGATON_HAMMER, bundle)

    if enemy == Enemies.MORPHA:
        return (has_boss_soul(Items.MORPHAS_SOUL, bundle)
                & (can_use(Items.HOOKSHOT, bundle)
                   | (can_do_trick(Tricks.WATER_MORPHA_WITHOUT_HOOKSHOT, bundle)
                      & has_item(Items.BRONZE_SCALE, bundle)))
                & (can_use_sword(bundle) | can_use(Items.MEGATON_HAMMER, bundle)))

    if enemy == Enemies.BONGO_BONGO:
        return (has_boss_soul(Items.BONGO_BONGOS_SOUL, bundle)
                & (can_use(Items.LENS_OF_TRUTH, bundle) | can_do_trick(Tricks.LENS_BONGO, bundle))
                & can_use_sword(bundle)
                & (can_use_any([Items.HOOKSHOT, Items.FAIRY_BOW, Items.FAIRY_SLINGSHOT], bundle)
                   | can_do_trick(Tricks.SHADOW_BONGO, bundle)))

    if enemy == Enemies.TWINROVA:
        return (has_boss_soul(Items.TWINROVAS_SOUL, bundle) & can_use(Items.MIRROR_SHIELD, bundle)
                & (can_use_sword(bundle) | can_use(Items.MEGATON_HAMMER, bundle)))

    if enemy == Enemies.GANONDORF:
        return has_boss_soul(Items.GANONS_SOUL, bundle) & can_use(Items.LIGHT_ARROW, bundle) & can_use_sword(bundle)

    if enemy == Enemies.GANON:
        return has_boss_soul(Items.GANONS_SOUL, bundle) & can_use(Items.MASTER_SWORD, bundle)

    if enemy == Enemies.DARK_LINK:
        return (can_use_sword(bundle)
                | (can_use(Items.BOOMERANG, bundle)
                   & (can_use_any([Items.FAIRY_BOW, Items.STICKS, Items.MEGATON_HAMMER], bundle)
                      | has_explosives(bundle)))
                | (can_use(Items.NUTS, bundle) & can_use_any([Items.STICKS, Items.MEGATON_HAMMER], bundle)))

    if enemy == Enemies.ANUBIS:
        # there's a restoration that allows beating them with mirror shield + some way to trigger their attack
        return has_fire_source(bundle)

    if enemy == Enemies.BEAMOS:
        return has_explosives(bundle)

    if enemy == Enemies.PURPLE_LEEVER:
        # dies on its own, so this is the conditions to spawn it (killing 10 normal leevers)
        return can_use_any([Items.MASTER_SWORD, Items.BIGGORONS_SWORD], bundle)

    if enemy == Enemies.TENTACLE:
        return can_use(Items.BOOMERANG, bundle)

    if enemy == Enemies.BARI:
        return (hookshot_or_boomerang(bundle)
                | can_use_any([Items.FAIRY_BOW, Items.MEGATON_HAMMER, Items.STICKS, Items.DINS_FIRE], bundle)
                | has_explosives(bundle)
                | (take_damage(bundle) & can_use_sword(bundle)))

    if enemy == Enemies.SHABOM:
        # EffectiveHealth() > quantity * 4 (1/16 hearts): tank the hits
        return (can_use_any([Items.BOOMERANG, Items.NUTS, Items.DINS_FIRE, Items.ICE_ARROW], bundle)
                | can_jump_slash(bundle)
                | effective_health_at_least(bundle, quantity * 4 + 1))

    if enemy == Enemies.OCTOROK:
        rule = (can_reflect_nuts(bundle) | hookshot_or_boomerang(bundle)
                | can_use_any([Items.FAIRY_BOW, Items.FAIRY_SLINGSHOT, Items.BOMB_BAG], bundle))
        if wall_or_floor:
            rule |= can_use(Items.BOMBCHUS_5, bundle)
        return rule

    if enemy == Enemies.WALLTULA:
        rule = False_()
        if at(EnemyDistance.SHORT_JUMPSLASH):
            rule |= can_use(Items.KOKIRI_SWORD, bundle)
        if at(EnemyDistance.MASTER_SWORD_JUMPSLASH):
            rule |= can_use(Items.MASTER_SWORD, bundle)
        if at(EnemyDistance.LONG_JUMPSLASH):
            rule |= can_use_any([Items.BIGGORONS_SWORD, Items.STICKS], bundle)
        if at(EnemyDistance.BOMB_THROW):
            if not in_water:
                rule |= can_use(Items.BOMB_BAG, bundle)
            rule |= can_use(Items.DINS_FIRE, bundle)
        if at(EnemyDistance.BOOMERANG):
            rule |= can_use(Items.BOOMERANG, bundle)
        if at(EnemyDistance.HOOKSHOT):
            rule |= can_use_any([Items.HOOKSHOT, Items.BOMBCHUS_5, Items.MEGATON_HAMMER], bundle)
        if at(EnemyDistance.LONGSHOT):
            rule |= can_use(Items.LONGSHOT, bundle)
        rule |= can_use_any([Items.FAIRY_SLINGSHOT, Items.FAIRY_BOW], bundle)
        return rule

    raise ValueError(f"can_kill_enemy: no rule for {enemy}")  # upstream: SPDLOG_ERROR + assert(false)


BOSS_SOULS = {Items.GOHMAS_SOUL, Items.KING_DODONGOS_SOUL, Items.BARINADES_SOUL, Items.PHANTOM_GANONS_SOUL,
              Items.VOLVAGIAS_SOUL, Items.MORPHAS_SOUL, Items.BONGO_BONGOS_SOUL, Items.TWINROVAS_SOUL, Items.GANONS_SOUL}


def has_boss_soul(soul: Items, bundle: tuple[Regions, "SohWorld"]):
    # only check for possesion of gannons soul if the option 'on_plus_ganons' is selected
    if soul == Items.GANONS_SOUL:
        # 9.3.1 Logic::HasItem(RG_GANON_SOUL): RSK_GANONS_SOUL "Start With" or found (the old "On + Ganon" boss soul
        # setting is migrated to Ganon's Soul "Anywhere" in Options.adjust_ganons_soul)
        return OptionFilter(GanonsSoul, GanonsSoul.option_start_with) | Has(soul)
        
    return OptionFilter(ShuffleBossSouls, ShuffleBossSouls.option_off) | Has(soul)


def can_pass_enemy(bundle: tuple[Regions, "SohWorld"], enemy: Enemies,
                   distance: EnemyDistance = EnemyDistance.CLOSE, wall_or_floor: bool = True) -> Rule:
    # upstream 9.3.1 Logic::CanPassEnemy
    if enemy in {Enemies.GOLD_SKULLTULA, Enemies.GOHMA_LARVA, Enemies.LIZALFOS, Enemies.DODONGO, Enemies.MAD_SCRUB,
                 Enemies.KEESE, Enemies.FIRE_KEESE, Enemies.BLUE_BUBBLE, Enemies.DEAD_HAND, Enemies.DEKU_BABA,
                 Enemies.WITHERED_DEKU_BABA, Enemies.STALFOS, Enemies.FLARE_DANCER, Enemies.WOLFOS,
                 Enemies.WHITE_WOLFOS, Enemies.FLOORMASTER, Enemies.MEG, Enemies.ARMOS, Enemies.FREEZARD, Enemies.SPIKE,
                 Enemies.DARK_LINK, Enemies.ANUBIS, Enemies.WALLMASTER, Enemies.PURPLE_LEEVER, Enemies.OCTOROK}:
        return True_()

    if enemy == Enemies.GERUDO_GUARD:
        return (can_do_trick(Tricks.PASS_GUARDS_WITH_NOTHING, bundle)
                | has_item(Items.GERUDO_MEMBERSHIP_CARD, bundle)
                | can_use_any([Items.FAIRY_BOW, Items.HOOKSHOT], bundle))

    if enemy == Enemies.BREAK_ROOM_GUARD:
        return (has_item(Items.GERUDO_MEMBERSHIP_CARD, bundle)
                | can_use_any([Items.FAIRY_BOW, Items.HOOKSHOT], bundle))

    if enemy == Enemies.BIG_SKULLTULA:
        # hammer jumpslash can pass, but only on flat land where you can kill with hammer swing
        rule = (can_kill_enemy(bundle, enemy, distance, wall_or_floor)
                | can_use_any([Items.NUTS, Items.BOOMERANG], bundle))
        if wall_or_floor and distance == EnemyDistance.CLOSE:
            rule |= can_do_trick(Tricks.BIG_SKULLTULA_PAUSE_LIFT, bundle)
        return rule

    if enemy == Enemies.LIKE_LIKE:
        return (can_kill_enemy(bundle, enemy, distance, wall_or_floor)
                | can_use_any([Items.HOOKSHOT, Items.BOOMERANG], bundle))

    if enemy in [Enemies.GIBDO, Enemies.REDEAD]:
        # 9.3.1: you can move slowly to avoid getting screamed at
        return True_()

    if enemy in [Enemies.IRON_KNUCKLE, Enemies.BIG_OCTO, Enemies.WALLTULA]:  # Walltula: consistent with RT_SPIRIT_WALL
        return can_kill_enemy(bundle, enemy, distance, wall_or_floor)

    if enemy == Enemies.GREEN_BUBBLE:
        return (can_kill_enemy(bundle, enemy, distance, wall_or_floor)
                | take_damage(bundle)
                | can_use_any([Items.NUTS, Items.BOOMERANG, Items.HOOKSHOT], bundle))

    return can_kill_enemy(bundle, enemy, distance, wall_or_floor)


def can_cut_shrubs(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """Check if Link can cut shrubs (grass, bushes)."""
    # upstream 9.3.1 Logic::CanCutShrubs also lists Giant's Knife
    return (can_use_sword(bundle) | can_use(Items.GIANTS_KNIFE, bundle) |
            has_explosives(bundle) |
            can_use_any([Items.BOOMERANG, Items.MEGATON_HAMMER], bundle) |
            has_item(Items.GORONS_BRACELET, bundle))  # upstream: HasItem, not CanUse (no per-scene restriction)


def hookshot_or_boomerang(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """Check if Link has hookshot or boomerang."""
    return can_use_any([Items.HOOKSHOT, Items.BOOMERANG], bundle)


def can_open_underwater_chest(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return (can_do_trick(Tricks.OPEN_UNDERWATER_CHEST, bundle) &
            can_use(Items.IRON_BOOTS, bundle) &
            can_use(Items.HOOKSHOT, bundle) &
            has_open_chest(bundle))  # 9.3.1 Logic::CanOpenUnderwaterChest: && HasItem(RG_OPEN_CHEST)


def can_open_overworld_door(key: Items, bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return OptionFilter(LockOverworldDoors, False) | HasAny(Items.SKELETON_KEY, key)


key_to_ring: dict[Items, Items] = {
    Items.FOREST_TEMPLE_SMALL_KEY: Items.FOREST_TEMPLE_KEY_RING,
    Items.FIRE_TEMPLE_SMALL_KEY: Items.FIRE_TEMPLE_KEY_RING,
    Items.WATER_TEMPLE_SMALL_KEY: Items.WATER_TEMPLE_KEY_RING,
    Items.BOTTOM_OF_THE_WELL_SMALL_KEY: Items.BOTTOM_OF_THE_WELL_KEY_RING,
    Items.SHADOW_TEMPLE_SMALL_KEY: Items.SHADOW_TEMPLE_KEY_RING,
    Items.GERUDO_FORTRESS_SMALL_KEY: Items.GERUDO_FORTRESS_KEY_RING,
    Items.TRAINING_GROUND_SMALL_KEY: Items.TRAINING_GROUND_KEY_RING,
    Items.SPIRIT_TEMPLE_SMALL_KEY: Items.SPIRIT_TEMPLE_KEY_RING,
    Items.GANONS_CASTLE_SMALL_KEY: Items.GANONS_CASTLE_KEY_RING,
}


def small_keys(key: Items, requiredAmount: int, bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return HasAny(Items.SKELETON_KEY, key_to_ring[key]) | Has(key, requiredAmount)


def can_get_enemy_drop(bundle: tuple[Regions, "SohWorld"], enemy: Enemies,
                       distance: EnemyDistance = EnemyDistance.CLOSE, aboveLink: bool = False) -> Rule:
    rule: Rule = can_kill_enemy(bundle, enemy, distance)
    if distance.value <= EnemyDistance.MASTER_SWORD_JUMPSLASH.value:
        return rule
    match enemy:
        case Enemies.GOLD_SKULLTULA:
            gs_rule: Rule = False_()
            if distance <= EnemyDistance.BOOMERANG:
                gs_rule |= can_use(Items.BOOMERANG, bundle)
            if distance <= EnemyDistance.HOOKSHOT:
                gs_rule |= can_use(Items.HOOKSHOT, bundle)
            if distance <= EnemyDistance.LONGSHOT:
                gs_rule |= can_use(Items.LONGSHOT, bundle)
            return rule & gs_rule
        case Enemies.KEESE | Enemies.FIRE_KEESE | Enemies.GUAY:
            return rule
        case _:
            # upstream 9.3.1 Logic::CanGetEnemyDrop: aboveLink || (distance <= ED_BOOMERANG && CanUse(RG_BOOMERANG))
            if aboveLink:
                return rule
            if distance <= EnemyDistance.BOOMERANG:
                return rule & can_use(Items.BOOMERANG, bundle)
            return False_()
    return False_()

def can_detonate_bomb_flowers(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return can_use_any([Items.FAIRY_BOW, Items.DINS_FIRE], bundle) | has_explosives(bundle)


def can_detonate_upright_bomb_flower(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return (can_detonate_bomb_flowers(bundle)
            | has_item(Items.GORONS_BRACELET, bundle)
            | (can_do_trick(Tricks.BLUE_FIRE_MUD_WALLS, bundle)
                & blue_fire(bundle)
                # 9.3.1 Logic::CanDetonateUprightBombFlower: EffectiveHealth() > 8 (1/16 hearts)
                & (effective_health_at_least(bundle, 9)
                     | can_use(Items.NAYRUS_LOVE, bundle))))

  
def get_group_name(item_group: GroupTag) -> str:
    return item_group.name.replace('_', " ")


def item_group_count_enough(item_group: str, count: int):
    return HasGroupUnique(item_group, count)


def has_enough_ocarina_buttons(bundle: tuple[Regions, "SohWorld"], amount: int) -> Rule:
    group_name = get_group_name(GroupTag.Ocarina_Button)
    return OptionFilter(ShuffleOcarinaButtons, False) | HasGroup(group_name, amount)


def has_enough_stones(bundle: tuple[Regions, "SohWorld"], amount: int) -> Rule:
    group_name = get_group_name(GroupTag.Spiritual_Stone)
    return HasGroupUnique(group_name, amount)


def has_enough_medallions(amount: int) -> Rule:
    group_name = get_group_name(GroupTag.Medallion)
    return HasGroupUnique(group_name, amount)


dungeon_events: list[Events] = [Events.DEKU_TREE_COMPLETED, Events.DODONGOS_CAVERN_COMPLETED,
                                Events.JABU_JABUS_BELLY_COMPLETED, Events.FOREST_TEMPLE_COMPLETED,
                                Events.FIRE_TEMPLE_COMPLETED, Events.WATER_TEMPLE_COMPLETED,
                                Events.SPIRIT_TEMPLE_COMPLETED, Events.SHADOW_TEMPLE_COMPLETED]


def cleared_enough_dungeons(amount: int):
    return HasFromList(*dungeon_events, count=amount)


def can_spawn_soil_skull(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return is_child(bundle) & can_use(Items.BOTTLE_WITH_BUGS, bundle)


def fire_timer_at_least(bundle: tuple[Regions, "SohWorld"], amount: int) -> Rule:
    return can_use(Items.GORON_TUNIC, bundle) | (HeartsAtLeast(amount=int(math.ceil(amount/8))) & can_do_trick(Tricks.FEWER_TUNIC_REQUIREMENTS, bundle))


def water_timer_at_least(bundle: tuple[Regions, "SohWorld"], amount: int) -> Rule:
    return can_use(Items.ZORA_TUNIC, bundle) | (HeartsAtLeast(amount=int(math.ceil(amount/8))) & can_do_trick(Tricks.FEWER_TUNIC_REQUIREMENTS, bundle))


@dataclasses.dataclass
class HeartsAtLeast(Rule, game="Ship of Harkinian"):
    amount: int
    def _instantiate(self, world: World) -> Rule.Resolved:
        return self.Resolved(player=world.player, amount = self.amount, caching_enabled=getattr(world, "rule_caching_enabled", False))
    class Resolved(Rule.Resolved):
        player: int
        amount: int
        def _evaluate(self, state: CollectionState) -> bool:
            return state.soh_heart_count[self.player] >= self.amount # type: ignore
        
        def item_dependencies(self) -> dict[str, set[int]]:
            return {str(item_id): {id(self)} for item_id in (Items.HEART_CONTAINER, Items.PIECE_OF_HEART, Items.PIECE_OF_HEART_WINNER)}
        
        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            verb = "Does not have " if state and not self(state) else "Has "
            messages: list[JSONMessagePart] = [{"type": "text", "text": verb}]
            if state:
                color = "green" if self(state) else "salmon"
                messages.append({"type": "color", "color": "cyan", "text": str(self.amount)})

                if self.amount > 1:
                    messages.append({"type": "color", "color": color, "text": " hearts "})
                else:
                    messages.append({"type": "color", "color": color, "text": " heart "})

                messages.append({"type": "text", "text": f"or more"})
            return messages
        
        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            prefix = "Has" if self(state) else "Does not have"
            return f"{prefix} {self.amount} or more"

        @override
        def __str__(self) -> str:
            return f"Has {self.amount} hearts or more"

def hearts_at_least(bundle: tuple[Regions, "SohWorld"], amount) -> Rule:
    return HeartsAtLeast(amount=amount)


def can_open_bomb_grotto(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return blast_or_smash(bundle) & (has_item(Items.STONE_OF_AGONY, bundle) | can_do_trick(Tricks.GROTTOS_WITHOUT_AGONY, bundle))


def trade_quest_step(item: Items, bundle: tuple[Regions, "SohWorld"]) -> Rule:
    # If adult trade shuffle is off, it'll automatically assume the whole trade quest is complete as soon as claim check is obtained.

    rule: Rule = False_()
    # Since the original used fallthrough, we will loop through all trade quest items after this point too
    trade_items = [Items.POCKET_EGG, Items.COJIRO, Items.ODD_MUSHROOM, Items.ODD_POTION, Items.POACHERS_SAW, Items.BROKEN_GORONS_SWORD, Items.PRESCRIPTION, Items.WORLDS_FINEST_EYEDROPS, Items.CLAIM_CHECK]
    if item not in trade_items:
        return rule
    pos = trade_items.index(item)
    for i in range(pos, len(trade_items)):
        rule |= has_item(trade_items[i], bundle)
    return Filtered(has_item(Items.CLAIM_CHECK, bundle), options=[OptionFilter(ShuffleAdultTradeItems, False)]) \
        | Filtered(rule, options=[OptionFilter(ShuffleAdultTradeItems, True)])

@dataclasses.dataclass
class ItemsPlusGregEnough(Rule, game="Ship of Harkinian"):
    target: FieldResolver
    item_tag: GroupTag | list[Events]   # todo figure out a way to change dungeon events to a tag as well
    greg: FieldResolver
    def _instantiate(self, world: World) -> Rule.Resolved:
        world = cast("SohWorld", world)
        items = list()
        if isinstance(self.item_tag, list):
            items.extend(self.item_tag)
        else:
            for tag in self.item_tag:
                items.extend(world.item_name_groups[get_group_name(tag)])
        if self.greg.resolve(world) == 1: #reward, for both classes
            items.append(Items.GREG_THE_GREEN_RUPEE)
        return HasFromList(*items, count=self.target).resolve(world)

def can_build_rainbow_bridge(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    greg = FromOption(RainbowBridgeGregModifier)
    return OptionFilter(RainbowBridge, RainbowBridge.option_always_open) \
         | (OptionFilter(RainbowBridge, RainbowBridge.option_vanilla) & has_item(Items.SHADOW_MEDALLION, bundle) & has_item(Items.SPIRIT_MEDALLION, bundle) & can_use(Items.LIGHT_ARROW, bundle)) \
         | (OptionFilter(RainbowBridge, RainbowBridge.option_stones) & ItemsPlusGregEnough(target=FromOption(RainbowBridgeStonesRequired), item_tag=GroupTag.Spiritual_Stone, greg=greg)) \
         | (OptionFilter(RainbowBridge, RainbowBridge.option_medallions) & ItemsPlusGregEnough(target=FromOption(RainbowBridgeMedallionsRequired), item_tag=GroupTag.Medallion, greg=greg)) \
         | (OptionFilter(RainbowBridge, RainbowBridge.option_dungeon_rewards) & ItemsPlusGregEnough(target=FromOption(RainbowBridgeDungeonRewardsRequired), item_tag=GroupTag.Spiritual_Stone | GroupTag.Medallion, greg=greg)) \
         | (OptionFilter(RainbowBridge, RainbowBridge.option_dungeons) & ItemsPlusGregEnough(target=FromOption(RainbowBridgeDungeonsRequired), item_tag=dungeon_events, greg=greg)) \
         | (OptionFilter(RainbowBridge, RainbowBridge.option_tokens) & Has(Items.GOLD_SKULLTULA_TOKEN, count=FromOption(RainbowBridgeSkullTokensRequired))) \
         | (OptionFilter(RainbowBridge, RainbowBridge.option_greg) & Has(Items.GREG_THE_GREEN_RUPEE)) \
         | (OptionFilter(RainbowBridge, RainbowBridge.option_triforce_pieces) & TriforcePiecesAtLeast(requirement="rainbow_bridge_triforce_pieces_required"))


GANONS_SOUL_TRIGGER_OPTIONS = [GanonsSoul.option_trigger_stones, GanonsSoul.option_trigger_medallions,
                               GanonsSoul.option_trigger_dungeon_rewards, GanonsSoul.option_trigger_dungeons,
                               GanonsSoul.option_trigger_skull_tokens, GanonsSoul.option_trigger_triforce_pieces]


@dataclasses.dataclass
class TriforcePiecesAtLeast(Rule, game="Ship of Harkinian"):
    """Triforce Pieces for a trigger (Rainbow Bridge, Ganon's Boss Key, Ganon's Soul). `requirement` names the SohWorld
    attribute with the count: it is capped at the pieces actually in the pool, which is only known after
    create_triforce_pieces (ItemPool.py)."""
    requirement: str = ""

    def _instantiate(self, world: "SohWorld") -> Rule.Resolved:  # type: ignore
        return self.Resolved(requirement=self.requirement, player=world.player,
                             caching_enabled=getattr(world, "rule_caching_enabled", False))

    class Resolved(Rule.Resolved):
        item_name: str = str(Items.TRIFORCE_PIECE)
        requirement: str = ""

        def _evaluate(self, state: CollectionState) -> bool:
            world = cast("SohWorld", state.multiworld.worlds[self.player])
            return state.prog_items[self.player][self.item_name] >= getattr(world, self.requirement)

        def item_dependencies(self) -> dict[str, set[int]]:
            return {self.item_name: {id(self)}}


def can_trigger_ganons_soul(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """9.3.1 Logic::CanTriggerGanonsSoul (pseudo-location RC_GANON_SOUL in Root). Greg counts in logic only with the
    "reward" modifier (RO_CHECK_TRIGGER_GREG_REWARD)."""
    greg = FromOption(GanonsSoulGregModifier)
    return (OptionFilter(GanonsSoul, GanonsSoul.option_trigger_stones) & ItemsPlusGregEnough(target=FromOption(GanonsSoulStonesRequired), item_tag=GroupTag.Spiritual_Stone, greg=greg)) \
         | (OptionFilter(GanonsSoul, GanonsSoul.option_trigger_medallions) & ItemsPlusGregEnough(target=FromOption(GanonsSoulMedallionsRequired), item_tag=GroupTag.Medallion, greg=greg)) \
         | (OptionFilter(GanonsSoul, GanonsSoul.option_trigger_dungeon_rewards) & ItemsPlusGregEnough(target=FromOption(GanonsSoulDungeonRewardsRequired), item_tag=GroupTag.Spiritual_Stone | GroupTag.Medallion, greg=greg)) \
         | (OptionFilter(GanonsSoul, GanonsSoul.option_trigger_dungeons) & ItemsPlusGregEnough(target=FromOption(GanonsSoulDungeonsRequired), item_tag=dungeon_events, greg=greg)) \
         | (OptionFilter(GanonsSoul, GanonsSoul.option_trigger_skull_tokens) & Has(Items.GOLD_SKULLTULA_TOKEN, count=FromOption(GanonsSoulSkullTokensRequired))) \
         | (OptionFilter(GanonsSoul, GanonsSoul.option_trigger_triforce_pieces) & TriforcePiecesAtLeast(requirement="ganons_soul_triforce_pieces_required"))


GBK_TRIGGER_OPTIONS = [GanonsCastleBossKey.option_lacs_vanilla, GanonsCastleBossKey.option_lacs_stones,
                       GanonsCastleBossKey.option_lacs_medallions, GanonsCastleBossKey.option_lacs_dungeon_rewards,
                       GanonsCastleBossKey.option_lacs_dungeons, GanonsCastleBossKey.option_lacs_skull_tokens,
                       GanonsCastleBossKey.option_lacs_triforce_pieces]


def can_trigger_gbk(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """9.3.1 Logic::CanTriggerGBK: Ganon's Boss Key is granted as soon as the condition is met (upstream pseudo-location
    RC_GANONS_BOSS_KEY in Root), no longer at the Light Arrow Cutscene. The apworld's lacs_* options are the trigger
    conditions; lacs_vanilla is upstream's own migration of LACS-Vanilla (ConfigVersion7Updater): any 2 medallions.
    Greg counts in logic only with the "reward" modifier (RO_CHECK_TRIGGER_GREG_REWARD)."""
    greg = FromOption(GanonsCastleBossKeyGregModifier)
    return (OptionFilter(GanonsCastleBossKey, GanonsCastleBossKey.option_lacs_vanilla) & ItemsPlusGregEnough(target=2, item_tag=GroupTag.Medallion, greg=greg)) \
         | (OptionFilter(GanonsCastleBossKey, GanonsCastleBossKey.option_lacs_stones) & ItemsPlusGregEnough(target=FromOption(GanonsCastleBossKeyStonesRequired), item_tag=GroupTag.Spiritual_Stone, greg=greg))\
         | (OptionFilter(GanonsCastleBossKey, GanonsCastleBossKey.option_lacs_medallions) & ItemsPlusGregEnough(target=FromOption(GanonsCastleBossKeyMedallionsRequired), item_tag=GroupTag.Medallion, greg=greg)) \
         | (OptionFilter(GanonsCastleBossKey, GanonsCastleBossKey.option_lacs_dungeon_rewards) & ItemsPlusGregEnough(target=FromOption(GanonsCastleBossKeyDungeonRewardsRequired), item_tag=GroupTag.Spiritual_Stone | GroupTag.Medallion, greg=greg)) \
         | (OptionFilter(GanonsCastleBossKey, GanonsCastleBossKey.option_lacs_dungeons) & ItemsPlusGregEnough(target=FromOption(GanonsCastleBossKeyDungeonsRequired), item_tag=dungeon_events, greg=greg)) \
         | (OptionFilter(GanonsCastleBossKey, GanonsCastleBossKey.option_lacs_skull_tokens) & Has(Items.GOLD_SKULLTULA_TOKEN, count=FromOption(GanonsCastleBossKeySkullTokensRequired))) \
         | (OptionFilter(GanonsCastleBossKey, GanonsCastleBossKey.option_lacs_triforce_pieces) & TriforcePiecesAtLeast(requirement="gbk_triforce_pieces_required"))


def can_trigger_wincon(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    """9.3.1 Logic::CanTriggerWincon (pseudo-location RC_WINCON in Root) for the trigger win conditions except
    Triforce Pieces, which keeps the apworld's CanWinTriforceHunt. Greg counts in logic only with "reward"."""
    greg = FromOption(WinConditionGregModifier)
    return (OptionFilter(WinCondition, WinCondition.option_trigger_stones) & ItemsPlusGregEnough(target=FromOption(WinConditionStonesRequired), item_tag=GroupTag.Spiritual_Stone, greg=greg)) \
         | (OptionFilter(WinCondition, WinCondition.option_trigger_medallions) & ItemsPlusGregEnough(target=FromOption(WinConditionMedallionsRequired), item_tag=GroupTag.Medallion, greg=greg)) \
         | (OptionFilter(WinCondition, WinCondition.option_trigger_dungeon_rewards) & ItemsPlusGregEnough(target=FromOption(WinConditionDungeonRewardsRequired), item_tag=GroupTag.Spiritual_Stone | GroupTag.Medallion, greg=greg)) \
         | (OptionFilter(WinCondition, WinCondition.option_trigger_dungeons) & ItemsPlusGregEnough(target=FromOption(WinConditionDungeonsRequired), item_tag=dungeon_events, greg=greg)) \
         | (OptionFilter(WinCondition, WinCondition.option_trigger_skull_tokens) & Has(Items.GOLD_SKULLTULA_TOKEN, count=FromOption(WinConditionSkullTokensRequired)))



# TODO implement EffectiveHealth(); Returns 2 for now. Requires implementing a damage multiplier option
def is_fire_loop_unlocked(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return False_(options=[OptionFilter(SmallKeyShuffle, [SmallKeyShuffle.option_anywhere, SmallKeyShuffle.option_overworld, SmallKeyShuffle.option_any_dungeon], operator="in")], filtered_resolution=True)


def can_ground_jump(bundle: tuple[Regions, "SohWorld"], hasBombFlower: bool = False) -> Rule:
    if hasBombFlower:
        return (can_do_trick(Tricks.GROUND_JUMP, bundle)
                & can_standing_shield(bundle)
                & (can_use(Items.BOMB_BAG, bundle) | has_item(Items.GORONS_BRACELET, bundle)))
    else:
        return (can_do_trick(Tricks.GROUND_JUMP, bundle)
                & can_standing_shield(bundle)
                & can_use(Items.BOMB_BAG, bundle))

def can_clear_stalagmite(bundle: tuple[Regions, "SohWorld"]):
    # upstream 9.3.1 Logic::CanClearStalagmite
    return (can_jump_slash(bundle) | has_explosives(bundle) | can_use(Items.GIANTS_KNIFE, bundle)
            | (can_do_trick(Tricks.ICE_STALAGMITE_HOOKSHOT, bundle) & can_use(Items.HOOKSHOT, bundle)))


@dataclasses.dataclass
class CanWinTriforceHunt(Rule, game="Ship of Harkinian"):
    def _instantiate(self, world: "SohWorld") -> Rule.Resolved: # type: ignore
        return self.Resolved(player = world.player, caching_enabled=getattr(world, "rule_caching_enabled", False))

    class Resolved(Rule.Resolved):
        item_name: str = str(Items.TRIFORCE_PIECE)
        player: int
        def _evaluate(self, state: CollectionState) -> bool:
            return state.prog_items[self.player][self.item_name] >= cast("SohWorld", state.multiworld.worlds[self.player]).triforce_pieces_required

        def item_dependencies(self) -> dict[str, set[int]]:
            return {self.item_name: {id(self)}}
        
        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            amount = cast("SohWorld", state.multiworld.worlds[self.player]).triforce_pieces_required
            verb = "Does not have " if state and not self(state) else "Has "
            messages: list[JSONMessagePart] = [{"type": "text", "text": verb}]
            if state:
                color = "green" if self(state) else "salmon"
                messages.append({"type": "color", "color": "cyan", "text": str(amount)})

                if amount > 1:
                    messages.append({"type": "color", "color": color, "text": " Triforce Pieces "})
                else:
                    messages.append({"type": "color", "color": color, "text": " Triforce Piece "})

                messages.append({"type": "text", "text": f"or more"})
            return messages
        
        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            prefix = "Has" if self(state) else "Does not have"
            return f"{prefix} {str(cast("SohWorld", state.multiworld.worlds[self.player]).triforce_pieces_required)} Triforce Pieces or more"

        @override
        def __str__(self) -> str:
            return f"Has enough Triforce Pieces to win"


class SohHeartState(LogicMixin):
    # tracking how many hearts the player has instead of checking the collection state every time
    soh_piece_of_heart_count: Counter[int]
    soh_heart_count: Counter[int]

    def init_mixin(self, parent: MultiWorld):
        soh_players = list(parent.get_game_players(
            "Ship of Harkinian") + parent.get_game_groups("Ship of Harkinian"))
        self.soh_piece_of_heart_count = Counter()
        self.soh_heart_count = Counter({player: cast("SohWorld", parent.worlds[player]).options.starting_hearts.value for player in soh_players})

    def copy_mixin(self, ret: CollectionState) -> CollectionState:
        ret.soh_piece_of_heart_count = Counter(self.soh_piece_of_heart_count)  # type: ignore # noqa
        ret.soh_heart_count = Counter(self.soh_heart_count)  # type: ignore # noqa
        return ret


# ======================================================================================================================
# Helpers ported from upstream Ship of Harkinian 9.3.1 (soh/soh/Enhancements/randomizer/logic.cpp unless noted).
# Upstream settings the apworld doesn't offer yet are treated as off; the TODO notes name the feature that adds them
# (see docs/ap-update/feature-plan.md).
# ======================================================================================================================

class WaterLevel(IntEnum):
    """upstream RandoWaterLevel"""
    LOW = 0
    LOW_OR_MID = 1
    MID = 2
    HIGH = 3
    HIGH_OR_MID = 4


class Recoil(IntEnum):
    """upstream RecoilRequirements"""
    SWORD = 0
    SWORD_AND_SHIELD = 1
    HAMMER = 2
    HAMMER_AND_SHIELD = 3


class TorchRecoil(IntEnum):
    """upstream TorchRecoilRequirements"""
    LONG_AND_SHIELD = 0
    SHORT = 1
    MASTER = 2
    LONG = 3


# --- abilities (upstream RG_CLIMB, RG_CRAWL, RG_OPEN_CHEST, RG_POWER_BRACELET, RG_SPEAK_*) ---------------------------
# Without the ability shuffles (feature 3.11) the game gives all of them at the start.
def has_climb(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return True_()  # TODO feature 3.11 (Shuffle Climb)


def has_crawl(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return True_()  # TODO feature 3.11 (Shuffle Crawl)


def has_open_chest(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return True_()  # TODO feature 3.11 (Shuffle Open Chest)


def has_grab(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return True_()  # TODO feature 3.11 (Shuffle Grab / RG_POWER_BRACELET)


def has_speak(bundle: tuple[Regions, "SohWorld"], language: str) -> Rule:
    return True_()  # TODO feature 3.11 (Shuffle Speak)


def can_open_large_chest(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    # Logic::CanOpenLargeChest: RAND_INF_CAN_OPEN_LARGE_CHEST, only withheld by Shuffle Open Chest "Progressive"
    return True_()  # TODO feature 3.11


# --- masks (Logic::HasItem RG_*_MASK / RG_BUNNY_HOOD, Logic::CanUse) -------------------------------------------------
def has_mask(bundle: tuple[Regions, "SohWorld"], mask: str) -> Rule:
    # Complete Mask Quest = start with every mask (client maps it to the RSK_STARTING_* masks).
    # Otherwise masks are borrowed in order: Keaton -> Skull -> Spooky -> Bunny Hood, Mask of Truth after all four.
    borrow = has_item(Events.CAN_BORROW_MASKS, bundle)
    sold = {
        "KEATON_MASK": [],
        "SKULL_MASK": [Events.SOLD_KEATON_MASK],
        "SPOOKY_MASK": [Events.SOLD_SKULL_MASK],
        "BUNNY_HOOD": [Events.SOLD_SPOOKY_MASK],
        "MASK_OF_TRUTH": [Events.SOLD_KEATON_MASK, Events.SOLD_SKULL_MASK, Events.SOLD_SPOOKY_MASK,
                          Events.SOLD_BUNNY_HOOD],
    }[mask]
    rule: Rule = borrow
    for event in sold:
        rule &= has_item(event, bundle)
    starting = {"KEATON_MASK": StartWithKeatonMask, "SKULL_MASK": StartWithSkullMask, "SPOOKY_MASK": StartWithSpookyMask, "BUNNY_HOOD": StartWithBunnyHood, "MASK_OF_TRUTH": StartWithMaskOfTruth}[mask]
    # RSK_STARTING_<mask> (9.3.1 HasItem: RAND_INF_CHILD_TRADES_HAS_MASK_*)
    return (True_(options=[OptionFilter(CompleteMaskQuest, True)]) | True_(options=[OptionFilter(starting, True)])
            | rule)


def can_use_mask(bundle: tuple[Regions, "SohWorld"], mask: str) -> Rule:
    # Logic::CanUse: masks need child, unless Masks as Adult (RSK_MASKS_AS_ADULT)
    if not mask_use_allowed(bundle[0]):  # Logic::ItemUseAllowed
        return False_()
    return has_mask(bundle, mask) & (is_child(bundle) | True_(options=[OptionFilter(MasksAsAdult, True)]))


def bunny_hood(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    # Logic::BunnyHood: RSK_BUNNY_HOOD ("Bunny Hood Effect") && CanUse(RG_BUNNY_HOOD)
    return True_(options=[OptionFilter(BunnyHoodEffect, True)]) & can_use_mask(bundle, "BUNNY_HOOD")


def bunny_hovers(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return can_use(Items.HOVER_BOOTS, bundle) & bunny_hood(bundle)


# --- health / damage ---------------------------------------------------------------------------------------------
def effective_health_at_least(bundle: tuple[Regions, "SohWorld"], amount: int) -> Rule:
    """Logic::EffectiveHealth() >= amount, in 1/16 hearts (9.3.1 units).
    The apworld has no damage multiplier setting, so damage is normal: effective health = health, doubled by
    Double Defense."""
    return (HeartsAtLeast(amount=int(math.ceil(amount / 16)))
            | (has_item(Items.DOUBLE_DEFENSE, bundle) & HeartsAtLeast(amount=int(math.ceil(amount / 32)))))


def take_damage(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    # Logic::TakeDamage: fairy || EffectiveHealth() > 8 || Nayru's Love
    return (can_use_any([Items.BOTTLE_WITH_FAIRY, Items.NAYRUS_LOVE], bundle)
            | effective_health_at_least(bundle, 9))


def can_void(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    # Logic::CanVoid: fairy, or more than a full heart (half a heart with Double Defense); no OHKO in the apworld
    return (has_item(Items.BOTTLE_WITH_FAIRY, bundle) | HeartsAtLeast(amount=2)
            | (has_item(Items.DOUBLE_DEFENSE, bundle) & HeartsAtLeast(amount=1)))


# --- movement ------------------------------------------------------------------------------------------------------
def can_climb_ladder(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return has_climb(bundle) | (can_do_trick(Tricks.HOOKSHOT_LADDERS, bundle) & can_use(Items.HOOKSHOT, bundle))


def can_climb_high_ladder(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return has_climb(bundle) | (can_do_trick(Tricks.HOOKSHOT_LADDERS, bundle) & can_use(Items.LONGSHOT, bundle))


def can_middair_ground_jump(bundle: tuple[Regions, "SohWorld"], has_bombflower: bool = False) -> Rule:
    explosive = can_use(Items.BOMB_BAG, bundle)
    if has_bombflower:
        explosive |= has_item(Items.GORONS_BRACELET, bundle)
    return (can_do_trick(Tricks.GROUND_JUMP_HARD, bundle) & can_standing_shield(bundle)
            & can_use(Items.HOVER_BOOTS, bundle) & explosive)


def can_ground_jumpslash(bundle: tuple[Regions, "SohWorld"], has_bombflower: bool = False) -> Rule:
    explosive = can_use(Items.BOMB_BAG, bundle)
    if has_bombflower:
        explosive |= has_item(Items.GORONS_BRACELET, bundle)
    return can_do_trick(Tricks.GROUND_JUMP_HARD, bundle) & can_standing_shield(bundle) & can_jump_slash(bundle) & explosive


def can_recoil_hover(bundle: tuple[Regions, "SohWorld"], req: Recoil) -> Rule:
    base = can_use(Items.HOVER_BOOTS, bundle) & can_do_trick(Tricks.HOVER_BOOST_SIMPLE, bundle)
    if req == Recoil.SWORD:
        can = can_jump_slash(bundle)
    elif req == Recoil.SWORD_AND_SHIELD:
        # hammer without shield gives better recoils than sword and shield
        can = (can_jump_slash(bundle) & can_standing_shield(bundle)) | can_use(Items.MEGATON_HAMMER, bundle)
    elif req == Recoil.HAMMER:
        can = can_use(Items.MEGATON_HAMMER, bundle)
    else:
        can = can_use(Items.MEGATON_HAMMER, bundle) & can_standing_shield(bundle)
    return base & can


def can_recoil_hover_from_object(bundle: tuple[Regions, "SohWorld"], req: TorchRecoil) -> Rule:
    base = can_use(Items.HOVER_BOOTS, bundle) & can_do_trick(Tricks.HOVER_BOOST_SIMPLE, bundle)
    long_ = can_use(Items.STICKS, bundle) | can_use(Items.BIGGORONS_SWORD, bundle)
    if req == TorchRecoil.LONG_AND_SHIELD:
        can = long_ & can_standing_shield(bundle)
    elif req == TorchRecoil.SHORT:
        can = can_use_any([Items.MEGATON_HAMMER, Items.KOKIRI_SWORD, Items.MASTER_SWORD], bundle) | long_
    elif req == TorchRecoil.MASTER:
        can = can_use(Items.MASTER_SWORD, bundle) | long_
    else:
        can = long_
    return base & can


def summon_epona(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return is_adult(bundle) & has_item(Events.FREED_EPONA, bundle) & can_use(Items.EPONAS_SONG, bundle)


def reach_scarecrow(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return scarecrows_song(bundle) & can_use(Items.HOOKSHOT, bundle)


def reach_distant_scarecrow(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return scarecrows_song(bundle) & can_use(Items.LONGSHOT, bundle)


def sunlight_arrows(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return OptionFilter(SunlightArrows, True) & can_use(Items.LIGHT_ARROW, bundle)


# --- switches / enemies --------------------------------------------------------------------------------------------
def can_hit_switch(bundle: tuple[Regions, "SohWorld"], distance: EnemyDistance = EnemyDistance.CLOSE,
                   in_water: bool = False) -> Rule:
    # upstream switch with fallthrough: every option of a farther distance also works up close
    hit: Rule = can_use_any([Items.FAIRY_SLINGSHOT, Items.FAIRY_BOW], bundle)
    if distance <= EnemyDistance.LONGSHOT:
        hit |= can_use(Items.LONGSHOT, bundle)
    if distance <= EnemyDistance.HOOKSHOT:
        hit |= can_use_any([Items.HOOKSHOT, Items.BOMBCHUS_5], bundle)
    if distance <= EnemyDistance.BOOMERANG:
        hit |= can_use(Items.BOOMERANG, bundle)
    if distance <= EnemyDistance.BOMB_THROW and not in_water:
        hit |= can_use(Items.BOMB_BAG, bundle)
    if distance <= EnemyDistance.LONG_JUMPSLASH:
        hit |= can_use_any([Items.BIGGORONS_SWORD, Items.STICKS], bundle)
    if distance <= EnemyDistance.MASTER_SWORD_JUMPSLASH:
        hit |= can_use(Items.MASTER_SWORD, bundle)
    if distance <= EnemyDistance.SHORT_JUMPSLASH:
        hit |= can_use_any([Items.KOKIRI_SWORD, Items.MEGATON_HAMMER, Items.GIANTS_KNIFE], bundle)
    return hit


def can_break_pots(bundle: tuple[Regions, "SohWorld"], distance: EnemyDistance = EnemyDistance.CLOSE,
                   wall_or_floor: bool = True, in_water: bool = False) -> Rule:
    hit: Rule = can_use_any([Items.FAIRY_SLINGSHOT, Items.FAIRY_BOW], bundle)
    if distance <= EnemyDistance.LONGSHOT:
        hit |= can_use(Items.LONGSHOT, bundle)
    if distance <= EnemyDistance.HOOKSHOT:
        hit |= can_use(Items.HOOKSHOT, bundle)
    if distance <= EnemyDistance.BOOMERANG:
        hit |= can_use(Items.BOOMERANG, bundle)
    if distance <= EnemyDistance.BOMB_THROW and not in_water:
        hit |= can_use(Items.BOMB_BAG, bundle)
    if distance <= EnemyDistance.LONG_JUMPSLASH:
        hit |= can_use_any([Items.BIGGORONS_SWORD, Items.STICKS], bundle)
    if distance <= EnemyDistance.MASTER_SWORD_JUMPSLASH:
        hit |= can_use(Items.MASTER_SWORD, bundle)
    if distance <= EnemyDistance.SHORT_JUMPSLASH:
        hit |= can_use_any([Items.KOKIRI_SWORD, Items.MEGATON_HAMMER, Items.GIANTS_KNIFE], bundle)
    if distance <= EnemyDistance.CLOSE:
        hit |= has_grab(bundle)
    if wall_or_floor:
        hit |= can_use(Items.BOMBCHUS_5, bundle)
    return hit


def can_break_crates(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return True_()


def can_break_small_crates(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return can_jump_slash(bundle) | has_explosives(bundle) | has_grab(bundle)


def can_avoid_enemy(bundle: tuple[Regions, "SohWorld"], enemy: Enemies, distance: EnemyDistance = EnemyDistance.CLOSE,
                    grounded: bool = False, quantity: int = 1) -> Rule:
    kill = can_kill_enemy(bundle, enemy, distance, True, quantity)
    if enemy == Enemies.BEAMOS:
        if not grounded:
            return True_()
        avoided: Rule = can_use_any([Items.FAIRY_SLINGSHOT, Items.FAIRY_BOW], bundle)
        if distance <= EnemyDistance.LONGSHOT:
            avoided |= can_use(Items.LONGSHOT, bundle)
        if distance <= EnemyDistance.HOOKSHOT:
            avoided |= can_use(Items.HOOKSHOT, bundle)
        if distance <= EnemyDistance.BOOMERANG:
            avoided |= can_use(Items.BOOMERANG, bundle)
        if distance <= EnemyDistance.BOMB_THROW:
            avoided |= can_use_any([Items.DINS_FIRE, Items.NUTS], bundle)
        return kill | avoided
    if enemy == Enemies.MAD_SCRUB:
        return True_() if not grounded else kill | can_use(Items.NUTS, bundle)
    if enemy in (Enemies.KEESE, Enemies.FIRE_KEESE, Enemies.GUAY):
        return kill | can_use(Items.NUTS, bundle) | can_use_mask(bundle, "SKULL_MASK")
    if enemy == Enemies.BLUE_BUBBLE:
        return True_() if not grounded else kill | can_use(Items.NUTS, bundle) | hookshot_or_boomerang(bundle) | can_standing_shield(bundle)
    if enemy == Enemies.TORCH_SLUG:
        return True_() if not grounded else kill | can_use_any([Items.NUTS, Items.HOOKSHOT, Items.DINS_FIRE], bundle)
    # every other enemy upstream lists can simply be walked past
    return True_()


# --- beans ---------------------------------------------------------------------------------------------------------
def can_plant_bean(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    # location_access.cpp CanPlantBean: bean soul (always held, no bean soul shuffle) && beans && (child || Skip
    # Planting Beans)
    return has_item(Items.MAGIC_BEAN, bundle) & (is_child(bundle) | True_(options=[OptionFilter(SkipPlantingBeans, True)]))


def bean_planted(bundle: tuple[Regions, "SohWorld"], plant_event: Events) -> Rule:
    # Logic::BeanPlanted: the LOGIC_PLANT_*_BEAN event (planting outside of logic is ignored here)
    return has_item(plant_event, bundle)


# --- Death Mountain Crater ---------------------------------------------------------------------------------------
def dmc_upper_to_pots(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return (can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle)
            | (is_adult(bundle) & (has_item(Events.DMC_BOULDER, bundle) | can_do_trick(Tricks.DMC_BOULDER_SKIP, bundle))))


def dmc_pots_to_pad(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return (can_use(Items.HOVER_BOOTS, bundle) | (bunny_hood(bundle) & (is_adult(bundle) | has_climb(bundle)))
            | can_use(Items.HOOKSHOT, bundle)
            | (is_adult(bundle) & can_shield(bundle) & can_do_trick(Tricks.DMC_BOLERO_JUMP, bundle) & has_grab(bundle)))


def dmc_pad_to_pots(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return ((can_use(Items.HOVER_BOOTS, bundle) & (is_adult(bundle) | has_climb(bundle)))
            | can_use(Items.HOOKSHOT, bundle) | (is_adult(bundle) & bunny_hood(bundle) & has_climb(bundle)))


def dmc_upper_to_pad(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return (is_adult(bundle) & take_damage(bundle) & can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle)
            & reach_distant_scarecrow(bundle))


# --- Water Temple --------------------------------------------------------------------------------------------------
def water_level(bundle: tuple[Regions, "SohWorld"], level: WaterLevel) -> Rule:
    low, mid, high = (has_item(Events.WATER_LOW, bundle), has_item(Events.WATER_MIDDLE, bundle),
                      has_item(Events.WATER_HIGH, bundle))
    could_low = has_item(Events.WATER_COULD_LOW, bundle)
    could_low_from_high = has_item(Events.WATER_COULD_LOW_FROM_HIGH, bundle)
    could_mid = has_item(Events.WATER_COULD_MIDDLE, bundle)
    could_high_from_mid = has_item(Events.WATER_COULD_HIGH_FROM_MID, bundle)
    zl = can_use(Items.ZELDAS_LULLABY, bundle)
    if level == WaterLevel.LOW:
        return low | (could_low_from_high & (could_high_from_mid | high) & zl)
    if level == WaterLevel.LOW_OR_MID:
        return low | mid | ((could_low_from_high | low) & zl)
    if level == WaterLevel.MID:
        return mid | (low & could_mid) | ((could_low_from_high | could_low) & could_mid & zl)
    if level == WaterLevel.HIGH:
        return high | (could_high_from_mid & could_mid)
    return mid | high | could_mid  # HIGH_OR_MID


def water_rising_target_to_3f_central(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return can_use(Items.LONGSHOT, bundle) | (can_do_trick(Tricks.HOVER_BOOST_SIMPLE, bundle)
                                              & can_do_trick(Tricks.DAMAGE_BOOST_SIMPLE, bundle)
                                              & has_explosives(bundle) & can_use(Items.HOVER_BOOTS, bundle))


def water_3f_central_to_high_emblem(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return ((is_adult(bundle) & can_use(Items.HOVER_BOOTS, bundle)) | can_middair_ground_jump(bundle)
            | (has_item(Events.WATER_SCARECROW, bundle) & can_use(Items.HOOKSHOT, bundle))
            | ((is_adult(bundle) | bunny_hood(bundle)) & can_do_trick(Tricks.WATER_HIGH_EMBLEM_JUMP, bundle)))


# --- Spirit Temple -------------------------------------------------------------------------------------------------
def spirit_sun_block_south_ledge(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return (has_grab(bundle) | is_adult(bundle) | can_kill_enemy(bundle, Enemies.BEAMOS) | bunny_hovers(bundle)
            | (can_use(Items.HOOKSHOT, bundle)
               & (has_fire_source(bundle)
                  | (has_item(Events.SPIRIT_SUN_BLOCK_TORCH, bundle)
                     & (can_use(Items.STICKS, bundle)
                        | (can_do_trick(Tricks.SPIRIT_SUN_CHEST, bundle) & can_use(Items.FAIRY_BOW, bundle)))))))


def spirit_east_to_switch(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return ((is_adult(bundle) & (can_do_trick(Tricks.SPIRIT_STATUE_JUMP, bundle) | bunny_hood(bundle)))
            | can_use(Items.HOVER_BOOTS, bundle)
            | (can_use(Items.ZELDAS_LULLABY, bundle) & can_use(Items.HOOKSHOT, bundle)))


# --- counters / misc ------------------------------------------------------------------------------------------------
def gs_count_at_least(bundle: tuple[Regions, "SohWorld"], amount: int) -> Rule:
    return Has(Items.GOLD_SKULLTULA_TOKEN, count=amount)


def stone_count_at_least(bundle: tuple[Regions, "SohWorld"], amount: int) -> Rule:
    return has_enough_stones(bundle, amount)


def big_poes_at_least_target(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    # logic->BigPoes >= RSK_BIG_POE_COUNT (big poes in bottles)
    return has_item(Items.BOTTLE_WITH_BIG_POE, bundle, bundle[1].options.big_poe_target_count.value)


def is_fire_loop_locked(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return OptionFilter(SmallKeyShuffle, [SmallKeyShuffle.option_anywhere, SmallKeyShuffle.option_overworld,
                                          SmallKeyShuffle.option_any_dungeon], operator="in")


def trial_skipped(bundle: tuple[Regions, "SohWorld"], trial: str) -> Rule:
    # ctx->GetTrial(TK_X)->IsSkipped(); the required trials are rolled in generate_early (world.ganons_trials)
    name = trial.replace("_", " ").title()  # "FOREST_TRIAL" -> "Forest Trial"
    return False_() if name in bundle[1].ganons_trials else True_()


SCENE_SMALL_KEYS = {
    "SCENE_FOREST_TEMPLE": Items.FOREST_TEMPLE_SMALL_KEY, "SCENE_FIRE_TEMPLE": Items.FIRE_TEMPLE_SMALL_KEY,
    "SCENE_WATER_TEMPLE": Items.WATER_TEMPLE_SMALL_KEY, "SCENE_SPIRIT_TEMPLE": Items.SPIRIT_TEMPLE_SMALL_KEY,
    "SCENE_SHADOW_TEMPLE": Items.SHADOW_TEMPLE_SMALL_KEY,
    "SCENE_BOTTOM_OF_THE_WELL": Items.BOTTOM_OF_THE_WELL_SMALL_KEY,
    "SCENE_GERUDO_TRAINING_GROUND": Items.TRAINING_GROUND_SMALL_KEY,
    "SCENE_THIEVES_HIDEOUT": Items.GERUDO_FORTRESS_SMALL_KEY, "SCENE_INSIDE_GANONS_CASTLE": Items.GANONS_CASTLE_SMALL_KEY,
    "SCENE_TREASURE_BOX_SHOP": Items.TREASURE_GAME_SMALL_KEY,
}


def small_keys_scene(scene: str, amount: int, bundle: tuple[Regions, "SohWorld"]) -> Rule:
    # Logic::SmallKeys(SceneID, amount)
    if scene == "SCENE_TREASURE_BOX_SHOP":
        # Treasure Chest Game keys only matter with the Treasure Chest Game shuffle (feature 3.10), which the
        # apworld doesn't offer yet, so the key branch never applies.
        return False_()  # TODO feature 3.10
    return small_keys(SCENE_SMALL_KEYS[scene], amount, bundle)


# --- AnyAgeTime (location_access.h Region::AnyAgeTime) -------------------------------------------------------------
@dataclasses.dataclass()
class AnyAgeTime(WrapperRule, game="Ship of Harkinian"):
    """The condition holds if it holds for any age that can reach the region (e.g. adult breaks the rocks with the
    hammer, so child can pass afterwards too)."""
    parent_region: Regions = Regions.ROOT

    def _instantiate(self, world: "SohWorld") -> Rule.Resolved:  # type: ignore
        return self.Resolved(self.child.resolve(world), parent_region=self.parent_region, player=world.player,
                             caching_enabled=getattr(world, "rule_caching_enabled", False))

    class Resolved(WrapperRule.Resolved):
        parent_region: Regions = Regions.ROOT
        force_recalculate = True

        def _evaluate(self, state: CollectionState) -> bool:
            player = self.player
            region = state.multiworld.get_region(self.parent_region.value, player)
            stored = state._soh_age[player]  # type: ignore
            result = False
            try:
                for age, reachable in ((Ages.CHILD, state._soh_child_reachable_regions[player]),  # type: ignore
                                       (Ages.ADULT, state._soh_adult_reachable_regions[player])):  # type: ignore
                    if region in reachable:
                        state._soh_age[player] = age  # type: ignore
                        if self.child(state):
                            result = True
                            break
            finally:
                state._soh_age[player] = stored  # type: ignore
            return result

        def region_dependencies(self) -> dict[str, set[int]]:
            deps = super().region_dependencies()
            deps.setdefault(self.parent_region.value, set()).add(id(self))
            return deps


def any_age_time(bundle: tuple[Regions, "SohWorld"], rule_fn: Callable[[tuple[Regions, "SohWorld"]], Rule]) -> Rule:
    return AnyAgeTime(rule_fn(bundle), parent_region=bundle[0])


# --- Spirit Temple shared access (location_access.cpp SpiritCertainAccess / SpiritShared) ---------------------------
# Logic::IsReverseAccessPossible() is only true with boss entrance shuffle, which the apworld doesn't have, so every
# "!IsReverseAccessPossible() || reverseAccess" term is true and "knownFrontAccess" always holds.
def spirit_certain_access_rule(bundle: tuple[Regions, "SohWorld"], data: tuple, child: bool) -> Rule:
    child_keys, child_rev_keys, adult_keys, adult_rev_keys, child_access, adult_access, reverse_access = data
    keys, rev_keys = (child_keys, child_rev_keys) if child else (adult_keys, adult_rev_keys)
    access = child_access(bundle) if child else adult_access(bundle)
    rev = reverse_access(bundle)
    reverse_event = Events.REVERSE_SPIRIT_CHILD if child else Events.REVERSE_SPIRIT_ADULT
    spirit_key = Items.SPIRIT_TEMPLE_SMALL_KEY
    return ((access & small_keys(spirit_key, keys, bundle))
            | (has_item(reverse_event, bundle) & rev & small_keys(spirit_key, rev_keys, bundle))
            | (access & rev & small_keys(spirit_key, max(keys, rev_keys), bundle)))


@dataclasses.dataclass(init=False)
class SpiritShared(NestedRule, game="Ship of Harkinian"):
    """Upstream SpiritShared: a check reachable by one age only counts if the other age could reach it too, unless
    the current age has enough keys to be certain to get there ("certain access").
    children: [certain_child, certain_adult, cond_0, child_access_0, adult_access_0, cond_1, ...]
    Difference to upstream: with any_age and certain access for both ages, upstream evaluates the condition with
    IsChild and IsAdult both set at once; here it is evaluated per age and OR'ed."""
    region: Regions = Regions.ROOT
    any_age: bool = False

    def __init__(self, *children: Rule, region: Regions, any_age: bool, options=(), filtered_resolution=False):
        super().__init__(*children, options=options, filtered_resolution=filtered_resolution)
        self.region = region
        self.any_age = any_age

    def _instantiate(self, world: "SohWorld") -> Rule.Resolved:  # type: ignore
        return self.Resolved(tuple(c.resolve(world) for c in self.children), region=self.region,
                             any_age=self.any_age, player=world.player,
                             caching_enabled=getattr(world, "rule_caching_enabled", False))

    class Resolved(NestedRule.Resolved):
        region: Regions = Regions.ROOT
        any_age: bool = False
        force_recalculate = True

        def _evaluate(self, state: CollectionState) -> bool:
            player = self.player
            stored = state._soh_age[player]  # type: ignore

            def at(rule: Rule.Resolved, age: Ages) -> bool:
                state._soh_age[player] = age  # type: ignore
                try:
                    return rule(state)
                finally:
                    state._soh_age[player] = stored  # type: ignore

            certain_child, certain_adult = self.children[0], self.children[1]
            parts = [self.children[i:i + 3] for i in range(2, len(self.children), 3)]
            cc, ac = at(certain_child, Ages.CHILD), at(certain_adult, Ages.ADULT)
            if self.any_age and (cc or ac):
                return (cc and at(parts[0][0], Ages.CHILD)) or (ac and at(parts[0][0], Ages.ADULT))
            region = state.multiworld.get_region(self.region.value, player)
            if stored == Ages.CHILD and region in state._soh_child_reachable_regions[player]:  # type: ignore
                if not at(parts[0][0], Ages.CHILD):
                    return False
                return cc or any(at(adult_acc, Ages.ADULT) and at(cond, Ages.ADULT) for cond, _, adult_acc in parts)
            if stored == Ages.ADULT and region in state._soh_adult_reachable_regions[player]:  # type: ignore
                if not at(parts[0][0], Ages.ADULT):
                    return False
                return ac or any(at(child_acc, Ages.CHILD) and at(cond, Ages.CHILD) for cond, child_acc, _ in parts)
            return False

        def region_dependencies(self) -> dict[str, set[int]]:
            deps = super().region_dependencies()
            deps.setdefault(self.region.value, set()).add(id(self))
            return deps


def make_spirit_shared(world: "SohWorld", data_table: dict, region: Regions, cond_fn, any_age: bool = False,
                       others: list | None = None) -> Rule:
    regions = [(region, cond_fn)] + list(others or [])
    first = (region, world)
    children: list[Rule] = [spirit_certain_access_rule(first, data_table[region], True),
                            spirit_certain_access_rule(first, data_table[region], False)]
    for reg, fn in regions:
        b = (reg, world)
        data = data_table[reg]
        children += [fn(b), data[4](b), data[5](b)]
    return SpiritShared(*children, region=region, any_age=any_age)


def spirit_explosive_key_logic(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    # Logic::SpiritExplosiveKeyLogic: SmallKeys(SCENE_SPIRIT_TEMPLE, HasExplosives() ? 1 : 2)
    key = Items.SPIRIT_TEMPLE_SMALL_KEY
    return (has_explosives(bundle) & small_keys(key, 1, bundle)) | small_keys(key, 2, bundle)


def spirit_west_to_skull(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return ((is_adult(bundle) & (can_do_trick(Tricks.SPIRIT_STATUE_JUMP, bundle) | bunny_hood(bundle)))
            | can_use(Items.HOVER_BOOTS, bundle) | reach_scarecrow(bundle))


def outer_west_hand_logic(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    # Logic::OuterWestHandLogic: explosives, (climb or longshot), grab, SmallKeys(SPIRIT, HasItem(LONGSHOT) ? 3 : 5)
    key = Items.SPIRIT_TEMPLE_SMALL_KEY
    return (has_explosives(bundle) & (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)) & has_grab(bundle)
            & ((has_item(Items.LONGSHOT, bundle) & small_keys(key, 3, bundle)) | small_keys(key, 5, bundle)))


# --- static negation -----------------------------------------------------------------------------------------------
# rule_builder has no negation on purpose: logic must stay monotonic in items. Upstream negates settings and tricks,
# which are fixed at generation time, so these two rules only accept those and fail loudly otherwise.
@dataclasses.dataclass()
class Not(WrapperRule, game="Ship of Harkinian"):
    """!child for a child that resolves to a constant (settings, dungeon type, ...)."""

    def _instantiate(self, world: "SohWorld") -> Rule.Resolved:  # type: ignore
        if isinstance(self.child, OptionFilter):  # helpers like is_fire_loop_locked return a bare option filter
            return (False_() if self.child.check(world.options) else True_()).resolve(world)
        resolved = self.child.resolve(world)
        if isinstance(resolved, True_.Resolved):
            return False_().resolve(world)
        if isinstance(resolved, False_.Resolved):
            return True_().resolve(world)
        raise ValueError(f"Not() needs a rule that is constant at generation time, got {resolved}")


@dataclasses.dataclass()
class TrickDisabled(Rule, game="Ship of Harkinian"):
    """!ctx->GetTrickOption(trick): true when the trick is not enabled in the options."""
    trick: str = ""

    def _instantiate(self, world: "SohWorld") -> Rule.Resolved:  # type: ignore
        enabled = bool(world.options.enable_all_tricks.value) or self.trick in world.options.tricks_in_logic.value
        return (False_() if enabled else True_()).resolve(world)


def trick_disabled(trick: Tricks, bundle: tuple[Regions, "SohWorld"]) -> Rule:
    return TrickDisabled(trick=trick.value)


def starting_zeldas_letter(bundle: tuple[Regions, "SohWorld"]) -> Rule:
    # RSK_STARTING_ZELDAS_LETTER as the client sets it (SeedContext.cpp ParseArchipelagoOptions):
    # Skip Child Zelda, or Kakariko Gate "Open"
    return True_(options=[OptionFilter(SkipChildZelda, True)]) | True_(options=[OptionFilter(KakarikoGate, KakarikoGate.option_open)])
