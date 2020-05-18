from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList_iterative(self, head: ListNode) -> ListNode:
        
        
        prev = None
        current = head
        while current is not None:
            next_tmp = current.next
            
            current.next = prev
            prev = current
            
            current = next_tmp
            
        return prev
# 
# TIME : O(n)
# SPACE: O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        prev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
            
        return prev
# TIME : O(n)
# SPACE: O(n) - call stack