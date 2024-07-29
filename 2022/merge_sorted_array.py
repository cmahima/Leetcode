from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    k = 0
    end_ind = m
    for i in range(n):
        number = nums2[i]
        while k <end_ind and number >= nums1[k] and end_ind<m+n:
            k += 1
        for j in range(len(nums1) - 1, k, -1):
            nums1[j] = nums1[j - 1]
        end_ind = end_ind + 1
        nums1[k] = number
    print(nums1)


merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
