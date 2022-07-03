def most_frequent_char(s):
    d = make_dict(s)

    most_frequent_letter = ''
    most_frequent_count = 0
    for item in d:
        if d[item] > most_frequent_count:
            most_frequent_letter = item
            most_frequent_count = d[item]

    return most_frequent_letter



def make_dict(s):
    d = {}

    for item in s:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1

    return d
