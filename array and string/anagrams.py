def anagrams(s1, s2):
    return make_dict(s1) == make_dict(s2)


def make_dict(s):
    d = {}

    for item in s:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1

    return d
