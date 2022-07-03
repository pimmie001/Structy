def five_sort(nums):
    # bubble sort O(n^2)

    sorted = False
    while not sorted:
        sorted = True

        is_five = False
        for i in range(len(nums)):
            item = nums[i]

            if item == 5:
                is_five = True
            
            elif is_five:
                sorted = False
                nums[i-1], nums[i] = nums[i], nums[i-1]


    return nums



def five_sort(nums):
    # O(n)

    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[j] == 5:
            j -= 1
        elif nums[i] == 5:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        else: i += 1
    return nums
