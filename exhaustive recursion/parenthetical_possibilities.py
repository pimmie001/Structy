def parenthetical_possibilities(string):
    if not '(' in string:
        return [string]


    for i in range(len(string)):
        item = string[i]
        if item == '(':
            start = i
        elif item == ')':
            end = i
            break

    results = []
    for letter in string[start+1:end]:
        new_string = string[:start] + letter + string[end+1:]
        sub_result = parenthetical_possibilities(new_string)
        results.extend(sub_result)

    return results