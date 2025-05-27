def calculations(nums):

    addition_sum = 0
    multiplication_sum = 1
    max_num_index = nums.index(max(nums))
    min_num_index = nums.index(min(nums))


    for i in nums:
        if i > 0:
            addition_sum += i

    if max_num_index > min_num_index:
        for i in range(min_num_index+1, max_num_index):
            multiplication_sum *= nums[i]
    else:
        for i in range(max_num_index+1, min_num_index):
            multiplication_sum *= nums[i]
    return addition_sum, multiplication_sum
    
nums = [2,4,-1,12,3,34]
    
print(calculations(nums))

