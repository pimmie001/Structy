def max_palin_subsequence(string, memo={}):
    if len(string) < 2:
        return len(string)

    if string in memo:
        return memo[string]


    if string[0] == string[-1]:
        result = 2 + max_palin_subsequence(string[1:-1], memo)
    else:
        result = max(max_palin_subsequence(string[1:], memo), max_palin_subsequence(string[:-1], memo))

    memo[string] = result
    return result
