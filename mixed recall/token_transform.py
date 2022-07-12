def token_transform(string, tokens):
    all_good = False
    while not all_good:
        all_good = True
        for key in tokens:
            if '$' in tokens[key]:
                tokens[key] = token_replace(tokens[key], tokens)
                all_good = False

    return token_replace(string, tokens)


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



def token_transform(s, tokens):
    # faster solution using recursion
    output = []
    i = 0
    j = 1
    while i < len(s):
        if s[i] != '$':
            output += s[i]
            i += 1
            j = i + 1
        elif s[j] != '$':
            j += 1
        else:
            key = s[i:j+1]
            value = tokens[key]
            evaluated_value = token_transform(value, tokens)
            tokens[key] = evaluated_value 
            output.append(evaluated_value)
            i = j + 1
            j = i + 1
    
    return ''.join(output)

