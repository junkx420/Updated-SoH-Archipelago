from dataclasses import dataclass
from Options import Choice, Toggle, DefaultOnToggle, Range, PerGameCommonOptions, StartInventoryPool, Visibility, OptionGroup, OptionSet, Accessibility, OptionError
from .Enums import Tricks, Items, TokenCounts
from .TrickNames import TRICK_SOH_NAMES

wallet_capacities: dict[Items, int] = {
    Items.CHILD_WALLET: 99,
    Items.ADULT_WALLET: 200,
    Items.GIANT_WALLET: 500,
    Items.TYCOON_WALLET: 999
}

class ClosedForest(Choice):
    """
    On - Kokiri Sword & Deku Shield are required to access the Deku Tree, and completing the Deku Tree is required to access the Lost Woods Bridge Exit.
    Deku Only - Kokiri boy no longer blocks the path to the Bridge but Mido still requires the Kokiri Sword and Deku Shield to access the tree.
    Off - Mido no longer blocks the path to the Deku Tree. Kokiri boy no longer blocks the path out of the forest.
    """
    display_name = "Closed Forest"
    option_on = 0
    option_deku_only = 1
    option_off = 2
    default = 2


class KakarikoGate(Choice):
    """
    Closed - The gate will remain closed until Zelda's Letter is shown to the guard.
    Open - You start with Zelda's Letter, which opens the gate. Ship of Harkinian 9.3.1 no longer has a separate gate
    setting; starting with the letter also counts as having met Zelda, so the Song from Impa and Zelda's Letter checks
    are given at the start (as with Skip Child Zelda, but Talon still has to be woken with the Weird Egg).
    """
    display_name = "Kakariko Gate"
    option_closed = 0
    option_open = 1
    default = 1


class DoorOfTime(Choice):
    """
    Closed - The Ocarina of Time, the Song of Time and all three Spiritual Stones are required to open the Door of Time.
    Song only - Play the Song of Time in front of the Door of Time to open it.
    Open - The Door of Time is permanently open with no requirements.
    """
    display_name = "Door of Time"
    option_closed = 0
    option_song_only = 1
    option_open = 2
    default = 2


class ZorasFountain(Choice):
    """
    Closed - King Zora obstructs the way to Zora's Fountain. Ruto's Letter must be shown as child Link in order to move him in both time periods.
    Closed as child - Ruto's Letter is only required to move King Zora as child Link. Zora's Fountain starts open as adult.
    Open - King Zora has already mweeped out of the way in both time periods. Ruto's Letter is removed from the item pool.
    """
    display_name = "Zora's Domain"
    option_closed = 0
    option_closed_as_child = 1
    option_open = 2
    default = 1


class SleepingWaterfall(Choice):
    """
    Closed:
    Sleeping Waterfall obstructs the entrance to Zora's Domain. Zelda's Lullaby must be played in order to open it.

    Open: 
    Sleeping Waterfall is always open. Link may always enter Zora's Domain and Zelda's Lullaby is not required to enter Zora's Domain.
    """
    display_name = "Sleeping Waterfall"
    option_closed = 0
    option_open = 1
    default = 0


class JabuJabu(Choice):
    """
    Closed - A fish is required to open Jabu-Jabu's mouth.
    Open - Jabu-Jabu's mouth opens without the need for a fish.
    """
    display_name = "Jabu-Jabu"
    option_closed = 0
    option_open = 1
    default = 0


class LockOverworldDoors(Toggle):
    """
    Adds locks to all wooden overworld doors, requiring specific small keys to open them.
    """
    display_name = "Lock Overworld Doors"


class FortressCarpenters(Choice):
    """
    Sets the state of the carpenters captured by Gerudo in Gerudo Fortress, and with it the number of guards that spawn.
    Normal - All 4 carpenters are required to be saved.
    Fast - Only the bottom left carpenter requires rescuing.
    Free - The bridge is repaired from the start, and Nabooru cannot spawn.
    Only Normal is compatible with the Gerudo Fortress Key Ring.
    """
    display_name = "Fortress Carpenters"
    option_normal = 0
    option_fast = 1
    option_free = 2
    default = 1


class RainbowBridge(Choice):
    """
    Alters the requirements to open the bridge to Ganon's Castle.
    Vanilla - Obtain the Shadow Medallion, Spirit Medallion and Light Arrows.
    Always open - No requirements.
    Stones - Obtain the specified amount of Spiritual Stones.
    Medallions - Obtain the specified amount of medallions.
    Dungeon rewards - Obtain the specified total sum of Spiritual Stones or medallions.
    Dungeons - Complete the specified amount of dungeons. Dungeons are considered complete after stepping in to the blue warp after the boss.
    Tokens - Obtain the specified amount of Gold Skulltula Tokens.
    Greg - Find Greg the Green Rupee.
    Triforce Pieces - Obtain the specified amount of Triforce Pieces (needs Triforce Hunt).
    """
    display_name = "Rainbow Bridge"
    option_vanilla = 0
    option_always_open = 1
    option_stones = 2
    option_medallions = 3
    option_dungeon_rewards = 4
    option_dungeons = 5
    option_tokens = 6
    option_greg = 7
    option_triforce_pieces = 8  # appended so existing values keep their numbers
    default = 7


class RainbowBridgeGregModifier(Choice):
    """
    If Rainbow Bridge is enabled, Greg will count toward the bridge requirement goal.
    Off - Greg won't count toward the bridge requirement.
    Reward - Greg will count toward the bridge requirement and be considered in the logic.
    Wildcard - Greg will count toward the bridge requirement but will not be considered in the logic.
    """
    display_name = "Rainbow Bridge Greg Modifier"
    option_off = 0
    option_reward = 1
    option_wildcard = 2
    default = 0

class RainbowBridgeStonesRequired(Range):
    """
    If Rainbow Bridge is set to Stones, this is how many Spiritual Stones are required to open it.
    If the Greg Modifier is not set to Reward, the max will be 3.
    """
    display_name = "Rainbow Bridge Stones Required"
    range_start = 1
    range_end = 4
    default = 3


class RainbowBridgeMedallionsRequired(Range):
    """
    If Rainbow Bridge is set to Medallions, this is how many medallions are required to open it.
    If the Greg Modifier is not set to Reward, the max will be 6.
    """
    display_name = "Rainbow Bridge Medallions Required"
    range_start = 1
    range_end = 7
    default = 6


class RainbowBridgeDungeonRewardsRequired(Range):
    """
    If Rainbow Bridge is set to Dungeon Rewards, this is how many dungeon rewards are required to open it.
    If the Greg Modifier is not set to Reward, the max will be 9.
    """
    display_name = "Rainbow Bridge Dungeon Rewards Required"
    range_start = 1
    range_end = 10
    default = 9


class RainbowBridgeDungeonsRequired(Range):
    """
    If Rainbow Bridge is set to Dungeons, this is how many completed dungeons are required to open it.
    If the Greg Modifier is not set to Reward, the max will be 8.
    """
    display_name = "Rainbow Bridge Dungeons Required"
    range_start = 1
    range_end = 9
    default = 8


class RainbowBridgeSkullTokensRequired(Range):
    """
    If Rainbow Bridge is set to Tokens, this is how many Gold Skulltula Tokens are required to open it.
    """
    display_name = "Rainbow Bridge Skull Tokens Required"
    range_start = 1
    range_end = 100
    default = 50


class GanonsTrials(Choice):
    """
    Sets the number of Ganon's Trials required to dispel the barrier.
    Skip - No trials are required and the barrier is already dispelled.
    Set Number - Select a number of trials that will be required. The required trials will be chosen randomly.
    """
    display_name = "Ganon's Trials"
    option_skip = 0
    option_set_number = 1
    default = 0


class GanonsTrialsCount(Range):
    """
    Sets how many of Ganon's Trials are required to dispel the barrier.
    """
    display_name = "Ganon's Trials Count"
    range_start = 0
    range_end = 6
    default = 6


class TriforceHunt(Toggle):
    """
    Pieces of the Triforce of Courage have been scattered across the world.
    With Win Condition "Default" (or "Trigger Triforce Pieces") finding the required share finishes the game: the game
    will save and credits will roll, Ganon's Boss Key is not shuffled then. The pieces can also be used for the
    Rainbow Bridge, Ganon's Boss Key or Ganon's Soul with another Win Condition.
    """
    display_name = "Triforce Hunt"


class TriforceHuntPiecesTotal(Range):
    """
    Specify an exact number of Triforce Pieces to add to the item pool. If the item pool is out of space, no more Triforce Pieces will be added.
    """
    display_name = "Triforce Hunt Pieces Total"
    range_start = 1
    range_end = 100
    default = 30


class TriforceHuntPiecesRequiredPercentage(Range):
    """
    The percentage of Triforce Pieces that will be required to complete the game.
    """
    display_name = "Triforce Hunt Pieces Required Percentage"
    range_start = 1
    range_end = 100
    default = 60


class ShuffleSongs(Choice):
    """
    Shuffles songs into the item pool.
    Off - Songs will appear at their vanilla locations.
    Song Locations - Songs will only appear at locations that normally teach songs.
    Dungeon rewards - Songs appear after beating a major dungeon boss.
        The 4 remaining songs are located at:
        - Zelda's Lullaby location
        - Ice Cavern's Serenade of Water location
        - Bottom of the Well Lens of Truth location
        - Gerudo Training Ground Ice Arrows Location
    Anywhere - Songs can appear at any location.
    """
    display_name = "Shuffle Songs"
    option_off = 0
    option_song_locations = 1
    option_dungeon_rewards = 2
    option_anywhere = 3
    default = 1


class ShuffleTokens(Choice):
    """
    Shuffles Gold Skulltula Tokens into the item pool. This means Gold Skulltulas can contain other items as well.
    Off - GS tokens will not be shuffled.
    Dungeons - Only shuffle GS tokens that are within dungeons.
    Overworld - Only shuffle GS tokens that are outside of dungeons.
    All Tokens - Shuffle all 100 GS tokens.
    """
    display_name = "Shuffle Tokens"
    option_off = 0
    option_dungeon = 1
    option_overworld = 2
    option_all = 3
    default = 0


class SkullsSunSong(Toggle):
    """
    All Gold Skulltulas that require nighttime to appear will only be expected to be collected after getting Sun's Song.
    """
    display_name = "Night Skulltulas Expect Sun's Song"


class ShuffleKokiriSword(Toggle):
    """
    Shuffles the Kokiri Sword into the item pool.
    This will require the use of Deku Sticks until the Kokiri Sword is found.
    """
    display_name = "Shuffle Kokiri Sword"


class ShuffleMasterSword(Toggle):
    """
    Shuffles the Master Sword into the item pool.
    If you haven't found the Master Sword before facing Ganon, you won't receive it during the fight.
    """
    display_name = "Shuffle Master Sword"


class ShuffleChildsWallet(Toggle):
    """
    Enabling this shuffles the Child's Wallet into the item pool.
    You will not be able to carry any rupees until you find a wallet.
    """
    display_name = "Shuffle Child's Wallet"


class ShuffleOcarinas(Toggle):
    """
    Enabling this shuffles the Fairy Ocarina and the Ocarina of Time into the item pool.
    This will require finding an Ocarina before being able to play songs.
    """
    display_name = "Shuffle Ocarinas"


class ShuffleOcarinaButtons(Toggle):
    """
    Enabling this shuffles the Ocarina buttons into the item pool.
    This will require finding the buttons before being able to use them in songs.
    """
    display_name = "Shuffle Ocarina Buttons"


class ShuffleSwim(Toggle):
    """
    Shuffles the ability to Swim into the item pool.
    The ability to swim has to be found as an item (you can still go underwater if you use the Iron Boots).
    If you enter a water entrance without swim you will be respawned on land to prevent infinite death loops.
    If you void out in Water Temple you will immediately be kicked out to prevent a softlock.
    """
    display_name = "Shuffle Swim"


class ShuffleWeirdEgg(Choice):
    """
    Off - Malon gives you the Weird Egg at Hyrule Castle.
    On - Shuffles the Weird Egg from Malon into the item pool.
    Skip Waking Talon - Talon is already awake and back at Lon Lon Ranch, the egg isn't needed
    (Ship of Harkinian 9.3.1 setting). Skip Child Zelda always uses this.
    The Weird Egg is required to unlock several events:
      - Zelda's Lullaby from Impa
      - Saria's Song in Sacred Forest Meadow
      - Epona's Song and chicken minigame at Lon Lon Ranch
      - Zelda's Letter for Kakariko gate (if Kakariko Gate is set to Closed)
      - Happy Mask Shop side quest
    """
    display_name = "Shuffle Weird Egg"
    option_off = 0
    option_on = 1
    option_skip_waking_talon = 2
    alias_false = 0
    alias_true = 1
    default = 0


class ShuffleGerudoMembershipCard(Toggle):
    """
    Shuffles the Gerudo Membership Card into the item pool.
    The Gerudo Membership Card is required to enter the Gerudo Training Ground, opening the gate to Haunted Wasteland and the Horseback Archery minigame.
    """
    display_name = "Shuffle Gerudo Membership Card"


class ShuffleFishingPole(Toggle):
    """
    Shuffles the fishing pole into the item pool. The fishing pole is required to play the fishing pond minigame.
    """
    display_name = "Shuffle Fishing Pole"


class ShuffleDekuStickBag(Toggle):
    """
    Shuffles the Deku Stick bag into the item pool. The Deku Stick bag is required to hold Deku Sticks.
    """
    display_name = "Shuffle Deku Stick Bag"


class ShuffleDekuNutBag(Toggle):
    """
    Shuffles the Deku Nut bag into the item pool. The Deku Nut bag is required to hold Deku Nuts.
    """
    display_name = "Shuffle Deku Nut Bag"


class ShuffleFreestandingItems(Choice):
    """
    Freestanding rupees & hearts are shuffled to random items. Freestanding heart pieces and small keys are already shuffled by default.
    Off - Freestanding rupees & hearts will not be shuffled.
    Dungeons - Only freestanding rupees & hearts that are within dungeons will be shuffled.
    Overworld - Only freestanding rupees & hearts that are outside of dungeons will be shuffled.
    All - Shuffle all freestanding rupees & hearts.
    """
    display_name = "Shuffle Freestanding Items"
    option_off = 0
    option_dungeon = 1
    option_overworld = 2
    option_all = 3
    default = 0


