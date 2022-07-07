def overlap_subsequence(string_1, string_2, memo={}):
    if len(string_1) == 0 or len(string_2) == 0:
        return 0

    if (string_1, string_2) in memo:
        return memo[(string_1, string_2)]
    

    if string_1[0] == string_2[0]:
        result = 1 + overlap_subsequence(string_1[1:], string_2[1:], memo)
    else:
        result = max(overlap_subsequence(string_1[1:], string_2, memo), overlap_subsequence(string_1, string_2[1:], memo))
        
    memo[(string_1, string_2)] = result   
    return result