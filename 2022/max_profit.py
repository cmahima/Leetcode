from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m, mp = float('inf'), 0
        for p in prices:
            if p < m:
                m = p
            if p - m > mp:
                mp = p - m
        return mp

print(Solution().maxProfit([7,1,5,3,6,4]))

