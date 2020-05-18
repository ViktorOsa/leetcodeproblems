from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TIME : O(m + n)
#SPACE O(1) !!! result is a POINTER
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        result = ListNode()
        head = result
        
        while l1 and l2 :
            
            if l1.val <= l2.val:
                result.next = l1
                l1 = l1.next
            else:
                result.next = l2
                l2 = l2.next
            
            result = result.next
        
        result.next = l1 or l2
        
        return head.next