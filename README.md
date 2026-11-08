# Updated SoH Archipelago (unofficial, work in progress)

> **Unofficial fan update.** This repository is **not** made by, affiliated with, or endorsed by the
> Archipelago-SoH team, the Harbour Masters, or the Archipelago project. It is **not officially supported**.
> Please **do not** send support requests or bug reports about anything in here to the original projects.

This is an attempt to bring the [Archipelago](https://archipelago.gg) integration of
[Ship of Harkinian](https://github.com/HarbourMasters/Shipwright) up to the randomizer features of current
upstream Ship of Harkinian (**SoH 9.3.1**).

**Status: work in progress and incomplete.** Things may be broken, seeds may be unbeatable, and save files or
generated games may not carry over between versions of this repository. Use at your own risk.

## Branches

| Branch | Contents | State |
|---|---|---|
| `client` | Ship of Harkinian with the Archipelago client (fork of `jeromkiller/Shipwright_archipellago`, branch `Harkipellago`), with upstream SoH tag **9.3.1** merged in | Builds on Windows (MSVC 2022). Existing AP settings are mapped onto the 9.3.1 randomizer settings. Not yet play-tested. New 9.3.1 settings are not wired up to Archipelago yet. |
| `apworld` | Archipelago with the `oot_soh` world (fork of `HarbourMasters/Archipelago-SoH`, branch `oot-soh`), in `worlds/oot_soh` | Location names synced with SoH 9.3.1. Porting the 9.3.1 randomizer logic is in progress. New options are not added yet. |
| `main` | This README only | |

Client and apworld have to come from this repository **together**; they are not compatible with the official
releases of either project once versions diverge.

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
