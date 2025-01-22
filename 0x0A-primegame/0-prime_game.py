#!/usr/bin/python3
"""
A script that determines the winner of each round of a game of prime numbers.
"""


def isWinner(x, nums):
    """
    Determines the winner of each game round based on optimal play.

    Args:
        x (int): No of rounds.
        nums (list of int): Where each element repr highest no in a round.

    Returns:
        str: "Maria" if Maria wins, "Ben" if Ben wins, or None if it's a tie.
    """
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = [0] * (max_n + 1)
    # Sieve of Eratosthenes to count primes up to max_n
    for i in range(2, max_n + 1):
        if primes[i] == 0:
            for multiple in range(i, max_n + 1, i):
                primes[multiple] += 1

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if primes[2:n+1].count(1) % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Return the player with the most wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