class ShuffleShops(Toggle):
    """
    Shuffle shop items amongst the different shops.
    """
    display_name = "Shuffle Shops"


class ShuffleShopsItemAmount(Range):
    """
    If Shuffle Shops is on, set how many shop items in each shop will be replaced by an entirely random item with a random price.
    """
    display_name = "Shuffle Shops Item Amount"
    range_start = 0
    range_end = 7
    default = 4


class ShuffleShopsMinimumPrice(Range):
    """
    If Shuffle Shops is on, set the minimum price of randomized shop items. Final price will be rounded down to multiples of 5.
    Shuffled vanilla shop items will keep their vanilla price regardless of what's chosen here.
    """
    display_name = "Shuffle Shops Minimum Price"
    range_start = 0
    range_end = 999
    default = 10


class ShuffleShopsMaximumPrice(Range):
    """
    If Shuffle Shops is on, set the maximum price of randomized shop items. Final price will be rounded down to multiples of 5.
    If this is set below the minimum, this option will be set to whatever the minimum is set to.
    Shuffled vanilla shop items will keep their vanilla price regardless of what's chosen here.
    """
    display_name = "Shuffle Shops Maximum Price"
    range_start = 0
    range_end = 999
    default = 250


class ShuffleFish(Choice):
    """
    Shuffles various fish in the game. The Hylian Loach is not included.
    Off - Fish will not be shuffled. No changes will be made to fish behavior.
    Pond - Only the fishing pond's fish will be shuffled. Catching a fish in the fishing pond will grant a reward
    (how many: "Pond Fish Count", per age with "Pond Fish Age Split").
    Overworld - Only fish in generic grottos and Zora's domain will be shuffled. These fish will need a bottle in order to scoop them up.
    All - All fish will be shuffled.
    """
    display_name = "Shuffle Fish"
    option_off = 0
    option_pond = 1
    option_overworld = 2
    option_all = 3
    default = 0


class FishsanityPondCount(Range):
    """
    How many fish in the fishing pond give a reward when Shuffle Fish includes the pond (Ship of Harkinian 9.3.1:
    "Pond Fish Count"). The Hylian Loach values 16 and 17 are not supported yet.
    """
    display_name = "Pond Fish Count"
    range_start = 0
    range_end = 15
    default = 15


class FishsanityAgeSplit(DefaultOnToggle):
    """
    Child and adult each have their own set of pond fish rewards (Ship of Harkinian 9.3.1: "Pond Age Split").
    When off, there is only one set, which can be caught as either age.
    """
    display_name = "Pond Fish Age Split"


class ShuffleScrubs(Choice):
    """
    Shuffles Deku Scrub merchants in the game.
    Off - Scrubs will not be shuffled. The 3 Scrubs that give one-time items in the vanilla game (POH, Deku Nut capacity, and Deku Stick capacity) will not spawn.
    One-Time Only - Only the 3 Scrubs that give one-time items in the vanilla game are shuffled.
    All - All Scrubs are shuffled.
    """
    display_name = "Shuffle Scrubs"
    option_off = 0
    option_one_time_only = 1
    option_all = 2
    default = 0


class ShuffleScrubsMinimumPrice(Range):
    """
    If Shuffle Scrubs is on, set their minimum price. Final price will be rounded down to multiples of 5.
    """
    display_name = "Shuffle Scrubs Minimum Price"
    range_start = 0
    range_end = 999
    default = 10


class ShuffleScrubsMaximumPrice(Range):
    """
    If Shuffle Scrubs is on, set their maximum price. Final price will be rounded down to multiples of 5.
    If this is set below the minimum, this option will be set to whatever the minimum is set to.
    """
    display_name = "Shuffle Scrubs Maximum Price"
    range_start = 0
    range_end = 999
    default = 90


class ShuffleBeehives(Toggle):
    """
    Shuffle all beehives.
    """
    display_name = "Shuffle Beehives"


class ShuffleCows(Toggle):
    """
    Randomize what cows will give when playing Epona's Song for them for the first time.
    """
    display_name = "Shuffle Cows"


class ShufflePots(Choice):
    """
    Pots will drop a randomized item the first time they're broken and collected. This does not include the flying pots.
    With this option enabled, Ganon's boss key door is moved further up the stairs to allow access to the pots before obtaining Ganon's Boss Key.
    Off - Pots will not be shuffled.
    Dungeons - Only shuffle pots that are within dungeons.
    Overworld - Only shuffle pots that are outside of dungeons.
    All Pots - Shuffle all pots.
    """
    display_name = "Shuffle Pots"
    option_off = 0
    option_dungeon = 1
    option_overworld = 2
    option_all = 3
    default = 0


class ShuffleSigns(Choice):
    """
    Reading a sign (or a plaque, grave, pedestal or statue with text) for the first time gives a randomized item
    (Ship of Harkinian 9.3.1: "Shuffle Signs").
    Off - Signs are not shuffled.
    Dungeons - Only signs within dungeons (5).
    Overworld - Only signs outside of dungeons (74).
    All Signs - All signs (79).
    """
    display_name = "Shuffle Signs"
    option_off = 0
    option_dungeon = 1
    option_overworld = 2
    option_all = 3
    default = 0


class ShuffleWonderItems(Choice):
    """
    Invisible "wonder items" (rupees, hearts etc. that appear when Link touches or shoots a spot) give a randomized item
    the first time (Ship of Harkinian 9.3.1: "Shuffle Wonder Items").
    Off - Wonder items are not shuffled.
    Dungeons - Only wonder items within dungeons (4).
    Overworld - Only wonder items outside of dungeons (115).
    All Items - All wonder items (119).
    """
    display_name = "Shuffle Wonder Items"
    option_off = 0
    option_dungeon = 1
    option_overworld = 2
    option_all = 3
    default = 0


class ShuffleIcicles(Toggle):
    """
    Icicles and stalagmites give a randomized item the first time they are broken
    (Ship of Harkinian 9.3.1: "Shuffle Icicles"). 90 new locations in the Ice Cavern and Ganon's Castle.
    """
    display_name = "Shuffle Icicles"


class ShuffleRedIce(Toggle):
    """
    Red ice gives a randomized item the first time it is melted with Blue Fire
    (Ship of Harkinian 9.3.1: "Shuffle Red Ice"). 17 new locations in Zora's Domain, the Ice Cavern and Ganon's Castle.
    """
    display_name = "Shuffle Red Ice"


class ShuffleRocks(Toggle):
    """
    Small rocks give a randomized item the first time they are picked up or destroyed
    (Ship of Harkinian 9.3.1: "Shuffle Rocks"). 121 new locations, all outside of dungeons.
    """
    display_name = "Shuffle Rocks"


class ShuffleBoulders(Choice):
    """
    Boulders (brown, silver and bronze boulders, rock circles etc.) give a randomized item the first time they are
    destroyed (Ship of Harkinian 9.3.1: "Shuffle Boulders").
    Off - Boulders are not shuffled.
    Dungeons - Only boulders within dungeons (6).
    Overworld - Only boulders outside of dungeons (113).
    All Boulders - All boulders (119).
    """
    display_name = "Shuffle Boulders"
    option_off = 0
    option_dungeon = 1
    option_overworld = 2
    option_all = 3
    default = 0


class ShuffleCrates(Choice):
    """
    Large and small crates will drop a randomized item the first time they're broken and collected.
    Off - Crates will not be shuffled.
    Dungeons - Only shuffle crates that are within dungeons.
    Overworld - Only shuffle crates that are outside of dungeons.
    All Crates - Shuffle all crates.
    """
    display_name = "Shuffle Crates"
    option_off = 0
    option_dungeon = 1
    option_overworld = 2
    option_all = 3
    default = 0


class ShuffleTrees(Toggle):
    """
    Trees will contain randomized items which are dropped the first time the player rolls into one.
    Trees will have a special appearance when carrying randomized items.

    Some trees are dependent on Link's age, such as some trees in Hyrule Field.
    Two trees at Hyrule Castle are only shuffled with No Logic.
    """
    display_name = "Shuffle Trees"


class ShuffleMerchants(Choice):
    """
    This setting governs if the Bean Salesman, Medigoron, Granny and the Carpet Salesman sell a random item.
    Beans Merchant Only - Only the Bean Salesman will have a check, and a pack of Magic Beans will be added to the item pool.
    All But Beans - Medigoron, Granny and the Carpet Salesman will have checks.
    All - Apply both effects.
    """
    display_name = "Shuffle Merchants"
    option_off = 0
    option_bean_merchant_only = 1
    option_all_but_beans = 2
    option_all = 3
    default = 0


class ShuffleMerchantsMinimumPrice(Range):
    """
    If Shuffle Merchants is on, set their minimum price. Final price will be rounded down to multiples of 5.
    """
    display_name = "Shuffle Merchants Minimum Price"
    range_start = 0
    range_end = 999
    default = 10


class ShuffleMerchantsMaximumPrice(Range):
    """
    If Shuffle Merchants is on, set their maximum price. Final price will be rounded down to multiples of 5.
    If this is set below the minimum, this option will be set to whatever the minimum is set to.
    """
    display_name = "Shuffle Merchants Maximum Price"
    range_start = 0
    range_end = 999
    default = 90


class ShuffleFrogSongRupees(Toggle):
    """
    Shuffle the purple rupee rewards from the frogs in Zora's River. If this is turned off, only the Song of Storms and Frog Minigame rewards are shuffled.
    """
    display_name = "Shuffle Frog Song Rupees"


class ShuffleBeggar(Toggle):
    """
    The beggars in Hyrule Market (as child, by day) and Kakariko Village (as adult) give a randomized item for
    Bugs, a Fish and Blue Fire instead of rupees (Ship of Harkinian 9.3.1: "Shuffle Beggar"). 6 new locations.
    """
    display_name = "Shuffle Beggar"


class ShuffleAdultTradeItems(Toggle):
    """
    Adds all adult trade quest items to the pool. If this is turned off, only the Claim Check is in the pool.
    """
    display_name = "Shuffle Adult Trade Items"


class ShuffleBossSouls(Choice):
    """
    Shuffles 8 boss souls (one for each blue warp dungeon). A boss will not appear until you collect its respective soul.
    On + Ganon will also hide Ganon and Ganondorf behind a boss soul.
    """
    display_name = "Shuffle Boss Souls"
    option_off = 0
    option_on = 1
    option_on_plus_ganons = 2
    default = 0


class WinCondition(Choice):
    """
    What finishes the game (Ship of Harkinian 9.3.1 "Win Condition").
    Default - Defeat Ganon, or collect the required Triforce Pieces if Triforce Hunt is on (the behavior before this
    option existed).
    Defeat Ganon - Defeat Ganon.
    Anywhere - The Triforce itself is hidden as an item somewhere in the multiworld; finding it wins the game.
    Trigger - The game is won as soon as the requirement is met: Spiritual Stones, medallions, dungeon rewards,
    completed dungeons, Gold Skulltula Tokens or Triforce Pieces (Triforce Pieces needs Triforce Hunt and uses its
    required percentage).
    """
    display_name = "Win Condition"
    option_default = 0
    option_defeat_ganon = 1
    option_anywhere = 2
    option_trigger_stones = 3
    option_trigger_medallions = 4
    option_trigger_dungeon_rewards = 5
    option_trigger_dungeons = 6
    option_trigger_skull_tokens = 7
    option_trigger_triforce_pieces = 8
    default = 0


class WinConditionGregModifier(Choice):
    """
    If the Win Condition is a trigger, Greg will count toward the requirement.
    Off - Greg will not count. Reward - Greg will count and be considered in the logic.
    Wildcard - Greg will count but not be considered in the logic.
    """
    display_name = "Win Condition Greg Wildcard"
    option_off = 0
    option_reward = 1
    option_wildcard = 2
    default = 0


class WinConditionStonesRequired(Range):
    """If the Win Condition is Trigger Stones, this is how many Spiritual Stones are required.
    If the Greg Modifier is not set to Reward, the max will be 3."""
    display_name = "Win Condition Stones Required"
    range_start = 1
    range_end = 4
    default = 3


class WinConditionMedallionsRequired(Range):
    """If the Win Condition is Trigger Medallions, this is how many medallions are required.
    If the Greg Modifier is not set to Reward, the max will be 6."""
    display_name = "Win Condition Medallions Required"
    range_start = 1
    range_end = 7
    default = 6


class WinConditionDungeonRewardsRequired(Range):
    """If the Win Condition is Trigger Dungeon Rewards, this is how many Spiritual Stones and medallions are required.
    If the Greg Modifier is not set to Reward, the max will be 9."""
    display_name = "Win Condition Dungeon Rewards Required"
    range_start = 1
    range_end = 10
    default = 9


class WinConditionDungeonsRequired(Range):
    """If the Win Condition is Trigger Dungeons, this is how many dungeons must be completed.
    If the Greg Modifier is not set to Reward, the max will be 8."""
    display_name = "Win Condition Dungeons Required"
    range_start = 1
    range_end = 9
    default = 8


class WinConditionSkullTokensRequired(Range):
    """If the Win Condition is Trigger Skull Tokens, this is how many Gold Skulltula Tokens are required."""
    display_name = "Win Condition Skull Tokens Required"
    range_start = 1
    range_end = 100
    default = 100


class TriforceHuntPiecesLocation(Choice):
    """Where the Triforce Pieces can be placed (Ship of Harkinian 9.3.1 "Triforce Pieces Location")."""
    display_name = "Triforce Hunt Pieces Location"
    option_any_dungeon = 0
    option_overworld = 1
    option_anywhere = 2
    default = 2


class RainbowBridgeTriforcePiecesRequired(Range):
    """If Rainbow Bridge is set to Triforce Pieces, this is how many Triforce Pieces are required to open it (at most
    the number of pieces in the item pool). Needs Triforce Hunt."""
    display_name = "Rainbow Bridge Triforce Pieces Required"
    range_start = 1
    range_end = 100
    default = 100


class GanonsCastleBossKeyTriforcePiecesRequired(Range):
    """If Ganon's Castle Boss Key is set to Triforce Pieces, this is how many Triforce Pieces are required (at most the
    number of pieces in the item pool). Needs Triforce Hunt."""
    display_name = "Ganon's Castle Boss Key Triforce Pieces Required"
    range_start = 1
    range_end = 100
    default = 100


