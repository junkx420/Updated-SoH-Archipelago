"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/gerudo_valley.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    GERUDO_VALLEY_CHILD_CAN_PASS_TIME = "Gerudo Valley Child Can Pass Time"
    GERUDO_VALLEY_ADULT_CAN_PASS_TIME = "Gerudo Valley Adult Can Pass Time"
    GERUDO_VALLEY_BUG_ACCESS = "Gerudo Valley Bug Access"
    GV_UPPER_STREAM_CHILD_CAN_PASS_TIME = "GV Upper Stream Child Can Pass Time"
    GV_UPPER_STREAM_ADULT_CAN_PASS_TIME = "GV Upper Stream Adult Can Pass Time"
    GV_UPPER_STREAM_PLANT_GERUDO_VALLEY_BEAN = "GV Upper Stream Plant Gerudo Valley Bean"
    GV_UPPER_STREAM_FAIRY_ACCESS = "GV Upper Stream Fairy Access"
    GV_UPPER_STREAM_WATER_CHILD_CAN_PASS_TIME = "GV Upper Stream Water Child Can Pass Time"
    GV_UPPER_STREAM_WATER_ADULT_CAN_PASS_TIME = "GV Upper Stream Water Adult Can Pass Time"
    GV_LOWER_STREAM_CHILD_CAN_PASS_TIME = "GV Lower Stream Child Can Pass Time"
    GV_LOWER_STREAM_ADULT_CAN_PASS_TIME = "GV Lower Stream Adult Can Pass Time"
    GV_WATERFALL_ALCOVE_CHILD_CAN_PASS_TIME = "GV Waterfall Alcove Child Can Pass Time"
    GV_WATERFALL_ALCOVE_ADULT_CAN_PASS_TIME = "GV Waterfall Alcove Adult Can Pass Time"
    GV_GROTTO_LEDGE_CHILD_CAN_PASS_TIME = "GV Grotto Ledge Child Can Pass Time"
    GV_GROTTO_LEDGE_ADULT_CAN_PASS_TIME = "GV Grotto Ledge Adult Can Pass Time"
    GV_CRATE_LEDGE_CHILD_CAN_PASS_TIME = "GV Crate Ledge Child Can Pass Time"
    GV_CRATE_LEDGE_ADULT_CAN_PASS_TIME = "GV Crate Ledge Adult Can Pass Time"
    GV_FORTRESS_SIDE_CHILD_CAN_PASS_TIME = "GV Fortress Side Child Can Pass Time"
    GV_FORTRESS_SIDE_ADULT_CAN_PASS_TIME = "GV Fortress Side Adult Can Pass Time"


