def befitting_brackets(string):
    braces = {'(':')', '[':']', '{':'}'}
    stack = []

    for item in string:
        if item in braces:
            stack.append(item)
        elif item in braces.values():
            if not stack or braces[stack.pop()] != item:
                return False

    return len(stack) == 0
