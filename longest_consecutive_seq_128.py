def longestConsecutive( nums) -> int:
    longestSeq = 0
    numsSet = set(nums)
    for i, item in enumerate(nums):
        if item-1 not in numsSet:
            index = 0
            while nums[i]+index in nums:
                index +=1
            longestSeq = max(longestSeq, index)
    return longestSeq
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))