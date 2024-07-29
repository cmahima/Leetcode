def search( nums, target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = int((left + right) / 2)
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            minEle = min(nums[left:mid + 1])
            if target == nums[mid]:
                return mid
            if minEle > target:
                left = mid + 1
            elif minEle < target:
                right = mid - 1
            else:
                return left
        elif target > nums[mid]:
            maxEle = max(nums[mid:right+1])
            if maxEle > target:
                left = mid + 1
            elif maxEle < target:
                right = mid -1
            else:
                    return right



    return -1

print(search(nums = [5,1,3], target = 3))