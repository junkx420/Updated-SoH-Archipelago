"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/kokiri_forest.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    KOKIRI_FOREST_PLANT_KOKIRI_FOREST_BEAN = "Kokiri Forest Plant Kokiri Forest Bean"
    KOKIRI_FOREST_FAIRY_ACCESS = "Kokiri Forest Fairy Access"
    KOKIRI_FOREST_SHOWED_MIDO_SWORD_AND_SHIELD = "Kokiri Forest Showed Mido Sword And Shield"
    KF_OUTSIDE_LOST_WOODS_FAIRY_ACCESS = "KF Outside Lost Woods Fairy Access"
    KF_OUTSIDE_DEKU_TREE_STICK_ACCESS = "KF Outside Deku Tree Stick Access"
    KF_OUTSIDE_DEKU_TREE_NUT_ACCESS = "KF Outside Deku Tree Nut Access"
    KF_OUTSIDE_DEKU_TREE_FAIRY_ACCESS = "KF Outside Deku Tree Fairy Access"
    KF_OUTSIDE_DEKU_TREE_SHOWED_MIDO_SWORD_AND_SHIELD = "KF Outside Deku Tree Showed Mido Sword And Shield"


def set_region_rules(world: "SohWorld") -> None:

    # Kokiri Forest  (upstream RR_KOKIRI_FOREST, SCENE_KOKIRI_FOREST)
    # Events
    add_events(Regions.KOKIRI_FOREST, world, [
        (EventLocations.KOKIRI_FOREST_PLANT_KOKIRI_FOREST_BEAN, Events.PLANT_KOKIRI_FOREST_BEAN,
         lambda bundle: can_plant_bean(bundle, Items.KOKIRI_FOREST_BEAN_SOUL)),
        (EventLocations.KOKIRI_FOREST_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: (is_child(bundle) & bean_planted(bundle, Events.PLANT_KOKIRI_FOREST_BEAN) & can_use(Items.SONG_OF_STORMS, bundle))),
        (EventLocations.KOKIRI_FOREST_SHOWED_MIDO_SWORD_AND_SHIELD, Events.SHOWED_MIDO_SWORD_AND_SHIELD,
         lambda bundle: is_child(bundle) & has_speak(bundle, "KOKIRI") & can_use(Items.KOKIRI_SWORD, bundle) & can_use(Items.DEKU_SHIELD, bundle)),
    ])
    # Locations
    add_locations(Regions.KOKIRI_FOREST, world, [
        (Locations.KF_GS_KNOW_IT_ALL_HOUSE,
         lambda bundle: is_child(bundle) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.CLOSE) & can_get_nighttime_gs(bundle)),
        (Locations.KF_GS_BEAN_PATCH,
         lambda bundle: can_spawn_soil_skull(bundle, Items.KOKIRI_FOREST_BEAN_SOUL) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.CLOSE)),
        (Locations.KF_GS_HOUSE_OF_TWINS,
         lambda bundle: is_adult(bundle) & can_get_nighttime_gs(bundle) & (can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.BOOMERANG) | (can_do_trick(Tricks.KF_ADULT_GS, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.SHORT_JUMPSLASH)))),
        (Locations.KF_BEAN_SPROUT_FAIRY1,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_KOKIRI_FOREST_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.KF_BEAN_SPROUT_FAIRY2,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_KOKIRI_FOREST_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.KF_BEAN_SPROUT_FAIRY3,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_KOKIRI_FOREST_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.KF_BRIDGE_RUPEE,
         lambda bundle: is_child(bundle)),
        (Locations.KF_BEHIND_MIDOS_HOUSE_RUPEE,
         lambda bundle: is_child(bundle)),
        (Locations.KF_SOUTH_GRASS_WEST_RUPEE,
         lambda bundle: is_child(bundle)),
        (Locations.KF_SOUTH_GRASS_EAST_RUPEE,
         lambda bundle: is_child(bundle)),
        (Locations.KF_NORTH_GRASS_WEST_RUPEE,
         lambda bundle: is_child(bundle)),
        (Locations.KF_NORTH_GRASS_EAST_RUPEE,
         lambda bundle: is_child(bundle)),
        (Locations.KF_BEAN_PLATFORM_RUPEE1,
         lambda bundle: is_adult(bundle) & can_use(Items.BOOMERANG, bundle)),
        (Locations.KF_BEAN_PLATFORM_RUPEE2,
         lambda bundle: is_adult(bundle) & can_use(Items.BOOMERANG, bundle)),
        (Locations.KF_BEAN_PLATFORM_RUPEE6,
         lambda bundle: is_adult(bundle) & can_use(Items.BOOMERANG, bundle)),
        (Locations.KF_SARIAS_ROOF_WEST_HEART,
         lambda bundle: is_child(bundle)),
        (Locations.KF_SARIAS_ROOF_EAST_HEART,
         lambda bundle: is_child(bundle)),
        (Locations.KF_SARIAS_ROOF_NORTH_HEART,
         lambda bundle: is_child(bundle)),
        (Locations.KF_CHILD_GRASS1,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_CHILD_GRASS2,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_CHILD_GRASS3,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_CHILD_GRASS4,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_CHILD_GRASS5,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_CHILD_GRASS6,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_CHILD_GRASS7,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_CHILD_GRASS8,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_CHILD_GRASS9,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_CHILD_GRASS10,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_CHILD_GRASS11,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_CHILD_GRASS12,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS1,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS2,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS3,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS4,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS5,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS6,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS7,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS8,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS9,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS10,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS11,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS12,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS13,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS14,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS15,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS16,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS17,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS18,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS19,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_ADULT_GRASS20,
         lambda bundle: is_adult(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_CIRCLE_ROCK_1,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.KF_CIRCLE_ROCK_2,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.KF_CIRCLE_ROCK_3,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.KF_CIRCLE_ROCK_4,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.KF_CIRCLE_ROCK_5,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.KF_CIRCLE_ROCK_6,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.KF_CIRCLE_ROCK_7,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.KF_CIRCLE_ROCK_8,
         lambda bundle: can_break_rocks(bundle)),
        (Locations.KF_ROCK_BY_SARIAS_HOUSE,
         lambda bundle: is_child(bundle) & can_break_rocks(bundle)),
        (Locations.KF_ROCK_BEHIND_SARIAS_HOUSE,
         lambda bundle: is_child(bundle) & can_break_rocks(bundle)),
        (Locations.KF_ROCK_BY_MIDOS_HOUSE,
         lambda bundle: is_child(bundle) & can_break_rocks(bundle)),
        (Locations.KF_ROCK_BY_KNOW_IT_ALLS_HOUSE,
         lambda bundle: is_child(bundle) & can_break_rocks(bundle)),
        (Locations.KF_DEKU_TREE_RECTANGLE_SIGN,
         lambda bundle: can_read(bundle)),
        (Locations.KF_STEPPING_STONES_RECTANGLE_SIGN,
         lambda bundle: can_read(bundle)),
        (Locations.KF_LINKS_HOUSE_RECTANGLE_SIGN,
         lambda bundle: can_read(bundle)),
        (Locations.KF_FIRST_TRAINING_CENTER_RECTANGLE_SIGN,
         lambda bundle: is_child(bundle) & can_read(bundle)),
        (Locations.KF_SECOND_TRAINING_CENTER_RECTANGLE_SIGN,
         lambda bundle: is_child(bundle) & can_read(bundle)),
        (Locations.KF_CRAWL_RECTANGLE_RECTANGLE_SIGN,
         lambda bundle: is_child(bundle) & can_read(bundle)),
        (Locations.KF_LOST_WOODS_RECTANGLE_SIGN,
         lambda bundle: can_read(bundle)),
        (Locations.KF_HOUSE_OF_TWINS_ARROW_SIGN,
         lambda bundle: can_read(bundle)),
        (Locations.KF_SHOP_ARROW_SIGN,
         lambda bundle: can_read(bundle)),
        (Locations.KF_SARIAS_HOUSE_ARROW_SIGN,
         lambda bundle: can_read(bundle)),
        (Locations.KF_MIDOS_HOUSE_ARROW_SIGN,
         lambda bundle: can_read(bundle)),
        (Locations.KF_TRAINING_CENTER_ENTRANCE_ARROW_SIGN,
         lambda bundle: is_child(bundle) & can_read(bundle)),
        (Locations.KF_INNER_TRAINING_CENTER_ARROW_SIGN,
         lambda bundle: is_child(bundle) & can_read(bundle)),
        (Locations.KF_KNOW_IT_ALL_BROTHERS_HOUSE_ARROW_SIGN,
         lambda bundle: can_read(bundle)),
        (Locations.KF_WONDER_TRAINING_1,
         lambda bundle: is_child(bundle)),
        (Locations.KF_WONDER_TRAINING_2,
         lambda bundle: is_child(bundle)),
        (Locations.KF_WONDER_TRAINING_3,
         lambda bundle: is_child(bundle)),
        (Locations.KF_WONDER_SIGN,
         lambda bundle: is_child(bundle) & can_jump_slash_except_hammer(bundle)),
        (Locations.KF_WONDER_PLATFORMS_1,
         lambda bundle: is_child(bundle)),
        (Locations.KF_WONDER_PLATFORMS_2,
         lambda bundle: is_child(bundle)),
        # DEFERRED RC_MIDO_HINT: !ctx->GetOption(RSK_FOREST).Is(RO_CLOSED_FOREST_OFF) && logic->IsChild && logic->HasItem(RG_SPEAK_KOKIRI)
    ])
    # Connections
    connect_regions(Regions.KOKIRI_FOREST, world, [
        (Regions.KF_BOULDER_LOOP,
         lambda bundle: can_crawl(bundle)),
        (Regions.KF_LINKS_PORCH,
         lambda bundle: has_climb(bundle) | can_use(Items.HOVER_BOOTS, bundle) | ((is_child(bundle) | can_kill_enemy(bundle, Enemies.DEKU_BABA) | has_item(Events.FOREST_TEMPLE_COMPLETED, bundle)) & can_climb_ladder(bundle))),
        (Regions.KF_MIDOS_HOUSE,
         lambda bundle: True_()),
        (Regions.KF_SARIAS_HOUSE,
         lambda bundle: True_()),
        (Regions.KF_HOUSE_OF_TWINS,
         lambda bundle: True_()),
        (Regions.KF_KNOW_IT_ALL_HOUSE,
         lambda bundle: True_()),
        (Regions.KF_KOKIRI_SHOP,
         lambda bundle: True_()),
        (Regions.KF_OUTSIDE_DEKU_TREE,
         lambda bundle: (is_adult(bundle) & (can_pass_enemy(bundle, Enemies.BIG_SKULLTULA) | has_item(Events.FOREST_TEMPLE_COMPLETED, bundle))) | has_item(Events.SHOWED_MIDO_SWORD_AND_SHIELD, bundle)),
        (Regions.KF_OUTSIDE_LOST_WOODS,
         lambda bundle: has_climb(bundle) | can_use(Items.HOOKSHOT, bundle) | (is_adult(bundle) & (bean_planted(bundle, Events.PLANT_KOKIRI_FOREST_BEAN) | can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle)))),
        (Regions.KF_RUPEE_ALCOVE,
         lambda bundle: is_adult(bundle) & bean_planted(bundle, Events.PLANT_KOKIRI_FOREST_BEAN)),
        (Regions.LW_BRIDGE_FROM_FOREST,
         lambda bundle: is_adult(bundle) | True_(options=[OptionFilter(ClosedForest, ClosedForest.option_on, "ne")]) | has_item(Events.DEKU_TREE_COMPLETED, bundle)),
    ])

    # KF Outside Lost Woods  (upstream RR_KF_OUTSIDE_LOST_WOODS, SCENE_KOKIRI_FOREST)
    # Events
    add_events(Regions.KF_OUTSIDE_LOST_WOODS, world, [
        (EventLocations.KF_OUTSIDE_LOST_WOODS_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
    ])
    # Locations
    add_locations(Regions.KF_OUTSIDE_LOST_WOODS, world, [
        (Locations.KF_BEAN_PLATFORM_RUPEE1,
         lambda bundle: is_adult(bundle) & can_use(Items.BOOMERANG, bundle)),
        (Locations.KF_BEAN_PLATFORM_RUPEE2,
         lambda bundle: is_adult(bundle) & can_use(Items.BOOMERANG, bundle)),
        (Locations.KF_BEAN_PLATFORM_RUPEE3,
         lambda bundle: is_adult(bundle) & can_use(Items.BOOMERANG, bundle)),
        (Locations.KF_BEAN_PLATFORM_RUPEE4,
         lambda bundle: is_adult(bundle) & can_use(Items.BOOMERANG, bundle)),
        (Locations.KF_BEAN_PLATFORM_RUPEE5,
         lambda bundle: is_adult(bundle) & can_use(Items.BOOMERANG, bundle)),
        (Locations.KF_BEAN_PLATFORM_RUPEE6,
         lambda bundle: is_adult(bundle) & can_use(Items.BOOMERANG, bundle)),
        (Locations.KF_BEAN_PLATFORM_RED_RUPEE,
         lambda bundle: is_adult(bundle) & can_use(Items.BOOMERANG, bundle)),
        (Locations.KF_LOST_WOODS_ARROW_SIGN,
         lambda bundle: is_child(bundle) & can_read(bundle)),
        (Locations.KF_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
        (Locations.KF_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_KF_GOSSIP_STONE: true
    ])
    # Connections
    connect_regions(Regions.KF_OUTSIDE_LOST_WOODS, world, [
        (Regions.KOKIRI_FOREST,
         lambda bundle: True_()),
        (Regions.THE_LOST_WOODS,
         lambda bundle: True_()),
        (Regions.KF_RUPEE_ALCOVE,
         lambda bundle: (is_adult(bundle) & can_use(Items.HOVER_BOOTS, bundle)) | can_middair_ground_jump(bundle)),
        (Regions.KF_STORMS_GROTTO,
         lambda bundle: can_open_storms_grotto(bundle)),
    ])

    # KF Alcove  (upstream RR_KF_RUPEE_ALCOVE, SCENE_KOKIRI_FOREST)
    # Locations
    add_locations(Regions.KF_RUPEE_ALCOVE, world, [
        (Locations.KF_BEAN_PLATFORM_RUPEE1,
         lambda bundle: is_adult(bundle)),
        (Locations.KF_BEAN_PLATFORM_RUPEE2,
         lambda bundle: is_adult(bundle)),
        (Locations.KF_BEAN_PLATFORM_RUPEE3,
         lambda bundle: is_adult(bundle)),
        (Locations.KF_BEAN_PLATFORM_RUPEE4,
         lambda bundle: is_adult(bundle)),
        (Locations.KF_BEAN_PLATFORM_RUPEE5,
         lambda bundle: is_adult(bundle)),
        (Locations.KF_BEAN_PLATFORM_RUPEE6,
         lambda bundle: is_adult(bundle)),
        (Locations.KF_BEAN_PLATFORM_RED_RUPEE,
         lambda bundle: is_adult(bundle)),
    ])
    # Connections
    connect_regions(Regions.KF_RUPEE_ALCOVE, world, [
        (Regions.KOKIRI_FOREST,
         lambda bundle: True_()),
    ])

    # KF Boulder Loop  (upstream RR_KF_BOULDER_LOOP, SCENE_KOKIRI_FOREST)
    # Locations
    add_locations(Regions.KF_BOULDER_LOOP, world, [
        (Locations.KF_KOKIRI_SWORD_CHEST,
         lambda bundle: is_child(bundle) & can_open_large_chest(bundle)),
        (Locations.KF_BOULDER_MAZE_FIRST_RUPEE,
         lambda bundle: is_child(bundle)),
        (Locations.KF_BOULDER_MAZE_SECOND_RUPEE,
         lambda bundle: is_child(bundle)),
        (Locations.KF_CHILD_GRASS_MAZE1,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_CHILD_GRASS_MAZE2,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_CHILD_GRASS_MAZE3,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (Locations.KF_AFTER_CRAWLSPACE_RECTANGLE_SIGN,
         lambda bundle: is_child(bundle) & can_read(bundle)),
        (Locations.KF_BOULDER_MAZE_RECTANGLE_SIGN,
         lambda bundle: is_child(bundle) & can_read(bundle)),
        (Locations.KF_WONDER_CRAWL_GRASS_1,
         lambda bundle: is_child(bundle)),
        (Locations.KF_WONDER_CRAWL_GRASS_2,
         lambda bundle: is_child(bundle)),
    ])
    # Connections
    connect_regions(Regions.KF_BOULDER_LOOP, world, [
        (Regions.KOKIRI_FOREST,
         lambda bundle: can_crawl(bundle)),
    ])

    # KF Outside Deku Tree  (upstream RR_KF_OUTSIDE_DEKU_TREE, SCENE_KOKIRI_FOREST)
    # Events
    add_events(Regions.KF_OUTSIDE_DEKU_TREE, world, [
        (EventLocations.KF_OUTSIDE_DEKU_TREE_STICK_ACCESS, Events.CAN_FARM_STICKS,
         lambda bundle: can_get_deku_baba_sticks(bundle)),
        (EventLocations.KF_OUTSIDE_DEKU_TREE_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_get_deku_baba_nuts(bundle)),
        (EventLocations.KF_OUTSIDE_DEKU_TREE_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
        (EventLocations.KF_OUTSIDE_DEKU_TREE_SHOWED_MIDO_SWORD_AND_SHIELD, Events.SHOWED_MIDO_SWORD_AND_SHIELD,
         lambda bundle: is_child(bundle) & has_speak(bundle, "KOKIRI") & can_use(Items.KOKIRI_SWORD, bundle) & can_use(Items.DEKU_SHIELD, bundle)),
    ])
    # Locations
    add_locations(Regions.KF_OUTSIDE_DEKU_TREE, world, [
        (Locations.KF_DEKU_TREE_LEFT_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
        (Locations.KF_DEKU_TREE_LEFT_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.KF_DEKU_TREE_RIGHT_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
        (Locations.KF_DEKU_TREE_RIGHT_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_KF_DEKU_TREE_LEFT_GOSSIP_STONE: true
        # DEFERRED RC_KF_DEKU_TREE_RIGHT_GOSSIP_STONE: true
    ])
    # Connections
    connect_regions(Regions.KF_OUTSIDE_DEKU_TREE, world, [
        (Regions.DEKU_TREE_ENTRYWAY,
         lambda bundle: is_child(bundle) | (False_() & (True_(options=[OptionFilter(ClosedForest, ClosedForest.option_off)]) | has_item(Events.SHOWED_MIDO_SWORD_AND_SHIELD, bundle)))),
        (Regions.KOKIRI_FOREST,
         lambda bundle: (is_adult(bundle) & (can_pass_enemy(bundle, Enemies.BIG_SKULLTULA) | has_item(Events.DEKU_TREE_COMPLETED, bundle))) | True_(options=[OptionFilter(ClosedForest, ClosedForest.option_off)]) | has_item(Events.SHOWED_MIDO_SWORD_AND_SHIELD, bundle)),
    ])

    # KF Link's Porch  (upstream RR_KF_LINKS_PORCH, SCENE_KOKIRI_FOREST)
    # Connections
    connect_regions(Regions.KF_LINKS_PORCH, world, [
        (Regions.KOKIRI_FOREST,
         lambda bundle: True_()),
        (Regions.KF_LINKS_HOUSE,
         lambda bundle: True_()),
    ])

    # KF Link's House  (upstream RR_KF_LINKS_HOUSE, SCENE_LINKS_HOUSE)
    # Locations
    add_locations(Regions.KF_LINKS_HOUSE, world, [
        (Locations.KF_LINKS_HOUSE_COW,
         lambda bundle: is_adult(bundle) & can_use(Items.EPONAS_SONG, bundle) & has_item(Events.GOTTEN_LINKS_COW, bundle)),
        (Locations.KF_LINKS_HOUSE_POT,
         lambda bundle: can_break_pots(bundle)),
        (Locations.KF_LINKS_HOUSE_SIGN,
         lambda bundle: can_read(bundle)),
    ])
    # Connections
    connect_regions(Regions.KF_LINKS_HOUSE, world, [
        (Regions.KF_LINKS_PORCH,
         lambda bundle: True_()),
    ])

    # KF Mido's House  (upstream RR_KF_MIDOS_HOUSE, SCENE_MIDOS_HOUSE)
    # Locations
    add_locations(Regions.KF_MIDOS_HOUSE, world, [
        (Locations.KF_MIDO_TOP_LEFT_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.KF_MIDO_TOP_RIGHT_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.KF_MIDO_BOTTOM_LEFT_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.KF_MIDO_BOTTOM_RIGHT_CHEST,
         lambda bundle: has_open_chest(bundle)),
        # DEFERRED RC_MIDO_HINT: logic->Get(LOGIC_SHOWED_MIDO_SWORD_AND_SHIELD) && logic->IsChild && logic->HasItem(RG_SPEAK_KOKIRI)
    ])
    # Connections
    connect_regions(Regions.KF_MIDOS_HOUSE, world, [
        (Regions.KOKIRI_FOREST,
         lambda bundle: True_()),
    ])

    # KF Saria's House  (upstream RR_KF_SARIAS_HOUSE, SCENE_SARIAS_HOUSE)
    # Locations
    add_locations(Regions.KF_SARIAS_HOUSE, world, [
        (Locations.KF_SARIAS_HOUSE_TOP_LEFT_HEART,
         lambda bundle: True_()),
        (Locations.KF_SARIAS_HOUSE_TOP_RIGHT_HEART,
         lambda bundle: True_()),
        (Locations.KF_SARIAS_HOUSE_BOTTOM_LEFT_HEART,
         lambda bundle: True_()),
        (Locations.KF_SARIAS_HOUSE_BOTTOM_RIGHT_HEART,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.KF_SARIAS_HOUSE, world, [
        (Regions.KOKIRI_FOREST,
         lambda bundle: True_()),
    ])

    # KF House of Twins  (upstream RR_KF_HOUSE_OF_TWINS, SCENE_TWINS_HOUSE)
    # Locations
    add_locations(Regions.KF_HOUSE_OF_TWINS, world, [
        (Locations.KF_TWINS_HOUSE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.KF_TWINS_HOUSE_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.KF_HOUSE_OF_TWINS, world, [
        (Regions.KOKIRI_FOREST,
         lambda bundle: True_()),
    ])

    # KF Know It All House  (upstream RR_KF_KNOW_IT_ALL_HOUSE, SCENE_KNOW_IT_ALL_BROS_HOUSE)
    # Locations
    add_locations(Regions.KF_KNOW_IT_ALL_HOUSE, world, [
        (Locations.KF_BROTHERS_HOUSE_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.KF_BROTHERS_HOUSE_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.KF_KNOW_IT_ALL_HOUSE, world, [
        (Regions.KOKIRI_FOREST,
         lambda bundle: True_()),
    ])

    # KF Kokiri Shop  (upstream RR_KF_KOKIRI_SHOP, SCENE_KOKIRI_SHOP)
    # Locations
    add_locations(Regions.KF_KOKIRI_SHOP, world, [
        (Locations.KF_SHOP_ITEM1,
         lambda bundle: has_speak(bundle, "KOKIRI") & can_afford_slot(Locations.KF_SHOP_ITEM1, bundle)),
        (Locations.KF_SHOP_ITEM2,
         lambda bundle: has_speak(bundle, "KOKIRI") & can_afford_slot(Locations.KF_SHOP_ITEM2, bundle)),
        (Locations.KF_SHOP_ITEM3,
         lambda bundle: has_speak(bundle, "KOKIRI") & can_afford_slot(Locations.KF_SHOP_ITEM3, bundle)),
        (Locations.KF_SHOP_ITEM4,
         lambda bundle: has_speak(bundle, "KOKIRI") & can_afford_slot(Locations.KF_SHOP_ITEM4, bundle)),
        (Locations.KF_SHOP_ITEM5,
         lambda bundle: has_speak(bundle, "KOKIRI") & can_afford_slot(Locations.KF_SHOP_ITEM5, bundle)),
        (Locations.KF_SHOP_ITEM6,
         lambda bundle: has_speak(bundle, "KOKIRI") & can_afford_slot(Locations.KF_SHOP_ITEM6, bundle)),
        (Locations.KF_SHOP_ITEM7,
         lambda bundle: has_speak(bundle, "KOKIRI") & can_afford_slot(Locations.KF_SHOP_ITEM7, bundle)),
        (Locations.KF_SHOP_ITEM8,
         lambda bundle: has_speak(bundle, "KOKIRI") & can_afford_slot(Locations.KF_SHOP_ITEM8, bundle)),
        (Locations.KF_WONDER_SHOP,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.KF_KOKIRI_SHOP, world, [
        (Regions.KOKIRI_FOREST,
         lambda bundle: True_()),
    ])

    # KF Storms Grotto  (upstream RR_KF_STORMS_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.KF_STORMS_GROTTO, world, [
        (Locations.KF_STORMS_GROTTO_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.KF_STORMS_GROTTO_FISH,
         lambda bundle: has_bottle(bundle)),
        (Locations.KF_STORMS_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.KF_STORMS_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_KF_STORMS_GROTTO_GOSSIP_STONE: true
        (Locations.KF_STORMS_GROTTO_BEEHIVE_LEFT,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.KF_STORMS_GROTTO_BEEHIVE_RIGHT,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.KF_STORMS_GROTTO_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KF_STORMS_GROTTO_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KF_STORMS_GROTTO_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KF_STORMS_GROTTO_GRASS4,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KF_STORMS_GROTTO_BUTTERFLY_FAIRY,
         lambda bundle: can_use(Items.STICKS, bundle)),
    ])
    # Connections
    connect_regions(Regions.KF_STORMS_GROTTO, world, [
        (Regions.KF_OUTSIDE_LOST_WOODS,
         lambda bundle: True_()),
    ])

# ---- summary
# notes: ['TODO feature 4.1']
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_FAIRIES', 'CAN_FARM_NUTS', 'CAN_FARM_STICKS', 'DEKU_TREE_COMPLETED', 'FOREST_TEMPLE_COMPLETED', 'GOTTEN_LINKS_COW', 'PLANT_KOKIRI_FOREST_BEAN', 'SHOWED_MIDO_SWORD_AND_SHIELD']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (6): ['RC_MIDO_HINT', 'RC_KF_GOSSIP_STONE', 'RC_KF_DEKU_TREE_LEFT_GOSSIP_STONE', 'RC_KF_DEKU_TREE_RIGHT_GOSSIP_STONE', 'RC_MIDO_HINT', 'RC_KF_STORMS_GROTTO_GOSSIP_STONE']
