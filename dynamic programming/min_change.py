def min_change(amount, coins):
    number_coins = _min_change(amount, coins)
    return -1 if number_coins == float("inf") else number_coins


def _min_change(amount, coins, memo={}):
    if amount == 0:
        return 0

    if amount < 0:
        return float("inf")

    if amount in memo:
        return memo[amount]


    minimum = float("inf")
    for coin in coins:
        minimum = min(minimum, 1 + _min_change(amount-coin, coins, memo))
    
    memo[amount] = minimum
    return minimum