class ProgressiveGoronSword(Toggle):
    """
    Giant's Knife and Biggoron's Sword become two "Progressive Goron Sword" items: the first is the Giant's Knife, the
    second the Biggoron's Sword. Medigoron then only replaces broken knives (Ship of Harkinian 9.3.1).
    """
    display_name = "Progressive Goron Sword"


class BunnyHoodEffect(Toggle):
    """
    Wearing the Bunny Hood makes Link run 1.5x faster and jump 1.5x further, like in Majora's Mask.
    The logic respects this, so it might be required to use it to progress (Ship of Harkinian 9.3.1 "Bunny Hood Effect").
    """
    display_name = "Bunny Hood Effect"


class MasksAsAdult(Toggle):
    """
    Masks can be equipped as adult instead of being child only.
    The logic respects this, so it might be required to use this to progress (Ship of Harkinian 9.3.1).
    """
    display_name = "Masks as Adult"


class EarlyGrannysShop(Toggle):
    """
    Granny's Potion Shop is available from the start instead of requiring the Claim Check.
    Only applies when Shuffle Adult Trade Items is off (Ship of Harkinian 9.3.1).
    """
    display_name = "Early Granny's Potion Shop"


class SwordlessEponaItems(Toggle):
    """
    Restores the vanilla glitch that lets a swordless player use C-button items (bottles, bombs, magic, ...) while
    riding Epona. Off blocks it (Ship of Harkinian 9.3.1). Doesn't change the logic.
    """
    display_name = "Swordless Epona Items"


class ShopShieldsAndTunicsOnlyRefill(Toggle):
    """
    Non-randomized shields and tunics sold in shops can't be bought until you have first found that shield or tunic
    elsewhere (Ship of Harkinian 9.3.1 "Gate Shop Shields & Tunics"). The found shields and tunics then count in the
    logic.
    """
    display_name = "Gate Shop Shields & Tunics"


class GanonsSoul(Choice):
    """
    Ganon's Soul hides Ganon and Ganondorf until it is found (Ship of Harkinian 9.3.1 setting, independent of
    Shuffle Boss Souls).
    Start With - You start with Ganon's Soul.
    Any Dungeon / Overworld / Anywhere - Ganon's Soul is shuffled into a dungeon, the overworld or anywhere.
    Trigger - You receive Ganon's Soul wherever you are as soon as the requirement below is met.
    "Shuffle Boss Souls: On + Ganon" from older settings counts as Anywhere while this is left on Start With.
    Trigger Triforce Pieces needs Triforce Hunt.
    """
    display_name = "Ganon's Soul"
    option_start_with = 0
    option_any_dungeon = 1
    option_overworld = 2
    option_anywhere = 3
    option_trigger_stones = 4
    option_trigger_medallions = 5
    option_trigger_dungeon_rewards = 6
    option_trigger_dungeons = 7
    option_trigger_skull_tokens = 8
    option_trigger_triforce_pieces = 9
    default = 0


class GanonsSoulGregModifier(Choice):
    """
    If Ganon's Soul is a trigger, Greg will count toward the requirement.
    Off - Greg will not count.
    Reward - Greg will count and be considered in the logic.
    Wildcard - Greg will count but not be considered in the logic.
    """
    display_name = "Ganon's Soul Greg Wildcard"
    option_off = 0
    option_reward = 1
    option_wildcard = 2
    default = 0


class GanonsSoulStonesRequired(Range):
    """If Ganon's Soul is set to Trigger Stones, this is how many Spiritual Stones are required.
    If the Greg Modifier is not set to Reward, the max will be 3."""
    display_name = "Ganon's Soul Stones Required"
    range_start = 1
    range_end = 4
    default = 3


class GanonsSoulMedallionsRequired(Range):
    """If Ganon's Soul is set to Trigger Medallions, this is how many medallions are required.
    If the Greg Modifier is not set to Reward, the max will be 6."""
    display_name = "Ganon's Soul Medallions Required"
    range_start = 1
    range_end = 7
    default = 6


class GanonsSoulDungeonRewardsRequired(Range):
    """If Ganon's Soul is set to Trigger Dungeon Rewards, this is how many Spiritual Stones and medallions are
    required. If the Greg Modifier is not set to Reward, the max will be 9."""
    display_name = "Ganon's Soul Dungeon Rewards Required"
    range_start = 1
    range_end = 10
    default = 9


class GanonsSoulDungeonsRequired(Range):
    """If Ganon's Soul is set to Trigger Dungeons, this is how many dungeons must be completed (stepping into the blue
    warp after the boss). If the Greg Modifier is not set to Reward, the max will be 8."""
    display_name = "Ganon's Soul Dungeons Required"
    range_start = 1
    range_end = 9
    default = 8


class GanonsSoulSkullTokensRequired(Range):
    """If Ganon's Soul is set to Trigger Skull Tokens, this is how many Gold Skulltula Tokens are required."""
    display_name = "Ganon's Soul Skull Tokens Required"
    range_start = 1
    range_end = 100
    default = 100


class GanonsSoulTriforcePiecesRequired(Range):
    """If Ganon's Soul is set to Trigger Triforce Pieces, this is how many Triforce Pieces are required (at most the
    number of pieces in the item pool)."""
    display_name = "Ganon's Soul Triforce Pieces Required"
    range_start = 1
    range_end = 100
    default = 100


class ShuffleFountainFairies(Toggle):
    """
    Shuffle fairies in fountain locations.
    This includes the sets of fairies found in Ganon's Castle and Desert Colossus.
    """
    display_name = "Shuffle Fairies in Fountains"


class ShuffleStoneFairies(Toggle):
    """
    Shuffle fairies from Gossip Stone locations.
    """
    display_name = "Shuffle Gossip Stone Fairies"


class ShuffleBeanFairies(Toggle):
    """
    Shuffle fairies from Magic Bean locations.
    """
    display_name = "Shuffle Bean Fairies"


class ShuffleSongFairies(Toggle):
    """
    Shuffle fairy spots. These are spots where a big fairy is revealed by a song.

    This excludes Gossip Stones and Magic Bean locations.
    """
    display_name = "Shuffle Fairy Spots"


class ShuffleButterflyFairies(Toggle):
    """
    Shuffle the fairies that appear when you swing a Deku Stick at a butterfly (Ship of Harkinian 9.3.1:
    "Shuffle Butterfly Fairies"). 20 new locations, 9 of them in grottos.
    """
    display_name = "Shuffle Butterfly Fairies"


class ShuffleGrass(Choice):
    """
    Grass/Bushes will drop a randomized item the first time they're cut and collected.
    Off - Grass/Bushes will not be shuffled.
    Dungeons - Only shuffle grass/bushes that are within dungeons.
    Overworld - Only shuffle grass/bushes that are outside of dungeons.
    All Grass/Bushes - Shuffle all grass/bushes.
    """
    display_name = "Shuffle Grass"
    option_off = 0
    option_dungeon = 1
    option_overworld = 2
    option_all = 3
    default = 0


class ShuffleDungeonRewards(Choice):
    """
    Shuffles the location of Spiritual Stones and medallions.
    Off - Spiritual Stones and medallions will be given in their vanilla location from their respective boss.
    End of Dungeons - Spiritual Stones and medallions will be given as rewards for beating major dungeons. Link will always start with one stone or medallion.
    Any Dungeon - Spiritual Stones and medallions can only appear inside any dungeon.
    Overworld - Spiritual Stones and medallions can only appear outside of dungeons.
    Anywhere - Spiritual Stones and medallions can appear anywhere.
    Own Dungeon - Each Spiritual Stone and medallion is somewhere inside the dungeon it normally comes from. The Light
    Medallion is the Gift from Rauru, unless Link's Pocket gets a dungeon reward (then it can appear anywhere).
    """
    display_name = "Shuffle Dungeon Rewards"
    option_off = 0
    option_end_of_dungeons = 1
    option_any_dungeon = 2
    option_overworld = 3
    option_anywhere = 4
    option_own_dungeon = 5  # 9.3.1 RO_DUNGEON_REWARDS_OWN_DUNGEON, appended so existing values keep their numbers
    default = 0
    alias_dungeons = option_end_of_dungeons


class MapsAndCompasses(Choice):
    """
    Start with - You will start with Maps & Compasses from all dungeons.
    Vanilla - Maps & Compasses will appear in their vanilla locations.
    Own Dungeon - Maps & Compasses can only appear in their respective dungeon.
    Any Dungeon - Maps & Compasses can only appear inside any dungeon.
    Overworld - Maps & Compasses can only appear outside of dungeons.
    Anywhere - Maps & Compasses can appear anywhere in the world.
    """
    display_name = "Maps and Compasses"
    option_start_with = 0
    option_vanilla = 1
    option_own_dungeon = 2
    option_any_dungeon = 3
    option_overworld = 4
    option_anywhere = 5
    default = 0
    alias_shuffle = 5


class GanonsCastleBossKey(Choice):
    """
    Vanilla - Ganon's Boss Key will appear in the vanilla location.
    Anywhere - Ganon's Boss Key can appear anywhere.
    LACS - Since Ship of Harkinian 9.3.1 these are triggers: you receive the boss key wherever you are as soon as the
    requirement is met. The Light Arrow Cutscene (Zelda in the Temple of Time as adult, after the Shadow and Spirit
    Medallions) is a normal location again. Requirements:
    - Vanilla: Obtain any 2 medallions (SoH 9.3.1 migrates the old "LACS Vanilla" setting to this).
    - Stones: Obtain the specified amount of Spiritual Stones.
    - Medallions: Obtain the specified amount of medallions.
    - Dungeon rewards: Obtain the specified total sum of Spiritual Stones or medallions.
    - Dungeons: Complete the specified amount of dungeons. Dungeons are considered complete after stepping into the blue warp after the boss.
    - Tokens: Obtain the specified amount of Gold Skulltula Tokens.
    """
    display_name = "Ganon's Castle Boss Key"
    option_vanilla = 0
    option_anywhere = 1
    option_lacs_vanilla = 2
    option_lacs_stones = 3
    option_lacs_medallions = 4
    option_lacs_dungeon_rewards = 5
    option_lacs_dungeons = 6
    option_lacs_skull_tokens = 7
    option_lacs_triforce_pieces = 8  # 9.3.1 "Trigger-Triforce Pieces", needs Triforce Hunt
    default = 5


class GanonsCastleBossKeyGregModifier(Choice):
    """
    If Ganon's Castle Boss Key is enabled, Greg will count toward the LACS goal.
    Off - Greg will not count toward the LACS goal requirement.
    Reward - Greg will count toward the LACS goal and be considered in the logic.
    Wildcard - Greg will count toward the LACS goal but not be considered in the logic.
    """
    display_name = "Ganon's Castle Boss Key Greg Wildcard"
    option_off = 0
    option_reward = 1
    option_wildcard = 2
    default = 0


class GanonsCastleBossKeyStonesRequired(Range):
    """
    If Ganon's Castle Boss Key is set to Stones, this is how many Spiritual Stones are required to open it.
    Once the required amount is reached, the boss key is granted right away (SoH 9.3.1 trigger).
    If the Greg Modifier is not set to Reward, the max will be 3.
    """
    display_name = "Ganon's Castle Boss Key Stones Required"
    range_start = 1
    range_end = 4
    default = 3


class GanonsCastleBossKeyMedallionsRequired(Range):
    """
    If Ganon's Castle Boss Key is set to Medallions, this is how many medallions are required to open it.
    Once the required amount is reached, the boss key is granted right away (SoH 9.3.1 trigger).
    If the Greg Modifier is not set to Reward, the max will be 6.
    """
    display_name = "Ganon's Castle Boss Key Medallions Required"
    range_start = 1
    range_end = 7
    default = 6


class GanonsCastleBossKeyDungeonRewardsRequired(Range):
    """
    If Ganon's Castle Boss Key is set to Dungeon Rewards, this is how many dungeon rewards are required to open it.
    Once the required amount is reached, the boss key is granted right away (SoH 9.3.1 trigger).
    If the Greg Modifier is not set to Reward, the max will be 9.
    """
    display_name = "Ganon's Castle Boss Key Dungeon Rewards Required"
    range_start = 1
    range_end = 10
    default = 6


class GanonsCastleBossKeyDungeonsRequired(Range):
    """
    If Ganon's Castle Boss Key is set to Dungeons, this is how many dungeon completions are required to open it.
    Once the required amount is reached, the boss key is granted right away (SoH 9.3.1 trigger).
    If the Greg Modifier is not set to Reward, the max will be 8.
    """
    display_name = "Ganon's Castle Boss Key Dungeons Required"
    range_start = 1
    range_end = 9
    default = 8


class GanonsCastleBossKeySkullTokensRequired(Range):
    """
    If Ganon's Castle Boss Key is set to Tokens, this is how many Gold Skulltula Tokens are required to open it.
    Once the required amount is reached, the boss key is granted right away (SoH 9.3.1 trigger).
    """
    display_name = "Ganon's Castle Boss Key Skull Tokens Required"
    range_start = 1
    range_end = 100
    default = 50


class SmallKeyShuffle(Choice):
    """
    Vanilla - Small Keys will appear in their vanilla locations. You start with 3 keys in Spirit Temple MQ because the vanilla key layout is not beatable in logic.
    Own Dungeon - Small Keys can only appear in their respective dungeon. If Fire Temple is not a Master Quest dungeon, the door to the Boss Key chest will be unlocked.
    Any Dungeon - Small Keys can only appear inside any dungeon.
    Overworld - Small Keys can only appear outside of dungeons.
    Anywhere - Small Keys can appear anywhere in the world.
    """
    display_name = "Small Key Shuffle"
    option_start_with = 0
    option_vanilla = 1
    option_own_dungeon = 2
    option_any_dungeon = 3
    option_overworld = 4
    option_anywhere = 5
    default = 2


class GerudoFortressKeyShuffle(Choice):
    """
    Vanilla - Thieves' Hideout Keys will appear in their vanilla locations.
    Any Dungeon - Thieves' Hideout Keys can only appear inside any dungeon.
    Overworld - Thieves' Hideout Keys can only appear outside of dungeons.
    Anywhere - Thieves' Hideout Keys can appear anywhere in the world.
    """
    display_name = "Gerudo Fortress Key Shuffle"
    option_vanilla = 0
    option_any_dungeon = 1
    option_overworld = 2
    option_anywhere = 3
    default = 0


