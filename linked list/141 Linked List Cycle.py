from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# TIME  O(n)
# SPACE O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if head == None or head.next == None:
            return False
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            if (fast.next == slow):
                return True
            
            slow = slow.next
            fast = fast.next.next
               
               
        
        return False