def create_combinations(items, k):
    if k == 0:
        return [[]]
    if k == 1:
        return [[x] for x in items]


    new_combinations = []
    for i in range(len(items)):
        item = items[i]
        new_list = items[i+1:]

        other_combinations = create_combinations(new_list, k-1)
        for lst in other_combinations:
            lst.append(item)
            new_combinations.append(lst)

    return new_combinations
