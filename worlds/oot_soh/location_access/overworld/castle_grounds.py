"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/castle_grounds.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    HC_GATE_CHILD_CAN_PASS_TIME = "Hyrule Castle Gate Child Can Pass Time"
    HC_GATE_ADULT_CAN_PASS_TIME = "Hyrule Castle Gate Adult Can Pass Time"
    HC_GATE_FAIRY_ACCESS = "Hyrule Castle Gate Fairy Access"
    HC_GATE_BUG_ACCESS = "Hyrule Castle Gate Bug Access"
    HC_GATE_MALON_RETURNED_FROM_CASTLE = "Hyrule Castle Gate Malon Returned From Castle"
    HC_ABOVE_VINE_CHILD_CAN_PASS_TIME = "Hyrule Castle Above Vine Child Can Pass Time"
    HC_ABOVE_VINE_ADULT_CAN_PASS_TIME = "Hyrule Castle Above Vine Adult Can Pass Time"
    HC_ABOVE_VINE_FAIRY_ACCESS = "Hyrule Castle Above Vine Fairy Access"
    HC_PAST_GATE_CHILD_CAN_PASS_TIME = "Hyrule Castle Past Gate Child Can Pass Time"
    HC_PAST_GATE_ADULT_CAN_PASS_TIME = "Hyrule Castle Past Gate Adult Can Pass Time"
    HC_PAST_GATE_FAIRY_ACCESS = "Hyrule Castle Past Gate Fairy Access"
    HC_ABOVE_CLIMBABLE_ROCKS_CHILD_CAN_PASS_TIME = "Hyrule Castle Above Climbable Rocks Child Can Pass Time"
    HC_ABOVE_CLIMBABLE_ROCKS_ADULT_CAN_PASS_TIME = "Hyrule Castle Above Climbable Rocks Adult Can Pass Time"
    HC_ABOVE_CLIMBABLE_ROCKS_FAIRY_ACCESS = "Hyrule Castle Above Climbable Rocks Fairy Access"
    HC_MOAT_CHILD_CAN_PASS_TIME = "Hyrule Castle Moat Child Can Pass Time"
    HC_MOAT_ADULT_CAN_PASS_TIME = "Hyrule Castle Moat Adult Can Pass Time"
    HC_MOAT_TALON_RETURNED_FROM_CASTLE = "Hyrule Castle Moat Talon Returned From Castle"
    HC_DRAIN_LEDGE_CHILD_CAN_PASS_TIME = "Hyrule Castle Drain Ledge Child Can Pass Time"
    HC_DRAIN_LEDGE_ADULT_CAN_PASS_TIME = "Hyrule Castle Drain Ledge Adult Can Pass Time"
    HC_GARDEN_MET_ZELDA = "HC Garden Met Zelda"
    HC_STORMS_GROTTO_BEHIND_WALLS_NUT_ACCESS = "HC Storms Grotto Behind Walls Nut Access"
    HC_STORMS_GROTTO_BEHIND_WALLS_FAIRY_ACCESS = "HC Storms Grotto Behind Walls Fairy Access"
    HC_STORMS_GROTTO_BEHIND_WALLS_BUG_ACCESS = "HC Storms Grotto Behind Walls Bug Access"
    GANONS_CASTLE_GROUNDS_BUILD_RAINBOW_BRIDGE = "Ganon's Castle Grounds Build Rainbow Bridge"


