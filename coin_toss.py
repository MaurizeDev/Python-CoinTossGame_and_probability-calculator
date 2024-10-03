# Coin Toss Game

# Theory from the stock market world: We look at winners like Warren Buffett, Ray Dalio, etc., and assume their
# success is due to their skills. But statistically, there must be these outliers. When billions of people are/were
# active in the stock market, it is inevitable that some have made gigantic profits. And consequently, some have only lost.

# So, is it statistically unavoidable and therefore luck? And even if it is statistically unavoidable, do you only
# get into this position with luck or skill? -> Chicken/Egg problem
# Assumption: If the entire population tosses coins in a tournament against each other, there will statistically be
# a winner who always tossed heads. For example, with 300 million people, after 30 tosses, there ist still a
# 25% chance, someone tossed 30 times heads in a row. The probability of tossing 30 times in row the same side is about
# 0,0000000931323 % (1 in over 1 billion). Yet in large populations it is almost certain, that it will occur.

# This program simulates the coin tosses with a given amount of players and tosses and sums up the result.


import random
import time

# ANSI Escape Code for light blue
light_blue = '\033[94m'
reset_color = '\033[0m'  # Reset to default color


class Player:
    """
    The Player class represents a player who tosses a coin in a game. The player can toss heads or tails,
    and the class tracks the number of heads and tails tossed, as well as whether only heads or only tails were tossed.

    Attributes:
        name (str): The name of the player.
        heads_count (int): The number of heads tosses by the player.
        tails_count (int): The number of tails tosses by the player.
        only_heads (bool): True if the player has only tossed heads, False otherwise.
        only_tails (bool): True if the player has only tossed tails, False otherwise.

    Methods:
        toss_coin(): Simulates a coin toss and updates heads and tails counters.
        check_booleans(): Checks whether the player has tossed only heads or only tails.
        display_results(): Displays the results of the player's tosses, including percentages.
    """

    def __init__(self, name):
        """Initializes the Player class with a name, counters for heads and tails tosses, and booleans."""
        self.name = name  # Name of the player (e.g., Player1, Player2, etc.)
        self.heads_count = 0  # Number of heads tosses
        self.tails_count = 0  # Number of tails tosses
        self.only_heads = False  # Boolean if only heads were tossed
        self.only_tails = False  # Boolean if only tails were tossed

    def toss_coin(self):
        """Tosses a coin and updates the counters and booleans accordingly."""
        toss = random.choice(['Heads', 'Tails'])  # Random coin toss
        if toss == 'Heads':
            self.heads_count += 1  # Increases the heads counter
        else:
            self.tails_count += 1  # Increases the tails counter
        self.check_booleans()  # Updates the booleans after the toss
        return toss

    def check_booleans(self):
        """Checks and sets the booleans for only heads or only tails tosses."""
        if self.tails_count == 0 and self.heads_count > 0:
            self.only_heads = True
        else:
            self.only_heads = False

        if self.heads_count == 0 and self.tails_count > 0:
            self.only_tails = True
        else:
            self.only_tails = False

    def display_results(self):
        """Displays the current results of the player, including the percentage of heads and tails tosses."""
        total_tosses = self.heads_count + self.tails_count

        if total_tosses > 0:
            heads_percent = (self.heads_count / total_tosses) * 100
            tails_percent = (self.tails_count / total_tosses) * 100
        else:
            heads_percent = tails_percent = 0

        print(f"{self.name}:")
        print(f"\tHeads tosses: {self.heads_count} ({heads_percent:.2f}%)")
        print(f"\tTails tosses: {self.tails_count} ({tails_percent:.2f}%)")
        print(f"\tOnly tossed heads: {self.only_heads}")
        print(f"\tOnly tossed tails: {self.only_tails} \n")


def total_score(player_list, start_time, number_of_tosses):
    """Displays the total result for all players, including percentage values for heads and tails tosses."""
    total_heads = 0
    total_tails = 0
    total_tosses = 0
    only_heads_count = 0
    only_tails_count = 0

    # Iterate through the list of all players and sum the results
    for player in player_list:
        total_heads += player.heads_count
        total_tails += player.tails_count
        total_tosses += player.heads_count + player.tails_count
        if player.only_heads:
            only_heads_count += 1
        if player.only_tails:
            only_tails_count += 1

    # Calculate percentage values
    if total_tosses > 0:
        heads_percent = (total_heads / total_tosses) * 100
        tails_percent = (total_tails / total_tosses) * 100
    else:
        heads_percent = tails_percent = 0

    print(f"Number of players: \t\t\t\t{light_blue}{len(player_list):,}{reset_color}")
    print(f"Total number of coin tosses: \t{total_tosses:,}")
    print(f"Total heads tosses: \t\t\t{total_heads:,} ({heads_percent:.5f}%)")
    print(f"Total tails tosses: \t\t\t{total_tails:,} ({tails_percent:.5f}%)")

    # Light blue output for the specific values
    print(
        f"Players only tossed heads: \t\t{light_blue}{only_heads_count:,}{reset_color} (Probability: {(only_heads_count / len(player_list)) * 100:.6f}%)")
    print(
        f"Players only tossed tails: \t\t{light_blue}{only_tails_count:,}{reset_color} (Probability: {(only_tails_count / len(player_list)) * 100:.6f}%)")

    # Calculate and display the runtime
    runtime = time.time() - start_time

    if runtime < 10:
        print(f"Program runtime: \t\t\t\t{runtime:.2f} seconds")
    elif runtime < 60:
        print(f"Program runtime: \t\t\t\t{int(runtime)} seconds")
    elif runtime < 3600:
        minutes = int(runtime // 60)
        seconds = int(runtime % 60)
        print(f"Program runtime: \t\t\t\t{minutes}:{seconds} min")
    else:
        hours = int(runtime // 3600)
        minutes = int((runtime % 3600) // 60)
        seconds = int(runtime % 60)
        print(f"Program runtime: \t\t\t\t{hours}:{minutes:02}:{seconds:02} h")


def play_with_multiple_players(number_of_players, number_of_tosses):
    """Creates multiple players and performs coin tosses for each player."""
    player_list = [Player(f"Player{i + 1}") for i in range(number_of_players)]  # Create Player1, Player2, ...

    for j in range(number_of_tosses):
        for player in player_list:
            player.toss_coin()

    return player_list  # Return the list of players


def divider(headline):
    """
    Prints a formatted section divider with a given headline. For better readability in console window.

    This function creates a visual break in the console output by printing a line of dashes (70 characters long),
    followed by the provided headline text, and then another line of dashes. This is useful for separating sections
    of output in a clear and organized way.

    Args:
        headline (str): The text to display in the center of the divider.
    """
    print("\n" + 60 * "─")
    print("\t" + headline)
    print(60 * "─")


##################################################################
### Usage of program: X players, each tossing the coin Y times ###
##################################################################

number_of_players = 1_000_000
number_of_tosses = 20
start_time = time.time()  # Start of time measurement
player_list = play_with_multiple_players(number_of_players, number_of_tosses)  # insert variables

# Display individual results for each player
# divider("Results by player")
# for player in player_list:
#     player.display_results()

divider(f"Total Result {light_blue}with {number_of_tosses} tosses{reset_color}")
total_score(player_list, start_time, number_of_tosses)  # show total Score

# FIXME: Caution Runtime on Macbook Air M1:
#  1M Players, 20 tosses: 7 sec
#  10M Players, 20 tosses: 2 min
#  85M Players, 20 tosses: 30 min
