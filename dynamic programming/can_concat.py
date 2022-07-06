def can_concat(s, words, memo={}):
    if s == '':
        return True

    if s in memo:
        return memo[s]

    for word in words:
        n = len(word)
        if len(s) >= n and s[:n] == word:
            if can_concat(s[n:], words, memo):
                memo[s] = True
                return True

    memo[s] = False
    return False
