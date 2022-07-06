def quickest_concat(s, words):
    length = _quickest_concat(s, words)
    return -1 if length == float("inf") else length


def _quickest_concat(s, words, memo={}):
    if s == '':
        return 0
    if s in memo:
        return memo[s]

    minimum = float("inf")
    for word in words:
        n = len(word)
        if len(s) >= n and s[:n] == word:
            minimum = min(minimum, 1 +_quickest_concat(s[n:], words, memo))
    
    memo[s] = minimum
    return minimum
