#!/usr/bin/python3
""" Make change module """


def makeChange(coins, total):
    """Determine the fewest number of coins needed to make a change

    Args:
        coins(list): A list of the values of the coins
        total(int): The total amount of change needed

    Returns:
        int: The minimum number of coins needed to make the change
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    coins_needed = 0
    for coin in coins:
        if total == 0:
            break
        coins_needed += total // coin
        total %= coin

    return coins_needed if total == 0 else -1
