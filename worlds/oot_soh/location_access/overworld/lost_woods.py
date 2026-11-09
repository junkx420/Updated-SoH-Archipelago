"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/lost_woods.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    THE_LOST_WOODS_PLANT_LOST_WOODS_BRIDGE_BEAN = "Lost Woods Plant Lost Woods Bridge Bean"
    THE_LOST_WOODS_FAIRY_ACCESS = "Lost Woods Fairy Access"
    THE_LOST_WOODS_BUG_ACCESS = "Lost Woods Bug Access"
    THE_LOST_WOODS_SOLD_SKULL_MASK = "Lost Woods Sold Skull Mask"
    LW_UNDER_BRIDGE_FAIRY_ACCESS = "Lost Woods Under the Bridge Fairy Access"
    LW_BEYOND_MIDO_PLANT_LOST_WOODS_THEATER_BEAN = "LW Beyond Mido Plant Lost Woods Theater Bean"
    LW_BEYOND_MIDO_FAIRY_ACCESS = "LW Beyond Mido Fairy Access"


def set_region_rules(world: "SohWorld") -> None:

    # LW Forest Exit  (upstream RR_LW_FOREST_EXIT, SCENE_LOST_WOODS)
    # Connections
    connect_regions(Regions.LW_FOREST_EXIT, world, [
        (Regions.KF_OUTSIDE_LOST_WOODS,
         lambda bundle: True_()),
    ])

    # Lost Woods  (upstream RR_THE_LOST_WOODS, SCENE_LOST_WOODS)
    # Events
    add_events(Regions.THE_LOST_WOODS, world, [
        (EventLocations.THE_LOST_WOODS_PLANT_LOST_WOODS_BRIDGE_BEAN, Events.PLANT_LOST_WOODS_BRIDGE_BEAN,
         lambda bundle: can_plant_bean(bundle)),
        (EventLocations.THE_LOST_WOODS_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_LOST_WOODS_BRIDGE_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (EventLocations.THE_LOST_WOODS_BUG_ACCESS, Events.CAN_ACCESS_BUGS,
         lambda bundle: is_child(bundle) & can_cut_shrubs(bundle)),
        (EventLocations.THE_LOST_WOODS_SOLD_SKULL_MASK, Events.SOLD_SKULL_MASK,
         lambda bundle: is_child(bundle) & has_mask(bundle, "SKULL_MASK") & can_use(Items.SARIAS_SONG, bundle) & has_item(Items.CHILD_WALLET, bundle) & has_speak(bundle, "KOKIRI") & has_speak(bundle, "HYLIAN")),
    ])
    # Locations
    add_locations(Regions.THE_LOST_WOODS, world, [
        (Locations.LW_SKULL_KID,
         lambda bundle: is_child(bundle) & can_use(Items.SARIAS_SONG, bundle)),
        (Locations.LW_TRADE_COJIRO,
         lambda bundle: is_adult(bundle) & can_use(Items.COJIRO, bundle)),
        (Locations.LW_TRADE_ODD_POTION,
         lambda bundle: is_adult(bundle) & can_use(Items.ODD_POTION, bundle)),
        (Locations.LW_OCARINA_MEMORY_GAME,
         lambda bundle: is_child(bundle) & has_item(Items.FAIRY_OCARINA, bundle) & has_enough_ocarina_buttons(bundle, 5)),
        (Locations.LW_TARGET_IN_WOODS,
         lambda bundle: is_child(bundle) & can_use(Items.FAIRY_SLINGSHOT, bundle)),
        (Locations.LW_GS_BEAN_PATCH_NEAR_BRIDGE,
         lambda bundle: can_spawn_soil_skull(bundle) & can_attack(bundle)),
        (Locations.LW_UNDERWATER_SHORTCUT_RUPEE1,
         lambda bundle: is_child(bundle) & (has_item(Items.SILVER_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle))),
        (Locations.LW_UNDERWATER_SHORTCUT_RUPEE2,
         lambda bundle: is_child(bundle) & (has_item(Items.SILVER_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle))),
        (Locations.LW_UNDERWATER_SHORTCUT_RUPEE3,
         lambda bundle: is_child(bundle) & (has_item(Items.SILVER_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle))),
        (Locations.LW_UNDERWATER_SHORTCUT_RUPEE4,
         lambda bundle: is_child(bundle) & (has_item(Items.SILVER_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle))),
        (Locations.LW_UNDERWATER_SHORTCUT_RUPEE5,
         lambda bundle: is_child(bundle) & (has_item(Items.SILVER_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle))),
        (Locations.LW_UNDERWATER_SHORTCUT_RUPEE6,
         lambda bundle: is_child(bundle) & (has_item(Items.SILVER_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle))),
        (Locations.LW_UNDERWATER_SHORTCUT_RUPEE7,
         lambda bundle: is_child(bundle) & (has_item(Items.SILVER_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle))),
        (Locations.LW_UNDERWATER_SHORTCUT_RUPEE8,
         lambda bundle: is_child(bundle) & (has_item(Items.SILVER_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle))),
        (Locations.LW_BEAN_SPROUT_NEAR_BRIDGE_FAIRY1,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_LOST_WOODS_BRIDGE_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.LW_BEAN_SPROUT_NEAR_BRIDGE_FAIRY2,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_LOST_WOODS_BRIDGE_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.LW_BEAN_SPROUT_NEAR_BRIDGE_FAIRY3,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_LOST_WOODS_BRIDGE_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.LW_SHORTCUTS_SONG_OF_STORMS_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.LW_NEAR_SHORTCUTS_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.LW_NEAR_SHORTCUTS_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.LW_NEAR_SHORTCUTS_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        # DEFERRED RC_LW_BOULDER_BY_GORON_CITY: logic->BlastOrSmash()
        (Locations.LW_WONDER_BACK_SKULL_KIDS_GRASS_1,
         lambda bundle: is_child(bundle)),
        (Locations.LW_WONDER_BACK_SKULL_KIDS_GRASS_2,
         lambda bundle: is_child(bundle)),
        (Locations.LW_WONDER_FRONT_SKULL_KIDS_GRASS,
         lambda bundle: is_child(bundle)),
    ])
    # Connections
    connect_regions(Regions.THE_LOST_WOODS, world, [
        (Regions.LW_FOREST_EXIT,
         lambda bundle: True_()),
        (Regions.LW_UNDER_BRIDGE,
         lambda bundle: True_()),
        (Regions.GC_WOODS_WARP,
         lambda bundle: True_()),
        (Regions.LW_BRIDGE,
         lambda bundle: (is_adult(bundle) & (bean_planted(bundle, Events.PLANT_LOST_WOODS_BRIDGE_BEAN) | (can_do_trick(Tricks.LW_BRIDGE, bundle) & can_jump_slash(bundle)))) | can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle) | can_use(Items.LONGSHOT, bundle)),
        (Regions.ZR_FROM_SHORTCUT,
         lambda bundle: has_item(Items.SILVER_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | (can_do_trick(Tricks.LOST_WOOD_NAVI_DIVE, bundle) & is_child(bundle) & has_item(Items.BRONZE_SCALE, bundle) & can_jump_slash(bundle))),
        (Regions.LW_BEYOND_MIDO,
         lambda bundle: is_child(bundle) | can_use(Items.SARIAS_SONG, bundle) | can_do_trick(Tricks.LW_MIDO_BACKFLIP, bundle)),
        (Regions.LW_NEAR_SHORTCUTS_GROTTO,
         lambda bundle: any_age_time(bundle, lambda bundle: blast_or_smash(bundle))),
    ])

    # Lost Woods Under the Bridge  (upstream RR_LW_UNDER_BRIDGE, SCENE_LOST_WOODS)
    # Events
    add_events(Regions.LW_UNDER_BRIDGE, world, [
        (EventLocations.LW_UNDER_BRIDGE_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
    ])
    # Locations
    add_locations(Regions.LW_UNDER_BRIDGE, world, [
        (Locations.LW_DEKU_SCRUB_NEAR_BRIDGE,
         lambda bundle: is_child(bundle) & can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.LW_DEKU_SCRUB_NEAR_BRIDGE, bundle)),
        (Locations.LW_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy_except_suns(bundle)),
        (Locations.LW_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_LW_GOSSIP_STONE: true
    ])
    # Connections
    connect_regions(Regions.LW_UNDER_BRIDGE, world, [
        (Regions.LW_BRIDGE,
         lambda bundle: can_use(Items.LONGSHOT, bundle)),
        (Regions.THE_LOST_WOODS,
         lambda bundle: can_climb_ladder(bundle)),
    ])

    # LW Beyond Mido  (upstream RR_LW_BEYOND_MIDO, SCENE_LOST_WOODS)
    # Events
    add_events(Regions.LW_BEYOND_MIDO, world, [
        (EventLocations.LW_BEYOND_MIDO_PLANT_LOST_WOODS_THEATER_BEAN, Events.PLANT_LOST_WOODS_THEATER_BEAN,
         lambda bundle: can_plant_bean(bundle)),
        (EventLocations.LW_BEYOND_MIDO_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: can_use(Items.STICKS, bundle) | (is_child(bundle) & bean_planted(bundle, Events.PLANT_LOST_WOODS_THEATER_BEAN) & can_use(Items.SONG_OF_STORMS, bundle))),
    ])
    # Locations
    add_locations(Regions.LW_BEYOND_MIDO, world, [
        (Locations.LW_DEKU_SCRUB_NEAR_DEKU_THEATER_RIGHT,
         lambda bundle: is_child(bundle) & can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.LW_DEKU_SCRUB_NEAR_DEKU_THEATER_RIGHT, bundle)),
        (Locations.LW_DEKU_SCRUB_NEAR_DEKU_THEATER_LEFT,
         lambda bundle: is_child(bundle) & can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.LW_DEKU_SCRUB_NEAR_DEKU_THEATER_LEFT, bundle)),
        (Locations.LW_GS_ABOVE_THEATER,
         lambda bundle: is_adult(bundle) & ((bean_planted(bundle, Events.PLANT_LOST_WOODS_THEATER_BEAN) & can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA)) | (can_do_trick(Tricks.LW_GS_BEAN, bundle) & can_use(Items.HOOKSHOT, bundle) & (can_use(Items.LONGSHOT, bundle) | can_use(Items.FAIRY_BOW, bundle) | can_use(Items.FAIRY_SLINGSHOT, bundle) | can_use(Items.BOMBCHUS_5, bundle) | can_use(Items.DINS_FIRE, bundle)))) & can_get_nighttime_gs(bundle)),
        (Locations.LW_GS_BEAN_PATCH_NEAR_THEATER,
         lambda bundle: can_spawn_soil_skull(bundle) & (can_get_enemy_drop(bundle, Enemies.GOLD_SKULLTULA) | (True_(options=[OptionFilter(ShuffleScrubs, ShuffleScrubs.option_off)]) & can_reflect_nuts(bundle)))),
        (Locations.LW_BOULDER_RUPEE,
         lambda bundle: blast_or_smash(bundle)),
        (Locations.LW_BEAN_SPROUT_NEAR_THEATRE_FAIRY1,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_LOST_WOODS_THEATER_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.LW_BEAN_SPROUT_NEAR_THEATRE_FAIRY2,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_LOST_WOODS_THEATER_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.LW_BEAN_SPROUT_NEAR_THEATRE_FAIRY3,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_LOST_WOODS_THEATER_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.LW_AFTER_MIDO_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.LW_AFTER_MIDO_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.LW_AFTER_MIDO_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.LW_NEAR_SFM_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.LW_NEAR_SFM_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.LW_NEAR_SFM_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        # DEFERRED RC_LW_BOULDER_BY_SACRED_FOREST_MEADOW: logic->BlastOrSmash()
        # DEFERRED RC_LW_RUPEE_BOULDER: logic->BlastOrSmash()
        (Locations.LW_MEADOW_BUTTERFLY_FAIRY,
         lambda bundle: is_child(bundle) & can_use(Items.STICKS, bundle)),
    ])
    # Connections
    connect_regions(Regions.LW_BEYOND_MIDO, world, [
        (Regions.LW_FOREST_EXIT,
         lambda bundle: True_()),
        (Regions.THE_LOST_WOODS,
         lambda bundle: is_child(bundle) | can_use(Items.SARIAS_SONG, bundle)),
        (Regions.SFM_ENTRYWAY,
         lambda bundle: True_()),
        (Regions.DEKU_THEATER,
         lambda bundle: True_()),
        (Regions.LW_SCRUBS_GROTTO,
         lambda bundle: any_age_time(bundle, lambda bundle: blast_or_smash(bundle))),
    ])

    # LW Near Shortcuts Grotto  (upstream RR_LW_NEAR_SHORTCUTS_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.LW_NEAR_SHORTCUTS_GROTTO, world, [
        (Locations.LW_NEAR_SHORTCUTS_GROTTO_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.LW_NEAR_SHORTCUTS_GROTTO_FISH,
         lambda bundle: has_bottle(bundle)),
        (Locations.LW_TUNNEL_GROTTO_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.LW_TUNNEL_GROTTO_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_LW_NEAR_SHORTCUTS_GROTTO_GOSSIP_STONE: true
        (Locations.LW_TUNNEL_GROTTO_BEEHIVE_LEFT,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.LW_TUNNEL_GROTTO_BEEHIVE_RIGHT,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.LW_NEAR_SHORTCUTS_GROTTO_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.LW_NEAR_SHORTCUTS_GROTTO_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.LW_NEAR_SHORTCUTS_GROTTO_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.LW_NEAR_SHORTCUTS_GROTTO_GRASS4,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.LW_TUNNEL_GROTTO_BUTTERFLY_FAIRY,
         lambda bundle: can_use(Items.STICKS, bundle)),
    ])
    # Connections
    connect_regions(Regions.LW_NEAR_SHORTCUTS_GROTTO, world, [
        (Regions.THE_LOST_WOODS,
         lambda bundle: True_()),
    ])

    # Deku Theater  (upstream RR_DEKU_THEATER, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.DEKU_THEATER, world, [
        (Locations.LW_DEKU_THEATER_SKULL_MASK,
         lambda bundle: can_use_mask(bundle, "SKULL_MASK")),
        (Locations.LW_DEKU_THEATER_MASK_OF_TRUTH,
         lambda bundle: can_use_mask(bundle, "MASK_OF_TRUTH") & has_speak(bundle, "DEKU")),
        (Locations.LW_THEATER_RECTANGLE_SIGN,
         lambda bundle: can_read(bundle)),
    ])
    # Connections
    connect_regions(Regions.DEKU_THEATER, world, [
        (Regions.LW_BEYOND_MIDO,
         lambda bundle: True_()),
    ])

    # LW Scrubs Grotto  (upstream RR_LW_SCRUBS_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.LW_SCRUBS_GROTTO, world, [
        (Locations.LW_DEKU_SCRUB_GROTTO_REAR,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.LW_DEKU_SCRUB_GROTTO_REAR, bundle)),
        (Locations.LW_DEKU_SCRUB_GROTTO_FRONT,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.LW_DEKU_SCRUB_GROTTO_FRONT, bundle)),
        (Locations.LW_DEKU_SCRUB_GROTTO_BEEHIVE,
         lambda bundle: can_break_upper_beehives(bundle)),
        (Locations.LW_DEKU_SCRUB_GROTTO_SUN_FAIRY,
         lambda bundle: can_use(Items.SUNS_SONG, bundle)),
    ])
    # Connections
    connect_regions(Regions.LW_SCRUBS_GROTTO, world, [
        (Regions.LW_BEYOND_MIDO,
         lambda bundle: True_()),
    ])

    # LW Bridge From Forest  (upstream RR_LW_BRIDGE_FROM_FOREST, SCENE_LOST_WOODS)
    # Locations
    add_locations(Regions.LW_BRIDGE_FROM_FOREST, world, [
        (Locations.LW_GIFT_FROM_SARIA,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.LW_BRIDGE_FROM_FOREST, world, [
        (Regions.LW_BRIDGE,
         lambda bundle: True_()),
    ])

    # LW Bridge  (upstream RR_LW_BRIDGE, SCENE_LOST_WOODS)
    # Connections
    connect_regions(Regions.LW_BRIDGE, world, [
        (Regions.KOKIRI_FOREST,
         lambda bundle: True_()),
        (Regions.HYRULE_FIELD,
         lambda bundle: True_()),
        (Regions.THE_LOST_WOODS,
         lambda bundle: can_use(Items.LONGSHOT, bundle)),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_BUGS', 'CAN_ACCESS_FAIRIES', 'PLANT_LOST_WOODS_BRIDGE_BEAN', 'PLANT_LOST_WOODS_THEATER_BEAN', 'SOLD_SKULL_MASK']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (5): ['RC_LW_BOULDER_BY_GORON_CITY', 'RC_LW_GOSSIP_STONE', 'RC_LW_BOULDER_BY_SACRED_FOREST_MEADOW', 'RC_LW_RUPEE_BOULDER', 'RC_LW_NEAR_SHORTCUTS_GROTTO_GOSSIP_STONE']