class BossKeyShuffle(Choice):
    """
    Vanilla - Boss Keys will appear in their vanilla locations.
    Own Dungeon - Boss Keys can only appear in their respective dungeon.
    Any Dungeon - Boss Keys can only appear inside any dungeon.
    Overworld - Boss Keys can only appear outside of dungeons.
    Anywhere - Boss Keys can appear anywhere in the world.
    """
    display_name = "Boss Key Shuffle"
    option_start_with = 0
    option_vanilla = 1
    option_own_dungeon = 2
    option_any_dungeon = 3
    option_overworld = 4
    option_anywhere = 5
    default = 2


class KeyRings(Choice):
    """
    Keyrings will replace all small keys from a particular dungeon with a single keyring that awards all keys for its associated dungeon.

    Off - No dungeons will have their keys replaced with keyrings.

    Count - A specified amount of randomly selected dungeons will have their keys replaced with keyrings.
    
    Selection - Hand select which dungeons will have their keys replaced with keyrings.
    
    Selecting key ring for dungeons will have no effect if Small Keys are set to Vanilla.
    
    If Gerudo Fortress Carpenters is set to Normal, and Gerudo Fortress Keys is set to anything other than Vanilla, then the maximum amount of Key Rings that can be selected by Count will be 9. Otherwise, the maximum amount of Key Rings will be 8.
    """
    display_name = "Key Rings"
    option_off = 0
    option_count = 1
    option_selection = 2
    default = 0


class KeyRingsCount(Range):
    """
    If "Count" is selected for the Key Rings option, this is the count that will be used. If 9 is selected and Gerudo Fortress Keys don't meet the specified requirements, this option will be set to 8.
    """
    display_name = "Key Rings Count"
    range_start = 0
    range_end = 9
    default = 0


class GerudoFortressKeyring(Toggle):
    """
    Only used if Key Rings option is set to "Selection". Will only work if Gerudo Fortress Keys meet the specified requirements.
    """
    display_name = "Gerudo Fortress Keyring"


class ForestTempleKeyring(Toggle):
    """
    Only used if Key Rings option is set to "Selection"
    """
    display_name = "Forest Temple Keyring"


class FireTempleKeyring(Toggle):
    """
    Only used if Key Rings option is set to "Selection"
    """
    display_name = "Fire Temple Keyring"


class WaterTempleKeyring(Toggle):
    """
    Only used if Key Rings option is set to "Selection"
    """
    display_name = "Water Temple Keyring"


class SpiritTempleKeyring(Toggle):
    """
    Only used if Key Rings option is set to "Selection"
    """
    display_name = "Spirit Temple Keyring"


class ShadowTempleKeyring(Toggle):
    """
    Only used if Key Rings option is set to "Selection"
    """
    display_name = "Shadow Temple Keyring"


class BottomOfTheWellKeyring(Toggle):
    """
    Only used if Key Rings option is set to "Selection"
    """
    display_name = "Bottom of the Well Keyring"


class GerudoTrainingGroundKeyring(Toggle):
    """
    Only used if Key Rings option is set to "Selection"
    """
    display_name = "Gerudo Training Ground Keyring"


class GanonsCastleKeyring(Toggle):
    """
    Only used if Key Rings option is set to "Selection"
    """
    display_name = "Ganon's Castle Keyring"


class BigPoeTargetCount(Range):
    """
    The Poe collector will give a reward for turning in this many Big Poes.
    """
    display_name = "Big Poe Target Count"
    range_start = 0
    range_end = 10
    default = 1


class SkipChildZelda(DefaultOnToggle):
    """
    Start with Zelda's Letter and the item Impa would normally give you and skip the sequence up until after meeting Zelda. Disables the ability to shuffle Weird Egg.
    Talon is already awake and back at Lon Lon Ranch (Ship of Harkinian 9.3.1: "Skip Waking Talon").
    """
    display_name = "Skip Child Zelda"


class SkipEponaRace(DefaultOnToggle):
    """
    Epona can be summoned with Epona's Song without needing to race Ingo.
    """
    display_name = "Skip Epona Race"


class SkipChildStealth(Toggle):
    """
    The crawlspace into Hyrule Castle goes straight to Zelda's Courtyard, skipping the guard stealth section
    (Ship of Harkinian 9.3.1: "Skip Child Stealth"). Has no effect on logic.
    """
    display_name = "Skip Child Stealth"


class SkipPlantingBeans(Toggle):
    """
    Getting the Magic Bean Pack (or buying the beans from the salesman) plants a Magic Bean in every soft soil patch
    at once, so beans don't have to be planted as child (Ship of Harkinian 9.3.1: "Skip Planting Beans").
    Logic then lets adult Link "plant" beans too.
    """
    display_name = "Skip Planting Beans"


class CompleteMaskQuest(DefaultOnToggle):
    """
    Once the Happy Mask Shop is opened, all masks will be available to be borrowed.
    """
    display_name = "Complete Mask Quest"


class SkipScarecrowsSong(DefaultOnToggle):
    """
    Start with the ability to summon Pierre the Scarecrow. Pulling out an Ocarina in Pierre's locations will automatically summon him.
    With Shuffle Ocarina Buttons enabled, you'll need at least two Ocarina buttons to summon him.
    """
    display_name = "Skip Scarecrow's Song"


class FullWallets(DefaultOnToggle):
    """
    Start with a full wallet. All wallet upgrades come filled with rupees.
    """
    display_name = "Full Wallets"


class BombchuBag(Choice):
    """
    None - Bombchus have vanilla behavior, and any Bombchu requirement is filled by Bomb Bag + a renewable source of Bombchus.

    Single Bag - Bombchus require their own bag to be found before use. 5 of them are added to the pool (6 if the Carpet Merchant is shuffled). The first Bombchu Bag you find will be a Bag containing 20 chus, and subsequent bags will be replaced with Bombchu Ammo refills. Once found, they can be replenished at shops selling refills, Bombchu Bowling and the carpet merchant. Bombchu Bowling is opened by obtaining the Bombchu Bag.

    Progressive Bags - 3 Bombchu Bags are added to the pool, and the first one will unlock Bombchus with a capacity of 20. The second one will upgrade this capacity to 30, and the final one will upgrade this capacity to the usual 50.

    Bombchu Bowling is opened by obtaining the first Bombchu bag.
    """
    display_name = "Bombchu Bag"
    option_none = 0
    option_single_bag = 1
    option_progressive_bags = 2
    default = 0


class BombchuDrops(DefaultOnToggle):
    """
    Once you obtain a Bombchu Bag, refills will sometimes replace Bomb drops that would spawn.
    If you have Bombchu Bag disabled, you will need a Bomb Bag and existing Bombchus for Bombchus to drop.
    """
    display_name = "Bombchu Drops"


class BlueFireArrows(DefaultOnToggle):
    """
    Ice Arrows act like Blue Fire, making them able to melt red ice. 
    """
    display_name = "Blue Fire Arrows"


class SunlightArrows(DefaultOnToggle):
    """
    Light Arrows can be used to light up the sun switches instead of using the Mirror Shield.
    """
    display_name = "Sunlight Arrows"


class RocsFeather(Toggle):
    """
    Adds Roc's Feather to the item pool. Roc's Feather is a custom item granting the player a jump on demand. 
    The jump can also be used when already in midair. Roc's Feather is not considered by logic.
    """
    display_name = "Roc's Feather"


class InfiniteUpgrades(Choice):
    """
    Adds upgrades that hold infinite quantities of items (bombs, arrows, etc.).
    Progressive - The infinite upgrades are obtained after getting the last normal capacity upgrade.
    Condensed Progressive - The infinite upgrades are obtained as the first capacity upgrade (doesn't apply to the infinite wallet or to infinite magic).
    """
    display_name = "Infinite Upgrades"
    option_off = 0
    option_progressive = 1
    option_condensed_progressive = 2
    default = 0


class SkeletonKey(Toggle):
    """
    Adds a new item called the Skeleton Key, it unlocks every door locked by a small key.
    """
    display_name = "Skeleton Key"


class SlingbowBreakBeehives(DefaultOnToggle):
    """
    Allows Slingshot and Bow to break beehives when Beehive Shuffle is turned on.
    """
    display_name = "Slingshot and Bow Can Break Beehives"


class StartingAge(Choice):
    """
    Decide whether to start as child Link or adult Link.
    Child Link starts in Link's House in Kokiri Forest.
    Adult Link starts in the Temple of Time.
    CAUTION: When "Closed Forest" is set to "On" or "Door of Time" is set to closed with either "Shuffle Dungeon Rewards" set to "Off" or "Shuffle Ocarinas" set to "Off,"
    this option will be forced to child.
    """
    display_name = "Starting Age"
    option_child = 0
    option_adult = 1
    default = 0


class Shuffle100GSReward(Toggle):
    """
    Shuffle the item the cursed rich man in the House of Skulltula gives you when you have collected all 100 Gold Skulltula Tokens.
    You can still talk to him multiple times to get Huge Rupees.
    """
    display_name = "Shuffle 100 GS Reward"


# TODO Ice Trap settings in ship were changed recently. Needs its own PR to figure out
class IceTrapCount(Range):
    """
    Specify an exact number of Ice Traps to add to the item pool. If the item pool is out of space, no more will be added.
    """
    display_name = "Ice Trap Count"
    range_start = 0
    range_end = 100
    default = 6


class IceTrapFillerReplacement(Range):
    """
    Specify a percentage of filler items to replace with Ice Traps.
    """
    display_name = "Ice Trap Filler Replacement Count"
    range_start = 0
    range_end = 100
    default = 0


class IceTrapNames(Choice):
    """
    How Ice Traps disguised as other items are named in the game (Ship of Harkinian 9.3.1).
    Identical - The exact name of the item they look like.
    Similar - A similar sounding name.
    Misspelled Vowel / Misspelled Duplicate - The item's name with a changed vowel or a doubled letter.
    Revealed - Always "Ice Trap".
    """
    display_name = "Ice Trap Names"
    option_identical = 0
    option_similar = 1
    option_misspelled_vowel = 2
    option_misspelled_duplicate = 3
    option_revealed = 4
    default = 1

class HintClarity(Choice):
    """
    Sets the clarity of hints.

    Obscure - Hints tell you the tier of an item but not what it is.
    Hookshot > Important Item

    Ambiguous (Experimental) - Hints tell you what the item could be based on its item group.
    Light Arrows > Magic Arrows
    (Quality of groups depends on game)

    Clear - Hints tell you exactly what the item is and opens the hint in the hint tab for free.
    Hints will not be automatically opened for Gossip Stones as not all Gossip Stone hints point
    to a location directly.
    Boomerang > Boomerang
    """
    display_name = "Hint Clarity"
    option_obscure = 0
    option_ambiguous = 1
    option_clear = 2
    default = 2

class GossipStoneHints(Choice):
    """
    Choose whether Gossip Stones should give hints and what is required to read them. Currently,
    Gossip Stones can only give out location hints and junk hints. Way of the Hero and Barren hints
    are not yet implemented.

    None - Gossip Stones do not give out hints.

    Need Nothing - Gossip Stones give out hints and you don't need anything to read them.

    Need Truth - Gossip Stones give out hints but you need Mask of Truth to read them.

    Need Stone - Gossip Stones give out hints but you need Stone of Agony to read them.
    """
    display_name = "Gossip Stone Hints"
    option_none = 0
    option_need_nothing = 1
    option_need_truth = 2
    option_need_stone = 3
    default = 1

class ToTAltarHint(Toggle):
    """
    Reading the Temple of Time altar as child will tell you the locations of the Spiritual Stones.
    Reading the Temple of Time altar as adult will tell you the locations of the medallions,
    as well as the conditions for building the Rainbow Bridge and getting the Boss Key for Ganon's Castle.
    """
    display_name = "ToT Altar Hint"
    default = 1

class GanondorfHint(Toggle):
    """
    Talking to Ganondorf in his boss room will tell you the location of the Light Arrows and Master Sword.
    If this option is enabled and Ganondorf is reachable without these items,
    Gossip Stones will never hint them.
    """
    display_name = "Ganondorf Hint"
    default = 1

class SheikLightArrowHint(Toggle):
    """
    Talking to Sheik inside Ganon's Castle will tell you the location of the Light Arrows.
    If this option is enabled and Sheik is reachable without Light Arrows,
    Gossip Stones will never hint the Light Arrows.
    """
    display_name = "Sheik Light Arrow Hint"

class BossKeyHint(Toggle):
    """
    Navi will tell you where the boss key can be found when prompted at a dungeon's boss door.
    """
    display_name = "Boss Key Hints"

class DampeDiaryHint(Toggle):
    """
    Reading the diary of Dampé the Gravekeeper as adult will tell you the location of a Progressive Hookshot.
    """
    display_name = "Dampe's Diary Hint"
    default = 1

class GregHint(Toggle):
    """
    Talking to the chest game owner after buying a key will tell you the location of Greg the Green Rupee.
    """
    display_name = "Greg the Green Rupee Hint"
    default = 1

#class HyruleLoachHint(Toggle):
#    """
#    Talking to the fishing pond owner and asking to talk about something will tell you what the reward for the Hyrule Loach is.
#
#    Loach hint is only avaliable with "Fishsanity" set to "Shuffle only Hyrule Loach"
#    as that's the only setting where you present the loach to the fishing pond owner.
#    """
#    display_name = "Hyrule Loach Hint"

class SariasHint(Toggle):
    """
    Talking to Saria either in person or by playing Saria's Song will tell you the location of a Progressive Magic Meter.
    """
    display_name = "Saria's Hint"
    default = 1

class MidosHint(Toggle):
    """
    Talking to Mido as child will tell you the location of the Kokiri Sword.
    """
    display_name = "Mido's Hint"

class FrogOcarinaGameHint(Toggle):
    """
    Standing near the pedestal for the frogs in Zora's River will tell you the reward for the frogs' Ocarina game.
    """
    display_name = "Frog Ocarina Game Hint"
    default = 1

class OcarinaOfTimeHint(Toggle):
    """
    Sheik in the Temple of Time will tell you the item and song on the Ocarina of Time.
    """
    display_name = "Ocarina of Time Hint"

class BiggoronHint(Toggle):
    """
    Talking to Biggoron will tell you the item he will give you in exchange for the Claim Check.
    """
    display_name = "Biggoron's Hint"
    default = 1

