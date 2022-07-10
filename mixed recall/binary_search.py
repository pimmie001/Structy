def binary_search(numbers, target):
    n = len(numbers)

    L = 0
    R = n-1

    while L <= R:
        m = (L+R)//2
        if numbers[m] == target:
            return m
        elif numbers[m] < target:
            L = m+1
        elif numbers[m] > target:
            R = m-1

    return -1