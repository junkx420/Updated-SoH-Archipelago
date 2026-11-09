"""Shuffle Zelda's Letter from SoH 9.3.1 (3drando/item_pool.cpp, root.cpp, feature 3.9)."""
from .bases import SohTestBase
from ..Enums import Items, Locations


def pool_count(test: SohTestBase, item: Items) -> int:
    return sum(1 for i in test.multiworld.itempool if i.player == test.player and i.name == item.value)


def precollected(test: SohTestBase, item: Items) -> int:
    return sum(1 for i in test.multiworld.precollected_items[test.player] if i.name == item.value)


class TestLetterVanilla(SohTestBase):
    options = {"skip_child_zelda": False}

    def test_vanilla_placement(self):
        location = self.multiworld.get_location(Locations.HC_ZELDAS_LETTER.value, self.player)
        self.assertEqual(location.item.name, Items.ZELDAS_LETTER.value)
        self.assertEqual(pool_count(self, Items.ZELDAS_LETTER), 0)


class TestLetterShuffled(SohTestBase):
    options = {"shuffle_zeldas_letter": True}

    def test_skip_child_zelda_turned_off(self):
        # decision 2026-11-09: Shuffle Zelda's Letter wins over Skip Child Zelda (on by default)
        self.assertFalse(self.world.options.skip_child_zelda)

    def test_letter_in_pool(self):
        self.assertEqual(pool_count(self, Items.ZELDAS_LETTER), 1)
        self.assertEqual(precollected(self, Items.ZELDAS_LETTER), 0)
        location = self.multiworld.get_location(Locations.HC_ZELDAS_LETTER.value, self.player)
        self.assertFalse(location.locked)

    def test_zelda_is_a_real_check(self):
        # root.cpp: RC_HC_ZELDAS_LETTER from Root only with an unshuffled starting letter; otherwise through the
        # castle courtyard (castle_grounds.cpp), which doesn't need the letter
        self.collect_all_but([Items.ZELDAS_LETTER.value])
        self.assertTrue(self.can_reach_location(Locations.HC_ZELDAS_LETTER.value))
        root_letter = self.multiworld.get_location(Locations.HC_ZELDAS_LETTER.value, self.player)
        self.assertNotEqual(root_letter.parent_region.name, "Root")


class TestLetterShuffledGateOpen(SohTestBase):
    options = {"shuffle_zeldas_letter": True, "kakariko_gate": "open", "skip_child_zelda": True}

    def test_gate_closed(self):
        # decision 2026-11-09: the shuffle also closes the Kakariko Gate (= starting letter in the client)
        self.assertEqual(self.world.options.kakariko_gate.value, 0)
        self.assertFalse(self.world.options.skip_child_zelda)
        self.assertEqual(pool_count(self, Items.ZELDAS_LETTER), 1)
        self.assertEqual(precollected(self, Items.ZELDAS_LETTER), 0)
