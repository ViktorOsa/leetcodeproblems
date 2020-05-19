from typing import List
import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# TIME O(nlogk) # n - number of elements, k - number of LL
# SPACE O(1)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
         
        # we will use heapq - min heap with 3 values
        min_heap = []
        
        result = ListNode()
        head = result
        
        # firstly push all start values to min heap
        counter = 0
        for listi in lists:
            if listi:
                heapq.heappush(min_heap, (listi.val,counter, listi))
                counter += 1
            
        
        while len(min_heap) != 0:
            min_value, _, list_ = heapq.heappop(min_heap)
            
            result.next = list_
            list_ = list_.next
            if list_:
                heapq.heappush(min_heap, (list_.val, counter, list_))
                counter += 1
            result = result.next
      
        return head.next