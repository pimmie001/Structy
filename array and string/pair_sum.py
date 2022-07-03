def pair_sum(numbers, target_sum):
    for i in range(len(numbers)):
        n = numbers[i]
        for j in range(len(numbers)):
            if i == j:
                continue

            m = numbers[j]
            if n + m == target_sum:
                return (i,j)
