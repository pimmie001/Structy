def non_adjacent_sum(nums):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]


    n = len(nums)//2 # index of the middle number
    left = nums[:n]
    mid = nums[n]
    right = nums[n+1:]

    return max(non_adjacent_sum(left) + non_adjacent_sum(right), non_adjacent_sum(left[:-1]) + mid + non_adjacent_sum(right[1:]))
    # return max('do not include the middle', 'include the middle')

