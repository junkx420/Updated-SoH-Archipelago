"""Abilities from SoH 9.3.1 (logic.cpp Logic::HasItem / Logic::CanUse for RG_CLIMB, RG_CRAWL, RG_OPEN_CHEST,
RG_POWER_BRACELET, RG_SPEAK_*; feature 3.11)."""
from .bases import SohTestBase
from ..Enums import Items, Regions


def reachable(test: SohTestBase, region: Regions, adult: bool) -> bool:
    state = test.multiworld.state
    state._soh_update_age_reachable_regions(test.player)  # type: ignore
    regions = state._soh_adult_reachable_regions if adult else state._soh_child_reachable_regions  # type: ignore
    return test.multiworld.get_region(region.value, test.player) in regions[test.player]


class TestCrawlNeedsChild(SohTestBase):
    """kokiri_forest.cpp: RR_KF_BOULDER_LOOP is entered with CanUse(RG_CRAWL) = HasItem(RG_CRAWL) && IsChild."""

    def test_only_child_crawls(self):
        self.collect_all_but([])
        self.assertTrue(reachable(self, Regions.KF_BOULDER_LOOP, adult=False))
        self.assertFalse(reachable(self, Regions.KF_BOULDER_LOOP, adult=True))


def precollected(test: SohTestBase, item: Items) -> int:
    return sum(1 for i in test.multiworld.precollected_items[test.player] if i.name == item.value)


def in_pool(test: SohTestBase, item: Items) -> int:
    return sum(1 for i in test.multiworld.itempool if i.player == test.player and i.name == item.value)


class TestShuffleSwimTurnsOffStartingScale(SohTestBase):
    """settings.cpp: Shuffle Swim sets RSK_STARTING_SCALE to 0 (the client would give the scale without swim)."""
    options = {"shuffle_swim": True, "start_with_scale": "silver_scale"}

    def test_starting_scale_off(self):
        self.assertEqual(0, self.world.options.start_with_scale.value)
        self.assertEqual(0, precollected(self, Items.PROGRESSIVE_SCALE))
        self.assertEqual(3, in_pool(self, Items.PROGRESSIVE_SCALE))


class TestStartingScaleWithoutShuffleSwim(SohTestBase):
    options = {"start_with_scale": "silver_scale"}

    def test_starting_scale_kept(self):
        self.assertEqual(1, self.world.options.start_with_scale.value)
        self.assertEqual(2, precollected(self, Items.PROGRESSIVE_SCALE))  # bronze (swim) + silver
        self.assertEqual(1, in_pool(self, Items.PROGRESSIVE_SCALE))


ABILITY_ITEMS = [Items.CLIMB, Items.CRAWL, Items.OPEN_CHESTS, Items.DEKU_JABBER_NUT, Items.GERUDO_JABBER_NUT,
                 Items.GORON_JABBER_NUT, Items.HYLIAN_JABBER_NUT, Items.KOKIRI_JABBER_NUT, Items.ZORA_JABBER_NUT]


class TestAbilitiesOff(SohTestBase):
    def test_no_ability_items(self):
        for item in ABILITY_ITEMS:
            self.assertEqual(0, in_pool(self, item), item)

    def test_grab_precollected(self):
        # first Strength Upgrade = Power Bracelet, the game gives grab at the start (savefile.cpp)
        self.assertEqual(1, precollected(self, Items.STRENGTH_UPGRADE))
        self.assertEqual(3, in_pool(self, Items.STRENGTH_UPGRADE))

