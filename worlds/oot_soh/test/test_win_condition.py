"""Win Condition and Triforce Piece triggers (SoH 9.3.1 RSK_WINCON etc., feature 2.1)."""
from .bases import SohTestBase
from ..Enums import Items
from ..LogicHelpers import can_build_rainbow_bridge
from ..Options import (WinCondition, RainbowBridge, GanonsCastleBossKey, ShuffleDungeonRewards,
                       StartWithLinksPocket)


def pool(test: SohTestBase, name: str) -> list:
    return [item for item in test.multiworld.itempool if item.player == test.player and item.name == name]


def location_names(test: SohTestBase) -> list[str]:
    return [location.name for location in test.multiworld.get_locations(test.player)]


class TestDefaultWithoutHunt(SohTestBase):
    def test_resolves_to_ganon(self):
        self.assertEqual(self.world.options.win_condition.value, WinCondition.option_defeat_ganon)
        self.assertIn("Ganon Defeated", location_names(self))


class TestDefaultWithHunt(SohTestBase):
    options = {"triforce_hunt": True, "triforce_hunt_pieces_total": 10}

    def test_resolves_to_pieces(self):
        self.assertEqual(self.world.options.win_condition.value, WinCondition.option_trigger_triforce_pieces)
        self.assertIn("Triforce Hunt Completion", location_names(self))
        self.assertEqual(pool(self, Items.GANONS_CASTLE_BOSS_KEY.value), [])  # as before the option


class TestHuntPiecesWithGanonWin(SohTestBase):
    # pieces only for the bridge, Ganon still has to be defeated
    options = {"triforce_hunt": True, "triforce_hunt_pieces_total": 10,
               "win_condition": WinCondition.option_defeat_ganon,
               "rainbow_bridge": RainbowBridge.option_triforce_pieces,
               "rainbow_bridge_triforce_pieces_required": 4,
               "ganons_castle_boss_key": GanonsCastleBossKey.option_anywhere}

    def test_bridge_needs_pieces(self):
        self.assertIn("Ganon Defeated", location_names(self))
        self.assertEqual(len(pool(self, Items.GANONS_CASTLE_BOSS_KEY.value)), 1)
        pieces = pool(self, Items.TRIFORCE_PIECE.value)
        self.assertEqual(len(pieces), 10)
        rule = can_build_rainbow_bridge(self.get_bundle()).resolve(self.world)
        self.collect(pieces[:3])
        self.assertFalse(rule(self.multiworld.state))
        self.collect(pieces[3])
        self.assertTrue(rule(self.multiworld.state))


class TestWinAnywhere(SohTestBase):
    options = {"win_condition": WinCondition.option_anywhere}

    def test_triforce_item(self):
        triforce = pool(self, Items.TRIFORCE.value)
        self.assertEqual(len(triforce), 1)
        self.assertIsNotNone(triforce[0].code)
        self.collect_all_but([Items.TRIFORCE.value])
        self.assertFalse(self.can_reach_location("Triforce Found"))
        self.collect(triforce)
        self.assertTrue(self.can_reach_location("Triforce Found"))


class TestWinTriggerMedallions(SohTestBase):
    options = {"win_condition": WinCondition.option_trigger_medallions, "win_condition_medallions_required": 2,
               "shuffle_dungeon_rewards": ShuffleDungeonRewards.option_anywhere,
               "start_with_links_pocket": StartWithLinksPocket.option_nothing}

    def test_trigger(self):
        self.assertNotIn("Ganon Defeated", location_names(self))
        self.collect_all_but([Items.FOREST_MEDALLION, Items.FIRE_MEDALLION, Items.WATER_MEDALLION,
                              Items.SPIRIT_MEDALLION, Items.SHADOW_MEDALLION, Items.LIGHT_MEDALLION])
        self.assertFalse(self.can_reach_location("Win Condition Trigger"))
        self.collect_by_name([Items.FOREST_MEDALLION, Items.FIRE_MEDALLION])
        self.assertTrue(self.can_reach_location("Win Condition Trigger"))


class TestGbkTriforcePieces(SohTestBase):
    options = {"triforce_hunt": True, "triforce_hunt_pieces_total": 10,
               "win_condition": WinCondition.option_defeat_ganon,
               "ganons_castle_boss_key": GanonsCastleBossKey.option_lacs_triforce_pieces,
               "ganons_castle_boss_key_triforce_pieces_required": 5}

    def test_gbk_trigger(self):
        self.assertEqual(pool(self, Items.GANONS_CASTLE_BOSS_KEY.value), [])
        pieces = pool(self, Items.TRIFORCE_PIECE.value)
        # the boss key needs 5, so 5 pieces count for logic even though the win doesn't use them
        self.assertEqual(sum(1 for piece in pieces if piece.advancement), 5)
        self.collect_all_but([Items.TRIFORCE_PIECE.value])
        self.assertFalse(self.can_reach_location("Ganon's Boss Key Trigger"))
        self.collect([piece for piece in pieces if piece.advancement])
        self.assertTrue(self.can_reach_location("Ganon's Boss Key Trigger"))
