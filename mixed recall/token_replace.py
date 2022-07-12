def token_replace(string, tokens):
    result = ''
    dollar_found = False

    for i in range(len(string)):
        char = string[i]

        if char == '$':
            if dollar_found:
                result += tokens[string[start:i+1]]
            else:
                start = i
            dollar_found = not dollar_found

        elif not dollar_found:
            result += char

    return result
