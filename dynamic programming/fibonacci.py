def fib(n):
    if n < 2:
        return n

    lst = [0, 1]
    for i in range(n-1):
        lst.append(lst[-1]+lst[-2])
    return lst[-1]