def set_region_rules(world: "SohWorld") -> None:

    # Castle Grounds  (upstream RR_CASTLE_GROUNDS, SCENE_OUTSIDE_GANONS_CASTLE)
    # Connections
    connect_regions(Regions.CASTLE_GROUNDS, world, [
        (Regions.THE_MARKET,
         lambda bundle: True_()),
        (Regions.HC_GATE,
         lambda bundle: is_child(bundle)),
        (Regions.GANONS_CASTLE_GROUNDS,
         lambda bundle: is_adult(bundle)),
    ])

    # Castle Grounds From Great Fairy  (upstream RR_CASTLE_GROUNDS_FROM_GREAT_FAIRY, SCENE_OUTSIDE_GANONS_CASTLE)
    # Connections
    connect_regions(Regions.CASTLE_GROUNDS_FROM_GREAT_FAIRY, world, [
        (Regions.HC_PAST_GATE,
         lambda bundle: is_child(bundle)),
        (Regions.GANONS_CASTLE_GROUNDS,
         lambda bundle: is_adult(bundle)),
    ])

    # Hyrule Castle Gate  (upstream RR_HC_GATE, SCENE_HYRULE_CASTLE)
    # Events
    add_events(Regions.HC_GATE, world, [
        (EventLocations.HC_GATE_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.HC_GATE_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
        (EventLocations.HC_GATE_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy(bundle) | can_use(Items.STICKS, bundle)),
        (EventLocations.HC_GATE_BUG_ACCESS, Events.CAN_ACCESS_BUGS,
         lambda bundle: has_grab(bundle)),
        (EventLocations.HC_GATE_MALON_RETURNED_FROM_CASTLE, Events.MALON_RETURNED_FROM_CASTLE,
         lambda bundle: has_item(Events.TALON_RETURNED_FROM_CASTLE, bundle) & has_speak(bundle, "HYLIAN")),
    ])
    # Locations
    add_locations(Regions.HC_GATE, world, [
        (Locations.HC_MALON_EGG,
         lambda bundle: has_speak(bundle, "HYLIAN")),
        (Locations.HC_ROCK_1,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.HC_ROCK_2,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.HC_ROCK_3,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.HC_GS_TREE,
         lambda bundle: can_bonk_trees(bundle) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.CLOSE)),
        (Locations.HC_SKULLTULA_TREE,
         lambda bundle: can_bonk_trees(bundle)),
    ])
    # Connections
    connect_regions(Regions.HC_GATE, world, [
        (Regions.CASTLE_GROUNDS,
         lambda bundle: True_()),
        (Regions.HC_ABOVE_VINE,
         lambda bundle: has_climb(bundle) | can_use(Items.HOOKSHOT, bundle)),
        (Regions.HC_PAST_GATE,
         lambda bundle: has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "HYLIAN")),
    ])

    # Hyrule Castle Above Vine  (upstream RR_HC_ABOVE_VINE, SCENE_HYRULE_CASTLE)
    # Events
    add_events(Regions.HC_ABOVE_VINE, world, [
        (EventLocations.HC_ABOVE_VINE_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.HC_ABOVE_VINE_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
        (EventLocations.HC_ABOVE_VINE_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy(bundle)),
    ])
    # Locations
    add_locations(Regions.HC_ABOVE_VINE, world, [
        (Locations.HC_MALON_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.HC_MALON_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_HC_MALON_GOSSIP_STONE: true
    ])
    # Connections
    connect_regions(Regions.HC_ABOVE_VINE, world, [
        (Regions.HC_GATE,
         lambda bundle: True_()),
        (Regions.HC_PAST_GATE,
         lambda bundle: True_()),
    ])

    # Hyrule Castle Past Gate  (upstream RR_HC_PAST_GATE, SCENE_HYRULE_CASTLE)
    # Events
    add_events(Regions.HC_PAST_GATE, world, [
        (EventLocations.HC_PAST_GATE_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.HC_PAST_GATE_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
        (EventLocations.HC_PAST_GATE_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: can_use(Items.STICKS, bundle)),
    ])
    # Locations
    add_locations(Regions.HC_PAST_GATE, world, [
        (Locations.HC_BOULDER,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.HC_NEAR_GUARDS_TREE_1,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HC_NEAR_GUARDS_TREE_2,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HC_NEAR_GUARDS_TREE_3,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HC_NEAR_GUARDS_TREE_4,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HC_NEAR_GUARDS_TREE_5,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HC_NEAR_GUARDS_TREE_6,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HC_NL_TREE_1,
         lambda bundle: False_()),
        (Locations.HC_NL_TREE_2,
         lambda bundle: False_()),
        (Locations.HC_NEAR_WALL_BUTTERFLY_FAIRY,
         lambda bundle: can_use(Items.STICKS, bundle)),
        (Locations.HC_NEAR_STAIRS_BUTTERFLY_FAIRY,
         lambda bundle: can_use(Items.STICKS, bundle)),
        (Locations.HC_NEAR_BOULDER_PATH_BUTTERFLY_FAIRY,
         lambda bundle: can_use(Items.STICKS, bundle)),
        (Locations.HC_NEAR_ARCHWAY_BUTTERFLY_FAIRY,
         lambda bundle: can_use(Items.STICKS, bundle)),
        (Locations.HC_DEAD_END_RECTANGLE_SIGN,
         lambda bundle: can_read(bundle)),
    ])
    # Connections
    connect_regions(Regions.HC_PAST_GATE, world, [
        (Regions.HC_GATE,
         lambda bundle: True_()),
        (Regions.HC_ABOVE_VINE,
         lambda bundle: has_climb(bundle) | can_use(Items.HOOKSHOT, bundle)),
        (Regions.HC_ABOVE_CLIMBABLE_ROCKS,
         lambda bundle: has_climb(bundle) | can_use(Items.HOOKSHOT, bundle)),
        (Regions.HC_GREAT_FAIRY_FOUNTAIN,
         lambda bundle: blast_or_smash(bundle) & has_crawl(bundle)),
    ])

    # Hyrule Castle Above Climbable Rocks  (upstream RR_HC_ABOVE_CLIMBABLE_ROCKS, SCENE_HYRULE_CASTLE)
    # Events
    add_events(Regions.HC_ABOVE_CLIMBABLE_ROCKS, world, [
        (EventLocations.HC_ABOVE_CLIMBABLE_ROCKS_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.HC_ABOVE_CLIMBABLE_ROCKS_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
        (EventLocations.HC_ABOVE_CLIMBABLE_ROCKS_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy(bundle)),
    ])
    # Locations
    add_locations(Regions.HC_ABOVE_CLIMBABLE_ROCKS, world, [
        # DEFERRED RC_HC_ROCK_WALL_GOSSIP_STONE: true
        (Locations.HC_ROCK_WALL_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.HC_ROCK_WALL_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
    ])
    # Connections
    connect_regions(Regions.HC_ABOVE_CLIMBABLE_ROCKS, world, [
        (Regions.HC_PAST_GATE,
         lambda bundle: True_()),
        (Regions.HC_MOAT,
         lambda bundle: True_()),
    ])

    # Hyrule Castle Moat  (upstream RR_HC_MOAT, SCENE_HYRULE_CASTLE)
    # Events
    add_events(Regions.HC_MOAT, world, [
        (EventLocations.HC_MOAT_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.HC_MOAT_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
        (EventLocations.HC_MOAT_TALON_RETURNED_FROM_CASTLE, Events.TALON_RETURNED_FROM_CASTLE,
         lambda bundle: can_use(Items.WEIRD_EGG, bundle) & has_speak(bundle, "HYLIAN")),
    ])
    # Locations
    add_locations(Regions.HC_MOAT, world, [
        (Locations.HC_NEAR_STORMS_GROTTO_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.HC_NEAR_STORMS_GROTTO_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.HC_GROTTO_TREE,
         lambda bundle: can_bonk_trees(bundle)),
        (Locations.HC_WONDER_LEFT_TORCH,
         lambda bundle: can_use(Items.FAIRY_SLINGSHOT, bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.BOOMERANG, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.HC_WONDER_RIGHT_TORCH,
         lambda bundle: can_use(Items.FAIRY_SLINGSHOT, bundle) & (has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.BOOMERANG, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.HC_WONDER_MOAT_1,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle))),
        (Locations.HC_WONDER_MOAT_2,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle))),
        (Locations.HC_WONDER_MOAT_3,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle))),
        (Locations.HC_WONDER_MOAT_4,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle))),
        (Locations.HC_WONDER_MOAT_5,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle))),
        (Locations.HC_WONDER_MOAT_6,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle))),
        (Locations.HC_WONDER_MOAT_7,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle))),
        (Locations.HC_WONDER_MOAT_8,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle))),
        (Locations.HC_WONDER_MOAT_9,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle))),
        (Locations.HC_WONDER_MOAT_10,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle))),
    ])
    # Connections
    connect_regions(Regions.HC_MOAT, world, [
        (Regions.HC_GATE,
         lambda bundle: True_()),
        (Regions.HC_STORMS_GROTTO,
         lambda bundle: can_open_storms_grotto(bundle)),
        (Regions.HC_DRAIN_LEDGE,
         lambda bundle: (has_item(Events.TALON_RETURNED_FROM_CASTLE, bundle) & has_grab(bundle)) | can_use(Items.HOVER_BOOTS, bundle) | (can_do_trick(Tricks.DAMAGE_BOOST_SIMPLE, bundle) & take_damage(bundle) & has_explosives(bundle) & can_jump_slash(bundle))),
    ])

    # Hyrule Castle Drain Ledge  (upstream RR_HC_DRAIN_LEDGE, SCENE_HYRULE_CASTLE)
    # Events
    add_events(Regions.HC_DRAIN_LEDGE, world, [
        (EventLocations.HC_DRAIN_LEDGE_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.HC_DRAIN_LEDGE_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
    ])
    # Connections
    connect_regions(Regions.HC_DRAIN_LEDGE, world, [
        (Regions.HC_MOAT,
         lambda bundle: True_()),
        (Regions.HC_GARDEN,
         lambda bundle: has_crawl(bundle)),
    ])

    # HC Garden  (upstream RR_HC_GARDEN, SCENE_CASTLE_COURTYARD_ZELDA)
    # Events
    add_events(Regions.HC_GARDEN, world, [
        (EventLocations.HC_GARDEN_MET_ZELDA, Events.MET_ZELDA,
         lambda bundle: has_speak(bundle, "HYLIAN")),
    ])
    # Locations
    add_locations(Regions.HC_GARDEN, world, [
        (Locations.HC_ZELDAS_LETTER,
         lambda bundle: has_item(Events.MET_ZELDA, bundle)),
        (Locations.SONG_FROM_IMPA,
         lambda bundle: has_item(Events.MET_ZELDA, bundle)),
        (Locations.HC_WONDER_COURTYARD_RIGHT_WINDOW,
         lambda bundle: can_use(Items.FAIRY_SLINGSHOT, bundle)),
        (Locations.HC_WONDER_COURTYARD_LEFT_WINDOW,
         lambda bundle: can_use(Items.FAIRY_SLINGSHOT, bundle)),
    ])
    # Connections
    connect_regions(Regions.HC_GARDEN, world, [
        (Regions.HC_DRAIN_LEDGE,
         lambda bundle: True_()),
    ])

    # HC Great Fairy Fountain  (upstream RR_HC_GREAT_FAIRY_FOUNTAIN, SCENE_GREAT_FAIRYS_FOUNTAIN_SPELLS)
    # Locations
    add_locations(Regions.HC_GREAT_FAIRY_FOUNTAIN, world, [
        (Locations.HC_GREAT_FAIRY_REWARD,
         lambda bundle: can_use(Items.ZELDAS_LULLABY, bundle)),
    ])
    # Connections
    connect_regions(Regions.HC_GREAT_FAIRY_FOUNTAIN, world, [
        (Regions.CASTLE_GROUNDS_FROM_GREAT_FAIRY,
         lambda bundle: True_()),
    ])

    # HC Storms Grotto  (upstream RR_HC_STORMS_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.HC_STORMS_GROTTO, world, [
        (Locations.HC_GS_STORMS_GROTTO,
         lambda bundle: can_use(Items.BOOMERANG, bundle) & can_do_trick(Tricks.HC_STORMS_GS, bundle)),
    ])
    # Connections
    connect_regions(Regions.HC_STORMS_GROTTO, world, [
        (Regions.CASTLE_GROUNDS_FROM_GROTTO,
         lambda bundle: True_()),
        (Regions.HC_STORMS_GROTTO_BEHIND_WALLS,
         lambda bundle: can_break_mud_walls(bundle)),
    ])

    # HC Storms Grotto Behind Walls  (upstream RR_HC_STORMS_GROTTO_BEHIND_WALLS, SCENE_GROTTOS)
    # Events
    add_events(Regions.HC_STORMS_GROTTO_BEHIND_WALLS, world, [
        (EventLocations.HC_STORMS_GROTTO_BEHIND_WALLS_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_break_pots(bundle)),
        (EventLocations.HC_STORMS_GROTTO_BEHIND_WALLS_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy(bundle)),
        (EventLocations.HC_STORMS_GROTTO_BEHIND_WALLS_BUG_ACCESS, Events.CAN_ACCESS_BUGS,
         lambda bundle: True_()),
    ])
    # Locations
    add_locations(Regions.HC_STORMS_GROTTO_BEHIND_WALLS, world, [
        (Locations.HC_GS_STORMS_GROTTO,
         lambda bundle: hookshot_or_boomerang(bundle)),
        (Locations.HC_STORMS_GROTTO_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.HC_STORMS_GROTTO_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_HC_STORMS_GROTTO_GOSSIP_STONE: true
        (Locations.HC_STORMS_GROTTO_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.HC_STORMS_GROTTO_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.HC_STORMS_GROTTO_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.HC_STORMS_GROTTO_POT4,
         lambda bundle: can_break_pots(bundle)),
        (Locations.HC_STORMS_GROTTO_ROCK_1,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.HC_STORMS_GROTTO_ROCK_2,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.HC_STORMS_GROTTO_ROCK_3,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.HC_STORMS_GROTTO_ROCK_4,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.HC_STORMS_GROTTO_ROCK_5,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.HC_STORMS_GROTTO_ROCK_6,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.HC_STORMS_GROTTO_ROCK_7,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.HC_STORMS_GROTTO_ROCK_8,
         lambda bundle: can_break_rocks(bundle)),
    ])
    # Connections
    connect_regions(Regions.HC_STORMS_GROTTO_BEHIND_WALLS, world, [
        (Regions.HC_STORMS_GROTTO,
         lambda bundle: True_()),
    ])

    # Castle Grounds From Grotto  (upstream RR_CASTLE_GROUNDS_FROM_GROTTO, SCENE_OUTSIDE_GANONS_CASTLE)
    # Connections
    connect_regions(Regions.CASTLE_GROUNDS_FROM_GROTTO, world, [
        (Regions.HC_MOAT,
         lambda bundle: is_child(bundle)),
        (Regions.GANONS_CASTLE_GROUNDS,
         lambda bundle: is_adult(bundle)),
    ])

    # Ganon's Castle Grounds  (upstream RR_GANONS_CASTLE_GROUNDS, SCENE_OUTSIDE_GANONS_CASTLE)
    # Events
    add_events(Regions.GANONS_CASTLE_GROUNDS, world, [
        (EventLocations.GANONS_CASTLE_GROUNDS_BUILD_RAINBOW_BRIDGE, Events.BUILD_RAINBOW_BRIDGE,
         lambda bundle: can_build_rainbow_bridge(bundle)),
    ])
    # Locations
    add_locations(Regions.GANONS_CASTLE_GROUNDS, world, [
        (Locations.HC_OGC_GS,
         lambda bundle: hookshot_or_boomerang(bundle) | ((can_jump_slash_except_hammer(bundle) | can_use_projectile(bundle) | (can_shield(bundle) & can_use(Items.MEGATON_HAMMER, bundle)) | can_use(Items.DINS_FIRE, bundle)) & (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.OGC_BRONZE_BOULDER_1,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
        (Locations.OGC_BRONZE_BOULDER_2,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
        (Locations.OGC_BRONZE_BOULDER_3,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
        (Locations.OGC_SILVER_BOULDER_1,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.OGC_SILVER_BOULDER_2,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.OGC_SILVER_BOULDER_3,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Locations.OGC_SILVER_BOULDER_4,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_GROUNDS, world, [
        (Regions.CASTLE_GROUNDS,
         lambda bundle: at_night(bundle)),
        (Regions.OGC_GREAT_FAIRY_FOUNTAIN,
         lambda bundle: can_use(Items.GOLDEN_GAUNTLETS, bundle) & at_night(bundle)),
        (Regions.GANONS_CASTLE_LEDGE,
         lambda bundle: has_item(Events.BUILD_RAINBOW_BRIDGE, bundle)),
    ])

    # OGC Great Fairy Fountain  (upstream RR_OGC_GREAT_FAIRY_FOUNTAIN, SCENE_GREAT_FAIRYS_FOUNTAIN_MAGIC)
    # Locations
    add_locations(Regions.OGC_GREAT_FAIRY_FOUNTAIN, world, [
        (Locations.OGC_GREAT_FAIRY_REWARD,
         lambda bundle: can_use(Items.ZELDAS_LULLABY, bundle)),
    ])
    # Connections
    connect_regions(Regions.OGC_GREAT_FAIRY_FOUNTAIN, world, [
        (Regions.CASTLE_GROUNDS_FROM_GREAT_FAIRY,
         lambda bundle: True_()),
    ])

    # Castle Grounds From Ganon's Castle  (upstream RR_CASTLE_GROUNDS_FROM_GANONS_CASTLE, SCENE_OUTSIDE_GANONS_CASTLE)
    # Connections
    connect_regions(Regions.CASTLE_GROUNDS_FROM_GANONS_CASTLE, world, [
        (Regions.HC_DRAIN_LEDGE,
         lambda bundle: is_child(bundle)),
        (Regions.GANONS_CASTLE_LEDGE,
         lambda bundle: is_adult(bundle)),
    ])

    # Ganon's Castle Ledge  (upstream RR_GANONS_CASTLE_LEDGE, SCENE_OUTSIDE_GANONS_CASTLE)
    # Connections
    connect_regions(Regions.GANONS_CASTLE_LEDGE, world, [
        (Regions.GANONS_CASTLE_GROUNDS,
         lambda bundle: has_item(Events.BUILD_RAINBOW_BRIDGE, bundle)),
        (Regions.GANONS_CASTLE_ENTRYWAY,
         lambda bundle: is_adult(bundle)),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['BUILD_RAINBOW_BRIDGE', 'CAN_ACCESS_BUGS', 'CAN_ACCESS_FAIRIES', 'CAN_FARM_NUTS', 'MALON_RETURNED_FROM_CASTLE', 'MET_ZELDA', 'TALON_RETURNED_FROM_CASTLE']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (3): ['RC_HC_MALON_GOSSIP_STONE', 'RC_HC_ROCK_WALL_GOSSIP_STONE', 'RC_HC_STORMS_GROTTO_GOSSIP_STONE']
