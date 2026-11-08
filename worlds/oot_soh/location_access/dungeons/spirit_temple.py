"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/dungeons/spirit_temple.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    SPIRIT_TEMPLE_FOYER_FORWARDS_SPIRIT_CHILD = "Spirit Temple Foyer Forwards Spirit Child"
    SPIRIT_TEMPLE_FOYER_FORWARDS_SPIRIT_ADULT = "Spirit Temple Foyer Forwards Spirit Adult"
    SPIRIT_TEMPLE_CHILD_SIDE_HUB_NUT_ACCESS = "Spirit Temple Child Side Hub Nut Access"
    SPIRIT_TEMPLE_CHILD_SIDE_HUB_SPIRIT_SILVER_RUPEE_BRIDGE_TORCHES = "Spirit Temple Child Side Hub Spirit Silver Rupee Bridge Torches"
    SPIRIT_TEMPLE_SWITCH_BRIDGE_SOUTH_SPIRIT_CHILD_SWITCH_BRIDGE = "Spirit Temple Switch Bridge South Spirit Child Switch Bridge"
    SPIRIT_TEMPLE_SWITCH_BRIDGE_NORTH_SPIRIT_CHILD_SWITCH_BRIDGE = "Spirit Temple Switch Bridge North Spirit Child Switch Bridge"
    SPIRIT_TEMPLE_RUPEE_BRIDGE_NORTH_SPIRIT_SILVER_CHILD = "Spirit Temple Rupee Bridge North Spirit Silver Child"
    SPIRIT_TEMPLE_RUPEE_BRIDGE_NORTH_SPIRIT_SILVER_RUPEE_BRIDGE_TORCHES = "Spirit Temple Rupee Bridge North Spirit Silver Rupee Bridge Torches"
    SPIRIT_TEMPLE_RUPEE_BRIDGE_SOUTH_SPIRIT_SILVER_RUPEE_BRIDGE_TORCHES = "Spirit Temple Rupee Bridge South Spirit Silver Rupee Bridge Torches"
    SPIRIT_TEMPLE_ABOVE_BOULDERS_SPIRIT_SILVER_BOULDERS = "Spirit Temple Above Boulders Spirit Silver Boulders"
    SPIRIT_TEMPLE_SUN_BLOCK_CHEST_LEDGE_SPIRIT_SILVER_SUN = "Spirit Temple Sun Block Chest Ledge Spirit Silver Sun"
    SPIRIT_TEMPLE_OUTER_RIGHT_HAND_SPIRIT_NABOORU_KIDNAPPED = "Spirit Temple Outer Right Hand Spirit Nabooru Kidnapped"
    SPIRIT_TEMPLE_SHORTCUT_SWITCH_SPIRIT_STATUE_SOUTH_DOOR = "Spirit Temple Shortcut Switch Spirit Statue South Door"
    SPIRIT_TEMPLE_BIG_MIRROR_ROOM_SPIRIT_4F_SWITCH = "Spirit Temple Big Mirror Room Spirit 4f Switch"
    SPIRIT_TEMPLE_BIG_MIRROR_ROOM_SPIRIT_PLATFORM_LOWERED = "Spirit Temple Big Mirror Room Spirit Platform Lowered"
    SPIRIT_TEMPLE_BIG_MIRROR_CAVE_SPIRIT_4F_SWITCH = "Spirit Temple Big Mirror Cave Spirit 4f Switch"
    SPIRIT_TEMPLE_BIG_MIRROR_CAVE_SPIRIT_PUSHED_4F_MIRRORS = "Spirit Temple Big Mirror Cave Spirit Pushed 4f Mirrors"
    SPIRIT_TEMPLE_STATUE_HEAD_REVERSE_SPIRIT_CHILD = "Spirit Temple Statue Head Reverse Spirit Child"
    SPIRIT_TEMPLE_STATUE_HEAD_REVERSE_SPIRIT_ADULT = "Spirit Temple Statue Head Reverse Spirit Adult"
    SPIRIT_TEMPLE_BOSS_ROOM_SPIRIT_TEMPLE_CLEAR = "Spirit Temple Boss Room Spirit Temple Clear"


# Region::spiritLogicData (location_access.cpp), non-MQ entries:
# region: (childKeys, childRevKeys, adultKeys, adultRevKeys, childAccess, adultAccess, reverseAccess)
SPIRIT_LOGIC_DATA = {
    Regions.SPIRIT_TEMPLE_SUN_ON_FLOOR_1F: (5, 0, 3, 0,
        lambda bundle: True_(),
        lambda bundle: spirit_explosive_key_logic(bundle) & (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)) & has_grab(bundle),
        lambda bundle: has_climb(bundle) | can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | (bunny_hood(bundle) & can_jump_slash(bundle) & is_adult(bundle))),
    Regions.SPIRIT_TEMPLE_SUN_ON_FLOOR_2F: (5, 0, 3, 0,
        lambda bundle: has_climb(bundle) | can_use(Items.LONGSHOT, bundle),
        lambda bundle: spirit_explosive_key_logic(bundle) & (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)) & has_grab(bundle),
        lambda bundle: has_climb(bundle) | can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | (bunny_hood(bundle) & can_jump_slash(bundle) & is_adult(bundle))),
    Regions.SPIRIT_TEMPLE_2F_MIRROR_ROOM: (5, 0, 3, 0,
        lambda bundle: False_(),
        lambda bundle: has_climb(bundle) | can_use(Items.LONGSHOT, bundle),
        lambda bundle: can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | (bunny_hood(bundle) & can_jump_slash(bundle) & is_adult(bundle))),
    Regions.SPIRIT_TEMPLE_STATUE_ROOM_CHILD: (5, 0, 3, 0,
        lambda bundle: spirit_explosive_key_logic(bundle) & (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)),
        lambda bundle: spirit_explosive_key_logic(bundle) & (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)) & has_grab(bundle),
        lambda bundle: has_climb(bundle) | can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | (bunny_hood(bundle) & can_jump_slash(bundle) & is_adult(bundle))),
    Regions.SPIRIT_TEMPLE_INNER_WEST_HAND: (5, 0, 3, 0,
        lambda bundle: spirit_explosive_key_logic(bundle) & (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)),
        lambda bundle: spirit_explosive_key_logic(bundle) & (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)) & has_grab(bundle),
        lambda bundle: has_climb(bundle) | can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | (bunny_hood(bundle) & can_jump_slash(bundle) & is_adult(bundle))),
    Regions.SPIRIT_TEMPLE_GS_LEDGE: (5, 0, 3, 0,
        lambda bundle: spirit_explosive_key_logic(bundle) & spirit_west_to_skull(bundle) & (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)),
        lambda bundle: spirit_explosive_key_logic(bundle) & spirit_west_to_skull(bundle) & (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)) & has_grab(bundle),
        lambda bundle: spirit_west_to_skull(bundle) & (has_climb(bundle) | can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | (bunny_hood(bundle) & can_jump_slash(bundle) & is_adult(bundle)))),
    Regions.SPIRIT_TEMPLE_STATUE_ROOM: (5, 0, 3, 0,
        lambda bundle: spirit_explosive_key_logic(bundle),
        lambda bundle: spirit_explosive_key_logic(bundle) & (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)) & has_grab(bundle),
        lambda bundle: True_()),
    Regions.SPIRIT_TEMPLE_SUN_BLOCK_CHEST_LEDGE: (5, 0, 3, 0,
        lambda bundle: spirit_explosive_key_logic(bundle) & (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)) & has_grab(bundle),
        lambda bundle: spirit_explosive_key_logic(bundle) & (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)) & has_grab(bundle),
        lambda bundle: (((has_climb(bundle) | can_use(Items.HOOKSHOT, bundle)) | can_use(Items.HOVER_BOOTS, bundle)) & has_grab(bundle)) | (can_kill_enemy(bundle, Enemies.BEAMOS) & can_use(Items.LONGSHOT, bundle))),
    Regions.SPIRIT_TEMPLE_SKULLTULA_STAIRS: (5, 0, 3, 0,
        lambda bundle: spirit_explosive_key_logic(bundle) & (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)) & has_grab(bundle),
        lambda bundle: spirit_explosive_key_logic(bundle) & (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)) & has_grab(bundle),
        lambda bundle: (((has_climb(bundle) | can_use(Items.HOOKSHOT, bundle)) | can_use(Items.HOVER_BOOTS, bundle)) & has_grab(bundle)) | (can_kill_enemy(bundle, Enemies.BEAMOS) & can_use(Items.LONGSHOT, bundle))),
    Regions.SPIRIT_TEMPLE_OUTER_RIGHT_HAND: (5, 5, 3, 3,
        lambda bundle: outer_west_hand_logic(bundle),
        lambda bundle: outer_west_hand_logic(bundle),
        lambda bundle: outer_west_hand_logic(bundle)),
    Regions.SPIRIT_TEMPLE_STATUE_ROOM_ADULT: (5, 0, 3, 0,
        lambda bundle: spirit_explosive_key_logic(bundle) & can_use(Items.HOOKSHOT, bundle) & (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)),
        lambda bundle: (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)) & has_grab(bundle),
        lambda bundle: can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | (bunny_hood(bundle) & can_jump_slash(bundle) & is_adult(bundle))),
    Regions.SPIRIT_TEMPLE_INNER_LEFT_HAND: (5, 0, 3, 0,
        lambda bundle: spirit_explosive_key_logic(bundle) & can_use(Items.HOOKSHOT, bundle) & (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)),
        lambda bundle: (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)) & has_grab(bundle),
        lambda bundle: can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | (bunny_hood(bundle) & can_jump_slash(bundle) & is_adult(bundle))),
    Regions.SPIRIT_TEMPLE_SHORTCUT_SWITCH: (5, 0, 3, 0,
        lambda bundle: spirit_explosive_key_logic(bundle) & can_use(Items.HOOKSHOT, bundle) & spirit_east_to_switch(bundle),
        lambda bundle: spirit_east_to_switch(bundle) & (has_climb(bundle) | can_use(Items.LONGSHOT, bundle)) & has_grab(bundle),
        lambda bundle: spirit_east_to_switch(bundle) & (can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | (bunny_hood(bundle) & can_jump_slash(bundle) & is_adult(bundle)))),
}

