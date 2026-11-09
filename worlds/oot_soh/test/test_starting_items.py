"""Starting item options from SoH 9.3.1 (RSK_STARTING_*, feature 2.7)."""
from BaseClasses import CollectionState

from .bases import SohTestBase
from ..Enums import Items, Regions
from ..LogicHelpers import has_mask


def pool_count(test: SohTestBase, item: Items) -> int:
    return sum(1 for i in test.multiworld.itempool if i.player == test.player and i.name == item.value)


def precollected(test: SohTestBase, item: Items) -> int:
    return sum(1 for i in test.multiworld.precollected_items[test.player] if i.name == item.value)


class TestNoStartingItems(SohTestBase):
    def test_pool_unchanged(self):
        self.assertEqual(pool_count(self, Items.MEGATON_HAMMER), 1)
        self.assertEqual(precollected(self, Items.MEGATON_HAMMER), 0)
        self.assertEqual(pool_count(self, Items.PROGRESSIVE_HOOKSHOT), 2)


class TestStartingItems(SohTestBase):
    options = {"start_with_megaton_hammer": True, "start_with_hookshot": "longshot", "start_with_bow": "quiver_40",
               "start_with_strength": "silver_gauntlets", "start_with_bottle_1": "empty_bottle",
               "start_with_keaton_mask": True, "complete_mask_quest": False}

    def test_taken_out_of_the_pool(self):
        self.assertEqual(pool_count(self, Items.MEGATON_HAMMER), 0)
        self.assertEqual(precollected(self, Items.MEGATON_HAMMER), 1)
        self.assertEqual(pool_count(self, Items.PROGRESSIVE_HOOKSHOT), 0)
        self.assertEqual(precollected(self, Items.PROGRESSIVE_HOOKSHOT), 2)
        self.assertEqual(precollected(self, Items.PROGRESSIVE_BOW), 2)
        self.assertEqual(precollected(self, Items.STRENGTH_UPGRADE), 2)

    def test_starting_items_have_no_id(self):
        # the client gives them at the start; with an ID the server would send them a second time
        for item in self.multiworld.precollected_items[self.player]:
            self.assertIsNone(item.code, item.name)

    def test_in_logic_from_the_start(self):
        state = CollectionState(self.multiworld)
        self.assertTrue(state.has(Items.MEGATON_HAMMER.value, self.player))
        self.assertTrue(state.has(Items.PROGRESSIVE_HOOKSHOT.value, self.player, 2))
        self.assertTrue(has_mask((Regions.ROOT, self.world), "KEATON_MASK").resolve(self.world)(state))
        self.assertFalse(has_mask((Regions.ROOT, self.world), "SKULL_MASK").resolve(self.world)(state))


class TestStartingScaleAndWallet(SohTestBase):
    # Bronze Scale / Child's Wallet are already precollected when not shuffled
    options = {"start_with_scale": "golden_scale", "start_with_wallet": "giants_wallet",
               "shuffle_swim": False, "shuffle_childs_wallet": False}

    def test_counts(self):
        self.assertEqual(precollected(self, Items.PROGRESSIVE_SCALE), 3)
        self.assertEqual(precollected(self, Items.PROGRESSIVE_WALLET), 3)
