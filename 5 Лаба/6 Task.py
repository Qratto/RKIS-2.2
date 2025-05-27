nums = [2,-1,3,10,-9,5,-6,-11]
for i in range(len(nums)):
    if nums[i] > 0:
        nums[i] = -nums[i]
    else:
        nums[i] = abs(nums[i])

print(nums)