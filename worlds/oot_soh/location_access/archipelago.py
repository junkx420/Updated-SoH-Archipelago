"""Archipelago-specific additions to the region logic ported from upstream Ship of Harkinian 9.3.1.

The files next to this one are generated from upstream's location_access/*.cpp (docs/ap-update/tools/translate.py).
Upstream does some things outside those files (the fill algorithm, the win condition), and the apworld has a few
events of its own. They live here so regenerating the ported files doesn't lose them. Runs after all ported files.
"""
from ..LogicHelpers import *

if TYPE_CHECKING:
    from .. import SohWorld


class EventLocations(StrEnum):
    TIME_TRAVEL = "Chamber of Sages"
    GANON_DEFEATED = "Ganon Defeated"
    TRIFORCE_HUNT_COMPLETION = "Triforce Hunt Completion"
    MAGIC_BEAN_SALESMAN_SHOP = "Magic Bean Salesman Shop"


def set_region_rules(world: "SohWorld") -> None:
    # Time travel: upstream 3drando/fill.cpp PropagateTimeTravel gives the other age access to Root once the starting
    # age reaches Beyond Door of Time. The ported root.cpp connects Root -> Root Exits unconditionally, because
    # upstream's search starts with the starting age only; the apworld searches both ages from Root, so the other age
    # has to wait for the time travel event here.
    add_events(Regions.TOT_BEYOND_DOOR_OF_TIME, world, [
        (EventLocations.TIME_TRAVEL, Events.TIME_TRAVEL, lambda bundle: True_()),
    ])
    override_connection(world, Regions.ROOT, Regions.ROOT_EXITS,
                        lambda bundle: starting_age(bundle) | has_item(Events.TIME_TRAVEL, bundle))

    # Triforce Hunt: the item pool has no Ganon's Boss Key (ItemPool.py), so Ganondorf's Lair opens without it, as in
    # the apworld before the 9.3.1 port
    if bool(world.options.triforce_hunt):
        override_connection(world, Regions.GANONS_TOWER_BEFORE_GANONDORF_LAIR, Regions.GANONS_TOWER_GANONDORF_LAIR,
                            lambda bundle: True_())

    # Win condition (the apworld's goal; upstream 9.3.1 uses the RC_GANON / RC_WINCON trigger locations, see
    # docs/ap-update/feature-plan.md 1.6 / 2.1)
    if bool(world.options.triforce_hunt):
        add_events(Regions.ROOT, world, [
            (EventLocations.TRIFORCE_HUNT_COMPLETION, Events.GAME_COMPLETED, lambda bundle: CanWinTriforceHunt()),
        ])
    else:
        add_events(Regions.GANONS_CASTLE_GANON_ARENA, world, [
            (EventLocations.GANON_DEFEATED, Events.GAME_COMPLETED,
             lambda bundle: can_kill_enemy(bundle, Enemies.GANON)),
        ])

    # Magic beans for planting: when the Bean Salesman sells his vanilla item, beans can be bought from him.
    if world.options.shuffle_merchants.value == 0 or world.options.shuffle_merchants.value == 2:
        add_events(Regions.ZORAS_RIVER, world, [
            (EventLocations.MAGIC_BEAN_SALESMAN_SHOP, Events.CAN_BUY_BEANS,
             lambda bundle: is_child(bundle) & has_item(Items.CHILD_WALLET, bundle)),
        ])


def override_connection(world: "SohWorld", parent: Regions, child: Regions,
                        rule_fn: Callable[[tuple[Regions, "SohWorld"]], Rule]) -> None:
    """Replace the rule of a connection a ported file created."""
    for entrance in world.get_region(str(parent)).exits:
        if entrance.connected_region is not None and entrance.connected_region.name == str(child):
            if not world.options.true_no_logic:
                world.set_rule(entrance, rule_fn((parent, world)))
            return
    raise RuntimeError(f"connection {parent} -> {child} is missing")

