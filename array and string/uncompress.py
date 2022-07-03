def uncompress(s):
    result = ''

    i = 0
    numeric = False
    for i in range(len(s)):
        item = s[i]
        
        if item.isnumeric():
            if not numeric:
                start = i
                numeric = True

        else:
            end = i
            number = int(s[start:end])
            result += item * number
            numeric = False

    return result

