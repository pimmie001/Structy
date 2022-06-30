def array_stepper(numbers, ind=0, memo={}):
    if ind == len(numbers) - 1:
        return True
    
    if ind in memo:
        return memo[ind]


    for i in range(numbers[ind]):
        if array_stepper(numbers, ind+i+1, memo):
            memo[ind] = True
            return True


    memo[ind] = False
    return False

