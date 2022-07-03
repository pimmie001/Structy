def compress(s):
    result = ''


    current = s[0]
    count = 1
    for item in s[1:]+'0':
        if item is current:
            count += 1
            continue
        
        if count == 1:
            result += current
        else:
            result += str(count) + current

        count = 1
        current = item


    return result