def set_region_rules(world: "SohWorld") -> None:

    # Gerudo Valley  (upstream RR_GERUDO_VALLEY, SCENE_GERUDO_VALLEY)
    # Events
    add_events(Regions.GERUDO_VALLEY, world, [
        (EventLocations.GERUDO_VALLEY_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.GERUDO_VALLEY_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
        (EventLocations.GERUDO_VALLEY_BUG_ACCESS, Events.CAN_ACCESS_BUGS,
         lambda bundle: is_child(bundle) & has_grab(bundle)),
    ])
    # Locations
    add_locations(Regions.GERUDO_VALLEY, world, [
        (Locations.GV_GS_SMALL_BRIDGE,
         lambda bundle: is_child(bundle) & hookshot_or_boomerang(bundle) & can_get_nighttime_gs(bundle)),
        # DEFERRED RC_GV_ROCK_1: logic->CanBreakRocks()
        # DEFERRED RC_GV_ROCK_2: logic->CanBreakRocks()
        # DEFERRED RC_GV_ROCK_3: logic->CanBreakRocks()
        # DEFERRED RC_GV_UNDERWATER_ROCK_1: (logic->CanUse(RG_BOMBCHU_5) || (logic->CanUse(RG_BOMB_BAG) && ctx->GetTrickOption(RT_BOMB_DETONATION)) || (logic->IsAdult && logic->HasItem(RG_POWER_BRACELET))) && (logic->IsAdult || logic->HasItem(RG_BRONZE_SCALE) || logic->CanUse(RG_BOOMERANG) || ((ctx->GetTrickOption(RT_VOIDOUT_COLLECTION) && logic->CanVoid()) && logic->HasItem(RG_POWER_BRACELET)))
        # DEFERRED RC_GV_UNDERWATER_ROCK_2: (logic->CanUse(RG_BOMBCHU_5) || (logic->CanUse(RG_BOMB_BAG) && ctx->GetTrickOption(RT_BOMB_DETONATION)) || (logic->IsAdult && logic->HasItem(RG_POWER_BRACELET))) && (logic->IsAdult || logic->HasItem(RG_BRONZE_SCALE) || logic->CanUse(RG_BOOMERANG) || ((ctx->GetTrickOption(RT_VOIDOUT_COLLECTION) && logic->CanVoid()) && logic->HasItem(RG_POWER_BRACELET)))
        # DEFERRED RC_GV_UNDERWATER_ROCK_3: (logic->CanUse(RG_BOMBCHU_5) || (logic->CanUse(RG_BOMB_BAG) && ctx->GetTrickOption(RT_BOMB_DETONATION)) || (logic->IsAdult && logic->HasItem(RG_POWER_BRACELET))) && (logic->IsAdult || logic->HasItem(RG_BRONZE_SCALE) || logic->CanUse(RG_BOOMERANG) || ((ctx->GetTrickOption(RT_VOIDOUT_COLLECTION) && logic->CanVoid()) && logic->HasItem(RG_POWER_BRACELET)))
        # DEFERRED RC_GV_BOULDER_1: logic->IsAdult && logic->BlastOrSmash()
        # DEFERRED RC_GV_BOULDER_2: logic->IsAdult && logic->BlastOrSmash()
        # DEFERRED RC_GV_BRONZE_BOULDER_1: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_GV_BRONZE_BOULDER_2: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        (Locations.GV_BRIDGE_RECTANGLE_SIGN,
         lambda bundle: can_read(bundle)),
        (Locations.GV_EAST_EXIT_ARROW_SIGN,
         lambda bundle: can_read(bundle)),
    ])
    # Connections
    connect_regions(Regions.GERUDO_VALLEY, world, [
        (Regions.HYRULE_FIELD,
         lambda bundle: True_()),
        (Regions.GV_UPPER_STREAM,
         lambda bundle: (is_child(bundle) & has_grab(bundle)) | take_damage(bundle)),
        (Regions.GV_UPPER_STREAM_WATER,
         lambda bundle: True_()),
        (Regions.GV_CRATE_LEDGE,
         lambda bundle: (is_child(bundle) & has_grab(bundle)) | can_use(Items.LONGSHOT, bundle)),
        (Regions.GV_GROTTO_LEDGE,
         lambda bundle: True_()),
        (Regions.GV_FORTRESS_SIDE,
         lambda bundle: (is_adult(bundle) & (summon_epona(bundle) | can_use(Items.LONGSHOT, bundle) | True_(options=[OptionFilter(FortressCarpenters, FortressCarpenters.option_free)]) | has_item(Events.TH_RESCUED_ALL_CARPENTERS, bundle))) | can_recoil_hover(bundle, Recoil.HAMMER) | (bunny_hovers(bundle) & has_climb(bundle)) | ((is_child(bundle) | can_do_trick(Tricks.GV_HOOKSHOT_BRIDGE, bundle)) & can_use(Items.HOOKSHOT, bundle)) | (is_child(bundle) & can_do_trick(Tricks.GV_CHILD_CUCCO_JUMP, bundle) & has_grab(bundle) & can_jump_slash(bundle))),
        (Regions.GV_WATERFALL_ALCOVE,
         lambda bundle: is_child(bundle) & has_grab(bundle)),
        (Regions.GV_LOWER_STREAM,
         lambda bundle: is_child(bundle) & has_grab(bundle)),
    ])

    # GV Upper Stream  (upstream RR_GV_UPPER_STREAM, SCENE_GERUDO_VALLEY)
    # Events
    add_events(Regions.GV_UPPER_STREAM, world, [
        (EventLocations.GV_UPPER_STREAM_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.GV_UPPER_STREAM_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
        (EventLocations.GV_UPPER_STREAM_PLANT_GERUDO_VALLEY_BEAN, Events.PLANT_GERUDO_VALLEY_BEAN,
         lambda bundle: can_plant_bean(bundle)),
        (EventLocations.GV_UPPER_STREAM_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: call_gossip_fairy(bundle) | (is_child(bundle) & bean_planted(bundle, Events.PLANT_GERUDO_VALLEY_BEAN) & can_use(Items.SONG_OF_STORMS, bundle))),
    ])
    # Locations
    add_locations(Regions.GV_UPPER_STREAM, world, [
        (Locations.GV_GS_BEAN_PATCH,
         lambda bundle: can_spawn_soil_skull(bundle) & can_attack(bundle)),
        (Locations.GV_COW,
         lambda bundle: is_child(bundle) & can_use(Items.EPONAS_SONG, bundle)),
        (Locations.GV_BEAN_SPROUT_FAIRY1,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_GERUDO_VALLEY_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.GV_BEAN_SPROUT_FAIRY2,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_GERUDO_VALLEY_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.GV_BEAN_SPROUT_FAIRY3,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_GERUDO_VALLEY_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.GV_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.GV_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_GV_GOSSIP_STONE: true
        (Locations.GV_NEAR_COW_CRATE,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
        # DEFERRED RC_GV_WONDER_LOWER_WATERFALL: logic->IsAdult && (logic->BeanPlanted(LOGIC_PLANT_GERUDO_VALLEY_BEAN) || logic->HasItem(RG_BRONZE_SCALE) || logic->CanUse(RG_IRON_BOOTS) || (ctx->GetTrickOption(RT_VOIDOUT_COLLECTION) && logic->CanVoid()))
        # DEFERRED RC_GV_WONDER_UPPER_WATERFALL: logic->IsAdult && logic->BeanPlanted(LOGIC_PLANT_GERUDO_VALLEY_BEAN)
    ])
    # Connections
    connect_regions(Regions.GV_UPPER_STREAM, world, [
        (Regions.GV_UPPER_STREAM_WATER,
         lambda bundle: True_()),
        (Regions.GV_WATERFALL_ALCOVE,
         lambda bundle: (can_use(Items.LONGSHOT, bundle) & (has_climb(bundle) | can_do_trick(Tricks.HOOKSHOT_LADDERS, bundle))) | bean_planted(bundle, Events.PLANT_GERUDO_VALLEY_BEAN)),
    ])

    # GV Upper Stream Water  (upstream RR_GV_UPPER_STREAM_WATER, SCENE_GERUDO_VALLEY)
    # Events
    add_events(Regions.GV_UPPER_STREAM_WATER, world, [
        (EventLocations.GV_UPPER_STREAM_WATER_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.GV_UPPER_STREAM_WATER_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
    ])
    # Connections
    connect_regions(Regions.GV_UPPER_STREAM_WATER, world, [
        (Regions.GV_UPPER_STREAM,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle)),
        (Regions.GV_LOWER_STREAM,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle)),
        (Regions.GV_WATERFALL_ALCOVE,
         lambda bundle: (has_item(Items.BRONZE_SCALE, bundle) | (can_use(Items.IRON_BOOTS, bundle) & can_use(Items.HOOKSHOT, bundle))) & has_climb(bundle)),
    ])

    # GV Lower Stream  (upstream RR_GV_LOWER_STREAM, SCENE_GERUDO_VALLEY)
    # Events
    add_events(Regions.GV_LOWER_STREAM, world, [
        (EventLocations.GV_LOWER_STREAM_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.GV_LOWER_STREAM_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
    ])
    # Connections
    connect_regions(Regions.GV_LOWER_STREAM, world, [
        (Regions.LAKE_HYLIA,
         lambda bundle: True_()),
    ])

    # GV Waterfall Alcove  (upstream RR_GV_WATERFALL_ALCOVE, SCENE_GERUDO_VALLEY)
    # Events
    add_events(Regions.GV_WATERFALL_ALCOVE, world, [
        (EventLocations.GV_WATERFALL_ALCOVE_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.GV_WATERFALL_ALCOVE_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
    ])
    # Locations
    add_locations(Regions.GV_WATERFALL_ALCOVE, world, [
        (Locations.GV_WATERFALL_FREESTANDING_POH,
         lambda bundle: True_()),
        # DEFERRED RC_GV_WONDER_UPPER_WATERFALL: logic->IsAdult && (logic->HasItem(RG_BRONZE_SCALE) || logic->CanUse(RG_IRON_BOOTS) || (ctx->GetTrickOption(RT_VOIDOUT_COLLECTION) && logic->CanVoid()))
    ])
    # Connections
    connect_regions(Regions.GV_WATERFALL_ALCOVE, world, [
        (Regions.GV_UPPER_STREAM,
         lambda bundle: is_adult(bundle) & can_use(Items.HOVER_BOOTS, bundle)),
        (Regions.GV_UPPER_STREAM_WATER,
         lambda bundle: True_()),
    ])

    # GV Grotto Ledge  (upstream RR_GV_GROTTO_LEDGE, SCENE_GERUDO_VALLEY)
    # Events
    add_events(Regions.GV_GROTTO_LEDGE, world, [
        (EventLocations.GV_GROTTO_LEDGE_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.GV_GROTTO_LEDGE_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
    ])
    # Locations
    add_locations(Regions.GV_GROTTO_LEDGE, world, [
        # DEFERRED RC_GV_SILVER_BOULDER: logic->CanUse(RG_SILVER_GAUNTLETS)
    ])
    # Connections
    connect_regions(Regions.GV_GROTTO_LEDGE, world, [
        (Regions.GV_UPPER_STREAM,
         lambda bundle: ((can_do_trick(Tricks.DAMAGE_BOOST_SIMPLE, bundle) & has_explosives(bundle)) | (bunny_hovers(bundle) & can_jump_slash(bundle)) | can_recoil_hover(bundle, Recoil.HAMMER)) & take_damage(bundle)),
        (Regions.GV_LOWER_STREAM,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle)),
        (Regions.GV_OCTOROK_GROTTO,
         lambda bundle: can_use(Items.SILVER_GAUNTLETS, bundle)),
        (Regions.GV_CRATE_LEDGE,
         lambda bundle: can_use(Items.LONGSHOT, bundle) | can_recoil_hover_from_object(bundle, TorchRecoil.SHORT)),
    ])

    # GV Crate Ledge  (upstream RR_GV_CRATE_LEDGE, SCENE_GERUDO_VALLEY)
    # Events
    add_events(Regions.GV_CRATE_LEDGE, world, [
        (EventLocations.GV_CRATE_LEDGE_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.GV_CRATE_LEDGE_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
    ])
    # Locations
    add_locations(Regions.GV_CRATE_LEDGE, world, [
        (Locations.GV_CRATE_FREESTANDING_POH,
         lambda bundle: can_break_crates(bundle)),
        (Locations.GV_FREESTANDING_POH_CRATE,
         lambda bundle: can_break_crates(bundle)),
    ])
    # Connections
    connect_regions(Regions.GV_CRATE_LEDGE, world, [
        (Regions.GV_UPPER_STREAM,
         lambda bundle: can_do_trick(Tricks.DAMAGE_BOOST_SIMPLE, bundle) & has_explosives(bundle) & take_damage(bundle)),
        (Regions.GV_LOWER_STREAM,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle)),
    ])

    # GV Fortress Side  (upstream RR_GV_FORTRESS_SIDE, SCENE_GERUDO_VALLEY)
    # Events
    add_events(Regions.GV_FORTRESS_SIDE, world, [
        (EventLocations.GV_FORTRESS_SIDE_CHILD_CAN_PASS_TIME, Events.CHILD_CAN_PASS_TIME,
         lambda bundle: is_child(bundle)),
        (EventLocations.GV_FORTRESS_SIDE_ADULT_CAN_PASS_TIME, Events.ADULT_CAN_PASS_TIME,
         lambda bundle: is_adult(bundle)),
    ])
    # Locations
    add_locations(Regions.GV_FORTRESS_SIDE, world, [
        (Locations.GV_CHEST,
         lambda bundle: is_adult(bundle) & (can_use(Items.MEGATON_HAMMER, bundle) | (can_do_trick(Tricks.BOULDER_COLLISION, bundle) & can_use(Items.LONGSHOT, bundle))) & has_open_chest(bundle)),
        (Locations.GV_TRADE_SAW,
         lambda bundle: is_adult(bundle) & can_use(Items.POACHERS_SAW, bundle)),
        (Locations.GV_GS_BEHIND_TENT,
         lambda bundle: is_adult(bundle) & hookshot_or_boomerang(bundle) & can_get_nighttime_gs(bundle)),
        (Locations.GV_GS_PILLAR,
         lambda bundle: is_adult(bundle) & hookshot_or_boomerang(bundle) & can_get_nighttime_gs(bundle)),
        (Locations.GV_NEAR_BRIDGE_CRATE1,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
        (Locations.GV_NEAR_BRIDGE_CRATE2,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
        (Locations.GV_NEAR_BRIDGE_CRATE3,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
        (Locations.GV_NEAR_BRIDGE_CRATE4,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
        # DEFERRED RC_GV_ROCK_ACROSS_BRIDGE_1: logic->IsAdult && logic->CanBreakRocks()
        # DEFERRED RC_GV_ROCK_ACROSS_BRIDGE_2: logic->IsAdult && logic->CanBreakRocks()
        # DEFERRED RC_GV_ROCK_ACROSS_BRIDGE_3: logic->IsAdult && logic->CanBreakRocks()
        # DEFERRED RC_GV_ROCK_ACROSS_BRIDGE_4: logic->IsAdult && logic->CanBreakRocks()
        # DEFERRED RC_GV_BOULDER_ACROSS_BRIDGE: logic->IsAdult && logic->BlastOrSmash()
        # DEFERRED RC_GV_BRONZE_BOULDER_ACROSS_BRIDGE_1: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_GV_BRONZE_BOULDER_ACROSS_BRIDGE_2: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_GV_BRONZE_BOULDER_ACROSS_BRIDGE_3: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_GV_BRONZE_BOULDER_ACROSS_BRIDGE_4: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_GV_BRONZE_BOULDER_ACROSS_BRIDGE_5: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
        # DEFERRED RC_GV_BRONZE_BOULDER_ACROSS_BRIDGE_6: logic->IsAdult && logic->CanUse(RG_MEGATON_HAMMER)
    ])
    # Connections
    connect_regions(Regions.GV_FORTRESS_SIDE, world, [
        (Regions.GF_OUTSKIRTS,
         lambda bundle: True_()),
        (Regions.GV_UPPER_STREAM,
         lambda bundle: take_damage(bundle)),
        (Regions.GV_UPPER_STREAM_WATER,
         lambda bundle: True_()),
        (Regions.GERUDO_VALLEY,
         lambda bundle: is_child(bundle) | summon_epona(bundle) | can_use(Items.LONGSHOT, bundle) | True_(options=[OptionFilter(FortressCarpenters, FortressCarpenters.option_free)]) | has_item(Events.TH_RESCUED_ALL_CARPENTERS, bundle) | can_recoil_hover(bundle, Recoil.HAMMER) | (bunny_hovers(bundle) & has_climb(bundle))),
        (Regions.GV_CARPENTER_TENT,
         lambda bundle: is_adult(bundle) | can_do_trick(Tricks.GV_CHILD_TENT, bundle)),
        (Regions.GV_STORMS_GROTTO,
         lambda bundle: is_adult(bundle) & can_open_storms_grotto(bundle)),
        (Regions.GV_CRATE_LEDGE,
         lambda bundle: (can_do_trick(Tricks.DAMAGE_BOOST_SIMPLE, bundle) & has_explosives(bundle)) | (can_do_trick(Tricks.GV_CRATE_HOVERS, bundle) & take_damage(bundle) & can_use(Items.HOVER_BOOTS, bundle) & (can_use(Items.MASTER_SWORD, bundle) | can_use(Items.BIGGORONS_SWORD, bundle)))),
    ])

    # GV Carpenter Tent  (upstream RR_GV_CARPENTER_TENT, SCENE_CARPENTERS_TENT)
    # Connections
    connect_regions(Regions.GV_CARPENTER_TENT, world, [
        (Regions.GV_FORTRESS_SIDE,
         lambda bundle: True_()),
    ])

    # GV Octorok Grotto  (upstream RR_GV_OCTOROK_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.GV_OCTOROK_GROTTO, world, [
        (Locations.GV_OCTOROK_GROTTO_FRONT_LEFT_BLUE_RUPEE,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle) | (is_adult(bundle) & (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.GV_OCTOROK_GROTTO_FRONT_RIGHT_BLUE_RUPEE,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle) | (is_adult(bundle) & (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.GV__OCTOROK_GROTTO_BACK_BLUE_RUPEE,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle) | (is_adult(bundle) & (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)) & can_use(Items.HOVER_BOOTS, bundle))),
        (Locations.GV_OCTOROK_GROTTO_FRONT_LEFT_GREEN_RUPEE,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle) | (is_adult(bundle) & (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)) & can_use(Items.HOVER_BOOTS, bundle))),
        (Locations.GV_OCTOROK_GROTTO_FRONT_RIGHT_GREEN_RUPEE,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle) | (is_adult(bundle) & (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)))),
        (Locations.GV_OCTOROK_GROTTO_BACK_LEFT_GREEN_RUPEE,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle) | (is_adult(bundle) & (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)) & can_use(Items.HOVER_BOOTS, bundle))),
        (Locations.GV_OCTOROK_GROTTO_BACK_RIGHT_GREEN_RUPEE,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle) | (is_adult(bundle) & (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)) & can_use(Items.HOVER_BOOTS, bundle))),
        (Locations.GV_OCTOROK_GROTTO_RED_RUPEE,
         lambda bundle: has_item(Items.BRONZE_SCALE, bundle) | can_use(Items.IRON_BOOTS, bundle) | can_use(Items.BOOMERANG, bundle) | (is_adult(bundle) & (can_do_trick(Tricks.VOIDOUT_COLLECTION, bundle) & can_void(bundle)) & can_use(Items.HOVER_BOOTS, bundle))),
    ])
    # Connections
    connect_regions(Regions.GV_OCTOROK_GROTTO, world, [
        (Regions.GV_GROTTO_LEDGE,
         lambda bundle: True_()),
    ])

    # GV Storms Grotto  (upstream RR_GV_STORMS_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.GV_STORMS_GROTTO, world, [
        (Locations.GV_DEKU_SCRUB_GROTTO_REAR,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.GV_DEKU_SCRUB_GROTTO_REAR, bundle)),
        (Locations.GV_DEKU_SCRUB_GROTTO_FRONT,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.GV_DEKU_SCRUB_GROTTO_FRONT, bundle)),
        (Locations.GV_DEKU_SCRUB_GROTTO_BEEHIVE,
         lambda bundle: can_break_upper_beehives(bundle)),
    ])
    # Connections
    connect_regions(Regions.GV_STORMS_GROTTO, world, [
        (Regions.GV_FORTRESS_SIDE,
         lambda bundle: True_()),
    ])

