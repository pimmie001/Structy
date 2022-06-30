def non_adjacent_sum(nums):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    if len(nums) == 2:
        return max(nums[0], nums[1])
    

    n = len(nums)//2 # index of middle 
    left = nums[:n]
    mid = nums[n]
    right = nums[n+1:]

    return max(non_adjacent_sum(left) + non_adjacent_sum(right), non_adjacent_sum(left[:-1]) + mid + non_adjacent_sum(right[1:]))
    # return max('do not use the middle', 'use the middle')