def spirit_shared(bundle, region, cond_fn, any_age=False, others=None):
    return make_spirit_shared(bundle[1], SPIRIT_LOGIC_DATA, region, cond_fn, any_age, others)


def spirit_certain_access(bundle, region):
    b = (region, bundle[1])
    return ((is_child(b) & spirit_certain_access_rule(b, SPIRIT_LOGIC_DATA[region], True))
            | (is_adult(b) & spirit_certain_access_rule(b, SPIRIT_LOGIC_DATA[region], False)))


def set_region_rules(world: "SohWorld") -> None:

    # Spirit Temple Entryway  (upstream RR_SPIRIT_TEMPLE_ENTRYWAY, SCENE_SPIRIT_TEMPLE)
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_ENTRYWAY, world, [
        (Regions.SPIRIT_TEMPLE_FOYER,
         lambda bundle: True_()),
        (Regions.DESERT_COLOSSUS_OUTSIDE_TEMPLE,
         lambda bundle: True_()),
    ])

    # Spirit Temple Foyer  (upstream RR_SPIRIT_TEMPLE_FOYER, SCENE_SPIRIT_TEMPLE)
    # Events
    add_events(Regions.SPIRIT_TEMPLE_FOYER, world, [
        (EventLocations.SPIRIT_TEMPLE_FOYER_FORWARDS_SPIRIT_CHILD, Events.FORWARDS_SPIRIT_CHILD,
         lambda bundle: is_child(bundle)),
        (EventLocations.SPIRIT_TEMPLE_FOYER_FORWARDS_SPIRIT_ADULT, Events.FORWARDS_SPIRIT_ADULT,
         lambda bundle: is_adult(bundle)),
    ])
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_FOYER, world, [
        (Locations.SPIRIT_TEMPLE_LOBBY_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.SPIRIT_TEMPLE_LOBBY_POT2,
         lambda bundle: can_break_pots(bundle)),
        # DEFERRED RC_SPIRIT_TEMPLE_LEFT_SNAKE_STATUE: logic->CanRead()
        # DEFERRED RC_SPIRIT_TEMPLE_RIGHT_SNAKE_STATUE: logic->CanRead()
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_FOYER, world, [
        (Regions.SPIRIT_TEMPLE_ENTRYWAY,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_CHILD_SIDE_HUB,
         lambda bundle: (is_adult(bundle) | has_speak(bundle, "GERUDO") | has_item(Events.SPIRIT_NABOORU_KIDNAPPED, bundle)) & has_crawl(bundle)),
        (Regions.SPIRIT_TEMPLE_ADULT_SIDE_HUB,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
    ])

    # Spirit Temple Child Side Hub  (upstream RR_SPIRIT_TEMPLE_CHILD_SIDE_HUB, SCENE_SPIRIT_TEMPLE)
    # Events
    add_events(Regions.SPIRIT_TEMPLE_CHILD_SIDE_HUB, world, [
        (EventLocations.SPIRIT_TEMPLE_CHILD_SIDE_HUB_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_break_small_crates(bundle)),
        (EventLocations.SPIRIT_TEMPLE_CHILD_SIDE_HUB_SPIRIT_SILVER_RUPEE_BRIDGE_TORCHES, Events.SPIRIT_SILVER_RUPEE_BRIDGE_TORCHES,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.ARMOS)) & can_use(Items.STICKS, bundle)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_CHILD_SIDE_HUB, world, [
        (Regions.SPIRIT_TEMPLE_FOYER,
         lambda bundle: has_crawl(bundle)),
        (Regions.SPIRIT_TEMPLE_CHILD_BOXES,
         lambda bundle: has_crawl(bundle)),
        (Regions.SPIRIT_TEMPLE_SWITCH_BRIDGE_SOUTH,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.ARMOS))),
        (Regions.SPIRIT_TEMPLE_RUPEE_BRIDGE_SOUTH,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.ARMOS))),
    ])

    # Spirit Temple Switch Bridge South  (upstream RR_SPIRIT_TEMPLE_SWITCH_BRIDGE_SOUTH, SCENE_SPIRIT_TEMPLE)
    # Events
    add_events(Regions.SPIRIT_TEMPLE_SWITCH_BRIDGE_SOUTH, world, [
        (EventLocations.SPIRIT_TEMPLE_SWITCH_BRIDGE_SOUTH_SPIRIT_CHILD_SWITCH_BRIDGE, Events.SPIRIT_CHILD_SWITCH_BRIDGE,
         lambda bundle: can_use(Items.BOOMERANG, bundle) | can_use(Items.FAIRY_SLINGSHOT, bundle) | can_use(Items.FAIRY_BOW, bundle) | (can_use(Items.BOMBCHUS_5, bundle) & can_do_trick(Tricks.SPIRIT_CHILD_CHU, bundle))),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_SWITCH_BRIDGE_SOUTH, world, [
        (Regions.SPIRIT_TEMPLE_CHILD_SIDE_HUB,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_SWITCH_BRIDGE_NORTH,
         lambda bundle: (has_item(Events.SPIRIT_CHILD_SWITCH_BRIDGE, bundle) & can_pass_enemy(bundle, Enemies.GREEN_BUBBLE, EnemyDistance.CLOSE, False)) | can_use(Items.HOVER_BOOTS, bundle) | can_use(Items.LONGSHOT, bundle) | (is_adult(bundle) & bunny_hood(bundle))),
    ])

    # Spirit Temple Switch Bridge North  (upstream RR_SPIRIT_TEMPLE_SWITCH_BRIDGE_NORTH, SCENE_SPIRIT_TEMPLE)
    # Events
    add_events(Regions.SPIRIT_TEMPLE_SWITCH_BRIDGE_NORTH, world, [
        (EventLocations.SPIRIT_TEMPLE_SWITCH_BRIDGE_NORTH_SPIRIT_CHILD_SWITCH_BRIDGE, Events.SPIRIT_CHILD_SWITCH_BRIDGE,
         lambda bundle: can_hit_switch(bundle)),
    ])
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_SWITCH_BRIDGE_NORTH, world, [
        (Locations.SPIRIT_TEMPLE_CHILD_BRIDGE_CHEST,
         lambda bundle: has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_SWITCH_BRIDGE_NORTH, world, [
        (Regions.SPIRIT_TEMPLE_SWITCH_BRIDGE_SOUTH,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle) | (has_item(Events.SPIRIT_CHILD_SWITCH_BRIDGE, bundle) & can_pass_enemy(bundle, Enemies.GREEN_BUBBLE, EnemyDistance.CLOSE, False)) | (is_adult(bundle) & bunny_hood(bundle))),
        (Regions.SPIRIT_TEMPLE_1F_ANUBIS,
         lambda bundle: True_()),
    ])

    # Spirit Temple 1F Anubis  (upstream RR_SPIRIT_TEMPLE_1F_ANUBIS, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_1F_ANUBIS, world, [
        (Locations.SPIRIT_TEMPLE_ANUBIS_POT1,
         lambda bundle: True_()),
        (Locations.SPIRIT_TEMPLE_ANUBIS_POT2,
         lambda bundle: True_()),
        (Locations.SPIRIT_TEMPLE_ANUBIS_POT3,
         lambda bundle: True_()),
        (Locations.SPIRIT_TEMPLE_ANUBIS_POT4,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_1F_ANUBIS, world, [
        (Regions.SPIRIT_TEMPLE_SWITCH_BRIDGE_NORTH,
         lambda bundle: any_age_time(bundle, lambda bundle: can_hit_switch(bundle) | has_grab(bundle) | can_kill_enemy(bundle, Enemies.ANUBIS))),
        (Regions.SPIRIT_TEMPLE_RUPEE_BRIDGE_NORTH,
         lambda bundle: any_age_time(bundle, lambda bundle: can_hit_switch(bundle) | has_grab(bundle) | can_kill_enemy(bundle, Enemies.ANUBIS))),
    ])

    # Spirit Temple Rupee Bridge North  (upstream RR_SPIRIT_TEMPLE_RUPEE_BRIDGE_NORTH, SCENE_SPIRIT_TEMPLE)
    # Events
    add_events(Regions.SPIRIT_TEMPLE_RUPEE_BRIDGE_NORTH, world, [
        (EventLocations.SPIRIT_TEMPLE_RUPEE_BRIDGE_NORTH_SPIRIT_SILVER_CHILD, Events.SPIRIT_SILVER_CHILD,
         lambda bundle: has_climb(bundle) | can_use(Items.HOOKSHOT, bundle)),
        (EventLocations.SPIRIT_TEMPLE_RUPEE_BRIDGE_NORTH_SPIRIT_SILVER_RUPEE_BRIDGE_TORCHES, Events.SPIRIT_SILVER_RUPEE_BRIDGE_TORCHES,
         lambda bundle: (has_item(Events.SPIRIT_SILVER_CHILD, bundle) & has_fire_source_with_torch(bundle)) | can_use(Items.DINS_FIRE, bundle)),
    ])
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_RUPEE_BRIDGE_NORTH, world, [
        (Locations.SPIRIT_TEMPLE_CHILD_EARLY_TORCHES_CHEST,
         lambda bundle: has_item(Events.SPIRIT_SILVER_RUPEE_BRIDGE_TORCHES, bundle) & has_open_chest(bundle)),
        (Locations.SPIRIT_TEMPLE_GS_METAL_FENCE,
         lambda bundle: has_item(Events.SPIRIT_SILVER_CHILD, bundle) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOMB_THROW) & has_climb(bundle)),
        # DEFERRED RC_SPIRIT_W_HIGH_CHILD_SILVER: logic->HasItem(RG_CLIMB) || logic->CanUse(RG_HOOKSHOT)
        # DEFERRED RC_SPIRIT_W_LOW_CHILD_SILVER: true
        # DEFERRED RC_SPIRIT_E_LOW_CHILD_SILVER: true
        # DEFERRED RC_SPIRIT_E_HIGH_CHILD_SILVER: logic->HasItem(RG_CLIMB) || logic->CanUse(RG_HOOKSHOT)
        # DEFERRED RC_SPIRIT_TORCH_CHILD_SILVER: true
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_RUPEE_BRIDGE_NORTH, world, [
        (Regions.SPIRIT_TEMPLE_RUPEE_BRIDGE_SOUTH,
         lambda bundle: has_item(Events.SPIRIT_SILVER_CHILD, bundle)),
        (Regions.SPIRIT_TEMPLE_1F_ANUBIS,
         lambda bundle: True_()),
    ])

    # Spirit Temple Rupee Bridge South  (upstream RR_SPIRIT_TEMPLE_RUPEE_BRIDGE_SOUTH, SCENE_SPIRIT_TEMPLE)
    # Events
    add_events(Regions.SPIRIT_TEMPLE_RUPEE_BRIDGE_SOUTH, world, [
        (EventLocations.SPIRIT_TEMPLE_RUPEE_BRIDGE_SOUTH_SPIRIT_SILVER_RUPEE_BRIDGE_TORCHES, Events.SPIRIT_SILVER_RUPEE_BRIDGE_TORCHES,
         lambda bundle: has_fire_source(bundle)),
    ])
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_RUPEE_BRIDGE_SOUTH, world, [
        (Locations.SPIRIT_TEMPLE_GS_METAL_FENCE,
         lambda bundle: can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_RUPEE_BRIDGE_SOUTH, world, [
        (Regions.SPIRIT_TEMPLE_CHILD_SIDE_HUB,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_RUPEE_BRIDGE_NORTH,
         lambda bundle: has_item(Events.SPIRIT_SILVER_CHILD, bundle)),
    ])

    # Spirit Temple Child Boxes  (upstream RR_SPIRIT_TEMPLE_CHILD_BOXES, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_CHILD_BOXES, world, [
        (Locations.SPIRIT_TEMPLE_BEFORE_CHILD_CLIMB_SMALL_CRATE1,
         lambda bundle: can_break_small_crates(bundle)),
        (Locations.SPIRIT_TEMPLE_BEFORE_CHILD_CLIMB_SMALL_CRATE2,
         lambda bundle: can_break_small_crates(bundle)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_CHILD_BOXES, world, [
        (Regions.SPIRIT_TEMPLE_CHILD_SIDE_HUB,
         lambda bundle: has_crawl(bundle)),
        (Regions.SPIRIT_TEMPLE_SUN_ON_FLOOR_1F,
         lambda bundle: small_keys_scene("SCENE_SPIRIT_TEMPLE", 1, bundle)),
    ])

    # Spirit Temple Sun On Floor 1F  (upstream RR_SPIRIT_TEMPLE_SUN_ON_FLOOR_1F, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_SUN_ON_FLOOR_1F, world, [
        (Locations.SPIRIT_TEMPLE_GS_SUN_ON_FLOOR_ROOM,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_SUN_ON_FLOOR_1F, lambda bundle: can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG), any_age=False, others=[(Regions.SPIRIT_TEMPLE_SUN_ON_FLOOR_2F, lambda bundle: ((take_damage(bundle)) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.SHORT_JUMPSLASH) | can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOMB_THROW)))])),
        (Locations.SPIRIT_TEMPLE_CHILD_CLIMB_POT1,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_SUN_ON_FLOOR_1F, lambda bundle: can_break_pots(bundle), any_age=False)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_SUN_ON_FLOOR_1F, world, [
        (Regions.SPIRIT_TEMPLE_CHILD_BOXES,
         lambda bundle: small_keys_scene("SCENE_SPIRIT_TEMPLE", 5, bundle)),
        (Regions.SPIRIT_TEMPLE_SUN_ON_FLOOR_2F,
         lambda bundle: has_climb(bundle) | can_use(Items.LONGSHOT, bundle)),
    ])

    # Spirit Temple Sun On Floor 2F  (upstream RR_SPIRIT_TEMPLE_SUN_ON_FLOOR_2F, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_SUN_ON_FLOOR_2F, world, [
        (Locations.SPIRIT_TEMPLE_CHILD_CLIMB_NORTH_CHEST,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_SUN_ON_FLOOR_2F, lambda bundle: can_hit_switch(bundle, EnemyDistance.BOMB_THROW) & has_open_chest(bundle), any_age=False)),
        (Locations.SPIRIT_TEMPLE_CHILD_CLIMB_EAST_CHEST,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_SUN_ON_FLOOR_2F, lambda bundle: can_hit_switch(bundle, EnemyDistance.BOMB_THROW) & has_open_chest(bundle), any_age=False)),
        (Locations.SPIRIT_TEMPLE_GS_SUN_ON_FLOOR_ROOM,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_SUN_ON_FLOOR_2F, lambda bundle: ((take_damage(bundle)) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.SHORT_JUMPSLASH) | can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOMB_THROW)), any_age=False, others=[(Regions.SPIRIT_TEMPLE_SUN_ON_FLOOR_1F, lambda bundle: can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG))])),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_SUN_ON_FLOOR_2F, world, [
        (Regions.SPIRIT_TEMPLE_SUN_ON_FLOOR_1F,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM_CHILD,
         lambda bundle: has_explosives(bundle) | (True_(options=[OptionFilter(SunlightArrows, True)]) & can_use(Items.LIGHT_ARROW, bundle))),
    ])

    # Spirit Temple Adult Side Hub  (upstream RR_SPIRIT_TEMPLE_ADULT_SIDE_HUB, SCENE_SPIRIT_TEMPLE)
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_ADULT_SIDE_HUB, world, [
        (Regions.SPIRIT_TEMPLE_FOYER,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_SAND_PIT,
         lambda bundle: any_age_time(bundle, lambda bundle: ((is_adult(bundle) & can_do_trick(Tricks.SPIRIT_LOWER_ADULT_SWITCH, bundle)) & can_hit_switch(bundle, EnemyDistance.BOMB_THROW) | ((is_child(bundle)) | (trick_disabled(Tricks.SPIRIT_LOWER_ADULT_SWITCH, bundle))) & can_hit_switch(bundle, EnemyDistance.BOOMERANG)))),
        (Regions.SPIRIT_TEMPLE_ABOVE_BOULDERS,
         lambda bundle: any_age_time(bundle, lambda bundle: ((is_adult(bundle) & can_do_trick(Tricks.SPIRIT_LOWER_ADULT_SWITCH, bundle)) & can_hit_switch(bundle, EnemyDistance.BOMB_THROW) | ((is_child(bundle)) | (trick_disabled(Tricks.SPIRIT_LOWER_ADULT_SWITCH, bundle))) & can_hit_switch(bundle, EnemyDistance.BOOMERANG)))),
        (Regions.SPIRIT_TEMPLE_1F_MIRROR_ROOM,
         lambda bundle: small_keys_scene("SCENE_SPIRIT_TEMPLE", 1, bundle)),
    ])

    # Spirit Temple Sand Pit  (upstream RR_SPIRIT_TEMPLE_SAND_PIT, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_SAND_PIT, world, [
        (Locations.SPIRIT_TEMPLE_COMPASS_CHEST,
         lambda bundle: can_use(Items.ZELDAS_LULLABY, bundle) & (can_use(Items.HOOKSHOT, bundle) | can_recoil_hover(bundle, Recoil.HAMMER)) & can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_SAND_PIT, world, [
        (Regions.SPIRIT_TEMPLE_ADULT_SIDE_HUB,
         lambda bundle: True_()),
    ])

    # Spirit Temple Above Boulders  (upstream RR_SPIRIT_TEMPLE_ABOVE_BOULDERS, SCENE_SPIRIT_TEMPLE)
    # Events
    add_events(Regions.SPIRIT_TEMPLE_ABOVE_BOULDERS, world, [
        (EventLocations.SPIRIT_TEMPLE_ABOVE_BOULDERS_SPIRIT_SILVER_BOULDERS, Events.SPIRIT_SILVER_BOULDERS,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle) | can_jump_slash(bundle) | can_use(Items.LONGSHOT, bundle) | bunny_hood(bundle)),
    ])
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_ABOVE_BOULDERS, world, [
        # DEFERRED RC_SPIRIT_AIRBORNE_BOULDER_SILVER: logic->CanUse(RG_HOVER_BOOTS) || logic->CanJumpslash() || logic->CanUse(RG_LONGSHOT) || logic->BunnyHood()
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_ABOVE_BOULDERS, world, [
        (Regions.SPIRIT_TEMPLE_ADULT_SIDE_HUB,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_BOULDERS,
         lambda bundle: True_()),
    ])

    # Spirit Temple Boulders  (upstream RR_SPIRIT_TEMPLE_BOULDERS, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_BOULDERS, world, [
        (Locations.SPIRIT_TEMPLE_GS_BOULDER_ROOM,
         lambda bundle: can_use(Items.SONG_OF_TIME, bundle) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA)),
        # DEFERRED RC_SPIRIT_NW_BOULDER_SILVER: true
        # DEFERRED RC_SPIRIT_SW_BOULDER_SILVER: true
        # DEFERRED RC_SPIRIT_SE_BOULDER_SILVER: true
        # DEFERRED RC_SPIRIT_NE_BOULDER_SILVER: true
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_BOULDERS, world, [
        (Regions.SPIRIT_TEMPLE_ABOVE_BOULDERS,
         lambda bundle: is_adult(bundle) | has_climb(bundle) | can_use(Items.HOOKSHOT, bundle) | can_ground_jump(bundle)),
        (Regions.SPIRIT_TEMPLE_PAST_BOULDERS,
         lambda bundle: has_item(Events.SPIRIT_SILVER_BOULDERS, bundle)),
    ])

    # Spirit Temple Past Boulders  (upstream RR_SPIRIT_TEMPLE_PAST_BOULDERS, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_PAST_BOULDERS, world, [
        (Locations.SPIRIT_TEMPLE_EARLY_ADULT_RIGHT_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.SPIRIT_TEMPLE_AFTER_BOULDER_ROOM_SUNS_SONG_FAIRY,
         lambda bundle: can_use(Items.SUNS_SONG, bundle)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_PAST_BOULDERS, world, [
        (Regions.SPIRIT_TEMPLE_BOULDERS,
         lambda bundle: True_()),
    ])

    # Spirit Temple 1F Mirror Room  (upstream RR_SPIRIT_TEMPLE_1F_MIRROR_ROOM, SCENE_SPIRIT_TEMPLE)
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_1F_MIRROR_ROOM, world, [
        (Regions.SPIRIT_TEMPLE_ADULT_SIDE_HUB,
         lambda bundle: small_keys_scene("SCENE_SPIRIT_TEMPLE", 5, bundle)),
        (Regions.SPIRIT_TEMPLE_2F_MIRROR_ROOM,
         lambda bundle: has_climb(bundle) | can_use(Items.LONGSHOT, bundle)),
    ])

    # Spirit Temple 2F Mirror Room  (upstream RR_SPIRIT_TEMPLE_2F_MIRROR_ROOM, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_2F_MIRROR_ROOM, world, [
        (Locations.SPIRIT_TEMPLE_FIRST_MIRROR_LEFT_CHEST,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_2F_MIRROR_ROOM, lambda bundle: has_open_chest(bundle) & (has_grab(bundle) | sunlight_arrows(bundle)), any_age=False)),
        (Locations.SPIRIT_TEMPLE_FIRST_MIRROR_RIGHT_CHEST,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_2F_MIRROR_ROOM, lambda bundle: has_open_chest(bundle) & (has_grab(bundle) | sunlight_arrows(bundle)), any_age=False)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_2F_MIRROR_ROOM, world, [
        (Regions.SPIRIT_TEMPLE_1F_MIRROR_ROOM,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM_ADULT,
         lambda bundle: has_grab(bundle) | sunlight_arrows(bundle)),
    ])

    # Spirit Temple Statue Room Child  (upstream RR_SPIRIT_TEMPLE_STATUE_ROOM_CHILD, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_STATUE_ROOM_CHILD, world, [
        (Locations.SPIRIT_TEMPLE_MAP_CHEST,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_STATUE_ROOM_CHILD, lambda bundle: has_fire_source_with_torch(bundle) | (can_do_trick(Tricks.SPIRIT_MAP_CHEST, bundle) & can_use(Items.FAIRY_BOW, bundle)), any_age=False, others=[(Regions.SPIRIT_TEMPLE_STATUE_ROOM_ADULT, lambda bundle: has_fire_source_with_torch(bundle)), (Regions.SPIRIT_TEMPLE_STATUE_ROOM, lambda bundle: has_fire_source(bundle))]) & can_open_large_chest(bundle)),
        (Locations.SPIRIT_TEMPLE_GS_LOBBY,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_STATUE_ROOM_CHILD, lambda bundle: can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.LONGSHOT), any_age=False, others=[(Regions.SPIRIT_TEMPLE_INNER_WEST_HAND, lambda bundle: ((can_do_trick(Tricks.SPIRIT_WEST_LEDGE, bundle)) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG) | (trick_disabled(Tricks.SPIRIT_WEST_LEDGE, bundle)) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.HOOKSHOT))), (Regions.SPIRIT_TEMPLE_GS_LEDGE, lambda bundle: can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA))])),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_STATUE_ROOM_CHILD, world, [
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_SUN_ON_FLOOR_2F,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_INNER_WEST_HAND,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_GS_LEDGE,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle) | reach_scarecrow(bundle)),
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM_ADULT,
         lambda bundle: can_recoil_hover_from_object(bundle, TorchRecoil.SHORT) & is_adult(bundle)),
        (Regions.SPIRIT_TEMPLE_PLATFORM,
         lambda bundle: has_item(Events.SPIRIT_PLATFORM_LOWERED, bundle) & (can_use(Items.LONGSHOT, bundle) | (can_do_trick(Tricks.SPIRIT_PLATFORM_HOOKSHOT, bundle) & can_use(Items.HOOKSHOT, bundle)))),
        (Regions.SPIRIT_TEMPLE_EMPTY_STAIRS,
         lambda bundle: has_grab(bundle)),
        (Regions.DESERT_COLOSSUS,
         lambda bundle: True_() & has_grab(bundle) & has_crawl(bundle) & small_keys_scene("SCENE_SPIRIT_TEMPLE", 4, bundle) & can_kill_enemy(bundle, Enemies.IRON_KNUCKLE)),
    ])

    # Spirit Temple Inner West Hand  (upstream RR_SPIRIT_TEMPLE_INNER_WEST_HAND, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_INNER_WEST_HAND, world, [
        (Locations.SPIRIT_TEMPLE_GS_LOBBY,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_INNER_WEST_HAND, lambda bundle: ((can_do_trick(Tricks.SPIRIT_WEST_LEDGE, bundle)) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG) | (trick_disabled(Tricks.SPIRIT_WEST_LEDGE, bundle)) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.HOOKSHOT)), any_age=False, others=[(Regions.SPIRIT_TEMPLE_GS_LEDGE, lambda bundle: can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA)), (Regions.SPIRIT_TEMPLE_STATUE_ROOM_CHILD, lambda bundle: can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.LONGSHOT))])),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_INNER_WEST_HAND, world, [
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM_CHILD,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle) | can_jump_slash(bundle) | can_use(Items.HOOKSHOT, bundle)),
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_GS_LEDGE,
         lambda bundle: is_adult(bundle) & (can_do_trick(Tricks.SPIRIT_STATUE_JUMP, bundle) | bunny_hood(bundle))),
    ])

    # Spirit Temple GS Ledge  (upstream RR_SPIRIT_TEMPLE_GS_LEDGE, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_GS_LEDGE, world, [
        (Locations.SPIRIT_TEMPLE_GS_LOBBY,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_GS_LEDGE, lambda bundle: can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA), any_age=False, others=[(Regions.SPIRIT_TEMPLE_INNER_WEST_HAND, lambda bundle: ((can_do_trick(Tricks.SPIRIT_WEST_LEDGE, bundle)) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG) | (trick_disabled(Tricks.SPIRIT_WEST_LEDGE, bundle)) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.HOOKSHOT))), (Regions.SPIRIT_TEMPLE_STATUE_ROOM_CHILD, lambda bundle: can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.LONGSHOT))])),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_GS_LEDGE, world, [
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM_CHILD,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle) | can_use(Items.HOOKSHOT, bundle) | bunny_hood(bundle)),
        (Regions.SPIRIT_TEMPLE_INNER_WEST_HAND,
         lambda bundle: True_()),
    ])

    # Spirit Temple Statue Room  (upstream RR_SPIRIT_TEMPLE_STATUE_ROOM, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_STATUE_ROOM, world, [
        (Locations.SPIRIT_TEMPLE_MAP_CHEST,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_STATUE_ROOM, lambda bundle: has_fire_source(bundle), any_age=False, others=[(Regions.SPIRIT_TEMPLE_STATUE_ROOM_CHILD, lambda bundle: has_fire_source_with_torch(bundle) | (can_do_trick(Tricks.SPIRIT_MAP_CHEST, bundle) & can_use(Items.FAIRY_BOW, bundle)))]) & can_open_large_chest(bundle)),
        (Locations.SPIRIT_TEMPLE_CENTRAL_CHAMBER_POT1,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_STATUE_ROOM, lambda bundle: can_break_pots(bundle), any_age=False)),
        (Locations.SPIRIT_TEMPLE_CENTRAL_CHAMBER_POT2,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_STATUE_ROOM, lambda bundle: can_break_pots(bundle), any_age=False)),
        (Locations.SPIRIT_TEMPLE_CENTRAL_CHAMBER_POT3,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_STATUE_ROOM, lambda bundle: can_break_pots(bundle), any_age=False)),
        (Locations.SPIRIT_TEMPLE_CENTRAL_CHAMBER_POT4,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_STATUE_ROOM, lambda bundle: can_break_pots(bundle), any_age=False)),
        (Locations.SPIRIT_TEMPLE_CENTRAL_CHAMBER_POT5,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_STATUE_ROOM, lambda bundle: can_break_pots(bundle), any_age=False)),
        (Locations.SPIRIT_TEMPLE_CENTRAL_CHAMBER_POT6,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_STATUE_ROOM, lambda bundle: can_break_pots(bundle), any_age=False)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_STATUE_ROOM, world, [
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM_CHILD,
         lambda bundle: has_climb(bundle) | can_use(Items.HOOKSHOT, bundle)),
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM_ADULT,
         lambda bundle: is_adult(bundle) & can_use(Items.HOOKSHOT, bundle)),
        (Regions.SPIRIT_TEMPLE_SHORTCUT,
         lambda bundle: has_item(Events.SPIRIT_STATUE_SOUTH_DOOR, bundle)),
        (Regions.SPIRIT_TEMPLE_ADULT_SIDE_HUB,
         lambda bundle: True_() & can_use(Items.SILVER_GAUNTLETS, bundle) & is_adult(bundle) & ((can_kill_enemy(bundle, Enemies.BEAMOS) & (((has_climb(bundle) | can_use(Items.HOOKSHOT, bundle)) & has_grab(bundle)) & small_keys_scene("SCENE_SPIRIT_TEMPLE", 2, bundle) | small_keys_scene("SCENE_SPIRIT_TEMPLE", 3, bundle))) | ((has_climb(bundle) | can_use(Items.HOOKSHOT, bundle)) & has_grab(bundle) & can_kill_enemy(bundle, Enemies.IRON_KNUCKLE) & small_keys_scene("SCENE_SPIRIT_TEMPLE", 4, bundle)))),
    ])

    # Spirit Temple Empty Stairs  (upstream RR_SPIRIT_TEMPLE_EMPTY_STAIRS, SCENE_SPIRIT_TEMPLE)
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_EMPTY_STAIRS, world, [
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM_CHILD,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_SUN_BLOCK_ROOM,
         lambda bundle: True_()),
    ])

    # Spirit Temple Sun Block Room  (upstream RR_SPIRIT_TEMPLE_SUN_BLOCK_ROOM, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_SUN_BLOCK_ROOM, world, [
        # DEFERRED RC_SPIRIT_NEAR_LIGHT_SUN_SILVER: true
        # DEFERRED RC_SPIRIT_AIRBORNE_SUN_SILVER: true
        # DEFERRED RC_SPIRIT_MID_PLATFORM_SUN_SILVER: true
        # DEFERRED RC_SPIRIT_NEAR_DOOR_SUN_SILVER: true
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_SUN_BLOCK_ROOM, world, [
        (Regions.SPIRIT_TEMPLE_EMPTY_STAIRS,
         lambda bundle: has_grab(bundle) | sunlight_arrows(bundle)),
        (Regions.SPIRIT_TEMPLE_SUN_BLOCK_CHEST_LEDGE,
         lambda bundle: spirit_sun_block_south_ledge(bundle)),
        (Regions.SPIRIT_TEMPLE_SKULLTULA_STAIRS,
         lambda bundle: has_grab(bundle) | sunlight_arrows(bundle)),
    ])

    # Spirit Temple Sun Block Chest Ledge  (upstream RR_SPIRIT_TEMPLE_SUN_BLOCK_CHEST_LEDGE, SCENE_SPIRIT_TEMPLE)
    # Events
    add_events(Regions.SPIRIT_TEMPLE_SUN_BLOCK_CHEST_LEDGE, world, [
        (EventLocations.SPIRIT_TEMPLE_SUN_BLOCK_CHEST_LEDGE_SPIRIT_SILVER_SUN, Events.SPIRIT_SILVER_SUN,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_SUN_BLOCK_CHEST_LEDGE, lambda bundle: True_(), any_age=True)),
    ])
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_SUN_BLOCK_CHEST_LEDGE, world, [
        (Locations.SPIRIT_TEMPLE_SUN_BLOCK_ROOM_CHEST,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_SUN_BLOCK_CHEST_LEDGE, lambda bundle: has_fire_source(bundle) | (has_item(Events.SPIRIT_SILVER_SUN, bundle) & (can_use(Items.STICKS, bundle) | (can_do_trick(Tricks.SPIRIT_SUN_CHEST, bundle) & can_use(Items.FAIRY_BOW, bundle)))), any_age=False) & has_open_chest(bundle)),
        # DEFERRED RC_SPIRIT_NEAR_CHEST_SUN_SILVER: SpiritShared(RR_SPIRIT_TEMPLE_SUN_BLOCK_CHEST_LEDGE, []{return true;}, true)
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_SUN_BLOCK_CHEST_LEDGE, world, [
        (Regions.SPIRIT_TEMPLE_SUN_BLOCK_ROOM,
         lambda bundle: True_()),
    ])

    # Spirit Temple Skulltula Stairs  (upstream RR_SPIRIT_TEMPLE_SKULLTULA_STAIRS, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_SKULLTULA_STAIRS, world, [
        (Locations.SPIRIT_TEMPLE_GS_HALL_AFTER_SUN_BLOCK_ROOM,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_SKULLTULA_STAIRS, lambda bundle: can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG), any_age=False)),
        (Locations.SPIRIT_TEMPLE_AFTER_SUN_BLOCK_POT1,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_SKULLTULA_STAIRS, lambda bundle: can_break_pots(bundle), any_age=False)),
        (Locations.SPIRIT_TEMPLE_AFTER_SUN_BLOCK_POT2,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_SKULLTULA_STAIRS, lambda bundle: can_break_pots(bundle), any_age=False)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_SKULLTULA_STAIRS, world, [
        (Regions.SPIRIT_TEMPLE_SUN_BLOCK_ROOM,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_CHILD_THRONE,
         lambda bundle: small_keys_scene("SCENE_SPIRIT_TEMPLE", 3, bundle)),
    ])

    # Spirit Temple Child Throne  (upstream RR_SPIRIT_TEMPLE_CHILD_THRONE, SCENE_SPIRIT_TEMPLE)
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_CHILD_THRONE, world, [
        (Regions.SPIRIT_TEMPLE_SKULLTULA_STAIRS,
         lambda bundle: small_keys_scene("SCENE_SPIRIT_TEMPLE", 3, bundle)),
        (Regions.SPIRIT_TEMPLE_RIGHT_HAND_EXIT,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.IRON_KNUCKLE))),
    ])

    # Spirit Temple Right Hand Exit  (upstream RR_SPIRIT_TEMPLE_RIGHT_HAND_EXIT, SCENE_SPIRIT_TEMPLE)
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_RIGHT_HAND_EXIT, world, [
        (Regions.SPIRIT_TEMPLE_CHILD_THRONE,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_OUTER_RIGHT_HAND,
         lambda bundle: True_()),
    ])

    # Spirit Temple Outer Right Hand  (upstream RR_SPIRIT_TEMPLE_OUTER_RIGHT_HAND, SCENE_SPIRIT_TEMPLE)
    # Events
    add_events(Regions.SPIRIT_TEMPLE_OUTER_RIGHT_HAND, world, [
        (EventLocations.SPIRIT_TEMPLE_OUTER_RIGHT_HAND_SPIRIT_NABOORU_KIDNAPPED, Events.SPIRIT_NABOORU_KIDNAPPED,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_OUTER_RIGHT_HAND, lambda bundle: has_open_chest(bundle), any_age=False)),
    ])
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_OUTER_RIGHT_HAND, world, [
        (Locations.SPIRIT_TEMPLE_SILVER_GAUNTLETS_CHEST,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_OUTER_RIGHT_HAND, lambda bundle: can_open_large_chest(bundle), any_age=False)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_OUTER_RIGHT_HAND, world, [
        (Regions.SPIRIT_TEMPLE_RIGHT_HAND_EXIT,
         lambda bundle: True_()),
        (Regions.DESERT_COLOSSUS,
         lambda bundle: spirit_certain_access(bundle, Regions.SPIRIT_TEMPLE_OUTER_RIGHT_HAND)),
    ])

    # Spirit Temple Statue Room Adult  (upstream RR_SPIRIT_TEMPLE_STATUE_ROOM_ADULT, SCENE_SPIRIT_TEMPLE)
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_STATUE_ROOM_ADULT, world, [
        (Regions.SPIRIT_TEMPLE_2F_MIRROR_ROOM,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_INNER_LEFT_HAND,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_SHORTCUT_SWITCH,
         lambda bundle: spirit_east_to_switch(bundle)),
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM_CHILD,
         lambda bundle: can_recoil_hover_from_object(bundle, TorchRecoil.SHORT)),
        (Regions.SPIRIT_TEMPLE_POT_STAIRS,
         lambda bundle: small_keys_scene("SCENE_SPIRIT_TEMPLE", 4, bundle)),
        (Regions.SPIRIT_TEMPLE_PLATFORM,
         lambda bundle: has_item(Events.SPIRIT_PLATFORM_LOWERED, bundle) & (can_use(Items.LONGSHOT, bundle) | (can_do_trick(Tricks.SPIRIT_PLATFORM_HOOKSHOT, bundle) & can_use(Items.HOOKSHOT, bundle)))),
    ])

    # Spirit Temple Inner Left Hand  (upstream RR_SPIRIT_TEMPLE_INNER_LEFT_HAND, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_INNER_LEFT_HAND, world, [
        (Locations.SPIRIT_TEMPLE_STATUE_ROOM_HAND_CHEST,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_INNER_LEFT_HAND, lambda bundle: can_use(Items.ZELDAS_LULLABY, bundle) & (has_climb(bundle) | can_use(Items.HOOKSHOT, bundle)) & has_open_chest(bundle), any_age=False)),
        (Locations.SPIRIT_TEMPLE_STATUE_ROOM_NORTHEAST_CHEST,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_INNER_LEFT_HAND, lambda bundle: can_use(Items.ZELDAS_LULLABY, bundle) & has_open_chest(bundle) & ((is_adult(bundle) & (can_do_trick(Tricks.SPIRIT_STATUE_JUMP, bundle) | bunny_hood(bundle))) | can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle)), any_age=False)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_INNER_LEFT_HAND, world, [
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM_ADULT,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle) | can_use(Items.HOOKSHOT, bundle)),
        (Regions.SPIRIT_TEMPLE_SHORTCUT_SWITCH,
         lambda bundle: (is_adult(bundle) & (can_do_trick(Tricks.SPIRIT_STATUE_JUMP, bundle) | bunny_hood(bundle))) | (can_use(Items.ZELDAS_LULLABY, bundle) & can_use(Items.HOOKSHOT, bundle))),
    ])

    # Spirit Temple Shortcut Switch  (upstream RR_SPIRIT_TEMPLE_SHORTCUT_SWITCH, SCENE_SPIRIT_TEMPLE)
    # Events
    add_events(Regions.SPIRIT_TEMPLE_SHORTCUT_SWITCH, world, [
        (EventLocations.SPIRIT_TEMPLE_SHORTCUT_SWITCH_SPIRIT_STATUE_SOUTH_DOOR, Events.SPIRIT_STATUE_SOUTH_DOOR,
         lambda bundle: spirit_shared(bundle, Regions.SPIRIT_TEMPLE_SHORTCUT_SWITCH, lambda bundle: can_use(Items.MEGATON_HAMMER, bundle), any_age=False)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_SHORTCUT_SWITCH, world, [
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM_ADULT,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_INNER_LEFT_HAND,
         lambda bundle: True_()),
    ])

    # Spirit Temple Shortcut  (upstream RR_SPIRIT_TEMPLE_SHORTCUT, SCENE_SPIRIT_TEMPLE)
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_SHORTCUT, world, [
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_FOYER,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle) & can_use(Items.MEGATON_HAMMER, bundle)),
    ])

    # Spirit Temple Pot Stairs  (upstream RR_SPIRIT_TEMPLE_POT_STAIRS, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_POT_STAIRS, world, [
        (Locations.SPIRIT_TEMPLE_BEAMOS_HALL_POT1,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_POT_STAIRS, world, [
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM_ADULT,
         lambda bundle: small_keys_scene("SCENE_SPIRIT_TEMPLE", 4, bundle)),
        (Regions.SPIRIT_TEMPLE_BEAMOS_PITS,
         lambda bundle: True_()),
    ])

    # Spirit Temple Beamos Pits  (upstream RR_SPIRIT_TEMPLE_BEAMOS_PITS, SCENE_SPIRIT_TEMPLE)
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_BEAMOS_PITS, world, [
        (Regions.SPIRIT_TEMPLE_POT_STAIRS,
         lambda bundle: can_kill_enemy(bundle, Enemies.BEAMOS)),
        (Regions.SPIRIT_TEMPLE_4_ARMOS,
         lambda bundle: can_kill_enemy(bundle, Enemies.BEAMOS)),
        (Regions.SPIRIT_TEMPLE_BIG_WALL_BASE,
         lambda bundle: small_keys_scene("SCENE_SPIRIT_TEMPLE", 5, bundle)),
    ])

    # Spirit Temple 4 Armos  (upstream RR_SPIRIT_TEMPLE_4_ARMOS, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_4_ARMOS, world, [
        (Locations.SPIRIT_TEMPLE_FOUR_ARMOS_ROOM_SUNS_SONG_FAIRY,
         lambda bundle: has_explosives(bundle) & can_use(Items.SUNS_SONG, bundle)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_4_ARMOS, world, [
        (Regions.SPIRIT_TEMPLE_BEAMOS_PITS,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_4_ARMOS_SIDE_ROOM,
         lambda bundle: can_use(Items.MIRROR_SHIELD, bundle) | sunlight_arrows(bundle)),
        (Regions.SPIRIT_TEMPLE_CHEST_STAIRS,
         lambda bundle: True_()),
    ])

    # Spirit Temple 4 Armos Side Room  (upstream RR_SPIRIT_TEMPLE_4_ARMOS_SIDE_ROOM, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_4_ARMOS_SIDE_ROOM, world, [
        (Locations.SPIRIT_TEMPLE_NEAR_FOUR_ARMOS_CHEST,
         lambda bundle: has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_4_ARMOS_SIDE_ROOM, world, [
        (Regions.SPIRIT_TEMPLE_4_ARMOS,
         lambda bundle: True_()),
    ])

    # Spirit Temple Chest Stairs  (upstream RR_SPIRIT_TEMPLE_CHEST_STAIRS, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_CHEST_STAIRS, world, [
        (Locations.SPIRIT_TEMPLE_HALLWAY_LEFT_INVISIBLE_CHEST,
         lambda bundle: (can_do_trick(Tricks.LENS_SPIRIT, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & has_open_chest(bundle)),
        (Locations.SPIRIT_TEMPLE_HALLWAY_RIGHT_INVISIBLE_CHEST,
         lambda bundle: (can_do_trick(Tricks.LENS_SPIRIT, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_CHEST_STAIRS, world, [
        (Regions.SPIRIT_TEMPLE_4_ARMOS,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_ADULT_THRONE,
         lambda bundle: True_()),
    ])

    # Spirit Temple Adult Throne  (upstream RR_SPIRIT_TEMPLE_ADULT_THRONE, SCENE_SPIRIT_TEMPLE)
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_ADULT_THRONE, world, [
        (Regions.SPIRIT_TEMPLE_CHEST_STAIRS,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.IRON_KNUCKLE))),
        (Regions.SPIRIT_TEMPLE_LEFT_HAND_EXIT,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.IRON_KNUCKLE))),
    ])

    # Spirit Temple Left Hand Exit  (upstream RR_SPIRIT_TEMPLE_LEFT_HAND_EXIT, SCENE_SPIRIT_TEMPLE)
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_LEFT_HAND_EXIT, world, [
        (Regions.SPIRIT_TEMPLE_ADULT_THRONE,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_OUTER_LEFT_HAND,
         lambda bundle: True_()),
    ])

    # Spirit Temple Outer Left Hand  (upstream RR_SPIRIT_TEMPLE_OUTER_LEFT_HAND, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_OUTER_LEFT_HAND, world, [
        (Locations.SPIRIT_TEMPLE_MIRROR_SHIELD_CHEST,
         lambda bundle: can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_OUTER_LEFT_HAND, world, [
        (Regions.SPIRIT_TEMPLE_LEFT_HAND_EXIT,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_OUTER_RIGHT_HAND,
         lambda bundle: can_use(Items.LONGSHOT, bundle)),
        (Regions.DESERT_COLOSSUS,
         lambda bundle: True_()),
    ])

    # Spirit Temple Big Wall Base  (upstream RR_SPIRIT_TEMPLE_BIG_WALL_BASE, SCENE_SPIRIT_TEMPLE)
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_BIG_WALL_BASE, world, [
        (Regions.SPIRIT_TEMPLE_BEAMOS_PITS,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_BIG_WALL_UPPER,
         lambda bundle: (can_do_trick(Tricks.SPIRIT_WALL, bundle) | (can_avoid_enemy(bundle, Enemies.BEAMOS, EnemyDistance.CLOSE, True, 2) & can_pass_enemy(bundle, Enemies.WALLTULA, EnemyDistance.BOOMERANG))) & (has_climb(bundle) | can_use(Items.LONGSHOT, bundle))),
    ])

    # Spirit Temple Big Wall Upper  (upstream RR_SPIRIT_TEMPLE_BIG_WALL_UPPER, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_BIG_WALL_UPPER, world, [
        (Locations.SPIRIT_TEMPLE_ADULT_CLIMB_LEFT_HEART,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
        (Locations.SPIRIT_TEMPLE_ADULT_CLIMB_RIGHT_HEART,
         lambda bundle: can_use(Items.HOOKSHOT, bundle)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_BIG_WALL_UPPER, world, [
        (Regions.SPIRIT_TEMPLE_BIG_WALL_BASE,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_4F_CENTRAL,
         lambda bundle: True_()),
    ])

    # Spirit Temple 4F Central  (upstream RR_SPIRIT_TEMPLE_4F_CENTRAL, SCENE_SPIRIT_TEMPLE)
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_4F_CENTRAL, world, [
        (Regions.SPIRIT_TEMPLE_BIG_WALL_UPPER,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_FAKE_DOORS_ROOM,
         lambda bundle: can_use(Items.ZELDAS_LULLABY, bundle)),
        (Regions.SPIRIT_TEMPLE_BIG_MIRROR_ROOM,
         lambda bundle: True_()),
    ])

    # Spirit Temple Fake Doors Room  (upstream RR_SPIRIT_TEMPLE_FAKE_DOORS_ROOM, SCENE_SPIRIT_TEMPLE)
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_FAKE_DOORS_ROOM, world, [
        (Locations.SPIRIT_TEMPLE_BOSS_KEY_CHEST,
         lambda bundle: ((take_damage(bundle) & can_do_trick(Tricks.FIRE_RINGS, bundle)) | (any_age_time(bundle, lambda bundle: can_hit_eye_targets(bundle) & can_avoid_enemy(bundle, Enemies.TORCH_SLUG, EnemyDistance.CLOSE, True, 4)) & can_use(Items.HOOKSHOT, bundle))) & can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_FAKE_DOORS_ROOM, world, [
        (Regions.SPIRIT_TEMPLE_4F_CENTRAL,
         lambda bundle: True_()),
    ])

    # Spirit Temple Big Mirror Room  (upstream RR_SPIRIT_TEMPLE_BIG_MIRROR_ROOM, SCENE_SPIRIT_TEMPLE)
    # Events
    add_events(Regions.SPIRIT_TEMPLE_BIG_MIRROR_ROOM, world, [
        (EventLocations.SPIRIT_TEMPLE_BIG_MIRROR_ROOM_SPIRIT_4F_SWITCH, Events.SPIRIT_4F_SWITCH,
         lambda bundle: can_jump_slash(bundle) | has_explosives(bundle) | can_use(Items.GIANTS_KNIFE, bundle) | (can_do_trick(Tricks.ITEM_EXTENSION, bundle) & ((is_adult(bundle) & can_use(Items.HOOKSHOT, bundle)) | can_use(Items.FAIRY_BOW, bundle) | can_use(Items.FAIRY_SLINGSHOT, bundle)))),
        (EventLocations.SPIRIT_TEMPLE_BIG_MIRROR_ROOM_SPIRIT_PLATFORM_LOWERED, Events.SPIRIT_PLATFORM_LOWERED,
         lambda bundle: (has_item(Events.SPIRIT_PUSHED_4F_MIRRORS, bundle) & can_use(Items.MIRROR_SHIELD, bundle)) | sunlight_arrows(bundle)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_BIG_MIRROR_ROOM, world, [
        (Regions.SPIRIT_TEMPLE_4F_CENTRAL,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_BIG_MIRROR_CAVE,
         lambda bundle: has_item(Events.SPIRIT_4F_SWITCH, bundle)),
        (Regions.SPIRIT_TEMPLE_PLATFORM,
         lambda bundle: has_item(Events.SPIRIT_PLATFORM_LOWERED, bundle)),
    ])

    # Spirit Temple Big Mirror Cave  (upstream RR_SPIRIT_TEMPLE_BIG_MIRROR_CAVE, SCENE_SPIRIT_TEMPLE)
    # Events
    add_events(Regions.SPIRIT_TEMPLE_BIG_MIRROR_CAVE, world, [
        (EventLocations.SPIRIT_TEMPLE_BIG_MIRROR_CAVE_SPIRIT_4F_SWITCH, Events.SPIRIT_4F_SWITCH,
         lambda bundle: has_explosives(bundle)),
        (EventLocations.SPIRIT_TEMPLE_BIG_MIRROR_CAVE_SPIRIT_PUSHED_4F_MIRRORS, Events.SPIRIT_PUSHED_4F_MIRRORS,
         lambda bundle: has_explosives(bundle) & has_grab(bundle)),
    ])
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_BIG_MIRROR_CAVE, world, [
        (Locations.SPIRIT_TEMPLE_TOPMOST_CHEST,
         lambda bundle: ((is_adult(bundle) & can_use(Items.MIRROR_SHIELD, bundle)) | sunlight_arrows(bundle)) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_BIG_MIRROR_CAVE, world, [
        (Regions.SPIRIT_TEMPLE_BIG_MIRROR_ROOM,
         lambda bundle: True_()),
    ])

    # Spirit Temple Lowered Platform  (upstream RR_SPIRIT_TEMPLE_PLATFORM, SCENE_SPIRIT_TEMPLE)
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_PLATFORM, world, [
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM_CHILD,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_INNER_WEST_HAND,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM_ADULT,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_INNER_LEFT_HAND,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_STATUE_HEAD,
         lambda bundle: has_item(Events.SPIRIT_PUSHED_4F_MIRRORS, bundle) & any_age_time(bundle, lambda bundle: can_use(Items.MIRROR_SHIELD, bundle)) & can_use(Items.HOOKSHOT, bundle)),
    ])

    # Spirit Temple Statue Head  (upstream RR_SPIRIT_TEMPLE_STATUE_HEAD, SCENE_SPIRIT_TEMPLE)
    # Events
    add_events(Regions.SPIRIT_TEMPLE_STATUE_HEAD, world, [
        (EventLocations.SPIRIT_TEMPLE_STATUE_HEAD_REVERSE_SPIRIT_CHILD, Events.REVERSE_SPIRIT_CHILD,
         lambda bundle: is_child(bundle)),
        (EventLocations.SPIRIT_TEMPLE_STATUE_HEAD_REVERSE_SPIRIT_ADULT, Events.REVERSE_SPIRIT_ADULT,
         lambda bundle: is_adult(bundle)),
    ])
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_STATUE_HEAD, world, [
        # DEFERRED RC_SPIRIT_BOSS_KEY_HINT: true
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_STATUE_HEAD, world, [
        (Regions.SPIRIT_TEMPLE_STATUE_ROOM,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_INNER_WEST_HAND,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle) | (bunny_hood(bundle) & can_jump_slash(bundle) & is_adult(bundle))),
        (Regions.SPIRIT_TEMPLE_INNER_LEFT_HAND,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle) | (bunny_hood(bundle) & can_jump_slash(bundle) & is_adult(bundle))),
        (Regions.SPIRIT_TEMPLE_PLATFORM,
         lambda bundle: has_item(Events.SPIRIT_PLATFORM_LOWERED, bundle) & (can_use(Items.HOVER_BOOTS, bundle) | can_use(Items.HOOKSHOT, bundle) | (is_adult(bundle) & bunny_hood(bundle)))),
        (Regions.SPIRIT_TEMPLE_BOSS_ENTRYWAY,
         lambda bundle: True_()),
    ])

    # Spirit Temple Boss Entryway  (upstream RR_SPIRIT_TEMPLE_BOSS_ENTRYWAY, SCENE_SPIRIT_TEMPLE)
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_BOSS_ENTRYWAY, world, [
        (Regions.SPIRIT_TEMPLE_STATUE_HEAD,
         lambda bundle: True_()),
        (Regions.SPIRIT_TEMPLE_BOSS_ROOM,
         lambda bundle: has_item(Items.SPIRIT_TEMPLE_BOSS_KEY, bundle)),
    ])

    # Spirit Temple Boss Room  (upstream RR_SPIRIT_TEMPLE_BOSS_ROOM, SCENE_SPIRIT_TEMPLE_BOSS)
    # Events
    add_events(Regions.SPIRIT_TEMPLE_BOSS_ROOM, world, [
        (EventLocations.SPIRIT_TEMPLE_BOSS_ROOM_SPIRIT_TEMPLE_CLEAR, Events.SPIRIT_TEMPLE_COMPLETED,
         lambda bundle: (has_climb(bundle) | can_use(Items.HOOKSHOT, bundle)) & can_kill_enemy(bundle, Enemies.TWINROVA)),
    ])
    # Locations
    add_locations(Regions.SPIRIT_TEMPLE_BOSS_ROOM, world, [
        (Locations.SPIRIT_TEMPLE_TWINROVA_HEART_CONTAINER,
         lambda bundle: has_item(Events.SPIRIT_TEMPLE_COMPLETED, bundle)),
        (Locations.TWINROVA,
         lambda bundle: has_item(Events.SPIRIT_TEMPLE_COMPLETED, bundle)),
    ])
    # Connections
    connect_regions(Regions.SPIRIT_TEMPLE_BOSS_ROOM, world, [
        (Regions.SPIRIT_TEMPLE_BOSS_ENTRYWAY,
         lambda bundle: False_()),
        (Regions.DESERT_COLOSSUS,
         lambda bundle: has_item(Events.SPIRIT_TEMPLE_COMPLETED, bundle)),
    ])