# ---- summary
# notes: []
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_BUGS', 'CAN_ACCESS_FAIRIES', 'PLANT_GERUDO_VALLEY_BEAN', 'TH_RESCUED_ALL_CARPENTERS']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (26): ['RC_GV_ROCK_1', 'RC_GV_ROCK_2', 'RC_GV_ROCK_3', 'RC_GV_UNDERWATER_ROCK_1', 'RC_GV_UNDERWATER_ROCK_2', 'RC_GV_UNDERWATER_ROCK_3', 'RC_GV_BOULDER_1', 'RC_GV_BOULDER_2', 'RC_GV_BRONZE_BOULDER_1', 'RC_GV_BRONZE_BOULDER_2', 'RC_GV_GOSSIP_STONE', 'RC_GV_WONDER_LOWER_WATERFALL', 'RC_GV_WONDER_UPPER_WATERFALL', 'RC_GV_WONDER_UPPER_WATERFALL', 'RC_GV_SILVER_BOULDER', 'RC_GV_ROCK_ACROSS_BRIDGE_1', 'RC_GV_ROCK_ACROSS_BRIDGE_2', 'RC_GV_ROCK_ACROSS_BRIDGE_3', 'RC_GV_ROCK_ACROSS_BRIDGE_4', 'RC_GV_BOULDER_ACROSS_BRIDGE', 'RC_GV_BRONZE_BOULDER_ACROSS_BRIDGE_1', 'RC_GV_BRONZE_BOULDER_ACROSS_BRIDGE_2', 'RC_GV_BRONZE_BOULDER_ACROSS_BRIDGE_3', 'RC_GV_BRONZE_BOULDER_ACROSS_BRIDGE_4', 'RC_GV_BRONZE_BOULDER_ACROSS_BRIDGE_5', 'RC_GV_BRONZE_BOULDER_ACROSS_BRIDGE_6']
