# Updated SoH Archipelago (unofficial, work in progress)

> **Unofficial fan update.** This repository is **not** made by, affiliated with, or endorsed by the
> Archipelago-SoH team, the Harbour Masters, or the Archipelago project. It is **not officially supported**.
> Please **do not** send support requests or bug reports about anything in here to the original projects.

This is an attempt to bring the [Archipelago](https://archipelago.gg) integration of
[Ship of Harkinian](https://github.com/HarbourMasters/Shipwright) up to the randomizer features of current
upstream Ship of Harkinian (**SoH 9.3.1**).

**Status: feature-complete for the planned scope, but barely play-tested.** Generation, the test suite and the
client build pass, and a first short play session worked. Things may still be broken, seeds may turn out
unbeatable in game, and save files or generated games may not carry over between versions of this repository.
Use at your own risk.

## Branches

| Branch | Contents | State |
|---|---|---|
| `client` | Ship of Harkinian with the Archipelago client (fork of `jeromkiller/Shipwright_archipellago`, branch `Harkipellago`), with upstream SoH tag **9.3.1** merged in | Builds on Windows (MSVC 2022). All options below are read from the Archipelago slot data. Expects apworld **1.5**. |
| `apworld` | Archipelago with the `oot_soh` world (fork of `HarbourMasters/Archipelago-SoH`, branch `oot-soh`), in `worlds/oot_soh` | apworld version **1.5.0**. Randomizer logic ported from SoH 9.3.1. |
| `main` | This README only | |

Client and apworld have to come from this repository **together**. The client checks the apworld's major.minor
version and refuses seeds of other versions (e.g. 1.4.x); neither side is compatible with the official releases.

## What is in it

- **Logic** re-ported from SoH 9.3.1 (all non-Master-Quest regions), including the 9.3.1 tricks, per-scene item
  restrictions and Ganon's Boss Key / Ganon's Soul / win condition triggers.
- **Updated existing options** to 9.3.1 behaviour (Kakariko Gate / Skip Child Zelda, Triforce Hunt, boss souls,
  Ganon's trials, weird egg, ...).
- **New options**, all off by default:
  - win condition, Link's Pocket reward, dungeon rewards "own dungeon";
  - gameplay switches (Bunny Hood, masks as adult, early Granny's shop, swordless Epona items, shop shield/tunic
    gate), Progressive Goron Sword, ice trap names, starting items, Skip Child Stealth, Skip Planting Beans,
    starting Skulltula tokens, fishsanity pond count / age split / Hyrule Loach;
  - new shuffles: beggar, butterfly fairies, signs, wonder items, icicles, red ice, rocks, boulders, bushes, bean
    souls, masks, Scarecrow's Song, Zelda's Letter, Treasure Chest Game (with key ring);
  - ability shuffles: climb, crawl, grab, speak (Jabber Nuts), open chest (off / on / progressive);
  - **entrance shuffle** for dungeons (optionally with Ganon's Castle) and for grottos/graves (coupled).
- Presets follow the SoH 9.3.1 rando presets (incl. "Demise Difficulty") as far as the apworld supports them.
- Universal Tracker support for the new options and the shuffled entrances.

## Not supported (yet)

Master Quest, silver rupee shuffle, the other entrance shuffles (overworld, interiors, boss rooms, owl drops,
warp songs, spawns, mixed and decoupled pools), and settings that only exist in upstream `develop`
(Nayru's Love uses, Fire Gorons, Fisherman's Hat).

## Not included

No ROMs, game data, extracted assets, `*.otr` or `*.o2r` files are part of this repository.
You need your **own legally obtained copy** of the game to use Ship of Harkinian.

## Credits and sources

All credit for the original work goes to the respective projects and their contributors. They are listed here
as sources, not as affiliations:

- [HarbourMasters/Shipwright](https://github.com/HarbourMasters/Shipwright) – Ship of Harkinian
- [jeromkiller/Shipwright_archipellago](https://github.com/jeromkiller/Shipwright_archipellago) – Archipelago client for Ship of Harkinian
- [HarbourMasters/Archipelago-SoH](https://github.com/HarbourMasters/Archipelago-SoH) – Ship of Harkinian world for Archipelago
- [ArchipelagoMW/Archipelago](https://github.com/ArchipelagoMW/Archipelago) – Archipelago

License files and credits of the original projects are kept unchanged in the `client` and `apworld` branches
and apply there.
