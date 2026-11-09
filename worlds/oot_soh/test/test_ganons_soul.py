"""Ganon's Soul as its own setting (SoH 9.3.1 RSK_GANONS_SOUL, feature 1.7)."""
from .bases import SohTestBase
from ..Enums import Items, Enemies
from ..LogicHelpers import can_kill_enemy
from ..Options import GanonsSoul, ShuffleBossSouls, ShuffleDungeonRewards, StartWithLinksPocket


def soul_items(test: SohTestBase) -> list[str]:
    return [item.name for item in test.multiworld.itempool
            if item.player == test.player and item.name == Items.GANONS_SOUL.value]


def location_names(test: SohTestBase) -> list[str]:
    return [location.name for location in test.multiworld.get_locations(test.player)]


class TestSoulStartWith(SohTestBase):
    options = {"ganons_soul": GanonsSoul.option_start_with}

    def test_no_soul_needed(self):
        self.assertEqual(soul_items(self), [])
        self.assertNotIn("Ganon's Soul Trigger", location_names(self))


class TestSoulLegacyOnPlusGanon(SohTestBase):
    # older YAMLs: "On + Ganon" boss souls still shuffle Ganon's soul anywhere
    options = {"shuffle_boss_souls": ShuffleBossSouls.option_on_plus_ganons}

    def test_migrated_to_anywhere(self):
        self.assertEqual(self.world.options.ganons_soul.value, GanonsSoul.option_anywhere)
        self.assertEqual(len(soul_items(self)), 1)


class TestSoulAnyDungeon(SohTestBase):
    options = {"ganons_soul": GanonsSoul.option_any_dungeon}

    def test_soul_in_a_dungeon(self):
        soul = next(location for location in self.multiworld.get_locations(self.player)
                    if location.item and location.item.name == Items.GANONS_SOUL.value
                    and location.item.player == self.player)
        self.assertIsNotNone(soul.address)


class TestSoulTriggerMedallions(SohTestBase):
    options = {"ganons_soul": GanonsSoul.option_trigger_medallions, "ganons_soul_medallions_required": 2,
               "shuffle_dungeon_rewards": ShuffleDungeonRewards.option_anywhere,
               "start_with_links_pocket": StartWithLinksPocket.option_nothing}

    def test_trigger(self):
        self.assertEqual(soul_items(self), [])
        self.collect_all_but([Items.FOREST_MEDALLION, Items.FIRE_MEDALLION, Items.WATER_MEDALLION,
                              Items.SPIRIT_MEDALLION, Items.SHADOW_MEDALLION, Items.LIGHT_MEDALLION,
                              Items.GANONS_SOUL])
        self.assertFalse(self.can_reach_location("Ganon's Soul Trigger"))
        self.collect_by_name([Items.FOREST_MEDALLION])
        self.assertFalse(self.can_reach_location("Ganon's Soul Trigger"))
        self.collect_by_name([Items.FIRE_MEDALLION])
        self.assertTrue(self.can_reach_location("Ganon's Soul Trigger"))


class TestSoulNeededForGanon(SohTestBase):
    options = {"ganons_soul": GanonsSoul.option_anywhere}

    def test_ganon_needs_soul(self):
        rule = can_kill_enemy(self.get_bundle(), Enemies.GANON)
        self.collect_all_but([Items.GANONS_SOUL])
        self.assertFalse(rule.resolve(self.world)(self.multiworld.state))
        self.collect_by_name([Items.GANONS_SOUL])
        self.assertTrue(rule.resolve(self.world)(self.multiworld.state))
