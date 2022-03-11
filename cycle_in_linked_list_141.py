# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        ptr = head
        visited_set = set()

        while ptr:
            if ptr not in visited_set:
                visited_set.add(ptr)
            ptr = ptr.next
            if ptr in visited_set:
                return True

        return False
