"""Gameplay switches from SoH 9.3.1 (feature 2.4): Bunny Hood Effect, Masks as Adult, Early Granny's Shop,
Gate Shop Shields & Tunics."""
from .bases import SohTestBase
from ..Enums import Items, Locations, Regions
from ..LogicHelpers import can_use_mask, bunny_hood


class TestSwitchesOff(SohTestBase):
    def test_defaults_keep_old_behavior(self):
        world = self.world
        self.assertFalse(world.options.bunny_hood_effect)
        self.assertFalse(world.options.masks_as_adult)
        rule = bunny_hood(self.get_bundle()).resolve(world)
        self.collect_all_but([])
        self.assertFalse(rule(self.multiworld.state))  # Bunny Hood Effect off: never in logic


class TestMasksAsAdult(SohTestBase):
    options = {"masks_as_adult": True, "starting_age": "adult"}

    def test_adult_can_use_masks(self):
        rule = can_use_mask((Regions.ROOT, self.world), "KEATON_MASK").resolve(self.world)
        self.collect_all_but([])
        self.assertTrue(rule(self.multiworld.state))


class TestBunnyHoodEffect(SohTestBase):
    options = {"bunny_hood_effect": True}

    def test_bunny_hood_in_logic(self):
        rule = bunny_hood(self.get_bundle()).resolve(self.world)
        self.collect_all_but([])
        self.assertTrue(rule(self.multiworld.state))


class TestEarlyGrannysShop(SohTestBase):
    options = {"early_grannys_shop": True, "shuffle_adult_trade_items": False, "starting_age": "adult",
               "shuffle_merchants": "all"}

    def test_no_claim_check_needed(self):
        self.collect_all_but([Items.CLAIM_CHECK.value, Items.ODD_MUSHROOM.value])
        self.assertTrue(self.can_reach_location(Locations.KAK_GRANNYS_SHOP.value))


class TestShopGate(SohTestBase):
    options = {"shop_shields_and_tunics_only_refill": True}

    def test_found_shields_are_progression(self):
        shields = [item for item in self.multiworld.itempool
                   if item.player == self.player and item.name == Items.HYLIAN_SHIELD.value]
        self.assertTrue(shields)
        self.assertTrue(all(item.advancement for item in shields))

    def test_gated_slot(self):
        # vanilla Market Bazaar slot 1 sells the Hylian Shield (shops not shuffled by default)
        location = self.multiworld.get_location(Locations.MARKET_BAZAAR_ITEM1.value, self.player)
        self.assertEqual(location.item.name, Items.BUY_HYLIAN_SHIELD.value)
        self.collect_all_but([Items.HYLIAN_SHIELD.value])
        self.assertFalse(self.can_reach_location(Locations.MARKET_BAZAAR_ITEM1.value))
        self.collect_by_name([Items.HYLIAN_SHIELD.value])
        self.assertTrue(self.can_reach_location(Locations.MARKET_BAZAAR_ITEM1.value))
