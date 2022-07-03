def pair_product(numbers, target_sum):
    for i in range(len(numbers)):
        n = numbers[i]
        for j in range(i + 1, len(numbers)):
            m = numbers[j]
            if n * m == target_sum:
                return (i,j)
