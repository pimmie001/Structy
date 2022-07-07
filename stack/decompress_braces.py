def decompress_braces(string):
    result = ''

    for i in range(len(string)):
        item = string[i]

        if item.isnumeric():
            n = int(item)
        elif item == '{':
            part1, part2 = remove_braces(string[i:])
            return result + decompress_braces(part1)*n + decompress_braces(part2)
        else:
            result += item

    return result


def remove_braces(string):
    # example: {abc{d}e}f  --> abc{d}e, f
    count = 0
    for i in range(len(string)):
        item = string[i]
        if item == '{':
            count += 1
        elif item == '}':
            count -= 1
            if count == 0:
                return string[1:i], string[i+1:]