# ---- summary
# notes: ['TODO feature 4.1']
# helpers not in LogicHelpers yet: ['outer_west_hand_logic']
# TODO count: 0
# new regions: []
# events used: ['CAN_FARM_NUTS', 'FORWARDS_SPIRIT_ADULT', 'FORWARDS_SPIRIT_CHILD', 'REVERSE_SPIRIT_ADULT', 'REVERSE_SPIRIT_CHILD', 'SPIRIT_4F_SWITCH', 'SPIRIT_CHILD_SWITCH_BRIDGE', 'SPIRIT_NABOORU_KIDNAPPED', 'SPIRIT_PLATFORM_LOWERED', 'SPIRIT_PUSHED_4F_MIRRORS', 'SPIRIT_SILVER_BOULDERS', 'SPIRIT_SILVER_CHILD', 'SPIRIT_SILVER_RUPEE_BRIDGE_TORCHES', 'SPIRIT_SILVER_SUN', 'SPIRIT_STATUE_SOUTH_DOOR', 'SPIRIT_TEMPLE_COMPLETED']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (18): ['RC_SPIRIT_TEMPLE_LEFT_SNAKE_STATUE', 'RC_SPIRIT_TEMPLE_RIGHT_SNAKE_STATUE', 'RC_SPIRIT_W_HIGH_CHILD_SILVER', 'RC_SPIRIT_W_LOW_CHILD_SILVER', 'RC_SPIRIT_E_LOW_CHILD_SILVER', 'RC_SPIRIT_E_HIGH_CHILD_SILVER', 'RC_SPIRIT_TORCH_CHILD_SILVER', 'RC_SPIRIT_AIRBORNE_BOULDER_SILVER', 'RC_SPIRIT_NW_BOULDER_SILVER', 'RC_SPIRIT_SW_BOULDER_SILVER', 'RC_SPIRIT_SE_BOULDER_SILVER', 'RC_SPIRIT_NE_BOULDER_SILVER', 'RC_SPIRIT_NEAR_LIGHT_SUN_SILVER', 'RC_SPIRIT_AIRBORNE_SUN_SILVER', 'RC_SPIRIT_MID_PLATFORM_SUN_SILVER', 'RC_SPIRIT_NEAR_DOOR_SUN_SILVER', 'RC_SPIRIT_NEAR_CHEST_SUN_SILVER', 'RC_SPIRIT_BOSS_KEY_HINT']