class BigPoeHint(Toggle):
    """
    Talking to the Poe Collector in the Market Guardhouse while adult will tell you what you receive for handing in Big Poes.
    """
    display_name = "Big Poes Hint"

class ChickenHint(Toggle):
    """
    Talking to Anju as child will tell you the item she will give you for delivering her cuccos to the pen.
    """
    display_name = "Chickens Hint"

class MalonHint(Toggle):
    """
    Talking to Malon as adult will tell you the item on "Link's Cow",
    the cow you win from beating her time on the Lon Lon Obstacle Course.
    """
    display_name = "Malon Hint"
    default = 1

class HorsebackArcheryHint(Toggle):
    """
    Talking to the Horseback Archery Gerudo in Gerudo Fortress, or the nearby sign,
    will tell you what you win for scoring 1000 and 1500 points on Horseback Archery.
    """
    display_name = "Horseback Archery Hint"
    default = 1

class FishingPoleHint(Toggle):
    """
    Talking to the fishing pond owner without the fishing pole will tell you its location.
    """
    display_name = "Fishing Pole Hint"

#class WarpSongHint(Toggle):
#    """
#    Playing a warp song will tell you where it leads.
#    (If warp song destinations are vanilla, this is always enabled)
#    """
#    display_name = "Warp Song Hints"

class ScrubHintText(Toggle):
    """
    Business scrubs will reveal the identity of what they're selling.
    """
    display_name = "Scrub Hint Text"
    default = 1

class MerchantHintText(Toggle):
    """
    Merchants will reveal the identity of what they're selling.
    (Shops are not affected by this setting)
    """
    display_name = "Merchant Hint Text"
    default = 1

class GS10Hint(Toggle):
    """
    Talking to the Cursed Resident in the Skulltula House who is saved after 10 tokens will tell you the reward.
    """
    display_name = "10 GS Hint"
    default = 1

class GS20Hint(Toggle):
    """
    Talking to the Cursed Resident in the Skulltula House who is saved after 20 tokens will tell you the reward.
    """
    display_name = "20 GS Hint"
    default = 1

class GS30Hint(Toggle):
    """
    Talking to the Cursed Resident in the Skulltula House who is saved after 30 tokens will tell you the reward.
    """
    display_name = "30 GS Hint"
    default = 1

class GS40Hint(Toggle):
    """
    Talking to the Cursed Resident in the Skulltula House who is saved after 40 tokens will tell you the reward.
    """
    display_name = "40 GS Hint"
    default = 1

class GS50Hint(Toggle):
    """
    Talking to the Cursed Resident in the Skulltula House who is saved after 50 tokens will tell you the reward.
    """
    display_name = "50 GS Hint"
    default = 1

class GS100Hint(Toggle):
    """
    Talking to the Cursed Resident in the Skulltula House who is saved after 100 tokens will tell you the reward.
    """
    display_name = "100 GS Hint"

class MaskShopHint(Toggle):
    """
    Reading the mask shop sign will tell you rewards from showing masks at the Deku Theatre.
    """
    display_name = "Mask Shop Hint"

class TrueNoLogic(Toggle):
    """
    Turn off logic completely.
    Generation will fail if this is enabled and allow_true_no_logic is not set to true in the host.yaml.
    """
    display_name = "True No Logic"
    visibility = Visibility.spoiler


class EnableAllTricks(Toggle):
    """
    Bypass the individual trick or glitch selections below and enable all of them.
    """
    display_name = "Enable All Tricks and Glitches"


# Tricks the apworld used to offer that SoH 9.3.1 no longer has (feature 1.3, docs/ap-update/feature-plan.md).
# A Tricks member as value: upstream renamed the trick 1:1, so the old YAML name turns the new trick on.
# A string: upstream merged it into a broader trick; turning that on would allow more than the YAML asked for, so the
# old name has no effect (a warning names the replacement). None: removed upstream without replacement.
LEGACY_TRICKS: dict[Tricks, Tricks | str | None] = {
    Tricks.FOREST_OUTDOORS_EAST_GS: Tricks.FOREST_COURTYARD_EAST_GS,
    Tricks.FOREST_OUTDOORS_LEDGE: Tricks.FOREST_COURTYARD_LEDGE,
    Tricks.FOREST_OUTDOORS_HEARTS_BOOMERANG: Tricks.FOREST_COURTYARD_HEARTS_BOOMERANG,
    Tricks.SPIRIT_LOBBY_GS: Tricks.SPIRIT_WEST_LEDGE,
    Tricks.SPIRIT_LOBBY_JUMP: Tricks.SPIRIT_STATUE_JUMP,
    Tricks.FIRE_FLAME_MAZE: Tricks.FIRE_SKIP_FLAME_WALLS,
    Tricks.KAK_MAN_ON_ROOF: Tricks.UNINTUITIVE_JUMPS.value,
    Tricks.KAK_ADULT_WINDMILL_POH: Tricks.UNINTUITIVE_JUMPS.value,
    Tricks.GF_JUMP: Tricks.UNINTUITIVE_JUMPS.value,
    Tricks.DC_JUMP: Tricks.UNINTUITIVE_JUMPS.value,
    Tricks.JABU_ALCOVE_JUMP_DIVE: Tricks.UNINTUITIVE_JUMPS.value,
    Tricks.FIRE_BOSS_DOOR_JUMP: Tricks.UNINTUITIVE_JUMPS.value,
    Tricks.WATER_BK_JUMP_DIVE: Tricks.UNINTUITIVE_JUMPS.value,
    Tricks.DMT_HOOKSHOT_LOWER_GS: Tricks.ITEM_EXTENSION.value,
    Tricks.HOOKSHOT_EXTENSION: Tricks.ITEM_EXTENSION.value,
    Tricks.DAMAGE_BOOST: Tricks.DAMAGE_BOOST_SIMPLE.value,
    Tricks.RUSTED_SWITCHES: None,
    Tricks.FLAMING_CHESTS: None,
}


def _trick_doc_line(trick: Tricks) -> str:
    if trick in LEGACY_TRICKS:
        target = LEGACY_TRICKS[trick]
        if isinstance(target, Tricks):
            return f"{trick.value} (old name, now {target.value})"
        return f"{trick.value} (no effect since SoH 9.3.1" + (f", see {target})" if target else ")")
    soh_name = TRICK_SOH_NAMES.get(trick.name)
    return f"{trick.value} ({soh_name})" if soh_name and soh_name != trick.value else trick.value


class TricksInLogic(OptionSet):
    display_name = "Tricks in Logic"
    valid_keys = [str(trick) for trick in Tricks]
    __doc__ = ("Define what tricks or glitches are considered in logic. "
               "For more information on what each trick does, check the Ship of Harkinian "
               "Randomizer -> Tricks/Glitches settings (the name in brackets is the one used there).\n"
               "Trick names: "
               f"{', '.join(_trick_doc_line(trick) for trick in Tricks)}")


class ShuffleTycoonWallet(Toggle):
    """
    Enabling this adds an extra Progressive Wallet to the pool and adds a new 999 capacity tier after Giants Wallet.
    """
    display_name = "Shuffle Tycoon Wallet"


class StartWithMasterSword(Toggle):
    """
    Start with the Master Sword in your inventory.
    """
    display_name = "Start with Master Sword"

class StartWithLinksPocket(Choice):
    """
    Sets the starting item in Link's pocket.
    Dungeon Reward - Starts you with a random dungeon reward.
    Advancement - Starts you with a random major item.
    Anything - Starts you with a random item.
    Nothing - Starts you with nothing in Link's pocket.
    CAUTION: When "Shuffle Dungeon Rewards" is set to "Off" or "End of Dungeons," this option will be forced to "Dungeon Reward."
    """
    display_name = "Link's Pocket"
    option_dungeon_reward = 0
    option_advancement = 1
    option_anything = 2
    option_nothing = 3
    default = 0

class LinksPocketReward(Choice):
    """
    If Link's Pocket is set to Dungeon Reward, which kind of reward it can be (Ship of Harkinian 9.3.1).
    Any Reward / Any Stone / Any Medallion / Light Medallion.
    Doesn't apply when Shuffle Dungeon Rewards is Off (Link's Pocket then has the Light Medallion as in the vanilla game).
    """
    display_name = "Link's Pocket Reward"
    option_any_reward = 0
    option_any_stone = 1
    option_any_medallion = 2
    option_light_medallion = 3
    default = 0


class StartWithKokiriSword(Toggle):
    """
    Start with the Kokiri Sword in your inventory.
    """
    display_name = "Start with Kokiri Sword"


class StartWithDekuShield(Toggle):
    """
    Start with a Deku Shield in your inventory.
    """
    display_name = "Start with Deku Shield"

class StartWithOcarina(Choice):
    """
    Start with an Ocarina in your inventory.
    """
    display_name = "Start with Ocarina"
    option_off = 0
    option_fairy_ocarina = 1
    option_ocarina_of_time = 2
    default = 0

class StartWithStickAmmo(Toggle):
    """
    Start with some Deku Sticks in your inventory.
    This option does nothing when "Shuffle Deku Stick Bag" is enabled.
    """
    display_name = "Start with Stick ammo"

class StartWithNutAmmo(Toggle):
    """
    Start with some Deku Nuts in your inventory.
    This option does nothing when "Shuffle Deku Nut Bag" is enabled.
    """
    display_name = "Start with Nut ammo"

class StartWithMagicBeans(Toggle):
    """
    Start with a pouch of Magic Beans in your inventory.
    """
    display_name = "Start with Magic Beans"

class StartWithZeldasLullaby(Toggle):
    """
    Start with Zelda's Lullaby in your inventory.
    """
    display_name = "Start with Zelda's Lullaby"
class StartWithEponasSong(Toggle):
    """
    Start with Epona's Song in your inventory.
    """
    display_name = "Start with Epona's Song"
class StartWithSariasSong(Toggle):
    """
    Start with Saria's Song in your inventory.
    """
    display_name = "Start with Saria's Song"
class StartWithSunsSong(Toggle):
    """
    Start with Sun's Song in your inventory.
    """
    display_name = "Start with Sun's Song"
class StartWithSongOfTime(Toggle):
    """
    Start with Song of Time in your inventory.
    """
    display_name = "Start with Song of Time"
class StartWithSongOfStorms(Toggle):
    """
    Start with Song of Storms in your inventory.
    """
    display_name = "Start with Song of Storms"
class StartWithMinuet(Toggle):
    """
    Start with Minuet of Forest in your inventory.
    """
    display_name = "Start with Minuet of Forest"
class StartWithBolero(Toggle):
    """
    Start with Bolero of Fire in your inventory.
    """
    display_name = "Start with Bolero of Fire"
class StartWithSerenade(Toggle):
    """
    Start with Serenade of Water in your inventory.
    """
    display_name = "Start with Serenade of Water"
class StartWithRequiem(Toggle):
    """
    Start with Requiem of Spirit in your inventory.
    """
    display_name = "Start with Requiem of Spirit"
class StartWithNocturne(Toggle):
    """
    Start with Nocturne of Shadow in your inventory.
    """
    display_name = "Start with Nocturne of Shadow"
class StartWithPrelude(Toggle):
    """
    Start with Prelude of Light in your inventory.
    """
    display_name = "Start with Prelude of Light"

# --- starting items added for SoH 9.3.1 (RSK_STARTING_*, feature 2.7) ---------------------------------------
class StartWithMegatonHammer(Toggle):
    """
    Start with the Megaton Hammer. It is taken out of the item pool.
    """
    display_name = "Start with Megaton Hammer"


class StartWithBoomerang(Toggle):
    """
    Start with the Boomerang. It is taken out of the item pool.
    """
    display_name = "Start with Boomerang"


class StartWithLensOfTruth(Toggle):
    """
    Start with the Lens of Truth. It is taken out of the item pool.
    """
    display_name = "Start with Lens of Truth"


class StartWithDinsFire(Toggle):
    """
    Start with the Din's Fire. It is taken out of the item pool.
    """
    display_name = "Start with Din's Fire"


class StartWithFaroresWind(Toggle):
    """
    Start with the Farore's Wind. It is taken out of the item pool.
    """
    display_name = "Start with Farore's Wind"


class StartWithNayrusLove(Toggle):
    """
    Start with the Nayru's Love. It is taken out of the item pool.
    """
    display_name = "Start with Nayru's Love"


class StartWithFireArrows(Toggle):
    """
    Start with the Fire Arrows. It is taken out of the item pool.
    """
    display_name = "Start with Fire Arrows"


class StartWithIceArrows(Toggle):
    """
    Start with the Ice Arrows. It is taken out of the item pool.
    """
    display_name = "Start with Ice Arrows"


class StartWithLightArrows(Toggle):
    """
    Start with the Light Arrows. It is taken out of the item pool.
    """
    display_name = "Start with Light Arrows"


class StartWithIronBoots(Toggle):
    """
    Start with the Iron Boots. It is taken out of the item pool.
    """
    display_name = "Start with Iron Boots"


class StartWithHoverBoots(Toggle):
    """
    Start with the Hover Boots. It is taken out of the item pool.
    """
    display_name = "Start with Hover Boots"


class StartWithHylianShield(Toggle):
    """
    Start with the Hylian Shield. It is taken out of the item pool.
    """
    display_name = "Start with Hylian Shield"


class StartWithMirrorShield(Toggle):
    """
    Start with the Mirror Shield. It is taken out of the item pool.
    """
    display_name = "Start with Mirror Shield"


class StartWithGoronTunic(Toggle):
    """
    Start with the Goron Tunic. It is taken out of the item pool.
    """
    display_name = "Start with Goron Tunic"


class StartWithZoraTunic(Toggle):
    """
    Start with the Zora Tunic. It is taken out of the item pool.
    """
    display_name = "Start with Zora Tunic"


class StartWithStoneOfAgony(Toggle):
    """
    Start with the Stone of Agony. It is taken out of the item pool.
    """
    display_name = "Start with Stone of Agony"


class StartWithWeirdEgg(Toggle):
    """
    Start with the Weird Egg. It is taken out of the item pool.
    """
    display_name = "Start with Weird Egg"


class StartWithClaimCheck(Toggle):
    """
    Start with the Claim Check. It is taken out of the item pool.
    """
    display_name = "Start with Claim Check"


class StartWithGerudoCard(Toggle):
    """
    Start with the Gerudo Membership Card. It is taken out of the item pool.
    """
    display_name = "Start with Gerudo Membership Card"


