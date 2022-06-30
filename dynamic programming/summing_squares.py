def summing_squares(n, memo={}):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n in memo:
        return memo[n]


    minimum = float("inf")
    for i in range(1, int(n**0.5) + 1):
        minimum = min(minimum, 1 + summing_squares(n - i**2, memo))

    memo[n] = minimum
    return minimum
