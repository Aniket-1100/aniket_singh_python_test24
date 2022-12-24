def findPair(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print('Pair found', (nums[i], nums[j]))
                return
    print('Pair not found')
    
nums = [1,5,7,-1]
target = 6
findPair(nums, target)