class StartWithKeatonMask(Toggle):
    """
    Start with the Keaton Mask.
    """
    display_name = "Start with Keaton Mask"


class StartWithSkullMask(Toggle):
    """
    Start with the Skull Mask.
    """
    display_name = "Start with Skull Mask"


class StartWithSpookyMask(Toggle):
    """
    Start with the Spooky Mask.
    """
    display_name = "Start with Spooky Mask"


class StartWithBunnyHood(Toggle):
    """
    Start with the Bunny Hood.
    """
    display_name = "Start with Bunny Hood"


class StartWithGoronMask(Toggle):
    """
    Start with the Goron Mask.
    """
    display_name = "Start with Goron Mask"


class StartWithZoraMask(Toggle):
    """
    Start with the Zora Mask.
    """
    display_name = "Start with Zora Mask"


class StartWithGerudoMask(Toggle):
    """
    Start with the Gerudo Mask.
    """
    display_name = "Start with Gerudo Mask"


class StartWithMaskOfTruth(Toggle):
    """
    Start with the Mask of Truth.
    """
    display_name = "Start with Mask of Truth"


class StartWithHookshot(Choice):
    """
    Start with the Hookshot at this level. The matching items are taken out of the item pool.
    """
    display_name = "Start with Hookshot"
    option_off = 0
    option_hookshot = 1
    option_longshot = 2
    default = 0


class StartWithBow(Choice):
    """
    Start with the Bow at this level. The matching items are taken out of the item pool.
    """
    display_name = "Start with Bow"
    option_off = 0
    option_quiver_30 = 1
    option_quiver_40 = 2
    option_quiver_50 = 3
    default = 0


class StartWithSlingshot(Choice):
    """
    Start with the Slingshot at this level. The matching items are taken out of the item pool.
    """
    display_name = "Start with Slingshot"
    option_off = 0
    option_bullet_bag_30 = 1
    option_bullet_bag_40 = 2
    option_bullet_bag_50 = 3
    default = 0


class StartWithBombBag(Choice):
    """
    Start with the Bomb Bag at this level. The matching items are taken out of the item pool.
    """
    display_name = "Start with Bomb Bag"
    option_off = 0
    option_bomb_bag_20 = 1
    option_bomb_bag_30 = 2
    option_bomb_bag_40 = 3
    default = 0


class StartWithStrength(Choice):
    """
    Start with the Strength at this level. The matching items are taken out of the item pool.
    """
    display_name = "Start with Strength"
    option_off = 0
    option_gorons_bracelet = 1
    option_silver_gauntlets = 2
    option_golden_gauntlets = 3
    default = 0


class StartWithScale(Choice):
    """
    Start with the Scale at this level. The matching items are taken out of the item pool.
    """
    display_name = "Start with Scale"
    option_off = 0
    option_silver_scale = 1
    option_golden_scale = 2
    default = 0


class StartWithWallet(Choice):
    """
    Start with the Wallet at this level. The matching items are taken out of the item pool.
    """
    display_name = "Start with Wallet"
    option_off = 0
    option_adults_wallet = 1
    option_giants_wallet = 2
    default = 0


class StartWithMagicMeter(Choice):
    """
    Start with the Magic Meter at this level. The matching items are taken out of the item pool.
    """
    display_name = "Start with Magic Meter"
    option_off = 0
    option_single_magic = 1
    option_double_magic = 2
    default = 0


class StartWithBombchuBag(Choice):
    """
    Start with the Bombchu Bag at this level. The matching items are taken out of the item pool.
    Only with Bombchu Bag "single_bag" (the level is the capacity in the game).
    """
    display_name = "Start with Bombchu Bag"
    option_off = 0
    option_bombchu_bag_20 = 1
    option_bombchu_bag_30 = 2
    option_bombchu_bag_50 = 3
    default = 0


class StartWithBiggoronsSword(Choice):
    """
    Start with the Biggoron's Sword at this level. The matching items are taken out of the item pool.
    """
    display_name = "Start with Biggoron's Sword"
    option_off = 0
    option_giants_knife = 1
    option_biggorons_sword = 2
    default = 0


class StartWithBottle1(Choice):
    """
    Start with a bottle in slot 1. A bottle from the item pool is taken out for it.
    """
    display_name = "Start with Bottle 1"
    option_off = 0
    option_empty_bottle = 1
    option_big_poe = 2
    option_rutos_letter = 3
    default = 0


class StartWithBottle2(Choice):
    """
    Start with a bottle in slot 2. A bottle from the item pool is taken out for it.
    """
    display_name = "Start with Bottle 2"
    option_off = 0
    option_empty_bottle = 1
    option_big_poe = 2
    default = 0


class StartWithBottle3(Choice):
    """
    Start with a bottle in slot 3. A bottle from the item pool is taken out for it.
    """
    display_name = "Start with Bottle 3"
    option_off = 0
    option_empty_bottle = 1
    option_big_poe = 2
    default = 0


class StartWithBottle4(Choice):
    """
    Start with a bottle in slot 4. A bottle from the item pool is taken out for it.
    """
    display_name = "Start with Bottle 4"
    option_off = 0
    option_empty_bottle = 1
    option_big_poe = 2
    default = 0


class ItemPool(Choice):
    """
    Sets how many major items appear in the item pool.
    Balanced - Original item pool.
    Plentiful - Extra major items are added to the pool.
    Scarce - Some excess items are removed, including health upgrades.
    Minimal - Most excess items are removed.
    """
    display_name = "Item Pool"
    option_balanced = 0
    option_plentiful = 1
    option_scarce = 2
    option_minimal = 3
    default = 0


class MedallionLockedTrials(Toggle):
    """
    Doors to trials will be barred until their corresponding medallion is acquired.
    """
    display_name = "Medallion Locked Trials"
    
    
class StartingSkulltulaTokens(Range):
    """
    Start with this many Gold Skulltula Tokens (Ship of Harkinian 9.3.1: "Starting Skulltula Tokens").
    They are taken out of the shuffled tokens in the item pool (vanilla-placed tokens stay where they are), and fewer
    tokens are needed from the pool for the Skulltula rewards and for token requirements of the bridge, Ganon's Boss Key etc.
    """
    display_name = "Starting Skulltula Tokens"
    range_start = 0
    range_end = 100
    default = 0


class StartingHearts(Range):
    """
    Specify the number of starting hearts Link will have. Modifies how many Heart Containers and Heart Pieces are in the pool.
    """
    display_name = "Starting Hearts Count"
    range_start = 1
    range_end = 20
    default = 3


class ShopAffordablePrices(Toggle):
    """
    After choosing a price range, set it to the affordable amount based on the wallet requirement.
    Affordable prices per tier: starter=1, adult=100, giant=201, tycoon=501
    Use this to enable wallet tier locking, but making shop items not as expensive as they could be.
    """
    display_name = "Shop Affordable Prices"


class ScrubAffordablePrices(Toggle):
    """
    After choosing a price range, set it to the affordable amount based on the wallet requirement.
    Affordable prices per tier: starter=1, adult=100, giant=201, tycoon=501
    Use this to enable wallet tier locking, but making shop items not as expensive as they could be.
    """
    display_name = "Scrub Affordable Prices"


class MerchantAffordablePrices(Toggle):
    """
    After choosing a price range, set it to the affordable amount based on the wallet requirement.
    Affordable prices per tier: starter=1, adult=100, giant=201, tycoon=501
    Use this to enable wallet tier locking, but making shop items not as expensive as they could be.
    """
    display_name = "Merchant Affordable Prices"


