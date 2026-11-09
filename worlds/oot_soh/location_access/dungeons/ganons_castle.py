"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/dungeons/ganons_castle.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    GANONS_CASTLE_DEKU_SCRUBS_FAIRY_ACCESS = "Ganon's Castle Deku Scrubs Fairy Access"
    GANONS_CASTLE_FOREST_TRIAL_BEAMOS_ROOM_GANONS_CASTLE_SILVER_FOREST = "Ganon's Castle Forest Trial Beamos Room Ganons Castle Silver Forest"
    GANONS_CASTLE_FOREST_TRIAL_FINAL_ROOM_FOREST_TRIAL_CLEAR = "Ganon's Castle Forest Trial Final Room Forest Trial Clear"
    GANONS_CASTLE_FIRE_TRIAL_FROM_OPEN_GANONS_CASTLE_SILVER_FIRE = "Ganon's Castle Fire Trial From Open Door Ganons Castle Silver Fire"
    GANONS_CASTLE_FIRE_TRIAL_FROM_BARRED_GANONS_CASTLE_SILVER_FIRE = "Ganon's Castle Fire Trial From Barred Door Ganons Castle Silver Fire"
    GANONS_CASTLE_FIRE_TRIAL_FINAL_ROOM_FIRE_TRIAL_CLEAR = "Ganon's Castle Fire Trial Final Room Fire Trial Clear"
    GANONS_CASTLE_WATER_TRIAL_BLUE_FIRE_ROOM_BLUE_FIRE_ACCESS = "Ganon's Castle Water Trial Blue Fire Room Blue Fire Access"
    GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM_FAIRY_ACCESS = "Ganon's Castle Water Trial Block Room Fairy Access"
    GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM_SWITCH_WATER_TRIAL_RUSTED_SWITCH = "Ganon's Castle Water Trial Block Room Switch Water Trial Rusted Switch"
    GANONS_CASTLE_WATER_TRIAL_FINAL_ROOM_WATER_TRIAL_CLEAR = "Ganon's Castle Water Trial Final Room Water Trial Clear"
    GANONS_CASTLE_SHADOW_TRIAL_LOWER_SWITCH_SHADOW_TRIAL_LATE_CHEST = "Ganon's Castle Shadow Trial Lower Switch Shadow Trial Late Chest"
    GANONS_CASTLE_SHADOW_TRIAL_RUSTED_SWITCH_SHADOW_TRIAL_RUSTED_SWITCH = "Ganon's Castle Shadow Trial Rusted Switch Shadow Trial Rusted Switch"
    GANONS_CASTLE_SHADOW_TRIAL_FINAL_ROOM_SHADOW_TRIAL_CLEAR = "Ganon's Castle Shadow Trial Final Room Shadow Trial Clear"
    GANONS_CASTLE_SPIRIT_TRIAL_BEAMOS_ROOM_GANONS_CASTLE_SILVER_SPIRIT = "Ganon's Castle Spirit Trial Beamos Room Ganons Castle Silver Spirit"
    GANONS_CASTLE_SPIRIT_TRIAL_FINAL_ROOM_SPIRIT_TRIAL_CLEAR = "Ganon's Castle Spirit Trial Final Room Spirit Trial Clear"
    GANONS_CASTLE_SPIRIT_TRIAL_FINAL_ROOM_NUT_ACCESS = "Ganon's Castle Spirit Trial Final Room Nut Access"
    GANONS_CASTLE_LIGHT_TRIAL_BOULDER_ROOM_GANONS_CASTLE_SILVER_LIGHT = "Ganon's Castle Light Trial Boulder Room Ganons Castle Silver Light"
    GANONS_CASTLE_LIGHT_TRIAL_FINAL_ROOM_LIGHT_TRIAL_CLEAR = "Ganon's Castle Light Trial Final Room Light Trial Clear"


