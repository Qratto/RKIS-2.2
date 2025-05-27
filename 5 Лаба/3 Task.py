import random

count = 0
nums = []

while count != 10: 
    random_num = random.randint(1,100)
    if random_num % 2 == 0:
        nums.append(random_num)
        count += 1

nums.sort()
print(nums)