@dataclass
class SohOptions(PerGameCommonOptions):
    closed_forest: ClosedForest
    kakariko_gate: KakarikoGate
    door_of_time: DoorOfTime
    zoras_fountain: ZorasFountain
    sleeping_waterfall: SleepingWaterfall
    jabu_jabu: JabuJabu
    lock_overworld_doors: LockOverworldDoors
    fortress_carpenters: FortressCarpenters
    rainbow_bridge: RainbowBridge
    rainbow_bridge_stones_required: RainbowBridgeStonesRequired
    rainbow_bridge_medallions_required: RainbowBridgeMedallionsRequired
    rainbow_bridge_dungeon_rewards_required: RainbowBridgeDungeonRewardsRequired
    rainbow_bridge_dungeons_required: RainbowBridgeDungeonsRequired
    rainbow_bridge_skull_tokens_required: RainbowBridgeSkullTokensRequired
    rainbow_bridge_greg_modifier: RainbowBridgeGregModifier
    ganons_trials: GanonsTrials
    ganons_trials_count: GanonsTrialsCount
    triforce_hunt: TriforceHunt
    triforce_hunt_pieces_total: TriforceHuntPiecesTotal
    triforce_hunt_pieces_required_percentage: TriforceHuntPiecesRequiredPercentage
    triforce_hunt_pieces_location: TriforceHuntPiecesLocation
    win_condition: WinCondition
    win_condition_greg_modifier: WinConditionGregModifier
    win_condition_stones_required: WinConditionStonesRequired
    win_condition_medallions_required: WinConditionMedallionsRequired
    win_condition_dungeon_rewards_required: WinConditionDungeonRewardsRequired
    win_condition_dungeons_required: WinConditionDungeonsRequired
    win_condition_skull_tokens_required: WinConditionSkullTokensRequired
    rainbow_bridge_triforce_pieces_required: RainbowBridgeTriforcePiecesRequired
    ganons_castle_boss_key_triforce_pieces_required: GanonsCastleBossKeyTriforcePiecesRequired
    shuffle_songs: ShuffleSongs
    shuffle_skull_tokens: ShuffleTokens
    skulls_sun_song: SkullsSunSong
    shuffle_kokiri_sword: ShuffleKokiriSword
    shuffle_master_sword: ShuffleMasterSword
    shuffle_childs_wallet: ShuffleChildsWallet
    shuffle_ocarinas: ShuffleOcarinas
    shuffle_ocarina_buttons: ShuffleOcarinaButtons
    shuffle_swim: ShuffleSwim
    shuffle_weird_egg: ShuffleWeirdEgg
    shuffle_gerudo_membership_card: ShuffleGerudoMembershipCard
    shuffle_fishing_pole: ShuffleFishingPole
    shuffle_deku_stick_bag: ShuffleDekuStickBag
    shuffle_deku_nut_bag: ShuffleDekuNutBag
    shuffle_freestanding_items: ShuffleFreestandingItems
    shuffle_shops: ShuffleShops
    shuffle_shops_item_amount: ShuffleShopsItemAmount
    shuffle_shops_minimum_price: ShuffleShopsMinimumPrice
    shuffle_shops_maximum_price: ShuffleShopsMaximumPrice
    shuffle_fish: ShuffleFish
    fishsanity_pond_count: FishsanityPondCount
    fishsanity_age_split: FishsanityAgeSplit
    shuffle_scrubs: ShuffleScrubs
    shuffle_scrubs_minimum_price: ShuffleScrubsMinimumPrice
    shuffle_scrubs_maximum_price: ShuffleScrubsMaximumPrice
    shuffle_beehives: ShuffleBeehives
    shuffle_cows: ShuffleCows
    shuffle_pots: ShufflePots
    shuffle_signs: ShuffleSigns
    shuffle_wonder_items: ShuffleWonderItems
    shuffle_icicles: ShuffleIcicles
    shuffle_red_ice: ShuffleRedIce
    shuffle_rocks: ShuffleRocks
    shuffle_boulders: ShuffleBoulders
    shuffle_crates: ShuffleCrates
    shuffle_trees: ShuffleTrees
    shuffle_merchants: ShuffleMerchants
    shuffle_merchants_minimum_price: ShuffleMerchantsMinimumPrice
    shuffle_merchants_maximum_price: ShuffleMerchantsMaximumPrice
    shuffle_frog_song_rupees: ShuffleFrogSongRupees
    shuffle_beggar: ShuffleBeggar
    shuffle_adult_trade_items: ShuffleAdultTradeItems
    shuffle_boss_souls: ShuffleBossSouls
    ganons_soul: GanonsSoul
    ganons_soul_greg_modifier: GanonsSoulGregModifier
    ganons_soul_stones_required: GanonsSoulStonesRequired
    ganons_soul_medallions_required: GanonsSoulMedallionsRequired
    ganons_soul_dungeon_rewards_required: GanonsSoulDungeonRewardsRequired
    ganons_soul_dungeons_required: GanonsSoulDungeonsRequired
    ganons_soul_skull_tokens_required: GanonsSoulSkullTokensRequired
    ganons_soul_triforce_pieces_required: GanonsSoulTriforcePiecesRequired
    shuffle_fountain_fairies: ShuffleFountainFairies
    shuffle_stone_fairies: ShuffleStoneFairies
    shuffle_bean_fairies: ShuffleBeanFairies
    shuffle_song_fairies: ShuffleSongFairies
    shuffle_butterfly_fairies: ShuffleButterflyFairies
    shuffle_grass: ShuffleGrass
    shuffle_dungeon_rewards: ShuffleDungeonRewards
    maps_and_compasses: MapsAndCompasses
    ganons_castle_boss_key: GanonsCastleBossKey
    ganons_castle_boss_key_stones_required: GanonsCastleBossKeyStonesRequired
    ganons_castle_boss_key_medallions_required: GanonsCastleBossKeyMedallionsRequired
    ganons_castle_boss_key_dungeon_rewards_required: GanonsCastleBossKeyDungeonRewardsRequired
    ganons_castle_boss_key_dungeons_required: GanonsCastleBossKeyDungeonsRequired
    ganons_castle_boss_key_skull_tokens_required: GanonsCastleBossKeySkullTokensRequired
    ganons_castle_boss_key_greg_modifier: GanonsCastleBossKeyGregModifier
    small_key_shuffle: SmallKeyShuffle
    gerudo_fortress_key_shuffle: GerudoFortressKeyShuffle
    boss_key_shuffle: BossKeyShuffle
    key_rings: KeyRings
    key_rings_count: KeyRingsCount
    gerudo_fortress_key_ring: GerudoFortressKeyring
    forest_temple_key_ring: ForestTempleKeyring
    fire_temple_key_ring: FireTempleKeyring
    water_temple_key_ring: WaterTempleKeyring
    spirit_temple_key_ring: SpiritTempleKeyring
    shadow_temple_key_ring: ShadowTempleKeyring
    bottom_of_the_well_key_ring: BottomOfTheWellKeyring
    gerudo_training_ground_key_ring: GerudoTrainingGroundKeyring
    ganons_castle_key_ring: GanonsCastleKeyring
    big_poe_target_count: BigPoeTargetCount
    skip_child_zelda: SkipChildZelda
    skip_epona_race: SkipEponaRace
    skip_child_stealth: SkipChildStealth
    skip_planting_beans: SkipPlantingBeans
    complete_mask_quest: CompleteMaskQuest
    skip_scarecrows_song: SkipScarecrowsSong
    start_with_links_pocket: StartWithLinksPocket
    links_pocket_reward: LinksPocketReward
    bunny_hood_effect: BunnyHoodEffect
    progressive_goron_sword: ProgressiveGoronSword
    masks_as_adult: MasksAsAdult
    early_grannys_shop: EarlyGrannysShop
    swordless_epona_items: SwordlessEponaItems
    shop_shields_and_tunics_only_refill: ShopShieldsAndTunicsOnlyRefill
    start_with_kokiri_sword: StartWithKokiriSword
    start_with_master_sword: StartWithMasterSword
    start_with_deku_shield: StartWithDekuShield
    start_with_ocarina: StartWithOcarina
    start_with_stick_ammo: StartWithStickAmmo
    start_with_nut_ammo: StartWithNutAmmo
    start_with_magic_beans: StartWithMagicBeans
    start_with_zeldas_lullaby :StartWithZeldasLullaby
    start_with_eponas_song :StartWithEponasSong
    start_with_sarias_song :StartWithSariasSong
    start_with_suns_song :StartWithSunsSong
    start_with_song_of_time :StartWithSongOfTime
    start_with_song_of_storms :StartWithSongOfStorms
    start_with_minuet :StartWithMinuet
    start_with_bolero :StartWithBolero
    start_with_serenade :StartWithSerenade
    start_with_requiem :StartWithRequiem
    start_with_nocturne :StartWithNocturne
    start_with_prelude :StartWithPrelude
    start_with_megaton_hammer: StartWithMegatonHammer
    start_with_boomerang: StartWithBoomerang
    start_with_lens_of_truth: StartWithLensOfTruth
    start_with_dins_fire: StartWithDinsFire
    start_with_farores_wind: StartWithFaroresWind
    start_with_nayrus_love: StartWithNayrusLove
    start_with_fire_arrows: StartWithFireArrows
    start_with_ice_arrows: StartWithIceArrows
    start_with_light_arrows: StartWithLightArrows
    start_with_iron_boots: StartWithIronBoots
    start_with_hover_boots: StartWithHoverBoots
    start_with_hylian_shield: StartWithHylianShield
    start_with_mirror_shield: StartWithMirrorShield
    start_with_goron_tunic: StartWithGoronTunic
    start_with_zora_tunic: StartWithZoraTunic
    start_with_stone_of_agony: StartWithStoneOfAgony
    start_with_weird_egg: StartWithWeirdEgg
    start_with_claim_check: StartWithClaimCheck
    start_with_gerudo_card: StartWithGerudoCard
    start_with_keaton_mask: StartWithKeatonMask
    start_with_skull_mask: StartWithSkullMask
    start_with_spooky_mask: StartWithSpookyMask
    start_with_bunny_hood: StartWithBunnyHood
    start_with_goron_mask: StartWithGoronMask
    start_with_zora_mask: StartWithZoraMask
    start_with_gerudo_mask: StartWithGerudoMask
    start_with_mask_of_truth: StartWithMaskOfTruth
    start_with_hookshot: StartWithHookshot
    start_with_bow: StartWithBow
    start_with_slingshot: StartWithSlingshot
    start_with_bomb_bag: StartWithBombBag
    start_with_strength: StartWithStrength
    start_with_scale: StartWithScale
    start_with_wallet: StartWithWallet
    start_with_magic_meter: StartWithMagicMeter
    start_with_bombchu_bag: StartWithBombchuBag
    start_with_biggorons_sword: StartWithBiggoronsSword
    start_with_bottle_1: StartWithBottle1
    start_with_bottle_2: StartWithBottle2
    start_with_bottle_3: StartWithBottle3
    start_with_bottle_4: StartWithBottle4
    starting_skulltula_tokens: StartingSkulltulaTokens
    full_wallets: FullWallets
    bombchu_bag: BombchuBag
    bombchu_drops: BombchuDrops
    start_inventory_from_pool: StartInventoryPool
    blue_fire_arrows: BlueFireArrows
    sunlight_arrows: SunlightArrows
    rocs_feather: RocsFeather
    infinite_upgrades: InfiniteUpgrades
    skeleton_key: SkeletonKey
    slingbow_break_beehives: SlingbowBreakBeehives
    starting_age: StartingAge
    shuffle_100_gs_reward: Shuffle100GSReward
    ice_trap_count: IceTrapCount
    ice_trap_filler_replacement: IceTrapFillerReplacement
    ice_trap_names: IceTrapNames
    true_no_logic: TrueNoLogic
    shuffle_tycoon_wallet: ShuffleTycoonWallet
    tricks_in_logic: TricksInLogic
    enable_all_tricks: EnableAllTricks
    item_pool: ItemPool
    medallion_locked_trials: MedallionLockedTrials
    starting_hearts: StartingHearts
    shop_affordable_prices: ShopAffordablePrices
    scrub_affordable_prices: ScrubAffordablePrices
    merchant_affordable_prices: MerchantAffordablePrices
    hint_clarity: HintClarity
    gossip_stone_hints: GossipStoneHints
    tot_altar_hint: ToTAltarHint
    ganondorf_hint: GanondorfHint
    sheik_la_hint: SheikLightArrowHint
    boss_key_hint: BossKeyHint
    dampe_diary_hint: DampeDiaryHint
    greg_hint: GregHint
    #hyrule_loach_hint: HyruleLoachHint
    saria_hint: SariasHint
    mido_hint: MidosHint
    frog_game_hint: FrogOcarinaGameHint
    ocarina_of_time_hint: OcarinaOfTimeHint
    big_goron_hint: BiggoronHint
    big_poe_hint: BigPoeHint
    chicken_hint: ChickenHint
    malon_hint: MalonHint
    horseback_archery_hint: HorsebackArcheryHint
    fishing_pole_hint: FishingPoleHint
    #warp_song_hint: WarpSongHint   # Not required until they can be randomized
    scrub_hints: ScrubHintText
    merchant_hints: MerchantHintText
    gs_10_hint: GS10Hint
    gs_20_hint: GS20Hint
    gs_30_hint: GS30Hint
    gs_40_hint: GS40Hint
    gs_50_hint: GS50Hint
    gs_100_hint: GS100Hint
    mask_shop_hint: MaskShopHint

    def apply_any_required_option_adjustments(self):
        self.adjust_win_condition()
        self.adjust_ganons_soul()
        self.adjust_for_forced_child_starts()
        self.adjust_prices()
        self.adjust_starting_items()
        self.adjust_irrelevant_hints()
        self.adjust_greg_modifiers()
        self.adjust_key_rings()


    def adjust_for_forced_child_starts(self):
        # We don't care about any of this if no logic is enabled
        if self.true_no_logic:
            return

        # If door of time is set to closed and dungeon rewards aren't shuffled or ocarinas aren't shuffled, force child spawn
        if self.door_of_time == DoorOfTime.option_closed and (
            any([self.shuffle_dungeon_rewards == ShuffleDungeonRewards.option_off,
                    self.shuffle_ocarinas == ShuffleOcarinas.option_false,
                    self.shuffle_songs == ShuffleSongs.option_off])):
            self.starting_age.value = StartingAge.option_child
            return

        # If door of time is set to song only and songs aren't shuffled, force child spawn
        if all([self.door_of_time == DoorOfTime.option_song_only, self.shuffle_songs == ShuffleSongs.option_off]):
            self.starting_age.value = StartingAge.option_child
            return
        
        # If closed forest is on, force child spawn. Will need additional logic when entrance shuffle is added in future.
        if self.closed_forest == ClosedForest.option_on:
            self.starting_age.value = StartingAge.option_child
            return
        

    def adjust_starting_items(self):
        # SoH 9.3.1: Skip Child Zelda = starting with Zelda's Letter + Weird Egg "Skip Waking Talon"
        if self.skip_child_zelda:
            self.shuffle_weird_egg.value = ShuffleWeirdEgg.option_skip_waking_talon

        if self.shuffle_deku_stick_bag == ShuffleDekuStickBag.option_true:
            self.start_with_stick_ammo.value = StartWithStickAmmo.option_false

        if self.shuffle_deku_nut_bag == ShuffleDekuNutBag.option_true:
            self.start_with_nut_ammo.value = StartWithNutAmmo.option_false

        if any([self.shuffle_dungeon_rewards == ShuffleDungeonRewards.option_off,
                self.shuffle_dungeon_rewards == ShuffleDungeonRewards.option_end_of_dungeons]):
            self.start_with_links_pocket.value = StartWithLinksPocket.option_dungeon_reward


    def adjust_prices(self):
        # Check if Tycoon Wallet is shuffled and if price settings are above what Giants Wallet can hold. Max/Min Prices need to be adjusted to fit in Giants Wallet.
        if self.shuffle_tycoon_wallet == ShuffleTycoonWallet.option_false:
            for option in (self.shuffle_shops_minimum_price, self.shuffle_shops_maximum_price, self.shuffle_scrubs_minimum_price, self.shuffle_scrubs_maximum_price, self.shuffle_merchants_minimum_price, self.shuffle_merchants_maximum_price):
                if option.value > wallet_capacities[Items.GIANT_WALLET]:
                    option.value = wallet_capacities[Items.GIANT_WALLET]

        # If maximum price is below minimum, set max to minimum.
        if self.shuffle_shops_minimum_price.value > self.shuffle_shops_maximum_price.value:
            self.shuffle_shops_maximum_price.value = self.shuffle_shops_minimum_price.value

        if self.shuffle_scrubs_minimum_price.value > self.shuffle_scrubs_maximum_price.value:
            self.shuffle_scrubs_maximum_price.value = self.shuffle_scrubs_minimum_price.value

        if self.shuffle_merchants_minimum_price.value > self.shuffle_merchants_maximum_price.value:
            self.shuffle_merchants_maximum_price.value = self.shuffle_merchants_minimum_price.value
    

    def adjust_irrelevant_hints(self):
        # disable hints for items we don't have shuffled
        #hyrule_loach_hint
        # todo turn loach off if fishsanity not set to loach only
        if self.shuffle_cows == ShuffleCows.option_false:
            self.malon_hint.value = MalonHint.option_false

        if self.shuffle_fishing_pole == ShuffleFish.option_off:
            self.fishing_pole_hint.value = FishingPoleHint.option_false

        if self.shuffle_100_gs_reward == Shuffle100GSReward.option_false:
            self.gs_100_hint.value = GS100Hint.option_false


    def calculate_progression_skulltula_count(self, token_reward_counts) -> int:
        # First we need to figure out how many skulltula tokens are shuffled.
        # This lets us know how many vanilla tokes there are in the seed
        if self.shuffle_skull_tokens == ShuffleTokens.option_all:
            shuffled_token_count = TokenCounts.TOTAL
        elif self.shuffle_skull_tokens == ShuffleTokens.option_dungeon:
            shuffled_token_count = TokenCounts.DUNGEON
        elif self.shuffle_skull_tokens == ShuffleTokens.option_overworld:
            shuffled_token_count = TokenCounts.OVERWORLD
        else:
            shuffled_token_count = 0
        vanilla_token_count = TokenCounts.TOTAL - shuffled_token_count

        # Start with 50 tokens for 0-50 rewards
        required_skulltula_count = 50

        # All 100 required to obtain 100gs reward, so all are progression if reward is shuffled
        if self.shuffle_100_gs_reward:
            required_skulltula_count = TokenCounts.TOTAL

        if self.accessibility == Accessibility.option_minimal:
            # Find the highest non-excluded token reward and set that as the required count
            # This assumes that the locations are in descending order of token amounts e.g. 50 -> 40 -> 30
            # Should end up with 50 most of the time since that's the biggest reward, but if 50 is excluded then it would be 40, etc.
            for location, amount in token_reward_counts.items():
                if str(location) not in self.exclude_locations:
                    required_skulltula_count = amount

        # Then we need to know if there's any other token count requirements. This is for things like 
        # Skulltula requires for Rainbow Bridge or Ganon's Castle Boss Key
        rainbow_bridge_tokens = 0
        ganons_castle_boss_key_tokens = 0
        
        if self.rainbow_bridge == RainbowBridge.option_tokens:
            rainbow_bridge_tokens = self.rainbow_bridge_skull_tokens_required.value
        if self.ganons_castle_boss_key == GanonsCastleBossKey.option_lacs_skull_tokens:
            ganons_castle_boss_key_tokens = self.ganons_castle_boss_key_skull_tokens_required.value
        
        ganons_soul_tokens = 0
        if self.ganons_soul == GanonsSoul.option_trigger_skull_tokens:
            ganons_soul_tokens = self.ganons_soul_skull_tokens_required.value
        win_condition_tokens = 0
        if self.win_condition == WinCondition.option_trigger_skull_tokens:
            win_condition_tokens = self.win_condition_skull_tokens_required.value

        required_skulltula_count = max(required_skulltula_count, rainbow_bridge_tokens, ganons_castle_boss_key_tokens,
                                       ganons_soul_tokens, win_condition_tokens)
        # 3drando/fill.cpp GetMaxGSCount: "minus the tokens in the starting inventory"
        required_skulltula_count = max(0, required_skulltula_count - self.starting_skulltula_tokens.value)

        if self.accessibility == Accessibility.option_full:
            # If full accessibility is enabled, assume all vanilla tokens are available and calculate the required shuffled tokens
            # This will be the total required skulltula count minus the amount of vanilla tokens
            # that are still available based on the skull shuffle settings.
            #
            # For example, if you need 80 GS tokens to complete the seed, and dungeon tokens are shuffled
            # then you have 56 vanilla tokens available to you, so you would require 24 of the shuffled
            # tokens to finish the game. The rest would be optional
            needed_shuffled_tokens = max(0, required_skulltula_count - vanilla_token_count)
        else:
            # If accessibility is set to minimal, set all the shuffled tokens to be progression.
            # This aims to better act in the spirit of minimal accessibility by reducing the number
            # of vanilla tokens that are available to the player that are considered 'progression'
            # This should hopefully allow for lower access minimal seeds.
            needed_shuffled_tokens = max(0, shuffled_token_count)

        # Make sure this can't exceed the total amount of shuffled tokens
        return min(needed_shuffled_tokens, shuffled_token_count)


    def adjust_greg_modifiers(self):
        # Check Rainbow Bridge and GBK options if their greg modifier is not Reward.
        # The if they are set to the max, they must be decremented once
        def decrement_option(option):
            if option != None:
                if option == option.range_end:
                        option.value -= 1

                option = None
        
        option = None
        
        if self.rainbow_bridge_greg_modifier != RainbowBridgeGregModifier.option_reward:
            if self.rainbow_bridge == RainbowBridge.option_stones:
                option = self.rainbow_bridge_stones_required
            elif self.rainbow_bridge == RainbowBridge.option_medallions:
                option = self.rainbow_bridge_medallions_required
            elif self.rainbow_bridge == RainbowBridge.option_dungeon_rewards:
                option = self.rainbow_bridge_dungeon_rewards_required
            elif self.rainbow_bridge == RainbowBridge.option_dungeons:
                option = self.rainbow_bridge_dungeons_required

            decrement_option(option)

        if self.win_condition_greg_modifier != WinConditionGregModifier.option_reward:
            option = None
            if self.win_condition == WinCondition.option_trigger_stones:
                option = self.win_condition_stones_required
            elif self.win_condition == WinCondition.option_trigger_medallions:
                option = self.win_condition_medallions_required
            elif self.win_condition == WinCondition.option_trigger_dungeon_rewards:
                option = self.win_condition_dungeon_rewards_required
            elif self.win_condition == WinCondition.option_trigger_dungeons:
                option = self.win_condition_dungeons_required
            decrement_option(option)
            option = None

        if self.ganons_soul_greg_modifier != GanonsSoulGregModifier.option_reward:
            option = None
            if self.ganons_soul == GanonsSoul.option_trigger_stones:
                option = self.ganons_soul_stones_required
            elif self.ganons_soul == GanonsSoul.option_trigger_medallions:
                option = self.ganons_soul_medallions_required
            elif self.ganons_soul == GanonsSoul.option_trigger_dungeon_rewards:
                option = self.ganons_soul_dungeon_rewards_required
            elif self.ganons_soul == GanonsSoul.option_trigger_dungeons:
                option = self.ganons_soul_dungeons_required
            decrement_option(option)
            option = None

        if self.ganons_castle_boss_key_greg_modifier != GanonsCastleBossKeyGregModifier.option_reward:
            if self.ganons_castle_boss_key == GanonsCastleBossKey.option_lacs_stones:
                option = self.ganons_castle_boss_key_stones_required
            elif self.ganons_castle_boss_key == GanonsCastleBossKey.option_lacs_medallions:
                option = self.ganons_castle_boss_key_medallions_required
            elif self.ganons_castle_boss_key == GanonsCastleBossKey.option_lacs_dungeon_rewards:
                option = self.ganons_castle_boss_key_dungeon_rewards_required
            elif self.ganons_castle_boss_key == GanonsCastleBossKey.option_lacs_dungeons:
                option = self.ganons_castle_boss_key_dungeons_required

            decrement_option(option)

    def adjust_win_condition(self):
        # "default" keeps the behavior from before the option: Triforce Hunt wins with the pieces, otherwise Ganon
        if self.win_condition == WinCondition.option_default:
            self.win_condition.value = (WinCondition.option_trigger_triforce_pieces if self.triforce_hunt
                                        else WinCondition.option_defeat_ganon)
        uses_pieces = {
            "Win Condition": self.win_condition == WinCondition.option_trigger_triforce_pieces,
            "Rainbow Bridge": self.rainbow_bridge == RainbowBridge.option_triforce_pieces,
            "Ganon's Castle Boss Key": self.ganons_castle_boss_key == GanonsCastleBossKey.option_lacs_triforce_pieces,
        }
        for name, used in uses_pieces.items():
            if used and not self.triforce_hunt:
                raise OptionError(f"{name} \"Triforce Pieces\" needs Triforce Hunt.")

    def adjust_ganons_soul(self):
        # SoH 9.3.1 split "Shuffle Boss Souls: On + Ganon" into "On" plus its own Ganon's Soul setting (upstream
        # ConfigVersion7Updater maps it to Ganon's Soul "Anywhere"); older YAMLs keep playing the same.
        if self.shuffle_boss_souls == ShuffleBossSouls.option_on_plus_ganons and self.ganons_soul == GanonsSoul.option_start_with:
            self.ganons_soul.value = GanonsSoul.option_anywhere
        if self.ganons_soul == GanonsSoul.option_trigger_triforce_pieces and not self.triforce_hunt:
            raise OptionError("Ganon's Soul \"trigger_triforce_pieces\" needs Triforce Hunt.")

    def adjust_key_rings(self):
        if self.small_key_shuffle not in (SmallKeyShuffle.option_start_with, SmallKeyShuffle.option_vanilla):
            return
        
        as_ring = Toggle.option_false
        if self.small_key_shuffle == SmallKeyShuffle.option_start_with:
            as_ring = Toggle.option_true

        self.forest_temple_key_ring.value = as_ring
        self.fire_temple_key_ring.value = as_ring
        self.water_temple_key_ring.value = as_ring
        self.spirit_temple_key_ring.value = as_ring
        self.shadow_temple_key_ring.value = as_ring
        self.bottom_of_the_well_key_ring.value = as_ring
        self.gerudo_training_ground_key_ring.value = as_ring
        self.ganons_castle_key_ring.value = as_ring

