def nesting_score(string):
    stack = [0]
    for i in range(len(string)):
        item = string[i]

        if item == '[':
            stack.append(0)
        
        elif item == ']':
            current = stack.pop()
            if current == 0:
                stack[-1] += 1
            else:
                stack[-1] += 2*current

    return stack[0]
