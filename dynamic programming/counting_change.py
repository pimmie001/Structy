def counting_change(amount, coins):
    sorted_coins = coins.copy()
    sorted_coins.sort()
    return _counting_change(amount, sorted_coins)


def _counting_change(amount, coins, ind=0, memo={}):
    # only works if the coins are sorted

    if amount == 0:
        return 1

    if ind == len(coins):
        return 0

    if (amount, ind) in memo:
        return memo[(amount, ind)]


    total = 0
    coin = coins[ind]
    for n in range(amount//coin + 1):
        total += _counting_change(amount - n*coin, coins, ind+1, memo)

    memo[(amount, ind)] = total
    return total
