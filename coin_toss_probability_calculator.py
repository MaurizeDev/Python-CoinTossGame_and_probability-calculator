import decimal

# Set the precision for Decimal to 110 digits (over 100 digits to also cover intermediate steps)
decimal.getcontext().prec = 110


def prob_only_heads(players, tosses):
    """
    Calculates the probability that at least one player will only toss heads.

    Args:
        players (int): The number of players participating in the coin tosses.
        tosses (int): The number of coin tosses each player performs.

    Returns:
        Decimal: The probability that at least one player tossed only heads.
    """
    # Use decimal.Decimal for high precision
    players_dec = decimal.Decimal(players)
    base = decimal.Decimal(0.5)
    tosses_dec = decimal.Decimal(tosses)

    # Perform logarithmic and exponential operations with Decimal
    probability_per_player = base ** tosses_dec
    logarithm_value = (1 - probability_per_player).ln()  # ln is the natural logarithm in decimal
    return 1 - (logarithm_value * players_dec).exp()  # exp is the exponential function in decimal


players = 300_000_000

# ANSI escape code for light blue
light_blue = '\033[94m'
reset_color = '\033[0m'  # Reset color to the default

print("Probability that a player tosses only heads:")
# Loop through the number of tosses from 18 to 40:
# To show where the probability of one player only tossing heads begins declining from nearly 100% to lower levels
for tosses in range(18, 40):
    probability = prob_only_heads(players, tosses)
    # Output as a percentage with 100 decimal places and thousands separators
    print(
        f"{light_blue}{players:,}{reset_color} players and {light_blue}{tosses}{reset_color} tosses: {probability * 100:.100f} %"
    )

print(".....")

# Loop through the number of tosses from 361 to 368:
# To show where the probability of one player only tossing heads begins heading zero (it never reaches zero). We calculate 100 decimal
# placements and with toss 367 we reach 0% probability and can not calculate further
for tosses in range(361, 368):
    probability = prob_only_heads(players, tosses)
    # Output as a percentage with 100 decimal places and thousands separators
    print(
        f"{light_blue}{players:,}{reset_color} players and {light_blue}{tosses}{reset_color} tosses: {probability * 100:.100f} %"
    )
