def sum_possible(amount, numbers, memo={}):
    if amount == 0:
        return True

    if amount < 0:
        return False

    if amount in memo:
        return memo[amount]


    is_possible = False
    for number in numbers:
        if sum_possible(amount-number, numbers, memo):
            is_possible = True
            break
    
    memo[amount] = is_possible
    return is_possible