def set_region_rules(world: "SohWorld") -> None:

    # Ganon's Castle Entryway  (upstream RR_GANONS_CASTLE_ENTRYWAY, SCENE_INSIDE_GANONS_CASTLE)
    # Connections
    connect_regions(Regions.GANONS_CASTLE_ENTRYWAY, world, [
        (Regions.GANONS_CASTLE_LOBBY,
         lambda bundle: True_()),
        (Regions.CASTLE_GROUNDS_FROM_GANONS_CASTLE,
         lambda bundle: True_()),
    ])

    # Ganon's Castle Lobby  (upstream RR_GANONS_CASTLE_LOBBY, SCENE_INSIDE_GANONS_CASTLE)
    # Connections
    connect_regions(Regions.GANONS_CASTLE_LOBBY, world, [
        (Regions.GANONS_CASTLE_ENTRYWAY,
         lambda bundle: True_()),
        (Regions.GANONS_CASTLE_MAIN,
         lambda bundle: True_()),
    ])

    # Ganon's Castle Main  (upstream RR_GANONS_CASTLE_MAIN, SCENE_INSIDE_GANONS_CASTLE)
    # Locations
    add_locations(Regions.GANONS_CASTLE_MAIN, world, [
        (Locations.GANONS_CASTLE_SHEIK_HINT,
         lambda bundle: has_speak(bundle, "HYLIAN")),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_MAIN, world, [
        (Regions.GANONS_CASTLE_LOBBY,
         lambda bundle: True_()),
        (Regions.GANONS_CASTLE_FOREST_TRIAL_WOLFOS_ROOM,
         lambda bundle: Not(True_(options=[OptionFilter(MedallionLockedTrials, True)])) | has_item(Items.FOREST_MEDALLION, bundle)),
        (Regions.GANONS_CASTLE_FIRE_TRIAL_FROM_OPEN,
         lambda bundle: Not(True_(options=[OptionFilter(MedallionLockedTrials, True)])) | has_item(Items.FIRE_MEDALLION, bundle)),
        (Regions.GANONS_CASTLE_WATER_TRIAL_BLUE_FIRE_ROOM,
         lambda bundle: Not(True_(options=[OptionFilter(MedallionLockedTrials, True)])) | has_item(Items.WATER_MEDALLION, bundle)),
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_START,
         lambda bundle: Not(True_(options=[OptionFilter(MedallionLockedTrials, True)])) | has_item(Items.SHADOW_MEDALLION, bundle)),
        (Regions.GANONS_CASTLE_SPIRIT_TRIAL_BEAMOS_ROOM,
         lambda bundle: Not(True_(options=[OptionFilter(MedallionLockedTrials, True)])) | has_item(Items.SPIRIT_MEDALLION, bundle)),
        (Regions.GANONS_CASTLE_LIGHT_TRIAL_CHESTS_ROOM,
         lambda bundle: (Not(True_(options=[OptionFilter(MedallionLockedTrials, True)])) | has_item(Items.LIGHT_MEDALLION, bundle)) & can_use(Items.GOLDEN_GAUNTLETS, bundle)),
        (Regions.GANONS_TOWER_ENTRYWAY,
         lambda bundle: (has_item(Events.FOREST_TRIAL_CLEAR, bundle) | trial_skipped(bundle, "FOREST_TRIAL")) & (has_item(Events.FIRE_TRIAL_CLEAR, bundle) | trial_skipped(bundle, "FIRE_TRIAL")) & (has_item(Events.WATER_TRIAL_CLEAR, bundle) | trial_skipped(bundle, "WATER_TRIAL")) & (has_item(Events.SHADOW_TRIAL_CLEAR, bundle) | trial_skipped(bundle, "SHADOW_TRIAL")) & (has_item(Events.SPIRIT_TRIAL_CLEAR, bundle) | trial_skipped(bundle, "SPIRIT_TRIAL")) & (has_item(Events.LIGHT_TRIAL_CLEAR, bundle) | trial_skipped(bundle, "LIGHT_TRIAL"))),
        (Regions.GANONS_CASTLE_DEKU_SCRUBS,
         lambda bundle: can_do_trick(Tricks.LENS_GANON, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
    ])

    # Ganon's Castle Deku Scrubs  (upstream RR_GANONS_CASTLE_DEKU_SCRUBS, SCENE_INSIDE_GANONS_CASTLE)
    # Events
    add_events(Regions.GANONS_CASTLE_DEKU_SCRUBS, world, [
        (EventLocations.GANONS_CASTLE_DEKU_SCRUBS_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: True_()),
    ])
    # Locations
    add_locations(Regions.GANONS_CASTLE_DEKU_SCRUBS, world, [
        (Locations.GANONS_CASTLE_DEKU_SCRUB_CENTER_LEFT,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.GANONS_CASTLE_DEKU_SCRUB_CENTER_LEFT, bundle)),
        (Locations.GANONS_CASTLE_DEKU_SCRUB_CENTER_RIGHT,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.GANONS_CASTLE_DEKU_SCRUB_CENTER_RIGHT, bundle)),
        (Locations.GANONS_CASTLE_DEKU_SCRUB_RIGHT,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.GANONS_CASTLE_DEKU_SCRUB_RIGHT, bundle)),
        (Locations.GANONS_CASTLE_DEKU_SCRUB_LEFT,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.GANONS_CASTLE_DEKU_SCRUB_LEFT, bundle)),
        (Locations.GANONS_CASTLE_SCRUBS_FAIRY1,
         lambda bundle: True_()),
        (Locations.GANONS_CASTLE_SCRUBS_FAIRY2,
         lambda bundle: True_()),
        (Locations.GANONS_CASTLE_SCRUBS_FAIRY3,
         lambda bundle: True_()),
        (Locations.GANONS_CASTLE_SCRUBS_FAIRY4,
         lambda bundle: True_()),
        (Locations.GANONS_CASTLE_SCRUBS_FAIRY5,
         lambda bundle: True_()),
        (Locations.GANONS_CASTLE_SCRUBS_FAIRY6,
         lambda bundle: True_()),
        (Locations.GANONS_CASTLE_SCRUBS_FAIRY7,
         lambda bundle: True_()),
        (Locations.GANONS_CASTLE_SCRUBS_FAIRY8,
         lambda bundle: True_()),
    ])

    # Ganon's Castle Forest Trial Wolfos Room  (upstream RR_GANONS_CASTLE_FOREST_TRIAL_WOLFOS_ROOM, SCENE_INSIDE_GANONS_CASTLE)
    # Locations
    add_locations(Regions.GANONS_CASTLE_FOREST_TRIAL_WOLFOS_ROOM, world, [
        (Locations.GANONS_CASTLE_FOREST_TRIAL_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.WOLFOS) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_FOREST_TRIAL_WOLFOS_ROOM, world, [
        (Regions.GANONS_CASTLE_MAIN,
         lambda bundle: True_()),
        (Regions.GANONS_CASTLE_FOREST_TRIAL_BEAMOS_ROOM,
         lambda bundle: can_use(Items.FIRE_ARROW, bundle) | (can_use(Items.HOOKSHOT, bundle) & can_use(Items.DINS_FIRE, bundle))),
    ])

    # Ganon's Castle Forest Trial Beamos Room  (upstream RR_GANONS_CASTLE_FOREST_TRIAL_BEAMOS_ROOM, SCENE_INSIDE_GANONS_CASTLE)
    # Events
    add_events(Regions.GANONS_CASTLE_FOREST_TRIAL_BEAMOS_ROOM, world, [
        (EventLocations.GANONS_CASTLE_FOREST_TRIAL_BEAMOS_ROOM_GANONS_CASTLE_SILVER_FOREST, Events.GANONS_CASTLE_SILVER_FOREST,
         lambda bundle: is_adult(bundle) | can_use(Items.HOOKSHOT, bundle) | (is_child(bundle) & can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle))),
    ])
    # Locations
    add_locations(Regions.GANONS_CASTLE_FOREST_TRIAL_BEAMOS_ROOM, world, [
        # DEFERRED RC_GANONS_CASTLE_SOT_BLOCK_FOREST_SILVER: true
        # DEFERRED RC_GANONS_CASTLE_ON_TARGET_FOREST_SILVER: (ctx->GetTrickOption(RT_VOIDOUT_COLLECTION) && logic->CanVoid()) || (logic->CanMiddairGroundJump())
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_FOREST_TRIAL_BEAMOS_ROOM, world, [
        (Regions.GANONS_CASTLE_FOREST_TRIAL_WOLFOS_ROOM,
         lambda bundle: True_()),
        (Regions.GANONS_CASTLE_FOREST_TRIAL_BEAMOS_ROOM_MIDDLE,
         lambda bundle: True_()),
    ])

    # Ganon's Castle Forest Trial Beamos Room Middle  (upstream RR_GANONS_CASTLE_FOREST_TRIAL_BEAMOS_ROOM_MIDDLE, SCENE_INSIDE_GANONS_CASTLE)
    # Locations
    add_locations(Regions.GANONS_CASTLE_FOREST_TRIAL_BEAMOS_ROOM_MIDDLE, world, [
        # DEFERRED RC_GANONS_CASTLE_LARGE_PLATFORM_FOREST_SILVER: true
        # DEFERRED RC_GANONS_CASTLE_UNDER_LEDGE_FOREST_SILVER: true
        # DEFERRED RC_GANONS_CASTLE_ON_TARGET_FOREST_SILVER: logic->IsAdult || logic->CanUse(RG_HOOKSHOT)
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_FOREST_TRIAL_BEAMOS_ROOM_MIDDLE, world, [
        (Regions.GANONS_CASTLE_FOREST_TRIAL_BEAMOS_ROOM,
         lambda bundle: can_use(Items.LONGSHOT, bundle) | ((is_adult(bundle) & can_use(Items.HOVER_BOOTS, bundle)) | (can_middair_ground_jump(bundle)))),
        (Regions.GANONS_CASTLE_FOREST_TRIAL_BEAMOS_ROOM_FINAL_DOOR,
         lambda bundle: is_adult(bundle) | can_ground_jump(bundle) | can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle)),
    ])

    # Ganon's Castle Forest Trial Beamos Room Final Door  (upstream RR_GANONS_CASTLE_FOREST_TRIAL_BEAMOS_ROOM_FINAL_DOOR, SCENE_INSIDE_GANONS_CASTLE)
    # Locations
    add_locations(Regions.GANONS_CASTLE_FOREST_TRIAL_BEAMOS_ROOM_FINAL_DOOR, world, [
        # DEFERRED RC_GANONS_CASTLE_SMALL_PLATFORM_FOREST_SILVER: true
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_FOREST_TRIAL_BEAMOS_ROOM_FINAL_DOOR, world, [
        (Regions.GANONS_CASTLE_FOREST_TRIAL_BEAMOS_ROOM_MIDDLE,
         lambda bundle: True_()),
        (Regions.GANONS_CASTLE_FOREST_TRIAL_FINAL_ROOM,
         lambda bundle: has_item(Events.GANONS_CASTLE_SILVER_FOREST, bundle)),
    ])

    # Ganon's Castle Forest Trial Final Room  (upstream RR_GANONS_CASTLE_FOREST_TRIAL_FINAL_ROOM, SCENE_INSIDE_GANONS_CASTLE)
    # Events
    add_events(Regions.GANONS_CASTLE_FOREST_TRIAL_FINAL_ROOM, world, [
        (EventLocations.GANONS_CASTLE_FOREST_TRIAL_FINAL_ROOM_FOREST_TRIAL_CLEAR, Events.FOREST_TRIAL_CLEAR,
         lambda bundle: can_use(Items.LIGHT_ARROW, bundle)),
    ])
    # Locations
    add_locations(Regions.GANONS_CASTLE_FOREST_TRIAL_FINAL_ROOM, world, [
        (Locations.GANONS_CASTLE_FOREST_TRIAL_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_FOREST_TRIAL_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_FOREST_TRIAL_FINAL_ROOM, world, [
        (Regions.GANONS_CASTLE_FOREST_TRIAL_BEAMOS_ROOM_FINAL_DOOR,
         lambda bundle: True_()),
    ])

    # Ganon's Castle Fire Trial Open Door  (upstream RR_GANONS_CASTLE_FIRE_TRIAL_OPEN_DOOR, SCENE_INSIDE_GANONS_CASTLE)
    # Connections
    connect_regions(Regions.GANONS_CASTLE_FIRE_TRIAL_OPEN_DOOR, world, [
        (Regions.GANONS_CASTLE_MAIN,
         lambda bundle: True_()),
    ])

    # Ganon's Castle Fire Trial From Open Door  (upstream RR_GANONS_CASTLE_FIRE_TRIAL_FROM_OPEN, SCENE_INSIDE_GANONS_CASTLE)
    # Events
    add_events(Regions.GANONS_CASTLE_FIRE_TRIAL_FROM_OPEN, world, [
        (EventLocations.GANONS_CASTLE_FIRE_TRIAL_FROM_OPEN_GANONS_CASTLE_SILVER_FIRE, Events.GANONS_CASTLE_SILVER_FIRE,
         lambda bundle: fire_timer_at_least(bundle, 48) & can_use(Items.GOLDEN_GAUNTLETS, bundle)),
    ])
    # Locations
    add_locations(Regions.GANONS_CASTLE_FIRE_TRIAL_FROM_OPEN, world, [
        (Locations.GANONS_CASTLE_FIRE_TRIAL_HEART,
         lambda bundle: fire_timer_at_least(bundle, 16)),
        # DEFERRED RC_GANONS_CASTLE_TORCH_SLUG_FIRE_SILVER: logic->FireTimer() >= 16
        # DEFERRED RC_GANONS_CASTLE_FLAME_JETS_FIRE_SILVER: logic->FireTimer() >= 16
        # DEFERRED RC_GANONS_CASTLE_DISTANT_PLATFORM_FIRE_SILVER: logic->FireTimer() >= 32 && (logic->CanUse(RG_GOLDEN_GAUNTLETS) || logic->BunnyHovers())
        # DEFERRED RC_GANONS_CASTLE_CLOSE_PLATFORM_FIRE_SILVER: logic->FireTimer() >= 8
        # DEFERRED RC_GANONS_GANONS_CASTLE_UNDER_PILLAR_FIRE_SILVER: logic->FireTimer() >= 24 && logic->CanUse(RG_GOLDEN_GAUNTLETS)
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_FIRE_TRIAL_FROM_OPEN, world, [
        (Regions.GANONS_CASTLE_FIRE_TRIAL_OPEN_DOOR,
         lambda bundle: True_()),
        (Regions.GANONS_CASTLE_FIRE_TRIAL_BARRED_DOOR,
         lambda bundle: can_use(Items.LONGSHOT, bundle) & fire_timer_at_least(bundle, 16)),
    ])

    # Ganon's Castle Fire Trial From Barred Door  (upstream RR_GANONS_CASTLE_FIRE_TRIAL_FROM_BARRED, SCENE_INSIDE_GANONS_CASTLE)
    # Events
    add_events(Regions.GANONS_CASTLE_FIRE_TRIAL_FROM_BARRED, world, [
        (EventLocations.GANONS_CASTLE_FIRE_TRIAL_FROM_BARRED_GANONS_CASTLE_SILVER_FIRE, Events.GANONS_CASTLE_SILVER_FIRE,
         lambda bundle: (can_use(Items.LONGSHOT, bundle) | can_recoil_hover(bundle, Recoil.HAMMER)) & fire_timer_at_least(bundle, 56) & can_use(Items.GOLDEN_GAUNTLETS, bundle)),
    ])
    # Locations
    add_locations(Regions.GANONS_CASTLE_FIRE_TRIAL_FROM_BARRED, world, [
        (Locations.GANONS_CASTLE_FIRE_TRIAL_HEART,
         lambda bundle: (can_use(Items.LONGSHOT, bundle) | can_recoil_hover(bundle, Recoil.HAMMER)) & fire_timer_at_least(bundle, 16)),
        # DEFERRED RC_GANONS_CASTLE_TORCH_SLUG_FIRE_SILVER: (logic->CanUse(RG_LONGSHOT) || logic->CanRecoilHover(RECOIL_HAMMER)) && logic->FireTimer() >= 8
        # DEFERRED RC_GANONS_CASTLE_FLAME_JETS_FIRE_SILVER: (logic->CanUse(RG_LONGSHOT) || logic->CanRecoilHover(RECOIL_HAMMER)) && logic->FireTimer() >= 16
        # DEFERRED RC_GANONS_CASTLE_DISTANT_PLATFORM_FIRE_SILVER: (logic->CanUse(RG_LONGSHOT) || logic->CanRecoilHover(RECOIL_HAMMER)) && logic->FireTimer() >= 32 && (logic->CanUse(RG_GOLDEN_GAUNTLETS) || logic->BunnyHovers())
        # DEFERRED RC_GANONS_CASTLE_CLOSE_PLATFORM_FIRE_SILVER: (logic->CanUse(RG_LONGSHOT) || logic->CanRecoilHover(RECOIL_HAMMER)) && logic->FireTimer() >= 16
        # DEFERRED RC_GANONS_GANONS_CASTLE_UNDER_PILLAR_FIRE_SILVER: (logic->CanUse(RG_LONGSHOT) || logic->CanRecoilHover(RECOIL_HAMMER)) && logic->FireTimer() >= 24 && logic->CanUse(RG_GOLDEN_GAUNTLETS)
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_FIRE_TRIAL_FROM_BARRED, world, [
        (Regions.GANONS_CASTLE_FIRE_TRIAL_OPEN_DOOR,
         lambda bundle: (can_use(Items.LONGSHOT, bundle) | can_recoil_hover(bundle, Recoil.HAMMER)) & fire_timer_at_least(bundle, 24)),
        (Regions.GANONS_CASTLE_FIRE_TRIAL_BARRED_DOOR,
         lambda bundle: True_()),
    ])

    # Ganon's Castle Fire Trial Barred Door  (upstream RR_GANONS_CASTLE_FIRE_TRIAL_BARRED_DOOR, SCENE_INSIDE_GANONS_CASTLE)
    # Connections
    connect_regions(Regions.GANONS_CASTLE_FIRE_TRIAL_BARRED_DOOR, world, [
        (Regions.GANONS_CASTLE_FIRE_TRIAL_FINAL_ROOM,
         lambda bundle: has_item(Events.GANONS_CASTLE_SILVER_FIRE, bundle)),
    ])

    # Ganon's Castle Fire Trial Final Room  (upstream RR_GANONS_CASTLE_FIRE_TRIAL_FINAL_ROOM, SCENE_INSIDE_GANONS_CASTLE)
    # Events
    add_events(Regions.GANONS_CASTLE_FIRE_TRIAL_FINAL_ROOM, world, [
        (EventLocations.GANONS_CASTLE_FIRE_TRIAL_FINAL_ROOM_FIRE_TRIAL_CLEAR, Events.FIRE_TRIAL_CLEAR,
         lambda bundle: can_use(Items.LIGHT_ARROW, bundle)),
    ])
    # Locations
    add_locations(Regions.GANONS_CASTLE_FIRE_TRIAL_FINAL_ROOM, world, [
        (Locations.GANONS_CASTLE_FIRE_TRIAL_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_FIRE_TRIAL_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_FIRE_TRIAL_FINAL_ROOM, world, [
        (Regions.GANONS_CASTLE_FIRE_TRIAL_FROM_BARRED,
         lambda bundle: True_()),
    ])

    # Ganon's Castle Water Trial Blue Fire Room  (upstream RR_GANONS_CASTLE_WATER_TRIAL_BLUE_FIRE_ROOM, SCENE_INSIDE_GANONS_CASTLE)
    # Events
    add_events(Regions.GANONS_CASTLE_WATER_TRIAL_BLUE_FIRE_ROOM, world, [
        (EventLocations.GANONS_CASTLE_WATER_TRIAL_BLUE_FIRE_ROOM_BLUE_FIRE_ACCESS, Events.CAN_ACCESS_BLUE_FIRE,
         lambda bundle: can_clear_stalagmite(bundle) | can_do_trick(Tricks.ICE_STALAGMITE_CLIP, bundle)),
    ])
    # Locations
    add_locations(Regions.GANONS_CASTLE_WATER_TRIAL_BLUE_FIRE_ROOM, world, [
        (Locations.GANONS_CASTLE_WATER_TRIAL_LEFT_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.GANONS_CASTLE_WATER_TRIAL_RIGHT_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALAGMITE_1,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALAGMITE_2,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALAGMITE_3,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALAGMITE_4,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALAGMITE_5,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALAGMITE_6,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALAGMITE_7,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALAGMITE_8,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALAGMITE_9,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALAGMITE_10,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.GANONS_CASTLE_WATER_TRIAL_LEFT_STALAGMITE_1,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.GANONS_CASTLE_WATER_TRIAL_LEFT_STALAGMITE_2,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.GANONS_CASTLE_WATER_TRIAL_RIGHT_STALAGMITE_1,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.GANONS_CASTLE_WATER_TRIAL_RIGHT_STALAGMITE_2,
         lambda bundle: can_clear_stalagmite(bundle)),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALACTITE_1,
         lambda bundle: True_()),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALACTITE_2,
         lambda bundle: True_()),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALACTITE_3,
         lambda bundle: True_()),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALACTITE_4,
         lambda bundle: True_()),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALACTITE_5,
         lambda bundle: True_()),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALACTITE_6,
         lambda bundle: True_()),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALACTITE_7,
         lambda bundle: True_()),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALACTITE_8,
         lambda bundle: True_()),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALACTITE_9,
         lambda bundle: True_()),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALACTITE_10,
         lambda bundle: True_()),
        (Locations.GANONS_CASTLE_WATER_TRIAL_STALACTITE_11,
         lambda bundle: True_()),
        (Locations.GANONS_CASTLE_WATER_TRIAL_DOOR_RED_ICE,
         lambda bundle: blue_fire(bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_WATER_TRIAL_BLUE_FIRE_ROOM, world, [
        (Regions.GANONS_CASTLE_MAIN,
         lambda bundle: True_()),
        (Regions.GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM,
         lambda bundle: blue_fire(bundle)),
    ])

    # Ganon's Castle Water Trial Block Room  (upstream RR_GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM, SCENE_INSIDE_GANONS_CASTLE)
    # Events
    add_events(Regions.GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM, world, [
        (EventLocations.GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Locations
    add_locations(Regions.GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM, world, [
        (Locations.GANONS_CASTLE_WATER_TRIAL_POT3,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM, world, [
        (Regions.GANONS_CASTLE_WATER_TRIAL_BLUE_FIRE_ROOM,
         lambda bundle: True_()),
        (Regions.GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM_SWITCH,
         lambda bundle: is_adult(bundle) & (has_grab(bundle) | can_middair_ground_jump(bundle))),
        (Regions.GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM_END,
         lambda bundle: is_adult(bundle) | (can_use(Items.HOVER_BOOTS, bundle)) | can_ground_jump(bundle) | can_do_trick(Tricks.SLIDE_JUMP, bundle) | ((bunny_hood(bundle) | has_grab(bundle)) & can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle))),
    ])

    # Ganon's Castle Water Trial Block Room Switch  (upstream RR_GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM_SWITCH, SCENE_INSIDE_GANONS_CASTLE)
    # Events
    add_events(Regions.GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM_SWITCH, world, [
        (EventLocations.GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM_SWITCH_WATER_TRIAL_RUSTED_SWITCH, Events.WATER_TRIAL_RUSTED_SWITCH,
         lambda bundle: (blue_fire(bundle) | can_do_trick(Tricks.VISIBLE_COLLISION, bundle)) & can_use(Items.MEGATON_HAMMER, bundle)),
    ])
    # Locations
    add_locations(Regions.GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM_SWITCH, world, [
        (Locations.GANONS_CASTLE_WATER_TRIAL_RUSTED_SWITCH_RED_ICE,
         lambda bundle: blue_fire(bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM_SWITCH, world, [
        (Regions.GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM,
         lambda bundle: True_()),
    ])

    # Ganon's Castle Water Trial Block Room End  (upstream RR_GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM_END, SCENE_INSIDE_GANONS_CASTLE)
    # Connections
    connect_regions(Regions.GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM_END, world, [
        (Regions.GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM,
         lambda bundle: True_()),
        (Regions.GANONS_CASTLE_WATER_TRIAL_FINAL_ROOM,
         lambda bundle: has_item(Events.WATER_TRIAL_RUSTED_SWITCH, bundle)),
    ])

    # Ganon's Castle Water Trial Final Room  (upstream RR_GANONS_CASTLE_WATER_TRIAL_FINAL_ROOM, SCENE_INSIDE_GANONS_CASTLE)
    # Events
    add_events(Regions.GANONS_CASTLE_WATER_TRIAL_FINAL_ROOM, world, [
        (EventLocations.GANONS_CASTLE_WATER_TRIAL_FINAL_ROOM_WATER_TRIAL_CLEAR, Events.WATER_TRIAL_CLEAR,
         lambda bundle: can_use(Items.LIGHT_ARROW, bundle)),
    ])
    # Locations
    add_locations(Regions.GANONS_CASTLE_WATER_TRIAL_FINAL_ROOM, world, [
        (Locations.GANONS_CASTLE_WATER_TRIAL_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_WATER_TRIAL_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_WATER_TRIAL_FINAL_ROOM, world, [
        (Regions.GANONS_CASTLE_WATER_TRIAL_BLOCK_ROOM_END,
         lambda bundle: True_()),
    ])

    # Ganon's Castle Shadow Trial Start  (upstream RR_GANONS_CASTLE_SHADOW_TRIAL_START, SCENE_INSIDE_GANONS_CASTLE)
    # Locations
    add_locations(Regions.GANONS_CASTLE_SHADOW_TRIAL_START, world, [
        (Locations.GANONS_CASTLE_SHADOW_TRIAL_FRONT_CHEST,
         lambda bundle: has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_SHADOW_TRIAL_START, world, [
        (Regions.GANONS_CASTLE_MAIN,
         lambda bundle: True_()),
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_SOT_PLATFORM,
         lambda bundle: can_use(Items.FIRE_ARROW, bundle) | can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle) | can_use(Items.SONG_OF_TIME, bundle) | is_child(bundle)),
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_TORCH,
         lambda bundle: can_use(Items.LONGSHOT, bundle) | (is_adult(bundle) & can_recoil_hover(bundle, Recoil.HAMMER)) | (can_use(Items.FIRE_ARROW, bundle) & ((is_adult(bundle) & bunny_hood(bundle)) | can_use(Items.HOVER_BOOTS, bundle)))),
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_POTS_PLATFORM,
         lambda bundle: can_use(Items.FIRE_ARROW, bundle)),
    ])

    # Ganon's Castle Shadow Trial SoT Platform  (upstream RR_GANONS_CASTLE_SHADOW_TRIAL_SOT_PLATFORM, SCENE_INSIDE_GANONS_CASTLE)
    # Locations
    add_locations(Regions.GANONS_CASTLE_SHADOW_TRIAL_SOT_PLATFORM, world, [
        (Locations.GANONS_CASTLE_SHADOW_TRIAL_FRONT_CHEST,
         lambda bundle: has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_SHADOW_TRIAL_SOT_PLATFORM, world, [
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_START,
         lambda bundle: can_use(Items.FIRE_ARROW, bundle) | can_use(Items.LONGSHOT, bundle) | (can_use(Items.HOVER_BOOTS, bundle)) | can_use(Items.SONG_OF_TIME, bundle) | is_child(bundle)),
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_TORCH,
         lambda bundle: can_use(Items.LONGSHOT, bundle)),
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_POTS_PLATFORM,
         lambda bundle: can_use(Items.FIRE_ARROW, bundle)),
    ])

    # Ganon's Castle Shadow Trial Torch  (upstream RR_GANONS_CASTLE_SHADOW_TRIAL_TORCH, SCENE_INSIDE_GANONS_CASTLE)
    # Connections
    connect_regions(Regions.GANONS_CASTLE_SHADOW_TRIAL_TORCH, world, [
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_START,
         lambda bundle: can_use(Items.LONGSHOT, bundle) | (has_fire_source(bundle) & can_use(Items.HOVER_BOOTS, bundle))),
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_POTS_PLATFORM,
         lambda bundle: can_use(Items.LONGSHOT, bundle) | (has_fire_source(bundle) & can_use(Items.HOVER_BOOTS, bundle))),
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_CHEST_PLATFORM,
         lambda bundle: can_use(Items.LONGSHOT, bundle) | (has_fire_source(bundle) & can_use(Items.HOVER_BOOTS, bundle))),
    ])

    # Ganon's Castle Shadow Pots Platform  (upstream RR_GANONS_CASTLE_SHADOW_TRIAL_POTS_PLATFORM, SCENE_INSIDE_GANONS_CASTLE)
    # Locations
    add_locations(Regions.GANONS_CASTLE_SHADOW_TRIAL_POTS_PLATFORM, world, [
        (Locations.GANONS_CASTLE_SHADOW_TRIAL_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_SHADOW_TRIAL_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_SHADOW_TRIAL_POTS_PLATFORM, world, [
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_START,
         lambda bundle: can_use(Items.FIRE_ARROW, bundle)),
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_TORCH,
         lambda bundle: can_use(Items.LONGSHOT, bundle) | (can_use(Items.FIRE_ARROW, bundle) & ((is_adult(bundle) & bunny_hood(bundle)) | can_use(Items.HOVER_BOOTS, bundle)))),
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_SOT_PLATFORM,
         lambda bundle: can_use(Items.LONGSHOT, bundle) | can_use(Items.FIRE_ARROW, bundle)),
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_CHEST_PLATFORM,
         lambda bundle: can_use(Items.FIRE_ARROW, bundle) | can_use(Items.HOVER_BOOTS, bundle) | (has_item(Events.SHADOW_TRIAL_LATE_CHEST, bundle) & can_use(Items.HOOKSHOT, bundle))),
    ])

    # Ganon's Castle Shadow Chest Platform  (upstream RR_GANONS_CASTLE_SHADOW_TRIAL_CHEST_PLATFORM, SCENE_INSIDE_GANONS_CASTLE)
    # Locations
    add_locations(Regions.GANONS_CASTLE_SHADOW_TRIAL_CHEST_PLATFORM, world, [
        (Locations.GANONS_CASTLE_SHADOW_TRIAL_GOLDEN_GAUNTLETS_CHEST,
         lambda bundle: has_item(Events.SHADOW_TRIAL_LATE_CHEST, bundle) & can_open_large_chest(bundle)),
        (Locations.GANONS_CASTLE_SHADOW_TRIAL_HEART1,
         lambda bundle: can_do_trick(Tricks.LENS_GANON, bundle) | can_use(Items.LENS_OF_TRUTH, bundle) | can_use(Items.BOOMERANG, bundle)),
        (Locations.GANONS_CASTLE_SHADOW_TRIAL_HEART2,
         lambda bundle: can_do_trick(Tricks.LENS_GANON, bundle) | can_use(Items.LENS_OF_TRUTH, bundle) | can_use(Items.BOOMERANG, bundle)),
        (Locations.GANONS_CASTLE_SHADOW_TRIAL_HEART3,
         lambda bundle: can_do_trick(Tricks.LENS_GANON, bundle) | can_use(Items.LENS_OF_TRUTH, bundle) | can_use(Items.BOOMERANG, bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_SHADOW_TRIAL_CHEST_PLATFORM, world, [
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_POTS_PLATFORM,
         lambda bundle: can_use(Items.FIRE_ARROW, bundle) | can_use(Items.HOOKSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle)),
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_LOWER_SWITCH,
         lambda bundle: can_use(Items.FIRE_ARROW, bundle) | can_do_trick(Tricks.LENS_GANON, bundle) | can_use(Items.LENS_OF_TRUTH, bundle) | can_use(Items.HOVER_BOOTS, bundle) | (is_adult(bundle) & bunny_hood(bundle) & can_jump_slash(bundle))),
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_RUSTED_SWITCH,
         lambda bundle: can_do_trick(Tricks.LENS_GANON, bundle) | can_use(Items.LENS_OF_TRUTH, bundle) | can_use(Items.HOVER_BOOTS, bundle)),
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_END,
         lambda bundle: can_do_trick(Tricks.LENS_GANON, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)),
    ])

    # Ganon's Castle Shadow Trial Lower Switch  (upstream RR_GANONS_CASTLE_SHADOW_TRIAL_LOWER_SWITCH, SCENE_INSIDE_GANONS_CASTLE)
    # Events
    add_events(Regions.GANONS_CASTLE_SHADOW_TRIAL_LOWER_SWITCH, world, [
        (EventLocations.GANONS_CASTLE_SHADOW_TRIAL_LOWER_SWITCH_SHADOW_TRIAL_LATE_CHEST, Events.SHADOW_TRIAL_LATE_CHEST,
         lambda bundle: True_()),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_SHADOW_TRIAL_LOWER_SWITCH, world, [
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_CHEST_PLATFORM,
         lambda bundle: can_use(Items.FIRE_ARROW, bundle) | (has_item(Events.SHADOW_TRIAL_LATE_CHEST, bundle) & can_use(Items.LONGSHOT, bundle))),
    ])

    # Ganon's Castle Shadow Trial Rusted Switch  (upstream RR_GANONS_CASTLE_SHADOW_TRIAL_RUSTED_SWITCH, SCENE_INSIDE_GANONS_CASTLE)
    # Events
    add_events(Regions.GANONS_CASTLE_SHADOW_TRIAL_RUSTED_SWITCH, world, [
        (EventLocations.GANONS_CASTLE_SHADOW_TRIAL_RUSTED_SWITCH_SHADOW_TRIAL_RUSTED_SWITCH, Events.SHADOW_TRIAL_RUSTED_SWITCH,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
    ])
    # Locations
    add_locations(Regions.GANONS_CASTLE_SHADOW_TRIAL_RUSTED_SWITCH, world, [
        (Locations.GANONS_CASTLE_SHADOW_TRIAL_HEART1,
         lambda bundle: can_use(Items.BOOMERANG, bundle)),
        (Locations.GANONS_CASTLE_SHADOW_TRIAL_HEART2,
         lambda bundle: can_use(Items.BOOMERANG, bundle)),
        (Locations.GANONS_CASTLE_SHADOW_TRIAL_HEART3,
         lambda bundle: can_use(Items.BOOMERANG, bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_SHADOW_TRIAL_RUSTED_SWITCH, world, [
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_CHEST_PLATFORM,
         lambda bundle: can_do_trick(Tricks.LENS_GANON, bundle) | can_use(Items.LENS_OF_TRUTH, bundle) | (has_item(Events.SHADOW_TRIAL_LATE_CHEST, bundle) & can_use(Items.LONGSHOT, bundle)) | can_use(Items.HOVER_BOOTS, bundle) | (is_adult(bundle) & bunny_hood(bundle))),
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_END,
         lambda bundle: can_use(Items.LONGSHOT, bundle)),
    ])

    # Ganon's Castle Shadow Trial End  (upstream RR_GANONS_CASTLE_SHADOW_TRIAL_END, SCENE_INSIDE_GANONS_CASTLE)
    # Locations
    add_locations(Regions.GANONS_CASTLE_SHADOW_TRIAL_END, world, [
        (Locations.GANONS_CASTLE_SHADOW_TRIAL_HEART1,
         lambda bundle: can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & bunny_hovers(bundle)),
        (Locations.GANONS_CASTLE_SHADOW_TRIAL_HEART2,
         lambda bundle: (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_use(Items.HOVER_BOOTS, bundle)) | can_use(Items.BOOMERANG, bundle)),
        (Locations.GANONS_CASTLE_SHADOW_TRIAL_HEART3,
         lambda bundle: (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & (can_use(Items.HOVER_BOOTS, bundle) | bunny_hood(bundle))) | can_use(Items.BOOMERANG, bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_SHADOW_TRIAL_END, world, [
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_CHEST_PLATFORM,
         lambda bundle: (can_do_trick(Tricks.LENS_GANON, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) | ((can_use(Items.HOVER_BOOTS, bundle) | ((is_adult(bundle) | can_jump_slash(bundle)) & bunny_hood(bundle))) & has_fire_source(bundle)) | (has_item(Events.SHADOW_TRIAL_LATE_CHEST, bundle) & can_use(Items.LONGSHOT, bundle))),
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_POTS_PLATFORM,
         lambda bundle: can_use(Items.DINS_FIRE, bundle) & (can_do_trick(Tricks.LENS_GANON, bundle) | can_use(Items.LENS_OF_TRUTH, bundle) | ((is_adult(bundle) | can_jump_slash(bundle)) & bunny_hood(bundle)))),
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_LOWER_SWITCH,
         lambda bundle: can_use(Items.HOVER_BOOTS, bundle) | ((is_adult(bundle) | can_jump_slash(bundle)) & bunny_hood(bundle))),
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_RUSTED_SWITCH,
         lambda bundle: (can_use(Items.HOVER_BOOTS, bundle) & (has_fire_source(bundle) | bunny_hood(bundle)))),
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_FINAL_ROOM,
         lambda bundle: has_item(Events.SHADOW_TRIAL_RUSTED_SWITCH, bundle)),
    ])

    # Ganon's Castle Shadow Trial Final Room  (upstream RR_GANONS_CASTLE_SHADOW_TRIAL_FINAL_ROOM, SCENE_INSIDE_GANONS_CASTLE)
    # Events
    add_events(Regions.GANONS_CASTLE_SHADOW_TRIAL_FINAL_ROOM, world, [
        (EventLocations.GANONS_CASTLE_SHADOW_TRIAL_FINAL_ROOM_SHADOW_TRIAL_CLEAR, Events.SHADOW_TRIAL_CLEAR,
         lambda bundle: can_use(Items.LIGHT_ARROW, bundle)),
    ])
    # Locations
    add_locations(Regions.GANONS_CASTLE_SHADOW_TRIAL_FINAL_ROOM, world, [
        (Locations.GANONS_CASTLE_SHADOW_TRIAL_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_SHADOW_TRIAL_POT4,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_SHADOW_TRIAL_FINAL_ROOM, world, [
        (Regions.GANONS_CASTLE_SHADOW_TRIAL_END,
         lambda bundle: True_()),
    ])

    # Ganon's Castle Spirit Trial Beamos Room  (upstream RR_GANONS_CASTLE_SPIRIT_TRIAL_BEAMOS_ROOM, SCENE_INSIDE_GANONS_CASTLE)
    # Events
    add_events(Regions.GANONS_CASTLE_SPIRIT_TRIAL_BEAMOS_ROOM, world, [
        (EventLocations.GANONS_CASTLE_SPIRIT_TRIAL_BEAMOS_ROOM_GANONS_CASTLE_SILVER_SPIRIT, Events.GANONS_CASTLE_SILVER_SPIRIT,
         lambda bundle: (can_do_trick(Tricks.GANON_SPIRIT_TRIAL_HOOKSHOT, bundle) & can_jump_slash(bundle) & has_grab(bundle)) | can_use(Items.HOOKSHOT, bundle)),
    ])
    # Locations
    add_locations(Regions.GANONS_CASTLE_SPIRIT_TRIAL_BEAMOS_ROOM, world, [
        (Locations.GANONS_CASTLE_SPIRIT_TRIAL_BEAMOS_SUNS_SONG_FAIRY,
         lambda bundle: can_use(Items.SUNS_SONG, bundle)),
        (Locations.GANONS_CASTLE_SPIRIT_TRIAL_HEART,
         lambda bundle: True_()),
        # DEFERRED RC_GANONS_CASTLE_AIRBORNE_SPIRIT_SILVER: (ctx->GetTrickOption(RT_GANON_SPIRIT_TRIAL_HOOKSHOT) && logic->CanJumpslash() && logic->HasItem(RG_POWER_BRACELET)) || logic->CanUse(RG_HOOKSHOT)
        # DEFERRED RC_GANONS_CASTLE_NEAR_DOORMAT_SPIRIT_SILVER: true
        # DEFERRED RC_GANONS_CASTLE_LOWER_MIDDLE_SPIRIT_SILVER: true
        # DEFERRED RC_GANONS_CASTLE_CORNER_SPIRIT_SILVER: true
        # DEFERRED RC_GANONS_CASTLE_NEAR_BARRED_DOOR_SPIRIT_SILVER: true
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_SPIRIT_TRIAL_BEAMOS_ROOM, world, [
        (Regions.GANONS_CASTLE_MAIN,
         lambda bundle: True_()),
        (Regions.GANONS_CASTLE_SPIRIT_TRIAL_BEFORE_SWITCH,
         lambda bundle: has_item(Events.GANONS_CASTLE_SILVER_SPIRIT, bundle)),
    ])

    # Ganon's Castle Spirit Trial Before Switch  (upstream RR_GANONS_CASTLE_SPIRIT_TRIAL_BEFORE_SWITCH, SCENE_INSIDE_GANONS_CASTLE)
    # Locations
    add_locations(Regions.GANONS_CASTLE_SPIRIT_TRIAL_BEFORE_SWITCH, world, [
        (Locations.GANONS_CASTLE_SPIRIT_TRIAL_CRYSTAL_SWITCH_CHEST,
         lambda bundle: (can_jump_slash(bundle) | has_explosives(bundle) | can_use(Items.GIANTS_KNIFE, bundle)) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_SPIRIT_TRIAL_BEFORE_SWITCH, world, [
        (Regions.GANONS_CASTLE_SPIRIT_TRIAL_BEAMOS_ROOM,
         lambda bundle: True_()),
        (Regions.GANONS_CASTLE_SPIRIT_TRIAL_AFTER_SWITCH,
         lambda bundle: can_use(Items.BOMBCHUS_5, bundle) | (can_do_trick(Tricks.ITEM_EXTENSION, bundle) & (can_use(Items.FAIRY_BOW, bundle) | can_use(Items.FAIRY_SLINGSHOT, bundle)))),
    ])

    # Ganon's Castle Spirit Trial After Switch  (upstream RR_GANONS_CASTLE_SPIRIT_TRIAL_AFTER_SWITCH, SCENE_INSIDE_GANONS_CASTLE)
    # Locations
    add_locations(Regions.GANONS_CASTLE_SPIRIT_TRIAL_AFTER_SWITCH, world, [
        (Locations.GANONS_CASTLE_SPIRIT_TRIAL_CRYSTAL_SWITCH_CHEST,
         lambda bundle: can_hit_switch(bundle) & has_open_chest(bundle)),
        (Locations.GANONS_CASTLE_SPIRIT_TRIAL_INVISIBLE_CHEST,
         lambda bundle: (can_do_trick(Tricks.LENS_GANON, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_SPIRIT_TRIAL_AFTER_SWITCH, world, [
        (Regions.GANONS_CASTLE_SPIRIT_TRIAL_BEFORE_SWITCH,
         lambda bundle: True_()),
        (Regions.GANONS_CASTLE_SPIRIT_TRIAL_FINAL_ROOM,
         lambda bundle: can_use(Items.FAIRY_BOW, bundle) & (can_use(Items.MIRROR_SHIELD, bundle) | (True_(options=[OptionFilter(SunlightArrows, True)]) & can_use(Items.LIGHT_ARROW, bundle)))),
    ])

    # Ganon's Castle Spirit Trial Final Room  (upstream RR_GANONS_CASTLE_SPIRIT_TRIAL_FINAL_ROOM, SCENE_INSIDE_GANONS_CASTLE)
    # Events
    add_events(Regions.GANONS_CASTLE_SPIRIT_TRIAL_FINAL_ROOM, world, [
        (EventLocations.GANONS_CASTLE_SPIRIT_TRIAL_FINAL_ROOM_SPIRIT_TRIAL_CLEAR, Events.SPIRIT_TRIAL_CLEAR,
         lambda bundle: can_use(Items.LIGHT_ARROW, bundle)),
        (EventLocations.GANONS_CASTLE_SPIRIT_TRIAL_FINAL_ROOM_NUT_ACCESS, Events.CAN_FARM_NUTS,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Locations
    add_locations(Regions.GANONS_CASTLE_SPIRIT_TRIAL_FINAL_ROOM, world, [
        (Locations.GANONS_CASTLE_SPIRIT_TRIAL_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_SPIRIT_TRIAL_POT2,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_SPIRIT_TRIAL_FINAL_ROOM, world, [
        (Regions.GANONS_CASTLE_SPIRIT_TRIAL_AFTER_SWITCH,
         lambda bundle: True_()),
    ])

    # Ganon's Castle Light Trial Chests Room  (upstream RR_GANONS_CASTLE_LIGHT_TRIAL_CHESTS_ROOM, SCENE_INSIDE_GANONS_CASTLE)
    # Locations
    add_locations(Regions.GANONS_CASTLE_LIGHT_TRIAL_CHESTS_ROOM, world, [
        (Locations.GANONS_CASTLE_LIGHT_TRIAL_FIRST_LEFT_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.GANONS_CASTLE_LIGHT_TRIAL_SECOND_LEFT_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.GANONS_CASTLE_LIGHT_TRIAL_THIRD_LEFT_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.GANONS_CASTLE_LIGHT_TRIAL_FIRST_RIGHT_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.GANONS_CASTLE_LIGHT_TRIAL_SECOND_RIGHT_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.GANONS_CASTLE_LIGHT_TRIAL_THIRD_RIGHT_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.GANONS_CASTLE_LIGHT_TRIAL_INVISIBLE_ENEMIES_CHEST,
         lambda bundle: (can_do_trick(Tricks.LENS_GANON, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & (can_kill_enemy(bundle, Enemies.BIG_SKULLTULA) & can_kill_enemy(bundle, Enemies.KEESE, EnemyDistance.CLOSE, True, 3)) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_LIGHT_TRIAL_CHESTS_ROOM, world, [
        (Regions.GANONS_CASTLE_MAIN,
         lambda bundle: True_()),
        (Regions.GANONS_CASTLE_LIGHT_TRIAL_TRIFORCE_ROOM,
         lambda bundle: small_keys_scene("SCENE_INSIDE_GANONS_CASTLE", 1, bundle)),
    ])

    # Ganon's Castle Light Trial Triforce Room  (upstream RR_GANONS_CASTLE_LIGHT_TRIAL_TRIFORCE_ROOM, SCENE_INSIDE_GANONS_CASTLE)
    # Locations
    add_locations(Regions.GANONS_CASTLE_LIGHT_TRIAL_TRIFORCE_ROOM, world, [
        (Locations.GANONS_CASTLE_LIGHT_TRIAL_LULLABY_CHEST,
         lambda bundle: can_use(Items.ZELDAS_LULLABY, bundle) & has_open_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_LIGHT_TRIAL_TRIFORCE_ROOM, world, [
        (Regions.GANONS_CASTLE_LIGHT_TRIAL_CHESTS_ROOM,
         lambda bundle: True_()),
        (Regions.GANONS_CASTLE_LIGHT_TRIAL_BOULDER_ROOM,
         lambda bundle: small_keys_scene("SCENE_INSIDE_GANONS_CASTLE", 2, bundle)),
    ])

    # Ganon's Castle Light Trial Boulder Room  (upstream RR_GANONS_CASTLE_LIGHT_TRIAL_BOULDER_ROOM, SCENE_INSIDE_GANONS_CASTLE)
    # Events
    add_events(Regions.GANONS_CASTLE_LIGHT_TRIAL_BOULDER_ROOM, world, [
        (EventLocations.GANONS_CASTLE_LIGHT_TRIAL_BOULDER_ROOM_GANONS_CASTLE_SILVER_LIGHT, Events.GANONS_CASTLE_SILVER_LIGHT,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) | (is_adult(bundle) & can_ground_jump(bundle))),
    ])
    # Locations
    add_locations(Regions.GANONS_CASTLE_LIGHT_TRIAL_BOULDER_ROOM, world, [
        (Locations.GANONS_CASTLE_LIGHT_TRIAL_BOULDER_POT1,
         lambda bundle: can_break_pots(bundle)),
        # DEFERRED RC_GANONS_CASTLE_OUTER_RIGHT_LIGHT_SILVER: true
        # DEFERRED RC_GANONS_CASTLE_OUTER_LEFT_LIGHT_SILVER: true
        # DEFERRED RC_GANONS_CASTLE_UPPER_LIGHT_SILVER: logic->CanUse(RG_HOOKSHOT) || (logic->IsAdult && logic->CanGroundJump())
        # DEFERRED RC_GANONS_CASTLE_INNER_RIGHT_LIGHT_SILVER: true
        # DEFERRED RC_GANONS_CASTLE_INNER_LEFT_LIGHT_SILVER: true
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_LIGHT_TRIAL_BOULDER_ROOM, world, [
        (Regions.GANONS_CASTLE_LIGHT_TRIAL_TRIFORCE_ROOM,
         lambda bundle: small_keys_scene("SCENE_INSIDE_GANONS_CASTLE", 2, bundle)),
        (Regions.GANONS_CASTLE_LIGHT_TRIAL_FINAL_ROOM,
         lambda bundle: has_item(Events.GANONS_CASTLE_SILVER_LIGHT, bundle)),
    ])

    # Ganon's Castle Light Trial Final Room  (upstream RR_GANONS_CASTLE_LIGHT_TRIAL_FINAL_ROOM, SCENE_INSIDE_GANONS_CASTLE)
    # Events
    add_events(Regions.GANONS_CASTLE_LIGHT_TRIAL_FINAL_ROOM, world, [
        (EventLocations.GANONS_CASTLE_LIGHT_TRIAL_FINAL_ROOM_LIGHT_TRIAL_CLEAR, Events.LIGHT_TRIAL_CLEAR,
         lambda bundle: (can_do_trick(Tricks.LENS_GANON, bundle) | can_use(Items.LENS_OF_TRUTH, bundle)) & can_use(Items.LIGHT_ARROW, bundle)),
    ])
    # Locations
    add_locations(Regions.GANONS_CASTLE_LIGHT_TRIAL_FINAL_ROOM, world, [
        (Locations.GANONS_CASTLE_LIGHT_TRIAL_POT1,
         lambda bundle: can_break_pots(bundle) & (can_do_trick(Tricks.LENS_GANON, bundle) | can_use(Items.LENS_OF_TRUTH, bundle))),
        (Locations.GANONS_CASTLE_LIGHT_TRIAL_POT2,
         lambda bundle: can_break_pots(bundle) & (can_do_trick(Tricks.LENS_GANON, bundle) | can_use(Items.LENS_OF_TRUTH, bundle))),
    ])
    # Connections
    connect_regions(Regions.GANONS_CASTLE_LIGHT_TRIAL_FINAL_ROOM, world, [
        (Regions.GANONS_CASTLE_LIGHT_TRIAL_BOULDER_ROOM,
         lambda bundle: True_()),
    ])

    # Ganon's Tower Entryway  (upstream RR_GANONS_TOWER_ENTRYWAY, SCENE_INSIDE_GANONS_CASTLE)
    # Connections
    connect_regions(Regions.GANONS_TOWER_ENTRYWAY, world, [
        (Regions.GANONS_CASTLE_LOBBY,
         lambda bundle: True_()),
        (Regions.GANONS_TOWER_STAIRS_1,
         lambda bundle: True_()),
    ])

    # Ganon's Tower Stairs 1  (upstream RR_GANONS_TOWER_STAIRS_1, SCENE_GANONS_TOWER)
    # Connections
    connect_regions(Regions.GANONS_TOWER_STAIRS_1, world, [
        (Regions.GANONS_TOWER_ENTRYWAY,
         lambda bundle: True_()),
        (Regions.GANONS_TOWER_FLOOR_1,
         lambda bundle: True_()),
        (Regions.CASTLE_GROUNDS_FROM_GANONS_CASTLE,
         lambda bundle: False_()),
    ])

    # Ganon's Tower Floor 1  (upstream RR_GANONS_TOWER_FLOOR_1, SCENE_GANONS_TOWER)
    # Connections
    connect_regions(Regions.GANONS_TOWER_FLOOR_1, world, [
        (Regions.GANONS_TOWER_STAIRS_1,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.DINOLFOS, EnemyDistance.CLOSE, True, 2))),
        (Regions.GANONS_TOWER_STAIRS_2,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.DINOLFOS, EnemyDistance.CLOSE, True, 2))),
    ])

    # Ganon's Tower Stairs 2  (upstream RR_GANONS_TOWER_STAIRS_2, SCENE_GANONS_TOWER)
    # Connections
    connect_regions(Regions.GANONS_TOWER_STAIRS_2, world, [
        (Regions.GANONS_TOWER_FLOOR_1,
         lambda bundle: True_()),
        (Regions.GANONS_TOWER_FLOOR_2,
         lambda bundle: True_()),
    ])

    # Ganon's Tower Floor 2  (upstream RR_GANONS_TOWER_FLOOR_2, SCENE_GANONS_TOWER)
    # Locations
    add_locations(Regions.GANONS_TOWER_FLOOR_2, world, [
        (Locations.GANONS_CASTLE_TOWER_BOSS_KEY_CHEST,
         lambda bundle: can_kill_enemy(bundle, Enemies.STALFOS, EnemyDistance.CLOSE, True, 2) & can_open_large_chest(bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_TOWER_FLOOR_2, world, [
        (Regions.GANONS_TOWER_STAIRS_2,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.STALFOS, EnemyDistance.CLOSE, True, 2))),
        (Regions.GANONS_TOWER_STAIRS_3,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.STALFOS, EnemyDistance.CLOSE, True, 2))),
    ])

    # Ganon's Tower Stairs 3  (upstream RR_GANONS_TOWER_STAIRS_3, SCENE_GANONS_TOWER)
    # Connections
    connect_regions(Regions.GANONS_TOWER_STAIRS_3, world, [
        (Regions.GANONS_TOWER_FLOOR_2,
         lambda bundle: True_()),
        (Regions.GANONS_TOWER_FLOOR_3,
         lambda bundle: True_()),
    ])

    # Ganon's Tower Floor 3  (upstream RR_GANONS_TOWER_FLOOR_3, SCENE_GANONS_TOWER)
    # Connections
    connect_regions(Regions.GANONS_TOWER_FLOOR_3, world, [
        (Regions.GANONS_TOWER_STAIRS_3,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.IRON_KNUCKLE, EnemyDistance.CLOSE, True, 2))),
        (Regions.GANONS_TOWER_STAIRS_4,
         lambda bundle: any_age_time(bundle, lambda bundle: can_kill_enemy(bundle, Enemies.IRON_KNUCKLE, EnemyDistance.CLOSE, True, 2))),
    ])

    # Ganon's Tower Stairs 4  (upstream RR_GANONS_TOWER_STAIRS_4, SCENE_GANONS_TOWER)
    # Connections
    connect_regions(Regions.GANONS_TOWER_STAIRS_4, world, [
        (Regions.GANONS_TOWER_FLOOR_3,
         lambda bundle: True_()),
        (Regions.GANONS_TOWER_POT_ROOM,
         lambda bundle: True_()),
    ])

    # Ganon's Tower Pot Room  (upstream RR_GANONS_TOWER_POT_ROOM, SCENE_GANONS_TOWER)
    # Locations
    add_locations(Regions.GANONS_TOWER_POT_ROOM, world, [
        (Locations.GANONS_CASTLE_GANONS_TOWER_POT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_GANONS_TOWER_POT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_GANONS_TOWER_POT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_GANONS_TOWER_POT4,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_GANONS_TOWER_POT5,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_GANONS_TOWER_POT6,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_GANONS_TOWER_POT7,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_GANONS_TOWER_POT8,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_GANONS_TOWER_POT9,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_GANONS_TOWER_POT10,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_GANONS_TOWER_POT11,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_GANONS_TOWER_POT12,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_GANONS_TOWER_POT13,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_GANONS_TOWER_POT14,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_GANONS_TOWER_POT15,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_GANONS_TOWER_POT16,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_GANONS_TOWER_POT17,
         lambda bundle: can_break_pots(bundle)),
        (Locations.GANONS_CASTLE_GANONS_TOWER_POT18,
         lambda bundle: can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_TOWER_POT_ROOM, world, [
        (Regions.GANONS_TOWER_STAIRS_4,
         lambda bundle: True_()),
        (Regions.GANONS_TOWER_BEFORE_GANONDORF_LAIR,
         lambda bundle: True_()),
    ])

    # Ganon's Tower Before Ganondorf's Lair  (upstream RR_GANONS_TOWER_BEFORE_GANONDORF_LAIR, SCENE_GANONS_TOWER)
    # Locations
    add_locations(Regions.GANONS_TOWER_BEFORE_GANONDORF_LAIR, world, [
        # DEFERRED RC_GANONS_BOSS_KEY_HINT: true
    ])
    # Connections
    connect_regions(Regions.GANONS_TOWER_BEFORE_GANONDORF_LAIR, world, [
        (Regions.GANONS_TOWER_POT_ROOM,
         lambda bundle: False_()),
        (Regions.GANONS_TOWER_GANONDORF_LAIR,
         lambda bundle: any_age_time(bundle, lambda bundle: has_item(Items.GANONS_CASTLE_BOSS_KEY, bundle))),
    ])

    # Ganondorf's Lair  (upstream RR_GANONS_TOWER_GANONDORF_LAIR, SCENE_GANONDORF_BOSS)
    # Locations
    add_locations(Regions.GANONS_TOWER_GANONDORF_LAIR, world, [
        (Locations.GANONS_CASTLE_GANONDORF_HINT,
         lambda bundle: has_item(Items.GANONS_SOUL, bundle)),
    ])
    # Connections
    connect_regions(Regions.GANONS_TOWER_GANONDORF_LAIR, world, [
        (Regions.GANONS_CASTLE_ESCAPE,
         lambda bundle: can_kill_enemy(bundle, Enemies.GANONDORF)),
    ])

    # Ganon's Castle Escape  (upstream RR_GANONS_CASTLE_ESCAPE, SCENE_GANONS_TOWER_COLLAPSE_EXTERIOR)
    # Connections
    connect_regions(Regions.GANONS_CASTLE_ESCAPE, world, [
        (Regions.GANONS_CASTLE_GANON_ARENA,
         lambda bundle: True_()),
    ])

    # Ganon's Arena  (upstream RR_GANONS_CASTLE_GANON_ARENA, SCENE_GANON_BOSS)
    # Locations
    add_locations(Regions.GANONS_CASTLE_GANON_ARENA, world, [
        (Locations.GANON,
         lambda bundle: can_kill_enemy(bundle, Enemies.GANON)),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_BLUE_FIRE', 'CAN_ACCESS_FAIRIES', 'CAN_FARM_NUTS', 'FIRE_TRIAL_CLEAR', 'FOREST_TRIAL_CLEAR', 'GANONS_CASTLE_SILVER_FIRE', 'GANONS_CASTLE_SILVER_FOREST', 'GANONS_CASTLE_SILVER_LIGHT', 'GANONS_CASTLE_SILVER_SPIRIT', 'LIGHT_TRIAL_CLEAR', 'SHADOW_TRIAL_CLEAR', 'SHADOW_TRIAL_LATE_CHEST', 'SHADOW_TRIAL_RUSTED_SWITCH', 'SPIRIT_TRIAL_CLEAR', 'WATER_TRIAL_CLEAR', 'WATER_TRIAL_RUSTED_SWITCH']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (27): ['RC_GANONS_CASTLE_SOT_BLOCK_FOREST_SILVER', 'RC_GANONS_CASTLE_ON_TARGET_FOREST_SILVER', 'RC_GANONS_CASTLE_LARGE_PLATFORM_FOREST_SILVER', 'RC_GANONS_CASTLE_UNDER_LEDGE_FOREST_SILVER', 'RC_GANONS_CASTLE_ON_TARGET_FOREST_SILVER', 'RC_GANONS_CASTLE_SMALL_PLATFORM_FOREST_SILVER', 'RC_GANONS_CASTLE_TORCH_SLUG_FIRE_SILVER', 'RC_GANONS_CASTLE_FLAME_JETS_FIRE_SILVER', 'RC_GANONS_CASTLE_DISTANT_PLATFORM_FIRE_SILVER', 'RC_GANONS_CASTLE_CLOSE_PLATFORM_FIRE_SILVER', 'RC_GANONS_GANONS_CASTLE_UNDER_PILLAR_FIRE_SILVER', 'RC_GANONS_CASTLE_TORCH_SLUG_FIRE_SILVER', 'RC_GANONS_CASTLE_FLAME_JETS_FIRE_SILVER', 'RC_GANONS_CASTLE_DISTANT_PLATFORM_FIRE_SILVER', 'RC_GANONS_CASTLE_CLOSE_PLATFORM_FIRE_SILVER', 'RC_GANONS_GANONS_CASTLE_UNDER_PILLAR_FIRE_SILVER', 'RC_GANONS_CASTLE_AIRBORNE_SPIRIT_SILVER', 'RC_GANONS_CASTLE_NEAR_DOORMAT_SPIRIT_SILVER', 'RC_GANONS_CASTLE_LOWER_MIDDLE_SPIRIT_SILVER', 'RC_GANONS_CASTLE_CORNER_SPIRIT_SILVER', 'RC_GANONS_CASTLE_NEAR_BARRED_DOOR_SPIRIT_SILVER', 'RC_GANONS_CASTLE_OUTER_RIGHT_LIGHT_SILVER', 'RC_GANONS_CASTLE_OUTER_LEFT_LIGHT_SILVER', 'RC_GANONS_CASTLE_UPPER_LIGHT_SILVER', 'RC_GANONS_CASTLE_INNER_RIGHT_LIGHT_SILVER', 'RC_GANONS_CASTLE_INNER_LEFT_LIGHT_SILVER', 'RC_GANONS_BOSS_KEY_HINT']
