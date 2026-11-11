"""Settings that already existed in the client but were never wired (feature 2.8): Skip Child Stealth,
Skip Planting Beans, Starting Skulltula Tokens."""
from BaseClasses import CollectionState

from .bases import SohTestBase
from ..Enums import Items, Locations, Regions
from ..LogicHelpers import can_plant_bean


def bean_state(test: SohTestBase) -> CollectionState:
    state = CollectionState(test.multiworld)
    # has_item(MAGIC_BEAN) = Magic Bean Pack or the bean salesman event
    state.collect(test.world.create_item(Items.MAGIC_BEAN_PACK), prevent_sweep=True)
    return state


def pool_tokens(test: SohTestBase) -> list:
    return [i for i in test.multiworld.itempool if i.player == test.player and i.name == Items.GOLD_SKULLTULA_TOKEN.value]


def precollected_tokens(test: SohTestBase) -> list:
    return [i for i in test.multiworld.precollected_items[test.player] if i.name == Items.GOLD_SKULLTULA_TOKEN.value]


class TestDefaults(SohTestBase):
    def test_off(self):
        self.assertFalse(self.world.options.skip_child_stealth)
        self.assertFalse(self.world.options.skip_planting_beans)
        self.assertEqual(self.world.options.starting_skulltula_tokens.value, 0)
        self.assertEqual(precollected_tokens(self), [])

    def test_beans_need_child(self):
        # location_access.cpp CanPlantBean: beans && (IsChild || Skip Planting Beans)
        rule = can_plant_bean((Regions.DESERT_COLOSSUS, self.world), Items.DESERT_COLOSSUS_BEAN_SOUL).resolve(self.world)
        self.assertFalse(rule(bean_state(self)))


class TestSkipPlantingBeans(SohTestBase):
    options = {"skip_planting_beans": True, "skip_child_stealth": True}

    def test_beans_without_child(self):
        rule = can_plant_bean((Regions.DESERT_COLOSSUS, self.world), Items.DESERT_COLOSSUS_BEAN_SOUL).resolve(self.world)
        self.assertTrue(rule(bean_state(self)))
        self.assertFalse(rule(CollectionState(self.multiworld)))


class TestStartingTokensVanilla(SohTestBase):
    # tokensanity off: upstream item_pool.cpp adds no tokens to the pool, so the starting ones come on top
    options = {"starting_skulltula_tokens": 10, "shuffle_skull_tokens": "off"}

    def test_tokens(self):
        self.assertEqual(len(precollected_tokens(self)), 10)
        self.assertEqual(pool_tokens(self), [])
        state = CollectionState(self.multiworld)
        self.assertTrue(state.has(Items.GOLD_SKULLTULA_TOKEN.value, self.player, 10))


class TestStartingTokensShuffled(SohTestBase):
    options = {"starting_skulltula_tokens": 30, "shuffle_skull_tokens": "all", "accessibility": "full"}

    def test_pool_reduced(self):
        self.assertEqual(len(pool_tokens(self)), 70)
        self.assertEqual(len(precollected_tokens(self)), 30)
        for item in precollected_tokens(self):
            self.assertIsNone(item.code)
            self.assertTrue(item.advancement)

    def test_progression_count(self):
        # 3drando/fill.cpp: maxUseful (50) minus the starting tokens
        self.assertEqual(self.world.randomized_progressive_skulltula_count, 20)
        self.assertEqual(sum(1 for item in pool_tokens(self) if item.advancement), 20)


class TestStartingTokensDungeon(SohTestBase):
    # only the 44 dungeon tokens are shuffled; the 56 overworld ones stay vanilla
    options = {"starting_skulltula_tokens": 60, "shuffle_skull_tokens": "dungeon"}

    def test_only_shuffled_tokens_removed(self):
        self.assertEqual(len(pool_tokens(self)), 0)
        self.assertEqual(len(precollected_tokens(self)), 60)
        placed = [loc for loc in self.multiworld.get_locations(self.player)
                  if loc.item and loc.item.name == Items.GOLD_SKULLTULA_TOKEN.value]
        self.assertEqual(len(placed), 56)


def pond_fish(test: SohTestBase) -> set[str]:
    return {loc.name for loc in test.multiworld.get_locations(test.player) if "Pond Fish" in loc.name}


class TestPondFishDefault(SohTestBase):
    options = {"shuffle_fish": "pond"}

    def test_fifteen_per_age(self):
        fish = pond_fish(self)
        self.assertEqual(len(fish), 30)
        self.assertIn(Locations.LH_ADULT_POND_FISH15.value, fish)


class TestPondFishCountNoSplit(SohTestBase):
    # fishsanity.cpp GetFishLocationIncluded: child fish 1..count, no adult set without age split
    options = {"shuffle_fish": "pond", "fishsanity_pond_count": 5, "fishsanity_age_split": False}

    def test_locations(self):
        self.assertEqual(pond_fish(self), {Locations[f"LH_CHILD_POND_FISH{n}"].value for n in range(1, 6)})

    def test_reachable(self):
        # lake_hylia.cpp: child fish need (IsChild || !RSK_FISHSANITY_AGE_SPLIT)
        self.collect_all_but([])
        self.assertTrue(self.can_reach_location(Locations.LH_CHILD_POND_FISH1.value))
