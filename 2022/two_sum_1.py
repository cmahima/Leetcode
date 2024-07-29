def twoSum(nums,target: int):
    numsDict = {}

    for i,item in enumerate(nums):
        diff = target - item
        if diff in numsDict:
            return [i, numsDict[diff]]
        numsDict[item] = i

print(twoSum(nums = [2,7,11,15], target = 9))