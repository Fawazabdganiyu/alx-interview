#!/usr/bin/python3
"""Prime game challenge"""


def isWinner(x, nums):
    """Determine the winner of the game

    Maria and Ben are playing a game. Given a set of consecutive integers
    starting from 1 up to and including n, they take turns choosing a
    prime number from the set and removing that number and its
    multiples from the set. The player that cannot make
    a move loses the game.

    Args:
        x (int): A number of rounds of the game
        nums (list[int]): An Array of integers that determine the max number
                          of prime that can be selected with its multiples

    Returns:
        string: The name of the winner between Maria and Ben
    """
    if not x or not nums or x != len(nums):
        return None

    def getPrimes(n):
        """Return the numbers of prime number between 1 and n inclusive
        """
        # Initialise all the nums element to True to denote all are prime
        nums = [True for _ in range(n+1)]
        # Set the first prime number and prime numbers list
        p = 2
        p_list = []
        # Update where square of p is greater than n and
        # also multiples of p to false
        while (p * p <= n):
            if nums[p]:
                p_list.append(p)
                for i in range(p * p, n+1, p):
                    nums[i] = False
            p += 1

        return nums

    # Go through each round
    maria_score = 0
    ben_score = 0
    primes_list = getPrimes(max(nums))
    for n in nums:
        # Get the numbers of prime numbers between 1 and n inclusive
        # dynamically
        primes = len([i for i in range(2, len(primes_list))
                      if i <= n and primes_list[i]])
        if primes % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    # Decide the winner
    if maria_score != ben_score:
        if maria_score > ben_score:
            return 'Maria'
        else:
            return 'Ben'

    return None
