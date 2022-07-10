def positioning_plants(costs, i=0, prev_plant = -1, memo={}):
    if i == len(costs):
        return 0

    if (i, prev_plant) in memo:
        return memo[(i, prev_plant)]

    minimum = float('inf')
    for j in range(len(costs[0])):
        cost = float('inf') if j == prev_plant else costs[i][j] + positioning_plants(costs, i+1, j, memo) # cost if plant j on position i
        minimum = min(minimum, cost)

    memo[(i, prev_plant)] = minimum
    return minimum
