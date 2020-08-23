from typing import List

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# TIME: O(n)
# SPACE: O(1)

class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        dummy = ListNode(0)
        dummy.next= head
        
        slow = dummy
        fast = dummy
        
        for i in range(n+1):
            fast = fast.next
            
        while fast is not None:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return dummy.next

    def removeNthFromEnd_dirty(self, head: ListNode, n: int) -> ListNode:
              
        # firstly calculate length
        len_list = 0
        current = head
        while current is not None:
            len_list +=1
            current = current.next
        
        # in case where we have lenght = 1
        if len_list == 1:
            head = None
            return head
        
        # calculate position to delete
        current_ind = 0
        prev = current = head
        while len_list - n != current_ind:
            prev = current
            current = current.next
            current_ind +=1
            
            
        if current.next is None: 
            # in case where we need to del last value
            prev.next = None
        else:
            current.val = current.next.val
            current.next = current.next.next
        
       
        return head
    
    
    def removeNthFromEnd_clean(self, head: ListNode, n: int) -> ListNode:
             
        dummy = ListNode(0)
        dummy.next = head
        
        #calculate lenght
        
        len_ll = 0
        current = head
        while current is not None:
            current = current.next
            len_ll += 1
            
        pos = len_ll - n
        node_to_delete = dummy
        while pos > 0:
            node_to_delete = node_to_delete.next
            pos -=1
            
        node_to_delete.next = node_to_delete.next.next
        return dummy.next
        
    
