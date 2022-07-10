def max_increasing_subseq(numbers, memo={}):
    key = tuple(numbers)
    if key in memo:
        return memo[key]

    n = len(numbers)
    if n < 2:
        return n


    # option 1: remove the first number
    option1 = max_increasing_subseq(numbers[1:], memo)

    # option 2: keep the first number
    remaining_numbers = list(filter(lambda x: x > numbers[0], numbers))
    option2 = 1 + max_increasing_subseq(remaining_numbers, memo)


    result = max(option1, option2)
    memo[key] = result
    return result

