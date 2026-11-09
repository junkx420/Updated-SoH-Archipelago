"""Region logic ported from upstream Ship of Harkinian 9.3.1
soh/soh/Enhancements/randomizer/location_access/overworld/death_mountain_crater.cpp (generated with translate.py, then reviewed by hand).
Master Quest regions are left out (not supported by the apworld)."""
from ...LogicHelpers import *

if TYPE_CHECKING:
    from ... import SohWorld


class EventLocations(StrEnum):
    DMC_CRACKED_WALL_FAIRY_ACCESS = "DMC Cracked Wall Fairy Access"
    DMC_SCRUB_DMC_BOULDER = "DMC Scrub Dmc Boulder"
    DMC_BLOCKED_EXIT_DMC_BOULDER = "DMC Blocked Exit Dmc Boulder"
    DMC_CENTRAL_PLANT_DEATH_MOUNTAIN_CRATER_BEAN = "DMC Central Plant Death Mountain Crater Bean"
    DMC_CENTRAL_FAIRY_ACCESS = "DMC Central Fairy Access"


def set_region_rules(world: "SohWorld") -> None:

    # DMC Upper Entry  (upstream RR_DMC_UPPER_ENTRY, SCENE_DEATH_MOUNTAIN_CRATER)
    # Locations
    add_locations(Regions.DMC_UPPER_ENTRY, world, [
        (Locations.DMC_WALL_FREESTANDING_POH,
         lambda bundle: ((fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3)) & (has_climb(bundle) | (can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & can_jump_slash(bundle)))) | (is_adult(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN) & (((fire_timer_at_least(bundle, 72) | hearts_at_least(bundle, 14)) & dmc_upper_to_pots(bundle) & dmc_pots_to_pad(bundle)) | ((fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & dmc_upper_to_pad(bundle))))),
        (Locations.DMC_VOLCANO_FREESTANDING_POH,
         lambda bundle: ((fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle)) | (is_adult(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN) & (((fire_timer_at_least(bundle, 56) | hearts_at_least(bundle, 11)) & dmc_upper_to_pots(bundle) & dmc_pots_to_pad(bundle)) | ((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_upper_to_pad(bundle))))),
    ])
    # Connections
    connect_regions(Regions.DMC_UPPER_ENTRY, world, [
        (Regions.DMC_CRATE,
         lambda bundle: True_()),
        (Regions.DMC_ROCK_GROTTO,
         lambda bundle: fire_timer_at_least(bundle, 8) | hearts_at_least(bundle, 2)),
        (Regions.DMC_CRACKED_WALL,
         lambda bundle: (fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3))),
        (Regions.DMC_SCRUB,
         lambda bundle: fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3)),
        (Regions.DMC_BLOCKED_EXIT,
         lambda bundle: ((fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & dmc_upper_to_pots(bundle)) | ((fire_timer_at_least(bundle, 56) | hearts_at_least(bundle, 11)) & dmc_upper_to_pad(bundle))),
        (Regions.DMC_POTS,
         lambda bundle: ((fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & dmc_upper_to_pots(bundle)) | ((fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & dmc_upper_to_pad(bundle))),
        (Regions.DMC_POT_GROTTO_EXIT,
         lambda bundle: ((fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & dmc_upper_to_pots(bundle)) | ((fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & dmc_upper_to_pad(bundle))),
        (Regions.DMC_CENTRAL,
         lambda bundle: ((fire_timer_at_least(bundle, 64) | hearts_at_least(bundle, 12)) & dmc_upper_to_pots(bundle) & dmc_pots_to_pad(bundle)) | ((fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & dmc_upper_to_pad(bundle))),
        (Regions.DMC_FAR_PLATFORM,
         lambda bundle: (is_adult(bundle) & (fire_timer_at_least(bundle, 72) | hearts_at_least(bundle, 14)) & dmc_upper_to_pots(bundle) & dmc_pots_to_pad(bundle) & reach_distant_scarecrow(bundle)) | (fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & take_damage(bundle) & can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle)),
        (Regions.DMC_TEMPLE_EXIT,
         lambda bundle: (is_adult(bundle) | (False_())) & (((fire_timer_at_least(bundle, 72) | hearts_at_least(bundle, 14)) & dmc_upper_to_pots(bundle) & dmc_pots_to_pad(bundle)) | ((fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & dmc_upper_to_pad(bundle)))),
    ])

    # DMC Rocks Grotto Entry  (upstream RR_DMC_ROCKS_GROTTO_ENTRY, SCENE_DEATH_MOUNTAIN_CRATER)
    # Locations
    add_locations(Regions.DMC_ROCKS_GROTTO_ENTRY, world, [
        (Locations.DMC_WALL_FREESTANDING_POH,
         lambda bundle: ((fire_timer_at_least(bundle, 8) | hearts_at_least(bundle, 2)) & (has_climb(bundle) | (can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & can_jump_slash(bundle)))) | (is_adult(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN) & (((fire_timer_at_least(bundle, 72) | hearts_at_least(bundle, 14)) & dmc_upper_to_pots(bundle) & dmc_pots_to_pad(bundle)) | ((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_upper_to_pad(bundle))))),
        (Locations.DMC_VOLCANO_FREESTANDING_POH,
         lambda bundle: ((fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle)) | (is_adult(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN) & (((fire_timer_at_least(bundle, 64) | hearts_at_least(bundle, 12)) & dmc_upper_to_pots(bundle) & dmc_pots_to_pad(bundle)) | ((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_upper_to_pad(bundle))))),
    ])
    # Connections
    connect_regions(Regions.DMC_ROCKS_GROTTO_ENTRY, world, [
        (Regions.DMC_CRATE,
         lambda bundle: fire_timer_at_least(bundle, 8) | hearts_at_least(bundle, 2)),
        (Regions.DMC_ROCK_GROTTO,
         lambda bundle: True_()),
        (Regions.DMC_CRACKED_WALL,
         lambda bundle: (fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3))),
        (Regions.DMC_SCRUB,
         lambda bundle: fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3)),
        (Regions.DMC_BLOCKED_EXIT,
         lambda bundle: ((fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & dmc_upper_to_pots(bundle)) | ((fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & dmc_upper_to_pad(bundle))),
        (Regions.DMC_POTS,
         lambda bundle: ((fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & dmc_upper_to_pots(bundle)) | ((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_upper_to_pad(bundle))),
        (Regions.DMC_POT_GROTTO_EXIT,
         lambda bundle: ((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_upper_to_pots(bundle)) | ((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_upper_to_pad(bundle))),
        (Regions.DMC_CENTRAL,
         lambda bundle: ((fire_timer_at_least(bundle, 64) | hearts_at_least(bundle, 12)) & dmc_upper_to_pots(bundle) & dmc_pots_to_pad(bundle)) | ((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_upper_to_pad(bundle))),
        (Regions.DMC_FAR_PLATFORM,
         lambda bundle: (is_adult(bundle) & (fire_timer_at_least(bundle, 72) | hearts_at_least(bundle, 14)) & dmc_upper_to_pots(bundle) & dmc_pots_to_pad(bundle) & reach_distant_scarecrow(bundle)) | (fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3)) & take_damage(bundle) & can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle)),
        (Regions.DMC_TEMPLE_EXIT,
         lambda bundle: (is_adult(bundle) | (False_())) & (((fire_timer_at_least(bundle, 64) | hearts_at_least(bundle, 12)) & dmc_upper_to_pots(bundle) & dmc_pots_to_pad(bundle)) | ((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_upper_to_pad(bundle)))),
    ])

    # DMC Blocked Entry  (upstream RR_DMC_BLOCKED_ENTRY, SCENE_DEATH_MOUNTAIN_CRATER)
    # Locations
    add_locations(Regions.DMC_BLOCKED_ENTRY, world, [
        (Locations.DMC_WALL_FREESTANDING_POH,
         lambda bundle: ((fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & can_climb_ladder(bundle) & (has_climb(bundle) | (can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & can_jump_slash(bundle)))) | (is_adult(bundle) & (fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_pots_to_pad(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)) | ((fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle))),
        (Locations.DMC_VOLCANO_FREESTANDING_POH,
         lambda bundle: ((fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_pots_to_pad(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN))),
    ])
    # Connections
    connect_regions(Regions.DMC_BLOCKED_ENTRY, world, [
        (Regions.DMC_CRATE,
         lambda bundle: ((fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & can_climb_ladder(bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 56) | hearts_at_least(bundle, 11)) & dmc_pots_to_pad(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)) | ((fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle))),
        (Regions.DMC_ROCK_GROTTO,
         lambda bundle: ((fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & can_climb_ladder(bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & dmc_pots_to_pad(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)) | ((fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle))),
        (Regions.DMC_CRACKED_WALL,
         lambda bundle: (fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & can_climb_ladder(bundle) | (is_adult(bundle) & (fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & dmc_pots_to_pad(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)) | ((fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle))),
        (Regions.DMC_SCRUB,
         lambda bundle: fire_timer_at_least(bundle, 8) | hearts_at_least(bundle, 2)),
        (Regions.DMC_BLOCKED_EXIT,
         lambda bundle: True_()),
        (Regions.DMC_POTS,
         lambda bundle: fire_timer_at_least(bundle, 8) | hearts_at_least(bundle, 2)),
        (Regions.DMC_POT_GROTTO_EXIT,
         lambda bundle: fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3)),
        (Regions.DMC_CENTRAL,
         lambda bundle: ((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_pots_to_pad(bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & dmc_upper_to_pad(bundle))),
        (Regions.DMC_FAR_PLATFORM,
         lambda bundle: (is_adult(bundle) & (fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & dmc_pots_to_pad(bundle) & reach_distant_scarecrow(bundle)) | ((fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & take_damage(bundle) & can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & can_climb_ladder(bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & dmc_pots_to_pad(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)) | ((fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & take_damage(bundle) & can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle))),
        (Regions.DMC_TEMPLE_EXIT,
         lambda bundle: (is_adult(bundle) | (False_())) & (((fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & dmc_pots_to_pad(bundle)) | ((fire_timer_at_least(bundle, 56) | hearts_at_least(bundle, 11)) & dmc_upper_to_pad(bundle) & can_climb_ladder(bundle)))),
    ])

    # DMC Pots Entry  (upstream RR_DMC_POTS_ENTRY, SCENE_DEATH_MOUNTAIN_CRATER)
    # Locations
    add_locations(Regions.DMC_POTS_ENTRY, world, [
        (Locations.DMC_WALL_FREESTANDING_POH,
         lambda bundle: ((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & can_climb_ladder(bundle) & (has_climb(bundle) | (can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & can_jump_slash(bundle)))) | (is_adult(bundle) & (fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_pots_to_pad(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)) | ((fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle))),
        (Locations.DMC_VOLCANO_FREESTANDING_POH,
         lambda bundle: ((fire_timer_at_least(bundle, 8) | hearts_at_least(bundle, 2)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & dmc_pots_to_pad(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN))),
    ])
    # Connections
    connect_regions(Regions.DMC_POTS_ENTRY, world, [
        (Regions.DMC_CRATE,
         lambda bundle: (fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & can_climb_ladder(bundle) | (is_adult(bundle) & (fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & dmc_pots_to_pad(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)) | ((fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle))),
        (Regions.DMC_ROCK_GROTTO,
         lambda bundle: (fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & can_climb_ladder(bundle) | (is_adult(bundle) & (fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & dmc_pots_to_pad(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)) | ((fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle))),
        (Regions.DMC_CRACKED_WALL,
         lambda bundle: (fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & can_climb_ladder(bundle) | (is_adult(bundle) & (fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_pots_to_pad(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)) | ((fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle))),
        (Regions.DMC_SCRUB,
         lambda bundle: fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3)),
        (Regions.DMC_BLOCKED_EXIT,
         lambda bundle: fire_timer_at_least(bundle, 8) | hearts_at_least(bundle, 2)),
        (Regions.DMC_POTS,
         lambda bundle: True_()),
        (Regions.DMC_POT_GROTTO_EXIT,
         lambda bundle: fire_timer_at_least(bundle, 8) | hearts_at_least(bundle, 2)),
        (Regions.DMC_CENTRAL,
         lambda bundle: ((fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & dmc_pots_to_pad(bundle)) | ((fire_timer_at_least(bundle, 56) | hearts_at_least(bundle, 11)) & dmc_upper_to_pad(bundle) & can_climb_ladder(bundle))),
        (Regions.DMC_FAR_PLATFORM,
         lambda bundle: (is_adult(bundle) & (fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_pots_to_pad(bundle) & reach_distant_scarecrow(bundle)) | ((fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & take_damage(bundle) & can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & can_climb_ladder(bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_pots_to_pad(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)) | ((fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & take_damage(bundle) & can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle))),
        (Regions.DMC_TEMPLE_EXIT,
         lambda bundle: (is_adult(bundle) | (False_())) & (((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_pots_to_pad(bundle)) | ((fire_timer_at_least(bundle, 56) | hearts_at_least(bundle, 11)) & dmc_upper_to_pad(bundle) & can_climb_ladder(bundle)))),
    ])

    # DMC Pot Grotto Entry  (upstream RR_DMC_POT_GROTTO_ENTRY, SCENE_DEATH_MOUNTAIN_CRATER)
    # Locations
    add_locations(Regions.DMC_POT_GROTTO_ENTRY, world, [
        (Locations.DMC_WALL_FREESTANDING_POH,
         lambda bundle: ((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & can_climb_ladder(bundle) & (has_climb(bundle) | (can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & can_jump_slash(bundle)))) | (is_adult(bundle) & (fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_pots_to_pad(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)) | ((fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle) & (has_climb(bundle) | (can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & can_jump_slash(bundle))))),
        (Locations.DMC_VOLCANO_FREESTANDING_POH,
         lambda bundle: (fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) | (is_adult(bundle) & (fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & dmc_pots_to_pad(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN))),
    ])
    # Connections
    connect_regions(Regions.DMC_POT_GROTTO_ENTRY, world, [
        (Regions.DMC_CRATE,
         lambda bundle: (fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & can_climb_ladder(bundle) | (is_adult(bundle) & (fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & dmc_pots_to_pad(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)) | ((fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle))),
        (Regions.DMC_ROCK_GROTTO,
         lambda bundle: (fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & can_climb_ladder(bundle) | (is_adult(bundle) & (fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_pots_to_pad(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)) | ((fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle))),
        (Regions.DMC_CRACKED_WALL,
         lambda bundle: (fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & can_climb_ladder(bundle) | (is_adult(bundle) & (fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & dmc_pots_to_pad(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)) | ((fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle))),
        (Regions.DMC_SCRUB,
         lambda bundle: fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)),
        (Regions.DMC_BLOCKED_EXIT,
         lambda bundle: fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3)),
        (Regions.DMC_POTS,
         lambda bundle: fire_timer_at_least(bundle, 8) | hearts_at_least(bundle, 2)),
        (Regions.DMC_POT_GROTTO_EXIT,
         lambda bundle: True_()),
        (Regions.DMC_CENTRAL,
         lambda bundle: ((fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & dmc_pots_to_pad(bundle)) | ((fire_timer_at_least(bundle, 56) | hearts_at_least(bundle, 11)) & dmc_upper_to_pad(bundle) & can_climb_ladder(bundle))),
        (Regions.DMC_FAR_PLATFORM,
         lambda bundle: (is_adult(bundle) & (fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_pots_to_pad(bundle) & reach_distant_scarecrow(bundle)) | ((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & take_damage(bundle) & can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & can_climb_ladder(bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_pots_to_pad(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)) | ((fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & take_damage(bundle) & can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle))),
        (Regions.DMC_TEMPLE_EXIT,
         lambda bundle: (is_adult(bundle) | (False_())) & (((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & dmc_pots_to_pad(bundle)) | ((fire_timer_at_least(bundle, 56) | hearts_at_least(bundle, 11)) & dmc_upper_to_pad(bundle) & can_climb_ladder(bundle)))),
    ])

    # DMC Pad Entry  (upstream RR_DMC_PAD_ENTRY, SCENE_DEATH_MOUNTAIN_CRATER)
    # Locations
    add_locations(Regions.DMC_PAD_ENTRY, world, [
        (Locations.DMC_WALL_FREESTANDING_POH,
         lambda bundle: ((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & can_climb_ladder(bundle) & dmc_pad_to_pots(bundle) & (has_climb(bundle) | (can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & can_jump_slash(bundle)))) | ((fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle) & (has_climb(bundle) | (can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & can_jump_slash(bundle)))) | (is_adult(bundle) & (fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN))),
        (Locations.DMC_VOLCANO_FREESTANDING_POH,
         lambda bundle: (fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & dmc_pad_to_pots(bundle) | (is_adult(bundle) & (fire_timer_at_least(bundle, 8) | hearts_at_least(bundle, 2)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN))),
    ])
    # Connections
    connect_regions(Regions.DMC_PAD_ENTRY, world, [
        (Regions.DMC_CRATE,
         lambda bundle: ((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & can_climb_ladder(bundle) & dmc_pad_to_pots(bundle)) | ((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN))),
        (Regions.DMC_ROCK_GROTTO,
         lambda bundle: ((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & can_climb_ladder(bundle) & dmc_pad_to_pots(bundle)) | ((fire_timer_at_least(bundle, 32) | hearts_at_least(bundle, 6)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN))),
        (Regions.DMC_CRACKED_WALL,
         lambda bundle: (fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & can_climb_ladder(bundle) & dmc_pad_to_pots(bundle) | ((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN))),
        (Regions.DMC_SCRUB,
         lambda bundle: (fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & dmc_pad_to_pots(bundle) | (is_adult(bundle) & (fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN))),
        (Regions.DMC_BLOCKED_EXIT,
         lambda bundle: (fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & dmc_pad_to_pots(bundle) | (is_adult(bundle) & (fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN))),
        (Regions.DMC_POTS,
         lambda bundle: (fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3)) & dmc_pad_to_pots(bundle) | (is_adult(bundle) & (fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN))),
        (Regions.DMC_POT_GROTTO_EXIT,
         lambda bundle: (fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3)) & dmc_pad_to_pots(bundle) | (is_adult(bundle) & (fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN))),
        (Regions.DMC_CENTRAL,
         lambda bundle: (fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3))),
        (Regions.DMC_FAR_PLATFORM,
         lambda bundle: ((fire_timer_at_least(bundle, 56) | hearts_at_least(bundle, 11)) & take_damage(bundle) & can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & can_climb_ladder(bundle) & dmc_pad_to_pots(bundle)) | ((fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 24) | hearts_at_least(bundle, 5)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3)) & reach_distant_scarecrow(bundle))),
        (Regions.DMC_TEMPLE_EXIT,
         lambda bundle: (is_adult(bundle) | (False_())) & (fire_timer_at_least(bundle, 16) | hearts_at_least(bundle, 3))),
    ])

    # DMC Temple Entry  (upstream RR_DMC_TEMPLE_ENTRY, SCENE_DEATH_MOUNTAIN_CRATER)
    # Locations
    add_locations(Regions.DMC_TEMPLE_ENTRY, world, [
        (Locations.DMC_WALL_FREESTANDING_POH,
         lambda bundle: has_climb(bundle) & (((fire_timer_at_least(bundle, 72) | hearts_at_least(bundle, 14)) & dmc_pad_to_pots(bundle)) | ((fire_timer_at_least(bundle, 64) | hearts_at_least(bundle, 12)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)))),
        (Locations.DMC_VOLCANO_FREESTANDING_POH,
         lambda bundle: has_climb(bundle) & ((fire_timer_at_least(bundle, 56) | hearts_at_least(bundle, 11)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & dmc_pad_to_pots(bundle) | (is_adult(bundle) & (fire_timer_at_least(bundle, 40) | hearts_at_least(bundle, 8)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)))),
    ])
    # Connections
    connect_regions(Regions.DMC_TEMPLE_ENTRY, world, [
        (Regions.DMC_CRATE,
         lambda bundle: has_climb(bundle) & (is_adult(bundle) | (False_())) & (((fire_timer_at_least(bundle, 72) | hearts_at_least(bundle, 14)) & dmc_pad_to_pots(bundle)) | ((fire_timer_at_least(bundle, 72) | hearts_at_least(bundle, 14)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 56) | hearts_at_least(bundle, 11)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)))),
        (Regions.DMC_ROCK_GROTTO,
         lambda bundle: has_climb(bundle) & (is_adult(bundle) | (False_())) & (((fire_timer_at_least(bundle, 72) | hearts_at_least(bundle, 14)) & dmc_pad_to_pots(bundle)) | ((fire_timer_at_least(bundle, 64) | hearts_at_least(bundle, 12)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)))),
        (Regions.DMC_CRACKED_WALL,
         lambda bundle: has_climb(bundle) & (is_adult(bundle) | (False_())) & (((fire_timer_at_least(bundle, 80) | hearts_at_least(bundle, 15)) & dmc_pad_to_pots(bundle)) | ((fire_timer_at_least(bundle, 72) | hearts_at_least(bundle, 14)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 56) | hearts_at_least(bundle, 11)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)))),
        (Regions.DMC_SCRUB,
         lambda bundle: has_climb(bundle) & (is_adult(bundle) | (False_())) & (((fire_timer_at_least(bundle, 56) | hearts_at_least(bundle, 11)) & dmc_pad_to_pots(bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)))),
        (Regions.DMC_BLOCKED_EXIT,
         lambda bundle: has_climb(bundle) & (is_adult(bundle) | (False_())) & (((fire_timer_at_least(bundle, 56) | hearts_at_least(bundle, 11)) & dmc_pad_to_pots(bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)))),
        (Regions.DMC_POTS,
         lambda bundle: has_climb(bundle) & (is_adult(bundle) | (False_())) & (((fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & dmc_pad_to_pots(bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)))),
        (Regions.DMC_POT_GROTTO_EXIT,
         lambda bundle: has_climb(bundle) & (is_adult(bundle) | (False_())) & (((fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & dmc_pad_to_pots(bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 56) | hearts_at_least(bundle, 11)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)))),
        (Regions.DMC_CENTRAL,
         lambda bundle: has_climb(bundle) & (is_adult(bundle) | (False_())) & (fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9))),
        (Regions.DMC_FAR_PLATFORM,
         lambda bundle: has_climb(bundle) & (is_adult(bundle) | (False_())) & (((fire_timer_at_least(bundle, 88) | hearts_at_least(bundle, 16)) & take_damage(bundle) & can_do_trick(Tricks.UNINTUITIVE_JUMPS, bundle) & can_climb_ladder(bundle) & dmc_pad_to_pots(bundle)) | ((fire_timer_at_least(bundle, 72) | hearts_at_least(bundle, 14)) & can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) & can_use(Items.HOVER_BOOTS, bundle) & can_use(Items.LONGSHOT, bundle)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 56) | hearts_at_least(bundle, 11)) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN)) | (is_adult(bundle) & (fire_timer_at_least(bundle, 48) | hearts_at_least(bundle, 9)) & reach_distant_scarecrow(bundle)))),
        (Regions.DMC_TEMPLE_EXIT,
         lambda bundle: True_()),
    ])

    # DMC Crate  (upstream RR_DMC_CRATE, SCENE_DEATH_MOUNTAIN_CRATER)
    # Locations
    add_locations(Regions.DMC_CRATE, world, [
        (Locations.DMC_GS_CRATE,
         lambda bundle: is_child(bundle) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA) & can_break_crates(bundle)),
        (Locations.DMC_CRATE,
         lambda bundle: is_child(bundle) & can_break_crates(bundle)),
    ])
    # Connections
    connect_regions(Regions.DMC_CRATE, world, [
        (Regions.DEATH_MOUNTAIN_SUMMIT,
         lambda bundle: True_()),
    ])

    # DMC Rock Grotto  (upstream RR_DMC_ROCK_GROTTO, SCENE_DEATH_MOUNTAIN_CRATER)
    # Locations
    add_locations(Regions.DMC_ROCK_GROTTO, world, [
        (Locations.DMC_CIRCLE_ROCK_1,
         lambda bundle: fire_timer_at_least(bundle, 8) & can_break_rocks(bundle)),
        (Locations.DMC_CIRCLE_ROCK_2,
         lambda bundle: fire_timer_at_least(bundle, 8) & can_break_rocks(bundle)),
        (Locations.DMC_CIRCLE_ROCK_3,
         lambda bundle: fire_timer_at_least(bundle, 8) & can_break_rocks(bundle)),
        (Locations.DMC_CIRCLE_ROCK_4,
         lambda bundle: fire_timer_at_least(bundle, 8) & can_break_rocks(bundle)),
        (Locations.DMC_CIRCLE_ROCK_5,
         lambda bundle: fire_timer_at_least(bundle, 8) & can_break_rocks(bundle)),
        (Locations.DMC_CIRCLE_ROCK_6,
         lambda bundle: fire_timer_at_least(bundle, 8) & can_break_rocks(bundle)),
        (Locations.DMC_CIRCLE_ROCK_7,
         lambda bundle: fire_timer_at_least(bundle, 8) & can_break_rocks(bundle)),
        (Locations.DMC_CIRCLE_ROCK_8,
         lambda bundle: fire_timer_at_least(bundle, 8) & can_break_rocks(bundle)),
        (Locations.DMC_BOULDER_1,
         lambda bundle: fire_timer_at_least(bundle, 8) & blast_or_smash(bundle)),
        (Locations.DMC_BOULDER_2,
         lambda bundle: fire_timer_at_least(bundle, 8) & blast_or_smash(bundle)),
        (Locations.DMC_BOULDER_3,
         lambda bundle: fire_timer_at_least(bundle, 8) & blast_or_smash(bundle)),
    ])
    # Connections
    connect_regions(Regions.DMC_ROCK_GROTTO, world, [
        (Regions.DMC_UPPER_GROTTO,
         lambda bundle: any_age_time(bundle, lambda bundle: blast_or_smash(bundle))),
    ])

    # DMC Cracked Wall  (upstream RR_DMC_CRACKED_WALL, SCENE_DEATH_MOUNTAIN_CRATER)
    # Events
    add_events(Regions.DMC_CRACKED_WALL, world, [
        (EventLocations.DMC_CRACKED_WALL_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: has_explosives(bundle) & call_gossip_fairy_except_suns(bundle)),
    ])
    # Locations
    add_locations(Regions.DMC_CRACKED_WALL, world, [
        (Locations.DMC_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy_except_suns(bundle) & has_explosives(bundle)),
        (Locations.DMC_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle) & has_explosives(bundle)),
        (Locations.DMC_GOSSIP_ROCK_1,
         lambda bundle: is_child(bundle)),
        (Locations.DMC_GOSSIP_ROCK_2,
         lambda bundle: is_child(bundle)),
        # DEFERRED RC_DMC_GOSSIP_STONE: logic->HasExplosives()
    ])

    # DMC Scrub  (upstream RR_DMC_SCRUB, SCENE_DEATH_MOUNTAIN_CRATER)
    # Events
    add_events(Regions.DMC_SCRUB, world, [
        (EventLocations.DMC_SCRUB_DMC_BOULDER, Events.DMC_BOULDER,
         lambda bundle: is_adult(bundle) & can_use(Items.MEGATON_HAMMER, bundle) & can_do_trick(Tricks.DMC_BOULDER_JS, bundle)),
    ])
    # Locations
    add_locations(Regions.DMC_SCRUB, world, [
        (Locations.DMC_DEKU_SCRUB,
         lambda bundle: is_child(bundle) & can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.DMC_DEKU_SCRUB, bundle)),
    ])

    # DMC Blocked Exit  (upstream RR_DMC_BLOCKED_EXIT, SCENE_DEATH_MOUNTAIN_CRATER)
    # Events
    add_events(Regions.DMC_BLOCKED_EXIT, world, [
        (EventLocations.DMC_BLOCKED_EXIT_DMC_BOULDER, Events.DMC_BOULDER,
         lambda bundle: is_adult(bundle) & can_use(Items.MEGATON_HAMMER, bundle)),
    ])
    # Connections
    connect_regions(Regions.DMC_BLOCKED_EXIT, world, [
        (Regions.DMC_GREAT_FAIRY_FOUNTAIN,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
    ])

    # DMC Pots  (upstream RR_DMC_POTS, SCENE_DEATH_MOUNTAIN_CRATER)
    # Locations
    add_locations(Regions.DMC_POTS, world, [
        (Locations.DMC_NEAR_GCPOT1,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DMC_NEAR_GCPOT2,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DMC_NEAR_GCPOT3,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DMC_NEAR_GCPOT4,
         lambda bundle: can_break_pots(bundle)),
        (Locations.DMC_BRONZE_BOULDER_1,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
        (Locations.DMC_BRONZE_BOULDER_2,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
        (Locations.DMC_BRONZE_BOULDER_3,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
        (Locations.DMC_BRONZE_BOULDER_SHORTCUT,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
        (Locations.DMC_BRIDGE_EXIT_ARROW_SIGN,
         lambda bundle: can_read(bundle)),
    ])
    # Connections
    connect_regions(Regions.DMC_POTS, world, [
        (Regions.GC_DARUNIAS_CHAMBER,
         lambda bundle: True_()),
    ])

    # DMC Pot Grotto Exit  (upstream RR_DMC_POT_GROTTO_EXIT, SCENE_DEATH_MOUNTAIN_CRATER)
    # Connections
    connect_regions(Regions.DMC_POT_GROTTO_EXIT, world, [
        (Regions.DMC_SCRUB_GROTTO,
         lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
    ])

    # DMC Central  (upstream RR_DMC_CENTRAL, SCENE_DEATH_MOUNTAIN_CRATER)
    # Events
    add_events(Regions.DMC_CENTRAL, world, [
        (EventLocations.DMC_CENTRAL_PLANT_DEATH_MOUNTAIN_CRATER_BEAN, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN,
         lambda bundle: can_plant_bean(bundle)),
        (EventLocations.DMC_CENTRAL_FAIRY_ACCESS, Events.CAN_ACCESS_FAIRIES,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
    ])
    # Locations
    add_locations(Regions.DMC_CENTRAL, world, [
        (Locations.SHEIK_IN_CRATER,
         lambda bundle: is_adult(bundle)),
        (Locations.DMC_GS_BEAN_PATCH,
         lambda bundle: can_spawn_soil_skull(bundle) & can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA)),
        (Locations.DMC_NEAR_WARP_PLATFORM_RED_RUPEE,
         lambda bundle: is_child(bundle)),
        (Locations.DMC_MIDDLE_PLATFORM_RED_RUPEE,
         lambda bundle: is_child(bundle)),
        (Locations.DMC_MIDDLE_PLATFORM_BLUE_RUPEE1,
         lambda bundle: is_child(bundle)),
        (Locations.DMC_MIDDLE_PLATFORM_BLUE_RUPEE2,
         lambda bundle: is_child(bundle)),
        (Locations.DMC_MIDDLE_PLATFORM_BLUE_RUPEE3,
         lambda bundle: is_child(bundle)),
        (Locations.DMC_MIDDLE_PLATFORM_BLUE_RUPEE4,
         lambda bundle: is_child(bundle)),
        (Locations.DMC_MIDDLE_PLATFORM_BLUE_RUPEE5,
         lambda bundle: is_child(bundle)),
        (Locations.DMC_MIDDLE_PLATFORM_BLUE_RUPEE6,
         lambda bundle: is_child(bundle)),
        (Locations.DMC_BEAN_SPROUT_FAIRY1,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.DMC_BEAN_SPROUT_FAIRY2,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.DMC_BEAN_SPROUT_FAIRY3,
         lambda bundle: is_child(bundle) & bean_planted(bundle, Events.PLANT_DEATH_MOUNTAIN_CRATER_BEAN) & can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.DMC_ROCK_BY_FIRE_TEMPLE_1,
         lambda bundle: is_adult(bundle)),
        (Locations.DMC_ROCK_BY_FIRE_TEMPLE_2,
         lambda bundle: is_adult(bundle)),
        (Locations.DMC_ROCK_BY_FIRE_TEMPLE_3,
         lambda bundle: is_adult(bundle)),
        (Locations.DMC_ROCK_BY_FIRE_TEMPLE_4,
         lambda bundle: is_adult(bundle)),
        (Locations.DMC_ROCK_BY_FIRE_TEMPLE_5,
         lambda bundle: is_adult(bundle)),
        (Locations.DMC_WONDER_BENEATH_BRIDGE_PLATFORM,
         lambda bundle: is_adult(bundle) & (can_use(Items.LONGSHOT, bundle) | can_use(Items.HOVER_BOOTS, bundle))),
    ])

    # DMC Far Platform  (upstream RR_DMC_FAR_PLATFORM, SCENE_DEATH_MOUNTAIN_CRATER)
    # Locations
    add_locations(Regions.DMC_FAR_PLATFORM, world, [
        (Locations.DMC_DISTANT_PLATFORM_RUPEE1,
         lambda bundle: is_adult(bundle)),
        (Locations.DMC_DISTANT_PLATFORM_RUPEE2,
         lambda bundle: is_adult(bundle)),
        (Locations.DMC_DISTANT_PLATFORM_RUPEE3,
         lambda bundle: is_adult(bundle)),
        (Locations.DMC_DISTANT_PLATFORM_RUPEE4,
         lambda bundle: is_adult(bundle)),
        (Locations.DMC_DISTANT_PLATFORM_RUPEE5,
         lambda bundle: is_adult(bundle)),
        (Locations.DMC_DISTANT_PLATFORM_RUPEE6,
         lambda bundle: is_adult(bundle)),
        (Locations.DMC_DISTANT_PLATFORM_RED_RUPEE,
         lambda bundle: is_adult(bundle)),
    ])

    # DMC Temple Exit  (upstream RR_DMC_TEMPLE_EXIT, SCENE_DEATH_MOUNTAIN_CRATER)
    # Connections
    connect_regions(Regions.DMC_TEMPLE_EXIT, world, [
        (Regions.FIRE_TEMPLE_ENTRYWAY,
         lambda bundle: True_()),
    ])

    # DMC Great Fairy Fountain  (upstream RR_DMC_GREAT_FAIRY_FOUNTAIN, SCENE_GREAT_FAIRYS_FOUNTAIN_MAGIC)
    # Locations
    add_locations(Regions.DMC_GREAT_FAIRY_FOUNTAIN, world, [
        (Locations.DMC_GREAT_FAIRY_REWARD,
         lambda bundle: can_use(Items.ZELDAS_LULLABY, bundle)),
    ])
    # Connections
    connect_regions(Regions.DMC_GREAT_FAIRY_FOUNTAIN, world, [
        (Regions.DMC_BLOCKED_ENTRY,
         lambda bundle: True_()),
    ])

    # DMC Upper Grotto  (upstream RR_DMC_UPPER_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.DMC_UPPER_GROTTO, world, [
        (Locations.DMC_UPPER_GROTTO_CHEST,
         lambda bundle: has_open_chest(bundle)),
        (Locations.DMC_UPPER_GROTTO_FISH,
         lambda bundle: has_bottle(bundle)),
        (Locations.DMC_UPPER_GROTTO_GOSSIP_STONE_FAIRY,
         lambda bundle: call_gossip_fairy(bundle)),
        (Locations.DMC_UPPER_GROTTO_GOSSIP_STONE_BIG_FAIRY,
         lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        # DEFERRED RC_DMC_UPPER_GROTTO_GOSSIP_STONE: true
        (Locations.DMC_UPPER_GROTTO_BEEHIVE_LEFT,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.DMC_UPPER_GROTTO_BEEHIVE_RIGHT,
         lambda bundle: can_break_lower_hives(bundle)),
        (Locations.DMC_UPPER_GROTTO_GRASS1,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DMC_UPPER_GROTTO_GRASS2,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DMC_UPPER_GROTTO_GRASS3,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DMC_UPPER_GROTTO_GRASS4,
         lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DMC_UPPER_BOULDER_GROTTO_BUTTERFLY_FAIRY,
         lambda bundle: can_use(Items.STICKS, bundle)),
    ])
    # Connections
    connect_regions(Regions.DMC_UPPER_GROTTO, world, [
        (Regions.DMC_ROCKS_GROTTO_ENTRY,
         lambda bundle: True_()),
    ])

    # DMC Scrub Grotto  (upstream RR_DMC_SCRUB_GROTTO, SCENE_GROTTOS)
    # Locations
    add_locations(Regions.DMC_SCRUB_GROTTO, world, [
        (Locations.DMC_DEKU_SCRUB_GROTTO_LEFT,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.DMC_DEKU_SCRUB_GROTTO_LEFT, bundle)),
        (Locations.DMC_DEKU_SCRUB_GROTTO_RIGHT,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.DMC_DEKU_SCRUB_GROTTO_RIGHT, bundle)),
        (Locations.DMC_DEKU_SCRUB_GROTTO_CENTER,
         lambda bundle: can_stun_deku(bundle) & has_speak(bundle, "DEKU") & can_afford_slot(Locations.DMC_DEKU_SCRUB_GROTTO_CENTER, bundle)),
        (Locations.DMC_HAMMER_GROTTO_BEEHIVE,
         lambda bundle: can_break_upper_beehives(bundle)),
    ])
    # Connections
    connect_regions(Regions.DMC_SCRUB_GROTTO, world, [
        (Regions.DMC_POT_GROTTO_ENTRY,
         lambda bundle: True_()),
    ])

# ---- summary
# notes: ['TODO feature 4.1']
# helpers not in LogicHelpers yet: []
# TODO count: 0
# new regions: []
# events used: ['CAN_ACCESS_FAIRIES', 'DMC_BOULDER', 'PLANT_DEATH_MOUNTAIN_CRATER_BEAN']
# tricks missing in apworld: []
# enemies missing: []
# items missing: []
# deferred locations (2): ['RC_DMC_GOSSIP_STONE', 'RC_DMC_UPPER_GROTTO_GOSSIP_STONE']
