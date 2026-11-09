"""Shuffle Masks from SoH 9.3.1 (3drando/item_pool.cpp, logic.cpp HasItem, feature 3.7)."""
from BaseClasses import CollectionState

from .bases import SohTestBase
from ..Enums import Items, Regions
from ..Items import item_data_table
from ..LogicHelpers import has_mask

MASKS = [Items.KEATON_MASK, Items.SKULL_MASK, Items.SPOOKY_MASK, Items.BUNNY_HOOD, Items.GORON_MASK, Items.ZORA_MASK,
         Items.GERUDO_MASK, Items.MASK_OF_TRUTH]


def pool_count(test: SohTestBase, item: Items) -> int:
    return sum(1 for i in test.multiworld.itempool if i.player == test.player and i.name == item.value)


class TestShuffleMasksOff(SohTestBase):
    def test_no_masks_in_pool(self):
        for mask in MASKS:
            self.assertEqual(pool_count(self, mask), 0, mask)

    def test_new_ids(self):
        self.assertEqual([item_data_table[mask].item_id for mask in MASKS], list(range(277, 285)))


class TestShuffleMasks(SohTestBase):
    options = {"shuffle_masks": True, "start_with_goron_mask": True}

    def test_complete_mask_quest_turned_off(self):
        # decision 2026-11-09: Shuffle Masks wins over Complete Mask Quest (on by default)
        self.assertFalse(self.world.options.complete_mask_quest)

    def test_pool(self):
        for mask in MASKS:
            self.assertEqual(pool_count(self, mask), 0 if mask == Items.GORON_MASK else 1, mask)

    def test_masks_only_from_the_item(self):
        # logic.cpp HasItem: RAND_INF_CHILD_TRADES_HAS_MASK_* || (!RSK_SHUFFLE_MASKS && borrowed)
        self.collect_all_but([Items.SKULL_MASK.value])
        rule = has_mask((Regions.ROOT, self.world), "SKULL_MASK").resolve(self.world)
        self.assertFalse(rule(self.multiworld.state))
        state = CollectionState(self.multiworld)
        state.collect(self.world.create_item(Items.SKULL_MASK), prevent_sweep=True)
        self.assertTrue(rule(state))


class TestBorrowedMasks(SohTestBase):
    options = {"complete_mask_quest": False}

    def test_borrowing_still_works(self):
        self.collect_all_but([])
        rule = has_mask((Regions.ROOT, self.world), "MASK_OF_TRUTH").resolve(self.world)
        self.assertTrue(rule(self.multiworld.state))
