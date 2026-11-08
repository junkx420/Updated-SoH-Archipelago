"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/thieves_hideout.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    TH_1_TORCH_CELL_TH_COULD_FREE_1_TORCH_CARPENTER = "Thieves Hideout 1 Torch Cell Th Could Free 1 Torch Carpenter"
    TH_1_TORCH_CELL_TH_RESCUED_ALL_CARPENTERS = "Thieves Hideout 1 Torch Cell Th Rescued All Carpenters"
    TH_DOUBLE_CELL_TH_COULD_FREE_DOUBLE_CELL_CARPENTER = "Thieves Hideout Double Cell Th Could Free Double Cell Carpenter"
    TH_DOUBLE_CELL_TH_RESCUED_ALL_CARPENTERS = "Thieves Hideout Double Cell Th Rescued All Carpenters"
    TH_DEAD_END_CELL_TH_COULD_FREE_DEAD_END_CARPENTER = "Thieves Hideout Dead End Cell Th Could Free Dead End Carpenter"
    TH_DEAD_END_CELL_TH_RESCUED_ALL_CARPENTERS = "Thieves Hideout Dead End Cell Th Rescued All Carpenters"
    TH_STEEP_SLOPE_CELL_TH_COULD_FREE_SLOPE_CARPENTER = "Thieves Hideout Steep Slope Cell Th Could Free Slope Carpenter"
    TH_STEEP_SLOPE_CELL_TH_RESCUED_ALL_CARPENTERS = "Thieves Hideout Steep Slope Cell Th Rescued All Carpenters"


