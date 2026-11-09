"""Progressive Goron Sword (SoH 9.3.1 RSK_PROGRESSIVE_GORON_SWORD, feature 2.5)."""
from .bases import SohTestBase
from ..Enums import Items, Events
from ..LogicHelpers import has_item


def pool_names(test: SohTestBase) -> list[str]:
    return [item.name for item in test.multiworld.itempool if item.player == test.player]


class TestProgressiveGoronSword(SohTestBase):
    options = {"progressive_goron_sword": True, "shuffle_merchants": "all"}

    def test_pool(self):
        names = pool_names(self)
        self.assertEqual(names.count(Items.PROGRESSIVE_GORON_SWORD.value), 2)
        self.assertNotIn(Items.BIGGORONS_SWORD.value, names)
        self.assertNotIn(Items.GIANTS_KNIFE.value, names)

    def test_progression(self):
        knife = has_item(Items.GIANTS_KNIFE, self.get_bundle()).resolve(self.world)
        bgs = has_item(Items.BIGGORONS_SWORD, self.get_bundle()).resolve(self.world)
        state = self.multiworld.state
        # Medigoron doesn't hand out a first knife with progressive swords
        self.collect(self.create_item(Events.MEDIGORON))
        self.assertFalse(knife(state))
        self.collect(self.create_item(Items.PROGRESSIVE_GORON_SWORD))
        self.assertTrue(knife(state))
        self.assertFalse(bgs(state))
        self.collect(self.create_item(Items.PROGRESSIVE_GORON_SWORD))
        self.assertTrue(bgs(state))


class TestClassicGoronSwords(SohTestBase):
    options = {"progressive_goron_sword": False}

    def test_pool_and_medigoron(self):
        names = pool_names(self)
        self.assertNotIn(Items.PROGRESSIVE_GORON_SWORD.value, names)
        self.assertEqual(names.count(Items.BIGGORONS_SWORD.value), 1)
        # 9.3.1 Logic::HasItem: buying from Medigoron counts as having the knife
        knife = has_item(Items.GIANTS_KNIFE, self.get_bundle()).resolve(self.world)
        self.assertFalse(knife(self.multiworld.state))
        self.collect(self.create_item(Events.MEDIGORON))
        self.assertTrue(knife(self.multiworld.state))
