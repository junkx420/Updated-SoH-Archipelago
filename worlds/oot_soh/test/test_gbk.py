"""Ganon's Boss Key trigger (SoH 9.3.1, feature 1.4)."""
from .bases import SohTestBase
from ..Enums import Items, Locations
from ..Options import GanonsCastleBossKey, ShuffleDungeonRewards, StartWithLinksPocket


class TestGbkTrigger(SohTestBase):
    options = {"ganons_castle_boss_key": GanonsCastleBossKey.option_lacs_medallions,
               "ganons_castle_boss_key_medallions_required": 3,
               "shuffle_dungeon_rewards": ShuffleDungeonRewards.option_anywhere,
               "start_with_links_pocket": StartWithLinksPocket.option_nothing}

    def test_key_is_trigger_event(self):
        # not a multiworld item any more
        self.assertNotIn(Items.GANONS_CASTLE_BOSS_KEY.value, [item.name for item in self.multiworld.itempool
                                                               if item.player == self.player])
        trigger = self.multiworld.get_location("Ganon's Boss Key Trigger", self.player)
        self.assertIsNone(trigger.address)
        self.assertEqual(trigger.item.name, Items.GANONS_CASTLE_BOSS_KEY.value)
        # the Light Arrow Cutscene is a normal location again
        lacs = self.multiworld.get_location(Locations.MARKET_TOT_LIGHT_ARROW_CUTSCENE.value, self.player)
        self.assertIsNotNone(lacs.address)
        self.assertFalse(lacs.locked)

    def test_trigger_needs_medallions(self):
        self.collect_all_but([Items.FOREST_MEDALLION, Items.FIRE_MEDALLION, Items.WATER_MEDALLION,
                              Items.SPIRIT_MEDALLION, Items.SHADOW_MEDALLION, Items.LIGHT_MEDALLION])
        self.assertFalse(self.can_reach_location("Ganon's Boss Key Trigger"))
        self.collect_by_name([Items.FOREST_MEDALLION, Items.FIRE_MEDALLION, Items.WATER_MEDALLION])
        self.assertTrue(self.can_reach_location("Ganon's Boss Key Trigger"))


class TestGbkAnywhere(SohTestBase):
    options = {"ganons_castle_boss_key": GanonsCastleBossKey.option_anywhere}

    def test_key_in_pool_no_trigger(self):
        self.assertIn(Items.GANONS_CASTLE_BOSS_KEY.value, [item.name for item in self.multiworld.itempool
                                                            if item.player == self.player])
        self.assertNotIn("Ganon's Boss Key Trigger",
                         [location.name for location in self.multiworld.get_locations(self.player)])
