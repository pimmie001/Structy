def permutations(items, k=None):
    if k is None:
        k = len(items)

    if k == 0:
        return [[]]


    new_combinations = []
    for i in range(len(items)):
        item = items[i]
        new_list = items[:i] + items[i+1:]

        other_combinations = permutations(new_list, k-1)
        for lst in other_combinations:
            lst.append(item)
            new_combinations.append(lst)

    return new_combinations