def set_region_rules(world: "SohWorld") -> None:

    # Thieves Hideout 1 Torch Cell  (upstream RR_TH_1_TORCH_CELL, SCENE_THIEVES_HIDEOUT)
    # Events
    add_events(Regions.TH_1_TORCH_CELL, world, [
        (EventLocations.TH_1_TORCH_CELL_TH_COULD_FREE_1_TORCH_CARPENTER, Events.TH_COULD_FREE_1_TORCH_CARPENTER,
         lambda bundle: can_kill_enemy(bundle, Enemies.GERUDO_WARRIOR) & has_speak(bundle, "HYLIAN")),
        (EventLocations.TH_1_TORCH_CELL_TH_RESCUED_ALL_CARPENTERS, Events.TH_RESCUED_ALL_CARPENTERS,
         lambda bundle: ((True_(options=[OptionFilter(FortressCarpenters, FortressCarpenters.option_normal)])) & small_keys_scene("SCENE_THIEVES_HIDEOUT", 4, bundle) | (Not(True_(options=[OptionFilter(FortressCarpenters, FortressCarpenters.option_normal)]))) & small_keys_scene("SCENE_THIEVES_HIDEOUT", 1, bundle)) & has_item(Events.TH_COULD_FREE_1_TORCH_CARPENTER, bundle) & has_item(Events.TH_COULD_FREE_DOUBLE_CELL_CARPENTER, bundle) & has_item(Events.TH_COULD_FREE_DEAD_END_CARPENTER, bundle) & has_item(Events.TH_COULD_FREE_SLOPE_CARPENTER, bundle)),
    ])
    # Locations
    add_locations(Regions.TH_1_TORCH_CELL, world, [
        (Locations.TH_1_TORCH_CARPENTER,
         lambda bundle: has_item(Events.TH_COULD_FREE_1_TORCH_CARPENTER, bundle)),
        (Locations.TH_1_TORCH_CELL_RIGHT_POT,
         lambda bundle: can_break_pots(bundle)),
        (Locations.TH_1_TORCH_CELL_MIDDLE_POT,
         lambda bundle: can_break_pots(bundle)),
        (Locations.TH_1_TORCH_CELL_LEFT_POT,
         lambda bundle: can_break_pots(bundle)),
        (Locations.TH_1_TORCH_CELL_CRATE,
         lambda bundle: can_break_crates(bundle)),
        # DEFERRED RC_TH_WONDER_1_TORCH_1: logic->CanUse(RG_FAIRY_BOW)
        # DEFERRED RC_TH_WONDER_1_TORCH_2: logic->CanUse(RG_FAIRY_BOW)
        (Locations.GF_GERUDO_MEMBERSHIP_CARD,
         lambda bundle: has_item(Events.TH_RESCUED_ALL_CARPENTERS, bundle)),
    ])
    # Connections
    connect_regions(Regions.TH_1_TORCH_CELL, world, [
        (Regions.GF_OUTSKIRTS,
         lambda bundle: True_()),
        (Regions.GF_NEAR_GROTTO,
         lambda bundle: True_()),
    ])

    # Thieves Hideout Double Cell  (upstream RR_TH_DOUBLE_CELL, SCENE_THIEVES_HIDEOUT)
    # Events
    add_events(Regions.TH_DOUBLE_CELL, world, [
        (EventLocations.TH_DOUBLE_CELL_TH_COULD_FREE_DOUBLE_CELL_CARPENTER, Events.TH_COULD_FREE_DOUBLE_CELL_CARPENTER,
         lambda bundle: can_kill_enemy(bundle, Enemies.GERUDO_WARRIOR) & has_speak(bundle, "HYLIAN")),
        (EventLocations.TH_DOUBLE_CELL_TH_RESCUED_ALL_CARPENTERS, Events.TH_RESCUED_ALL_CARPENTERS,
         lambda bundle: ((True_(options=[OptionFilter(FortressCarpenters, FortressCarpenters.option_normal)])) & small_keys_scene("SCENE_THIEVES_HIDEOUT", 4, bundle) | (Not(True_(options=[OptionFilter(FortressCarpenters, FortressCarpenters.option_normal)]))) & small_keys_scene("SCENE_THIEVES_HIDEOUT", 1, bundle)) & has_item(Events.TH_COULD_FREE_1_TORCH_CARPENTER, bundle) & has_item(Events.TH_COULD_FREE_DOUBLE_CELL_CARPENTER, bundle) & has_item(Events.TH_COULD_FREE_DEAD_END_CARPENTER, bundle) & has_item(Events.TH_COULD_FREE_SLOPE_CARPENTER, bundle)),
    ])
    # Locations
    add_locations(Regions.TH_DOUBLE_CELL, world, [
        (Locations.TH_DOUBLE_CELL_CARPENTER,
         lambda bundle: has_item(Events.TH_COULD_FREE_DOUBLE_CELL_CARPENTER, bundle)),
        (Locations.TH_DOUBLE_CELL_RIGHT_POT,
         lambda bundle: can_break_pots(bundle)),
        (Locations.TH_DOUBLE_CELL_MIDDLE_POT,
         lambda bundle: can_break_pots(bundle)),
        (Locations.TH_DOUBLE_CELL_LEFT_POT,
         lambda bundle: can_break_pots(bundle)),
        (Locations.TH_RIGHTMOST_JAILED_POT,
         lambda bundle: can_break_pots(bundle)),
        (Locations.TH_RIGHT_MIDDLE_JAILED_POT,
         lambda bundle: can_break_pots(bundle)),
        (Locations.TH_LEFT_MIDDLE_JAILED_POT,
         lambda bundle: can_break_pots(bundle)),
        (Locations.TH_LEFTMOST_JAILED_POT,
         lambda bundle: can_break_pots(bundle)),
        (Locations.TH_DOUBLE_CELL_LEFT_CRATE,
         lambda bundle: can_break_crates(bundle)),
        (Locations.TH_DOUBLE_CELL_RIGHT_CRATE,
         lambda bundle: can_break_crates(bundle)),
        # DEFERRED RC_TH_WONDER_DOUBLE_JAIL_LOWER_EXIT: logic->CanUse(RG_FAIRY_BOW)
        # DEFERRED RC_TH_WONDER_DOUBLE_JAIL_UPPER_EXIT: logic->CanUse(RG_FAIRY_BOW)
        (Locations.GF_GERUDO_MEMBERSHIP_CARD,
         lambda bundle: has_item(Events.TH_RESCUED_ALL_CARPENTERS, bundle)),
    ])
    # Connections
    connect_regions(Regions.TH_DOUBLE_CELL, world, [
        (Regions.GF_OUTSKIRTS,
         lambda bundle: True_()),
        (Regions.GF_ABOVE_GTG,
         lambda bundle: True_()),
        (Regions.GF_TOP_OF_LOWER_VINES,
         lambda bundle: True_()),
    ])

    # Thieves Hideout Dead End Cell  (upstream RR_TH_DEAD_END_CELL, SCENE_THIEVES_HIDEOUT)
    # Events
    add_events(Regions.TH_DEAD_END_CELL, world, [
        (EventLocations.TH_DEAD_END_CELL_TH_COULD_FREE_DEAD_END_CARPENTER, Events.TH_COULD_FREE_DEAD_END_CARPENTER,
         lambda bundle: can_kill_enemy(bundle, Enemies.GERUDO_WARRIOR) & has_speak(bundle, "HYLIAN")),
        (EventLocations.TH_DEAD_END_CELL_TH_RESCUED_ALL_CARPENTERS, Events.TH_RESCUED_ALL_CARPENTERS,
         lambda bundle: ((True_(options=[OptionFilter(FortressCarpenters, FortressCarpenters.option_normal)])) & small_keys_scene("SCENE_THIEVES_HIDEOUT", 4, bundle) | (Not(True_(options=[OptionFilter(FortressCarpenters, FortressCarpenters.option_normal)]))) & small_keys_scene("SCENE_THIEVES_HIDEOUT", 1, bundle)) & has_item(Events.TH_COULD_FREE_1_TORCH_CARPENTER, bundle) & has_item(Events.TH_COULD_FREE_DOUBLE_CELL_CARPENTER, bundle) & has_item(Events.TH_COULD_FREE_DEAD_END_CARPENTER, bundle) & has_item(Events.TH_COULD_FREE_SLOPE_CARPENTER, bundle)),
    ])
    # Locations
    add_locations(Regions.TH_DEAD_END_CELL, world, [
        (Locations.TH_DEAD_END_CARPENTER,
         lambda bundle: has_item(Events.TH_COULD_FREE_DEAD_END_CARPENTER, bundle)),
        (Locations.TH_DEAD_END_CELL_CRATE,
         lambda bundle: can_break_crates(bundle)),
        # DEFERRED RC_TH_WONDER_DEAD_END_SKULL_ENTRANCE: logic->CanUse(RG_FAIRY_BOW)
        # DEFERRED RC_TH_WONDER_DEAD_END_SKULL_NEAR_JAIL: logic->CanUse(RG_FAIRY_BOW)
        (Locations.GF_GERUDO_MEMBERSHIP_CARD,
         lambda bundle: has_item(Events.TH_RESCUED_ALL_CARPENTERS, bundle)),
    ])
    # Connections
    connect_regions(Regions.TH_DEAD_END_CELL, world, [
        (Regions.GF_BELOW_GS,
         lambda bundle: True_()),
    ])

    # Thieves Hideout Steep Slope Cell  (upstream RR_TH_STEEP_SLOPE_CELL, SCENE_THIEVES_HIDEOUT)
    # Events
    add_events(Regions.TH_STEEP_SLOPE_CELL, world, [
        (EventLocations.TH_STEEP_SLOPE_CELL_TH_COULD_FREE_SLOPE_CARPENTER, Events.TH_COULD_FREE_SLOPE_CARPENTER,
         lambda bundle: can_kill_enemy(bundle, Enemies.GERUDO_WARRIOR) & has_speak(bundle, "HYLIAN")),
        (EventLocations.TH_STEEP_SLOPE_CELL_TH_RESCUED_ALL_CARPENTERS, Events.TH_RESCUED_ALL_CARPENTERS,
         lambda bundle: ((True_(options=[OptionFilter(FortressCarpenters, FortressCarpenters.option_normal)])) & small_keys_scene("SCENE_THIEVES_HIDEOUT", 4, bundle) | (Not(True_(options=[OptionFilter(FortressCarpenters, FortressCarpenters.option_normal)]))) & small_keys_scene("SCENE_THIEVES_HIDEOUT", 1, bundle)) & has_item(Events.TH_COULD_FREE_1_TORCH_CARPENTER, bundle) & has_item(Events.TH_COULD_FREE_DOUBLE_CELL_CARPENTER, bundle) & has_item(Events.TH_COULD_FREE_DEAD_END_CARPENTER, bundle) & has_item(Events.TH_COULD_FREE_SLOPE_CARPENTER, bundle)),
    ])
    # Locations
    add_locations(Regions.TH_STEEP_SLOPE_CELL, world, [
        (Locations.TH_STEEP_SLOPE_CARPENTER,
         lambda bundle: has_item(Events.TH_COULD_FREE_SLOPE_CARPENTER, bundle)),
        (Locations.TH_STEEP_SLOPE_RIGHT_POT,
         lambda bundle: can_break_pots(bundle)),
        (Locations.TH_STEEP_SLOPE_LEFT_POT,
         lambda bundle: can_break_pots(bundle)),
        # DEFERRED RC_TH_WONDER_STEEP_SLOPE_LOWER_EXIT: logic->CanUse(RG_FAIRY_BOW)
        # DEFERRED RC_TH_WONDER_STEEP_SLOPE_UPPER_EXIT: logic->CanUse(RG_FAIRY_BOW)
        (Locations.GF_GERUDO_MEMBERSHIP_CARD,
         lambda bundle: has_item(Events.TH_RESCUED_ALL_CARPENTERS, bundle)),
    ])
    # Connections
    connect_regions(Regions.TH_STEEP_SLOPE_CELL, world, [
        (Regions.GF_BOTTOM_OF_LOWER_VINES,
         lambda bundle: True_()),
        (Regions.GF_NEAR_GROTTO,
         lambda bundle: True_()),
    ])

    # Thieves Hideout Kitchen Corridor  (upstream RR_TH_KITCHEN_CORRIDOR, SCENE_THIEVES_HIDEOUT)
    # Locations
    add_locations(Regions.TH_KITCHEN_CORRIDOR, world, [
        (Locations.TH_NEAR_KITCHEN_LEFTMOST_CRATE,
         lambda bundle: can_break_crates(bundle)),
        (Locations.TH_NEAR_KITCHEN_MIDDLE_LEFT_CRATE,
         lambda bundle: can_break_crates(bundle)),
        (Locations.TH_NEAR_KITCHEN_MIDDLE_RIGHT_CRATE,
         lambda bundle: can_break_crates(bundle)),
        (Locations.TH_NEAR_KITCHEN_RIGHTMOST_CRATE,
         lambda bundle: can_break_crates(bundle)),
    ])
    # Connections
    connect_regions(Regions.TH_KITCHEN_CORRIDOR, world, [
        (Regions.GF_NEAR_GROTTO,
         lambda bundle: True_()),
        (Regions.GF_ABOVE_GTG,
         lambda bundle: True_()),
        (Regions.TH_KITCHEN_MAIN,
         lambda bundle: can_pass_enemy(bundle, Enemies.GERUDO_GUARD)),
    ])

    # Thieves Hideout Kitchen Main  (upstream RR_TH_KITCHEN_MAIN, SCENE_THIEVES_HIDEOUT)
    # Locations
    add_locations(Regions.TH_KITCHEN_MAIN, world, [
        (Locations.TH_KITCHEN_POT1,
         lambda bundle: can_break_pots(bundle) & can_pass_enemy(bundle, Enemies.GERUDO_GUARD)),
        (Locations.TH_KITCHEN_POT2,
         lambda bundle: can_break_pots(bundle) & can_pass_enemy(bundle, Enemies.GERUDO_GUARD)),
        (Locations.TH_KITCHEN_CRATE,
         lambda bundle: can_break_crates(bundle) & can_pass_enemy(bundle, Enemies.GERUDO_GUARD)),
        (Locations.TH_KITCHEN_SUN_FAIRY,
         lambda bundle: can_pass_enemy(bundle, Enemies.GERUDO_GUARD) & can_use(Items.SUNS_SONG, bundle)),
        # DEFERRED RC_TH_WONDER_KITCHEN_SKULL: logic->CanUse(RG_FAIRY_BOW)
        # DEFERRED RC_TH_WONDER_KITCHEN_SOUP: (logic->TakeDamage() || logic->IsAdult || logic->CanUse(RG_GORON_TUNIC)) && logic->CanPassEnemy(RE_GERUDO_GUARD)
    ])
    # Connections
    connect_regions(Regions.TH_KITCHEN_MAIN, world, [
        (Regions.TH_KITCHEN_CORRIDOR,
         lambda bundle: can_pass_enemy(bundle, Enemies.GERUDO_GUARD)),
        (Regions.TH_KITCHEN_BY_CORRIDOR,
         lambda bundle: can_pass_enemy(bundle, Enemies.GERUDO_GUARD)),
        (Regions.TH_KITCHEN_OPPOSITE_CORRIDOR,
         lambda bundle: can_pass_enemy(bundle, Enemies.GERUDO_GUARD)),
    ])

    # Thieves Hideout Kitchen Top By Corridor  (upstream RR_TH_KITCHEN_BY_CORRIDOR, SCENE_THIEVES_HIDEOUT)
    # Locations
    add_locations(Regions.TH_KITCHEN_BY_CORRIDOR, world, [
        (Locations.TH_KITCHEN_POT1,
         lambda bundle: can_use(Items.BOOMERANG, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_break_pots(bundle, EnemyDistance.BOMB_THROW))),
        (Locations.TH_KITCHEN_POT2,
         lambda bundle: can_use(Items.BOOMERANG, bundle)),
        # DEFERRED RC_TH_WONDER_KITCHEN_SOUP: ctx->GetTrickOption(RT_VOIDOUT_COLLECTION) && logic->BunnyHovers()
    ])
    # Connections
    connect_regions(Regions.TH_KITCHEN_BY_CORRIDOR, world, [
        (Regions.TH_KITCHEN_MAIN,
         lambda bundle: True_()),
        (Regions.TH_KITCHEN_OPPOSITE_CORRIDOR,
         lambda bundle: can_pass_enemy(bundle, Enemies.GERUDO_GUARD) | can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle)),
        (Regions.GF_TOP_OF_LOWER_VINES,
         lambda bundle: True_()),
    ])

    # Thieves Hideout Kitchen Top Across From Corridor  (upstream RR_TH_KITCHEN_OPPOSITE_CORRIDOR, SCENE_THIEVES_HIDEOUT)
    # Locations
    add_locations(Regions.TH_KITCHEN_OPPOSITE_CORRIDOR, world, [
        (Locations.TH_KITCHEN_POT1,
         lambda bundle: can_use(Items.BOOMERANG, bundle)),
        (Locations.TH_KITCHEN_POT2,
         lambda bundle: can_use(Items.BOOMERANG, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_break_pots(bundle, EnemyDistance.BOMB_THROW))),
        # DEFERRED RC_TH_WONDER_KITCHEN_SOUP: ctx->GetTrickOption(RT_VOIDOUT_COLLECTION) && logic->BunnyHovers()
    ])
    # Connections
    connect_regions(Regions.TH_KITCHEN_OPPOSITE_CORRIDOR, world, [
        (Regions.TH_KITCHEN_MAIN,
         lambda bundle: True_()),
        (Regions.TH_KITCHEN_BY_CORRIDOR,
         lambda bundle: can_pass_enemy(bundle, Enemies.GERUDO_GUARD) | can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle)),
        (Regions.GF_NEAR_GS,
         lambda bundle: True_()),
    ])

    # Thieves Hideout Break Room  (upstream RR_TH_BREAK_ROOM, SCENE_THIEVES_HIDEOUT)
    # Locations
    add_locations(Regions.TH_BREAK_ROOM, world, [
        (Locations.TH_BREAK_ROOM_FRONT_POT,
         lambda bundle: (can_pass_enemy(bundle, Enemies.BREAK_ROOM_GUARD) & can_break_pots(bundle)) | (can_pass_enemy(bundle, Enemies.GERUDO_GUARD) & can_use(Items.BOOMERANG, bundle))),
        (Locations.TH_BREAK_ROOM_BACK_POT,
         lambda bundle: (can_pass_enemy(bundle, Enemies.BREAK_ROOM_GUARD) & can_break_pots(bundle)) | (can_pass_enemy(bundle, Enemies.GERUDO_GUARD) & can_use(Items.BOOMERANG, bundle))),
        (Locations.TH_BREAK_HALLWAY_OUTER_CRATE,
         lambda bundle: can_break_crates(bundle)),
        (Locations.TH_BREAK_HALLWAY_INNER_CRATE,
         lambda bundle: can_break_crates(bundle)),
        (Locations.TH_BREAK_ROOM_RIGHT_CRATE,
         lambda bundle: (can_pass_enemy(bundle, Enemies.BREAK_ROOM_GUARD) & can_break_crates(bundle)) | (can_pass_enemy(bundle, Enemies.GERUDO_GUARD) & has_explosives(bundle) & can_use(Items.BOOMERANG, bundle))),
        (Locations.TH_BREAK_ROOM_LEFT_CRATE,
         lambda bundle: (can_pass_enemy(bundle, Enemies.BREAK_ROOM_GUARD) & can_break_crates(bundle)) | (can_pass_enemy(bundle, Enemies.GERUDO_GUARD) & has_explosives(bundle) & can_use(Items.BOOMERANG, bundle))),
    ])
    # Connections
    connect_regions(Regions.TH_BREAK_ROOM, world, [
        (Regions.GF_BELOW_CHEST,
         lambda bundle: can_pass_enemy(bundle, Enemies.GERUDO_GUARD)),
        (Regions.TH_BREAK_ROOM_LOWER_CORRIDOR,
         lambda bundle: can_pass_enemy(bundle, Enemies.GERUDO_GUARD)),
    ])

    # Thieves Hideout Break Room Lower Corridor  (upstream RR_TH_BREAK_ROOM_LOWER_CORRIDOR, SCENE_THIEVES_HIDEOUT)
    # Locations
    add_locations(Regions.TH_BREAK_ROOM_LOWER_CORRIDOR, world, [
        # DEFERRED RC_TH_WONDER_BREAK_ROOM_BOTTOM_SKULL: logic->CanUse(RG_FAIRY_BOW)
    ])
    # Connections
    connect_regions(Regions.TH_BREAK_ROOM_LOWER_CORRIDOR, world, [
        (Regions.TH_BREAK_ROOM,
         lambda bundle: can_pass_enemy(bundle, Enemies.GERUDO_GUARD)),
        (Regions.TH_BREAK_ROOM_UPPER_CORRIDOR,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
    ])

    # Thieves Hideout Break Room Upper Corridor  (upstream RR_TH_BREAK_ROOM_UPPER_CORRIDOR, SCENE_THIEVES_HIDEOUT)
    # Locations
    add_locations(Regions.TH_BREAK_ROOM_UPPER_CORRIDOR, world, [
        # DEFERRED RC_TH_WONDER_BREAK_ROOM_TOP_SKULL: logic->CanUse(RG_FAIRY_BOW)
    ])
    # Connections
    connect_regions(Regions.TH_BREAK_ROOM_UPPER_CORRIDOR, world, [
        (Regions.TH_BREAK_ROOM_LOWER_CORRIDOR,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
        (Regions.GF_ABOVE_JAIL,
         lambda bundle: True_()),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['TH_COULD_FREE_1_TORCH_CARPENTER', 'TH_COULD_FREE_DEAD_END_CARPENTER', 'TH_COULD_FREE_DOUBLE_CELL_CARPENTER', 'TH_COULD_FREE_SLOPE_CARPENTER', 'TH_RESCUED_ALL_CARPENTERS']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (14): ['RC_TH_WONDER_1_TORCH_1', 'RC_TH_WONDER_1_TORCH_2', 'RC_TH_WONDER_DOUBLE_JAIL_LOWER_EXIT', 'RC_TH_WONDER_DOUBLE_JAIL_UPPER_EXIT', 'RC_TH_WONDER_DEAD_END_SKULL_ENTRANCE', 'RC_TH_WONDER_DEAD_END_SKULL_NEAR_JAIL', 'RC_TH_WONDER_STEEP_SLOPE_LOWER_EXIT', 'RC_TH_WONDER_STEEP_SLOPE_UPPER_EXIT', 'RC_TH_WONDER_KITCHEN_SKULL', 'RC_TH_WONDER_KITCHEN_SOUP', 'RC_TH_WONDER_KITCHEN_SOUP', 'RC_TH_WONDER_KITCHEN_SOUP', 'RC_TH_WONDER_BREAK_ROOM_BOTTOM_SKULL', 'RC_TH_WONDER_BREAK_ROOM_TOP_SKULL']
