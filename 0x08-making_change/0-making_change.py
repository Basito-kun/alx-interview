#!/usr/bin/python3
"""
A script that determine the fewest no of coins
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): A list of integers representing the values of the coins.
        total (int): The total amount to meet.

    Returns:
        int: The min no of coins needed to meet total, or -1 if not possible.
    """
    if total <= 0:
        return 0

    # Initialize a large value representing an impossible case
    dplist = [float('inf')] * (total + 1)
    dplist[0] = 0  # Base case: 0 coins are needed to make a total of 0

    # Build the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dplist[amount] = min(dplist[amount], dplist[amount - coin] + 1)

    # If dp[total] is still 'inf', it means it's not possible to make the total
    return dplist[total] if dplist[total] != float('inf') else -1