soh_option_groups = [
    OptionGroup("Area Access", [
        ClosedForest,
        KakarikoGate,
        DoorOfTime,
        ZorasFountain,
        SleepingWaterfall,
        JabuJabu,
        LockOverworldDoors,
        EnableAllTricks,
        TricksInLogic
    ]),
    OptionGroup("World Settings", [
        StartingAge,
        StartingHearts,
        FortressCarpenters,
        RainbowBridge,
        RainbowBridgeStonesRequired,
        RainbowBridgeMedallionsRequired,
        RainbowBridgeDungeonRewardsRequired,
        RainbowBridgeDungeonsRequired,
        RainbowBridgeSkullTokensRequired,
        RainbowBridgeGregModifier,
        MedallionLockedTrials,
        GanonsTrials,
        GanonsTrialsCount,
        RainbowBridgeTriforcePiecesRequired,
        TriforceHunt,
        TriforceHuntPiecesTotal,
        TriforceHuntPiecesRequiredPercentage,
        TriforceHuntPiecesLocation,
        WinCondition,
        WinConditionStonesRequired,
        WinConditionMedallionsRequired,
        WinConditionDungeonRewardsRequired,
        WinConditionDungeonsRequired,
        WinConditionSkullTokensRequired,
        WinConditionGregModifier,
    ]),
    # OptionGroup("Shuffle Entrances", [
    #     # Dungeon Entrances
    #     # Boss Entrances
    #     # Overworld Entrances
    #     # Interior Entrances
    #     # Grotto Entrances
    #     # Owl Drops
    #     # Warp Songs
    #     # Overworld Spawns
    #     # Decouple Entrances
    # ]),
    OptionGroup("Shuffle Items", [
        ShuffleSongs,
        ShuffleTokens,
        SkullsSunSong,
        ShuffleFreestandingItems,
        ShuffleKokiriSword,
        ShuffleMasterSword,
        ShuffleChildsWallet,
        ShuffleTycoonWallet,
        ShuffleOcarinas,
        ShuffleOcarinaButtons,
        ShuffleSwim,
        ShuffleWeirdEgg,
        ShuffleGerudoMembershipCard,
        ShuffleFishingPole,
        ShuffleDekuStickBag,
        ShuffleDekuNutBag,
        RocsFeather
    ]),
    OptionGroup("Shuffle NPCs & Merchants", [
        ShuffleShops,
        ShuffleShopsItemAmount,
        ShuffleShopsMinimumPrice,
        ShuffleShopsMaximumPrice,
        ShopAffordablePrices,
        # Other shop weight stuff
        ShuffleFish,
        FishsanityPondCount,
        FishsanityAgeSplit,
        ShuffleScrubs,
        ShuffleScrubsMinimumPrice,
        ShuffleScrubsMaximumPrice,
        ScrubAffordablePrices,
        ShuffleBeehives,
        ShuffleCows,
        ShufflePots,
        ShuffleSigns,
        ShuffleWonderItems,
        ShuffleIcicles,
        ShuffleRedIce,
        ShuffleRocks,
        ShuffleBoulders,
        ShuffleCrates,
        ShuffleTrees,
        ShuffleMerchants,
        ShuffleMerchantsMinimumPrice,
        ShuffleMerchantsMaximumPrice,
        MerchantAffordablePrices,
        ShuffleFrogSongRupees,
        ShuffleBeggar,
        ShuffleAdultTradeItems,
        Shuffle100GSReward,
        ShuffleBossSouls,
        GanonsSoul,
        GanonsSoulStonesRequired,
        GanonsSoulMedallionsRequired,
        GanonsSoulDungeonRewardsRequired,
        GanonsSoulDungeonsRequired,
        GanonsSoulSkullTokensRequired,
        GanonsSoulTriforcePiecesRequired,
        GanonsSoulGregModifier,
        ShuffleFountainFairies,
        ShuffleStoneFairies,
        ShuffleBeanFairies,
        ShuffleSongFairies,
        ShuffleButterflyFairies,
        ShuffleGrass,
    ]),
    OptionGroup("Shuffle Dungeon Items", [
        ShuffleDungeonRewards,
        MapsAndCompasses,
        SmallKeyShuffle,
        GerudoFortressKeyShuffle,
        BossKeyShuffle,
        GanonsCastleBossKey,
        GanonsCastleBossKeyStonesRequired,
        GanonsCastleBossKeyMedallionsRequired,
        GanonsCastleBossKeyDungeonRewardsRequired,
        GanonsCastleBossKeyDungeonsRequired,
        GanonsCastleBossKeySkullTokensRequired,
        GanonsCastleBossKeyTriforcePiecesRequired,
        GanonsCastleBossKeyGregModifier,
        KeyRings,
        KeyRingsCount,
        GerudoFortressKeyring,
        ForestTempleKeyring,
        FireTempleKeyring,
        WaterTempleKeyring,
        SpiritTempleKeyring,
        ShadowTempleKeyring,
        BottomOfTheWellKeyring,
        GerudoTrainingGroundKeyring,
        GanonsCastleKeyring
    ]),
    # todo: decide whether these should be in the yaml or just let you change them locally on the fly
    OptionGroup("Gameplay (SoH 9.3.1)", [
        ProgressiveGoronSword,
        BunnyHoodEffect,
        MasksAsAdult,
        EarlyGrannysShop,
        SwordlessEponaItems,
        ShopShieldsAndTunicsOnlyRefill,
    ]),
    OptionGroup("Timesavers", [
        BigPoeTargetCount,
        SkipChildZelda,
        SkipEponaRace,
        SkipChildStealth,
        SkipPlantingBeans,
        CompleteMaskQuest,
        SkipScarecrowsSong,
    ]),
    OptionGroup("Item Pool & Traps", [
        ItemPool,
        IceTrapCount,
        IceTrapFillerReplacement,
        IceTrapNames
    ]),
    OptionGroup("Hints", [
        HintClarity,
        #HintDistribution
        GossipStoneHints,
        ToTAltarHint,
        GanondorfHint,
        SheikLightArrowHint,
        BossKeyHint,
        DampeDiaryHint,
        GregHint,
        #HyruleLoachHint,
        SariasHint,
        MidosHint,
        FrogOcarinaGameHint,
        OcarinaOfTimeHint,
        BiggoronHint,
        BigPoeHint,
        ChickenHint,
        MalonHint,
        HorsebackArcheryHint,
        FishingPoleHint,
        #WarpSongHint,
        ScrubHintText,
        MerchantHintText,
        GS10Hint,
        GS20Hint,
        GS30Hint,
        GS40Hint,
        GS50Hint,
        GS100Hint,
        MaskShopHint
    ]),
    OptionGroup("Starting Items", [
        StartWithLinksPocket,
        LinksPocketReward,
        StartWithKokiriSword,
        StartWithMasterSword,
        StartWithDekuShield,
        StartWithOcarina,
        StartWithStickAmmo,
        StartWithNutAmmo,
        StartWithMagicBeans,
        StartWithZeldasLullaby,
        StartWithEponasSong,
        StartWithSariasSong,
        StartWithSunsSong,
        StartWithSongOfTime,
        StartWithSongOfStorms,
        StartWithMinuet,
        StartWithBolero,
        StartWithSerenade,
        StartWithRequiem,
        StartWithNocturne,
        StartWithPrelude,
        StartWithMegatonHammer,
        StartWithBoomerang,
        StartWithLensOfTruth,
        StartWithDinsFire,
        StartWithFaroresWind,
        StartWithNayrusLove,
        StartWithFireArrows,
        StartWithIceArrows,
        StartWithLightArrows,
        StartWithIronBoots,
        StartWithHoverBoots,
        StartWithHylianShield,
        StartWithMirrorShield,
        StartWithGoronTunic,
        StartWithZoraTunic,
        StartWithStoneOfAgony,
        StartWithWeirdEgg,
        StartWithClaimCheck,
        StartWithGerudoCard,
        StartWithKeatonMask,
        StartWithSkullMask,
        StartWithSpookyMask,
        StartWithBunnyHood,
        StartWithGoronMask,
        StartWithZoraMask,
        StartWithGerudoMask,
        StartWithMaskOfTruth,
        StartWithHookshot,
        StartWithBow,
        StartWithSlingshot,
        StartWithBombBag,
        StartWithStrength,
        StartWithScale,
        StartWithWallet,
        StartWithMagicMeter,
        StartWithBombchuBag,
        StartWithBiggoronsSword,
        StartWithBottle1,
        StartWithBottle2,
        StartWithBottle3,
        StartWithBottle4,
        StartingSkulltulaTokens,
        #StartingHearts,
    ]),
    OptionGroup("Additional Features", [
        FullWallets,  # another one that should maybe just be a locally changeable setting instead of in the yaml
        BombchuBag,
        BombchuDrops,
        BlueFireArrows,
        SunlightArrows,
        InfiniteUpgrades,
        SkeletonKey,
        SlingbowBreakBeehives
    ])
]
