from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TIME O(n)
# SPACE O(1)
class Solution:
    def reorderList_dirty(self, head: ListNode) -> None:
        if head is None or head.next is None:
            return

        # STEP 1 look for a middle
        tail = slow = fast = head
        while fast and fast.next:
            tail = slow
            slow = slow.next
            fast = fast.next.next
       
        # we have now: slow 3->4->None
    
        # make 1 - > 2 -> None
        tail.next = None
        
        # step 2: reverse slow
        prev = None
        current = slow
        while current:
            nxt_tmp = current.next
            current.next = prev
            prev = current
            current = nxt_tmp
            
        # we have head 1->2->None and slow 4->3->None
        
        # STEP 3 MERGE THEM: first and prev
        first = head
        while first:
            f_n = first.next
            s_n = prev.next
            
            first.next = prev
            
            if (f_n is None):
                break
            
            prev.next = f_n

            first = f_n
            prev  = s_n
    
        
        """ another solution
        result = ListNode()
        l1 = head
        l2 = prev
        while l1 and l2 :
            
            result.next = l1
            l1 = l1.next
            result = result.next
            result.next = l2
            l2 = l2.next
            result = result.next
        
        result.next = l1 or l2
        
        head = result.next
        """
        
class Solution2:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return 
        
        # find the middle of linked list [Problem 876]
        # in 1->2->3->4->5->6 find 4 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
        # reverse the second part of the list [Problem 206]
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next       

        # merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next