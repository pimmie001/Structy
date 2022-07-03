def pair_sum(numbers, target_sum):
    # time O(n^2), space O(1)

    for i in range(len(numbers)):
        n = numbers[i]
        for j in range(i+1, len(numbers)):
            m = numbers[j]
            if n + m == target_sum:
                return (i,j)


def pair_sum(numbers, target_sum):
    # time O(n), space O(n)

    memo = {}
    for i in range(len(numbers)):
        number = numbers[i]
        complement = target_sum - number

        if complement in memo: # hashmap has O(1) lookup
            return (memo[complement], i)
        
        memo[number] = i

