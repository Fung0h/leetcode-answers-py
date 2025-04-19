def twoSum(target, nums):
    for i in range (len(nums)):
        for j in range (len(nums)):
            if(nums[i] + nums[j] == target and i != j):
                return [i ,j]

result = twoSum(6, [3, 3])
print(result)