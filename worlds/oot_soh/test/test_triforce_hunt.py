"""Triforce Hunt as win condition (SoH 9.3.1, feature 1.6).

9.3.1 folded Triforce Hunt into "Total Pieces" plus the win condition "Trigger-Triforce Pieces"; the client maps the
apworld's options to that (SeedContext.cpp) and reports the goal when the game warps to the credits.
In the apworld the goal is the GAME_COMPLETED event in Root; there is no "Completed Triforce" location.
"""
from .bases import SohTestBase
from ..Enums import Items, Locations


class TestTriforceHunt(SohTestBase):
    options = {"triforce_hunt": True, "triforce_hunt_pieces_total": 10,
               "triforce_hunt_pieces_required_percentage": 50}

    def test_goal_needs_required_pieces(self):
        required = self.world.triforce_pieces_required
        self.assertEqual(required, 5)
        pieces = [item for item in self.multiworld.itempool
                  if item.player == self.player and item.name == Items.TRIFORCE_PIECE.value]
        self.assertEqual(len(pieces), 10)
        self.collect_all_but([Items.TRIFORCE_PIECE.value])
        goal = "Triforce Hunt Completion"  # location_access/archipelago.py, carries GAME_COMPLETED
        self.assertFalse(self.can_reach_location(goal))
        self.collect(pieces[:required - 1])
        self.assertFalse(self.can_reach_location(goal))
        self.collect(pieces[required - 1])
        self.assertTrue(self.can_reach_location(goal))

    def test_no_completed_triforce_location(self):
        names = [location.name for location in self.multiworld.get_locations(self.player)]
        self.assertNotIn(Locations.COMPLETED_TRIFORCE.value, names)
