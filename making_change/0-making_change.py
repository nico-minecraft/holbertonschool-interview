#!/usr/bin/python3
"""Making change: fewest coins needed to reach a total."""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet total.

    Returns 0 if total is 0 or less, and -1 if total cannot be met
    by any combination of the given coins.
    """
    if total <= 0:
        return 0

    usable = sorted({c for c in coins if 0 < c <= total})
    if not usable:
        return -1

    # best[i] is the fewest coins needed to make amount i
    unreachable = total + 1
    best = [0] + [unreachable] * total

    for amount in range(1, total + 1):
        for coin in usable:
            if coin > amount:
                break
            candidate = best[amount - coin] + 1
            if candidate < best[amount]:
                best[amount] = candidate

    return best[total] if best[total] != unreachable else -1
