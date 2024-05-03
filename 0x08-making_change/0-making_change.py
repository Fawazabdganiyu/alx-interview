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
    i = 0
    num_coins = 0
    while i < len(coins) and total > 0:
        if coins[i] <= total:
            total -= coins[i]
            num_coins += 1
        else:
            i += 1

    if total != 0:
        return -1

    return num_coins
