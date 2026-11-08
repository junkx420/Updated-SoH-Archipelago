"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/gerudo_fortress.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    GF_OUTSIDE_GTG_GTG_GATE_OPEN = "GF Outside GTG Gtg Gate Open"
    GF_TOWER_GF_GATE_OPEN = "Gerudo Fortress Tower Gf Gate Open"
    GF_OUTSIDE_GATE_GF_GATE_OPEN = "GF Outside Gate Gf Gate Open"
    GF_STORMS_GROTTO_FAIRY_ACCESS = "GF Storms Grotto Fairy Access"


def set_region_rules(world: "SohWorld") -> None:

    # Gerudo Fortress Outskirts  (upstream RR_GF_OUTSKIRTS, SCENE_GERUDOS_FORTRESS)
    # Locations
    add_locations(Regions.GF_OUTSKIRTS, world, [
        (Locations.GF_OUTSKIRTS_NORTHEAST_CRATE,
         lambda bundle: (is_child(bundle) | can_pass_enemy(bundle, Enemies.GERUDO_GUARD)) & can_break_crates(bundle)),
        (Locations.GF_OUTSKIRTS_NORTHWEST_CRATE,
         lambda bundle: (is_child(bundle) | can_pass_enemy(bundle, Enemies.GERUDO_GUARD)) & can_break_crates(bundle)),
        # DEFERRED RC_GF_EAST_EXIT_ARROW_SIGN: logic->CanRead()
        # DEFERRED RC_GF_WONDER_ENTRANCE_SIGN: logic->CanUse(RG_HOOKSHOT)
    ])
    # Connections
    connect_regions(Regions.GF_OUTSKIRTS, world, [
        (Regions.GV_FORTRESS_SIDE,
         lambda bundle: True_()),
        (Regions.TH_1_TORCH_CELL,
         lambda bundle: True_()),
        (Regions.GF_OUTSIDE_GATE,
         lambda bundle: has_item(Events.GF_GATE_OPEN, bundle)),
        (Regions.GF_NEAR_GROTTO,
         lambda bundle: is_child(bundle) | can_pass_enemy(bundle, Enemies.GERUDO_GUARD)),
        (Regions.GF_OUTSIDE_GTG,
         lambda bundle: is_child(bundle) | can_pass_enemy(bundle, Enemies.GERUDO_GUARD)),
        (Regions.GF_TOWER,
         lambda bundle: (is_child(bundle) | has_item(Items.GERUDO_MEMBERSHIP_CARD, bundle)) & can_climb_high_ladder(bundle)),
        (Regions.GF_JAIL_WINDOW,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
    ])

    # GF Near Grotto  (upstream RR_GF_NEAR_GROTTO, SCENE_GERUDOS_FORTRESS)
    # Locations
    add_locations(Regions.GF_NEAR_GROTTO, world, [
        (Locations.GF_SOUTHMOST_CENTER_CRATE,
         lambda bundle: can_break_crates(bundle)),
        (Locations.GF_MIDDLE_SOUTH_CENTER_CRATE,
         lambda bundle: can_break_crates(bundle)),
        (Locations.GF_MIDDLE_NORTH_CENTER_CRATE,
         lambda bundle: can_break_crates(bundle)),
        (Locations.GF_NORTHMOST_CENTER_CRATE,
         lambda bundle: can_break_crates(bundle)),
    ])
    # Connections
    connect_regions(Regions.GF_NEAR_GROTTO, world, [
        (Regions.TH_1_TORCH_CELL,
         lambda bundle: True_()),
        (Regions.TH_STEEP_SLOPE_CELL,
         lambda bundle: True_()),
        (Regions.TH_KITCHEN_CORRIDOR,
         lambda bundle: True_()),
        (Regions.GF_OUTSKIRTS,
         lambda bundle: True_()),
        (Regions.GF_JAIL_WINDOW,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
        (Regions.GF_OUTSIDE_GTG,
         lambda bundle: is_child(bundle) | can_pass_enemy(bundle, Enemies.GERUDO_GUARD)),
        (Regions.GF_TOP_OF_UPPER_VINES,
         lambda bundle: can_use(Items.LONGSHOT, bundle)),
        (Regions.GF_STORMS_GROTTO,
         lambda bundle: is_adult(bundle) & can_open_storms_grotto(bundle)),
    ])

    # GF Outside GTG  (upstream RR_GF_OUTSIDE_GTG, SCENE_GERUDOS_FORTRESS)
    # Events
    add_events(Regions.GF_OUTSIDE_GTG, world, [
        (EventLocations.GF_OUTSIDE_GTG_GTG_GATE_OPEN, Events.GTG_GATE_OPEN,
         lambda bundle: is_adult(bundle) & has_item(Items.GERUDO_MEMBERSHIP_CARD, bundle) & has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "GERUDO")),
    ])
    # Locations
    add_locations(Regions.GF_OUTSIDE_GTG, world, [
        # DEFERRED RC_GF_GTG_ENTRANCE_RECTANGLE_SIGN: logic->IsAdult && logic->CanRead() && (ctx->GetTrickOption(RT_PASS_GUARDS_WITH_NOTHING) || logic->HasItem(RG_GERUDO_MEMBERSHIP_CARD))
    ])
    # Connections
    connect_regions(Regions.GF_OUTSIDE_GTG, world, [
        (Regions.GF_TO_GTG,
         lambda bundle: has_item(Events.GTG_GATE_OPEN, bundle) & (is_adult(bundle) | False_())),
        (Regions.GF_JAIL_WINDOW,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
        (Regions.GF_OUTSKIRTS,
         lambda bundle: True_()),
        (Regions.GF_NEAR_GROTTO,
         lambda bundle: is_child(bundle) | can_pass_enemy(bundle, Enemies.GERUDO_GUARD)),
        (Regions.GF_ABOVE_GTG,
         lambda bundle: is_child(bundle) | can_pass_enemy(bundle, Enemies.GERUDO_GUARD)),
        (Regions.GF_TOP_OF_UPPER_VINES,
         lambda bundle: has_item(Items.GERUDO_MEMBERSHIP_CARD, bundle) & can_use(Items.LONGSHOT, bundle)),
        (Regions.GF_HBA_RANGE,
         lambda bundle: is_child(bundle) | has_item(Items.GERUDO_MEMBERSHIP_CARD, bundle)),
    ])

    # GF to GTG  (upstream RR_GF_TO_GTG, SCENE_GERUDOS_FORTRESS)
    # Connections
    connect_regions(Regions.GF_TO_GTG, world, [
        (Regions.GERUDO_TRAINING_GROUND_ENTRYWAY,
         lambda bundle: True_()),
    ])

    # GF Exiting GTG  (upstream RR_GF_EXITING_GTG, SCENE_GERUDOS_FORTRESS)
    # Connections
    connect_regions(Regions.GF_EXITING_GTG, world, [
        (Regions.GF_OUTSIDE_GTG,
         lambda bundle: is_child(bundle) | has_item(Items.GERUDO_MEMBERSHIP_CARD, bundle)),
        (Regions.GF_JAIL_WINDOW,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
        (Regions.GF_OUTSKIRTS,
         lambda bundle: True_()),
    ])

    # GF Above GTG  (upstream RR_GF_ABOVE_GTG, SCENE_GERUDOS_FORTRESS)
    # Connections
    connect_regions(Regions.GF_ABOVE_GTG, world, [
        (Regions.TH_DOUBLE_CELL,
         lambda bundle: True_()),
        (Regions.TH_KITCHEN_CORRIDOR,
         lambda bundle: True_()),
        (Regions.GF_JAIL_WINDOW,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
        (Regions.GF_OUTSKIRTS,
         lambda bundle: True_()),
        (Regions.GF_NEAR_GROTTO,
         lambda bundle: True_()),
        (Regions.GF_OUTSIDE_GTG,
         lambda bundle: is_child(bundle) | can_pass_enemy(bundle, Enemies.GERUDO_GUARD)),
        (Regions.GF_BOTTOM_OF_LOWER_VINES,
         lambda bundle: can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle)),
    ])

    # GF Bottom of Lower Vines  (upstream RR_GF_BOTTOM_OF_LOWER_VINES, SCENE_GERUDOS_FORTRESS)
    # Connections
    connect_regions(Regions.GF_BOTTOM_OF_LOWER_VINES, world, [
        (Regions.TH_STEEP_SLOPE_CELL,
         lambda bundle: True_()),
        (Regions.GF_NEAR_GROTTO,
         lambda bundle: True_()),
        (Regions.GF_TOP_OF_LOWER_VINES,
         lambda bundle: has_climb(bundle) | can_use(Items.HOOKSHOT, bundle)),
        (Regions.GF_ABOVE_GTG,
         lambda bundle: True_()),
        (Regions.GF_BELOW_GS,
         lambda bundle: is_adult(bundle) & can_ground_jump(bundle)),
    ])

    # GF Top of Lower Vines  (upstream RR_GF_TOP_OF_LOWER_VINES, SCENE_GERUDOS_FORTRESS)
    # Connections
    connect_regions(Regions.GF_TOP_OF_LOWER_VINES, world, [
        (Regions.TH_KITCHEN_BY_CORRIDOR,
         lambda bundle: True_()),
        (Regions.TH_DOUBLE_CELL,
         lambda bundle: True_()),
        (Regions.GF_ABOVE_GTG,
         lambda bundle: True_()),
        (Regions.GF_BOTTOM_OF_LOWER_VINES,
         lambda bundle: True_()),
        (Regions.GF_BOTTOM_OF_UPPER_VINES,
         lambda bundle: is_adult(bundle) & can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle)),
        (Regions.GF_BELOW_GS,
         lambda bundle: bunny_hovers(bundle)),
    ])

    # GF Near GS  (upstream RR_GF_NEAR_GS, SCENE_GERUDOS_FORTRESS)
    # Locations
    add_locations(Regions.GF_NEAR_GS, world, [
        (Locations.GF_GS_TOP_FLOOR,
         lambda bundle: is_adult(bundle) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOMB_THROW) & can_get_nighttime_gs(bundle)),
    ])
    # Connections
    connect_regions(Regions.GF_NEAR_GS, world, [
        (Regions.TH_KITCHEN_OPPOSITE_CORRIDOR,
         lambda bundle: True_()),
        (Regions.GF_BOTTOM_OF_LOWER_VINES,
         lambda bundle: True_()),
        (Regions.GF_TOP_OF_LOWER_VINES,
         lambda bundle: True_()),
        (Regions.GF_SLOPED_ROOF,
         lambda bundle: is_adult(bundle) | can_ground_jump(bundle)),
        (Regions.GF_LONG_ROOF,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle) | (is_adult(bundle) & bunny_hood(bundle))),
        (Regions.GF_NEAR_CHEST,
         lambda bundle: can_use(Items.LONGSHOT, bundle)),
        (Regions.GF_BELOW_GS,
         lambda bundle: True_()),
    ])

    # GF Sloped Roof  (upstream RR_GF_SLOPED_ROOF, SCENE_GERUDOS_FORTRESS)
    # Connections
    connect_regions(Regions.GF_SLOPED_ROOF, world, [
        (Regions.GF_TOP_OF_LOWER_VINES,
         lambda bundle: True_()),
        (Regions.GF_NEAR_GS,
         lambda bundle: True_()),
        (Regions.GF_BOTTOM_OF_UPPER_VINES,
         lambda bundle: True_()),
        (Regions.GF_TOP_OF_UPPER_VINES,
         lambda bundle: is_adult(bundle) & can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle)),
    ])

    # GF Bottom of Upper Vines  (upstream RR_GF_BOTTOM_OF_UPPER_VINES, SCENE_GERUDOS_FORTRESS)
    # Connections
    connect_regions(Regions.GF_BOTTOM_OF_UPPER_VINES, world, [
        (Regions.GF_OUTSIDE_GTG,
         lambda bundle: True_()),
        (Regions.GF_TOP_OF_LOWER_VINES,
         lambda bundle: True_()),
        (Regions.GF_SLOPED_ROOF,
         lambda bundle: is_adult(bundle) & (can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle) | (can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle)))),
        (Regions.GF_TOP_OF_UPPER_VINES,
         lambda bundle: has_climb(bundle) | can_use(Items.HOOKSHOT, bundle)),
        (Regions.GF_TO_GTG,
         lambda bundle: is_adult(bundle) & can_do_trick(Tricks.GF_LEDGE_CLIP_INTO_GTG, bundle)),
    ])

    # GF Top of Upper Vines  (upstream RR_GF_TOP_OF_UPPER_VINES, SCENE_GERUDOS_FORTRESS)
    # Locations
    add_locations(Regions.GF_TOP_OF_UPPER_VINES, world, [
        (Locations.GF_GS_TOP_FLOOR,
         lambda bundle: is_adult(bundle) & can_get_nighttime_gs(bundle) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.SHORT_JUMPSLASH) & (has_climb(bundle) | can_use(Items.HOOKSHOT, bundle) | can_use(Items.BOOMERANG, bundle) | can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle))),
    ])
    # Connections
    connect_regions(Regions.GF_TOP_OF_UPPER_VINES, world, [
        (Regions.GF_TOP_OF_LOWER_VINES,
         lambda bundle: True_()),
        (Regions.GF_SLOPED_ROOF,
         lambda bundle: True_()),
        (Regions.GF_BOTTOM_OF_UPPER_VINES,
         lambda bundle: True_()),
        (Regions.GF_NEAR_CHEST,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle) | (is_adult(bundle) & (reach_scarecrow(bundle) | bunny_hood(bundle))) | can_use(Items.LONGSHOT, bundle)),
    ])

    # GF Near Chest  (upstream RR_GF_NEAR_CHEST, SCENE_GERUDOS_FORTRESS)
    # Locations
    add_locations(Regions.GF_NEAR_CHEST, world, [
        (Locations.GF_CHEST,
         lambda bundle: can_open_large_chest(bundle)),
        (Locations.GF_GS_TOP_FLOOR,
         lambda bundle: is_adult(bundle) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG) & can_get_nighttime_gs(bundle)),
    ])
    # Connections
    connect_regions(Regions.GF_NEAR_CHEST, world, [
        (Regions.GF_NEAR_GS,
         lambda bundle: True_()),
        (Regions.GF_LONG_ROOF,
         lambda bundle: True_()),
    ])

    # GF Long Roof  (upstream RR_GF_LONG_ROOF, SCENE_GERUDOS_FORTRESS)
    # Connections
    connect_regions(Regions.GF_LONG_ROOF, world, [
        (Regions.GF_BOTTOM_OF_LOWER_VINES,
         lambda bundle: True_()),
        (Regions.GF_NEAR_GS,
         lambda bundle: (is_adult(bundle) & (can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) | bunny_hood(bundle))) | can_use(Items.HOVER_BOOTS, bundle)),
        (Regions.GF_BELOW_GS,
         lambda bundle: True_()),
        (Regions.GF_NEAR_CHEST,
         lambda bundle: can_use(Items.LONGSHOT, bundle)),
        (Regions.GF_BELOW_CHEST,
         lambda bundle: True_()),
    ])

    # GF Below GS  (upstream RR_GF_BELOW_GS, SCENE_GERUDOS_FORTRESS)
    # Locations
    add_locations(Regions.GF_BELOW_GS, world, [
        (Locations.GF_GS_TOP_FLOOR,
         lambda bundle: is_adult(bundle) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.LONGSHOT) & can_get_nighttime_gs(bundle)),
    ])
    # Connections
    connect_regions(Regions.GF_BELOW_GS, world, [
        (Regions.TH_DEAD_END_CELL,
         lambda bundle: True_()),
        (Regions.GF_BOTTOM_OF_LOWER_VINES,
         lambda bundle: True_()),
    ])

    # GF Below Chest  (upstream RR_GF_BELOW_CHEST, SCENE_GERUDOS_FORTRESS)
    # Connections
    connect_regions(Regions.GF_BELOW_CHEST, world, [
        (Regions.TH_BREAK_ROOM,
         lambda bundle: True_()),
        (Regions.GF_OUTSKIRTS,
         lambda bundle: True_()),
    ])

    # Gerudo Fortress Tower  (upstream RR_GF_TOWER, SCENE_GERUDOS_FORTRESS)
    # Events
    add_events(Regions.GF_TOWER, world, [
        (EventLocations.GF_TOWER_GF_GATE_OPEN, Events.GF_GATE_OPEN,
         lambda bundle: is_adult(bundle) & has_speak(bundle, "GERUDO")),
    ])
    # Connections
    connect_regions(Regions.GF_TOWER, world, [
        (Regions.GF_OUTSKIRTS,
         lambda bundle: True_()),
        (Regions.GF_OUTSIDE_GATE,
         lambda bundle: (is_adult(bundle) & can_ground_jump(bundle)) | can_do_trick(Tricks.GF_WASTELAND_GATE_SIDEHOP_SKIP, bundle)),
    ])

    # GF Above Jail  (upstream RR_GF_ABOVE_JAIL, SCENE_GERUDOS_FORTRESS)
    # Locations
    add_locations(Regions.GF_ABOVE_JAIL, world, [
        (Locations.GF_ABOVE_JAIL_CRATE,
         lambda bundle: is_adult(bundle)),
    ])
    # Connections
    connect_regions(Regions.GF_ABOVE_JAIL, world, [
        (Regions.GF_OUTSKIRTS,
         lambda bundle: True_()),
        (Regions.GF_NEAR_CHEST,
         lambda bundle: can_use(Items.LONGSHOT, bundle)),
        (Regions.GF_BELOW_CHEST,
         lambda bundle: take_damage(bundle)),
        (Regions.GF_JAIL_WINDOW,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
        (Regions.TH_BREAK_ROOM_UPPER_CORRIDOR,
         lambda bundle: True_()),
        (Regions.GF_TOWER,
         lambda bundle: can_do_trick(Tricks.GF_ADULT_SKIP_WASTELAND_GATE, bundle) & is_adult(bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_jump_slash(bundle) & has_item(Items.GERUDO_MEMBERSHIP_CARD, bundle)),
        (Regions.GF_OUTSIDE_GATE,
         lambda bundle: can_do_trick(Tricks.GF_ADULT_SKIP_WASTELAND_GATE, bundle) & is_adult(bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_jump_slash(bundle)),
    ])

    # GF Jail Window  (upstream RR_GF_JAIL_WINDOW, SCENE_GERUDOS_FORTRESS)
    # Connections
    connect_regions(Regions.GF_JAIL_WINDOW, world, [
        (Regions.GF_LONG_ROOF,
         lambda bundle: can_recoil_hover(bundle, Recoil.HAMMER)),
        (Regions.GF_OUTSKIRTS,
         lambda bundle: True_()),
        (Regions.GF_BELOW_CHEST,
         lambda bundle: True_()),
        (Regions.GF_ABOVE_JAIL,
         lambda bundle: can_do_trick(Tricks.HOOKSHOT_CLIP, bundle) & can_use(Items.HOOKSHOT, bundle)),
    ])

    # GF HBA Range  (upstream RR_GF_HBA_RANGE, SCENE_GERUDOS_FORTRESS)
    # Locations
    add_locations(Regions.GF_HBA_RANGE, world, [
        (Locations.GF_HBA_1000_POINTS,
         lambda bundle: is_adult(bundle) & has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "GERUDO") & has_item(Items.GERUDO_MEMBERSHIP_CARD, bundle) & summon_epona(bundle) & can_use(Items.FAIRY_BOW, bundle) & at_day(bundle)),
        (Locations.GF_HBA_1500_POINTS,
         lambda bundle: is_adult(bundle) & has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "GERUDO") & has_item(Items.GERUDO_MEMBERSHIP_CARD, bundle) & summon_epona(bundle) & can_use(Items.FAIRY_BOW, bundle) & at_day(bundle)),
        (Locations.GF_GS_ARCHERY_RANGE,
         lambda bundle: is_adult(bundle) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG) & can_get_nighttime_gs(bundle)),
        (Locations.GF_HBA_RANGE_CRATE_1,
         lambda bundle: can_break_crates(bundle)),
        (Locations.GF_HBA_RANGE_CRATE_2,
         lambda bundle: can_break_crates(bundle)),
        (Locations.GF_HBA_RANGE_CRATE_3,
         lambda bundle: can_break_crates(bundle)),
        (Locations.GF_HBA_RANGE_CRATE_4,
         lambda bundle: can_break_crates(bundle)),
        (Locations.GF_HBA_RANGE_CRATE_5,
         lambda bundle: can_break_crates(bundle)),
        (Locations.GF_HBA_RANGE_CRATE_6,
         lambda bundle: can_break_crates(bundle)),
        (Locations.GF_HBA_RANGE_CRATE_7,
         lambda bundle: can_break_crates(bundle)),
        (Locations.GF_HBA_CANOPY_EAST_CRATE,
         lambda bundle: can_break_crates(bundle)),
        (Locations.GF_HBA_CANOPY_WEST_CRATE,
         lambda bundle: can_break_crates(bundle)),
        (Locations.GF_NORTH_TARGET_EAST_CRATE,
         lambda bundle: can_break_crates(bundle)),
        (Locations.GF_NORTH_TARGET_WEST_CRATE,
         lambda bundle: is_adult(bundle) | (blast_or_smash(bundle) | hookshot_or_boomerang(bundle) | can_use(Items.HOVER_BOOTS, bundle))),
        (Locations.GF_NORTH_TARGET_CHILD_CRATE,
         lambda bundle: is_child(bundle) & blast_or_smash(bundle)),
        (Locations.GF_SOUTH_TARGET_EAST_CRATE,
         lambda bundle: can_break_crates(bundle)),
        (Locations.GF_SOUTH_TARGET_WEST_CRATE,
         lambda bundle: can_break_crates(bundle)),
        # DEFERRED RC_GF_HBA_RECTANGLE_SIGN: logic->IsAdult && logic->CanRead()
        # DEFERRED RC_GF_WONDER_ARCHERY_SIGN: logic->CanUse(RG_HOOKSHOT)
    ])
    # Connections
    connect_regions(Regions.GF_HBA_RANGE, world, [
        (Regions.GF_OUTSIDE_GTG,
         lambda bundle: is_child(bundle) | has_item(Items.GERUDO_MEMBERSHIP_CARD, bundle)),
    ])

    # GF Outside Gate  (upstream RR_GF_OUTSIDE_GATE, SCENE_GERUDOS_FORTRESS)
    # Events
    add_events(Regions.GF_OUTSIDE_GATE, world, [
        (EventLocations.GF_OUTSIDE_GATE_GF_GATE_OPEN, Events.GF_GATE_OPEN,
         lambda bundle: is_adult(bundle) & has_item(Items.GERUDO_MEMBERSHIP_CARD, bundle) & has_speak(bundle, "GERUDO")),
    ])
    # Locations
    add_locations(Regions.GF_OUTSIDE_GATE, world, [
        # DEFERRED RC_GF_GATE_EXIT_RECTANGLE_SIGN: logic->IsAdult && logic->CanRead()
        # DEFERRED RC_GF_FAR_AWAY_CRATE_CHILD: logic->IsChild && false
        # DEFERRED RC_GF_FAR_AWAY_CRATE_ADULT: logic->IsAdult && false
    ])
    # Connections
    connect_regions(Regions.GF_OUTSIDE_GATE, world, [
        (Regions.GF_OUTSKIRTS,
         lambda bundle: has_item(Events.GF_GATE_OPEN, bundle)),
        (Regions.WASTELAND_NEAR_FORTRESS,
         lambda bundle: True_()),
    ])

    # GF Storms Grotto  (upstream RR_GF_STORMS_GROTTO, SCENE_GROTTOS)
    # Events
    add_events(Regions.GF_STORMS_GROTTO, world, [
        (EventLocations.GF_STORMS_GROTTO_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: True_()),
    ])
    # Locations
    add_locations(Regions.GF_STORMS_GROTTO, world, [
        (Locations.GF_FAIRY_GROTTO_FAIRY1,
         lambda bundle: True_()),
        (Locations.GF_FAIRY_GROTTO_FAIRY2,
         lambda bundle: True_()),
        (Locations.GF_FAIRY_GROTTO_FAIRY3,
         lambda bundle: True_()),
        (Locations.GF_FAIRY_GROTTO_FAIRY4,
         lambda bundle: True_()),
        (Locations.GF_FAIRY_GROTTO_FAIRY5,
         lambda bundle: True_()),
        (Locations.GF_FAIRY_GROTTO_FAIRY6,
         lambda bundle: True_()),
        (Locations.GF_FAIRY_GROTTO_FAIRY7,
         lambda bundle: True_()),
        (Locations.GF_FAIRY_GROTTO_FAIRY8,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.GF_STORMS_GROTTO, world, [
        (Regions.GF_NEAR_GROTTO,
         lambda bundle: True_()),
    ])

# ---- summary
# notes: ['TODO feature 4.1']
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_FAIRIES', 'GF_GATE_OPEN', 'GTG_GATE_OPEN']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (8): ['RC_GF_EAST_EXIT_ARROW_SIGN', 'RC_GF_WONDER_ENTRANCE_SIGN', 'RC_GF_GTG_ENTRANCE_RECTANGLE_SIGN', 'RC_GF_HBA_RECTANGLE_SIGN', 'RC_GF_WONDER_ARCHERY_SIGN', 'RC_GF_GATE_EXIT_RECTANGLE_SIGN', 'RC_GF_FAR_AWAY_CRATE_CHILD', 'RC_GF_FAR_AWAY_CRATE_ADULT']