class TestAbilitiesOn(SohTestBase):
    options = {"shuffle_climb": True, "shuffle_crawl": True, "shuffle_grab": True, "shuffle_speak": True,
               "shuffle_open_chest": "on", "start_with_strength": "silver_gauntlets"}

    def test_ids(self):
        # new IDs 296-304 in RandomizerGet order (RG_CLIMB, RG_CRAWL, RG_OPEN_CHEST, RG_SPEAK_DEKU ... RG_SPEAK_ZORA)
        self.assertEqual(list(range(296, 305)), [self.world.item_name_to_id[i.value] for i in ABILITY_ITEMS])

    def test_items_in_pool(self):
        for item in ABILITY_ITEMS:
            self.assertEqual(1, in_pool(self, item), item)

    def test_grab_shuffled(self):
        # 3drando/item_pool.cpp: 3 + powerBracelet strength upgrades, settings.cpp: starting strength off
        self.assertEqual(0, self.world.options.start_with_strength.value)
        self.assertEqual(0, precollected(self, Items.STRENGTH_UPGRADE))
        self.assertEqual(4, in_pool(self, Items.STRENGTH_UPGRADE))

    def test_kokiri_shop_needs_kokiri_nut(self):
        # kokiri_forest.cpp RC_KF_SHOP_ITEM_1: HasItem(RG_SPEAK_KOKIRI) && GetCheckPrice() <= GetWalletCapacity()
        self.collect_all_but([Items.KOKIRI_JABBER_NUT.value])
        self.assertFalse(self.can_reach_location("KF Shop Item 1"))
        self.collect_by_name([Items.KOKIRI_JABBER_NUT.value])
        self.assertTrue(self.can_reach_location("KF Shop Item 1"))

    def test_chest_needs_open_chests(self):
        # kokiri_forest.cpp RC_KF_MIDOS_TOP_LEFT_CHEST: HasItem(RG_OPEN_CHEST)
        self.collect_all_but([Items.OPEN_CHESTS.value])
        self.assertFalse(self.can_reach_location("KF Mido Top Left Chest"))
        self.collect_by_name([Items.OPEN_CHESTS.value])
        self.assertTrue(self.can_reach_location("KF Mido Top Left Chest"))

    def test_crawl_item(self):
        self.collect_all_but([Items.CRAWL.value])
        self.assertFalse(reachable(self, Regions.KF_BOULDER_LOOP, adult=False))
        self.collect_by_name([Items.CRAWL.value])
        self.assertTrue(reachable(self, Regions.KF_BOULDER_LOOP, adult=False))

    def test_grab_is_first_strength(self):
        # item.cpp RG_PROGRESSIVE_STRENGTH: without RAND_INF_CAN_GRAB the first one is the Power Bracelet
        from ..LogicHelpers import has_grab, has_item
        bundle = (Regions.ROOT, self.world)
        grab = has_grab(bundle).resolve(self.world)
        goron = has_item(Items.GORONS_BRACELET, bundle).resolve(self.world)
        self.assertFalse(grab(self.multiworld.state))
        self.collect(self.world.create_item(Items.STRENGTH_UPGRADE.value))
        self.assertTrue(grab(self.multiworld.state))
        self.assertFalse(goron(self.multiworld.state))
        self.collect(self.world.create_item(Items.STRENGTH_UPGRADE.value))
        self.assertTrue(goron(self.multiworld.state))


class TestOpenChestProgressive(SohTestBase):
    options = {"shuffle_open_chest": "progressive"}

    def test_two_copies(self):
        self.assertEqual(2, in_pool(self, Items.OPEN_CHESTS))

    def test_large_chest_needs_second_copy(self):
        # logic.cpp ApplyItemEffect RG_OPEN_CHEST (progressive): 1st = RAND_INF_CAN_OPEN_CHEST, 2nd = ..._LARGE_CHEST
        from ..LogicHelpers import has_open_chest, can_open_large_chest
        bundle = (Regions.ROOT, self.world)
        small = has_open_chest(bundle).resolve(self.world)
        large = can_open_large_chest(bundle).resolve(self.world)
        state = self.multiworld.state
        self.assertFalse(small(state))
        self.collect(self.world.create_item(Items.OPEN_CHESTS.value))
        self.assertTrue(small(state))
        self.assertFalse(large(state))
        self.collect(self.world.create_item(Items.OPEN_CHESTS.value))
        self.assertTrue(large(state))


class TestOpenChestOn(SohTestBase):
    options = {"shuffle_open_chest": "on"}

    def test_one_copy_opens_large_chests(self):
        from ..LogicHelpers import can_open_large_chest
        large = can_open_large_chest((Regions.ROOT, self.world)).resolve(self.world)
        self.assertFalse(large(self.multiworld.state))
        self.collect(self.world.create_item(Items.OPEN_CHESTS.value))
        self.assertTrue(large(self.multiworld.state))
