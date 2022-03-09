def searchInsert( nums: [int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    while (start <= end):
        mid = (start + end) // 2

        if target == nums[mid]:
            return mid

        elif target < nums[mid]:
            end = mid - 1

        elif target > nums[mid]:
            start = mid + 1

    if target < nums[mid]:
        return end
    else:
        return start
print(searchInsert( nums =
[1,3,5,6], target = 2))