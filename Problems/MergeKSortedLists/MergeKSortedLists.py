# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
K Way Merge
'''

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        cnt = 0
        minHeap = []
        
        for node in lists:
            if node:
                heappush(minHeap, (node.val, cnt, node))
                cnt += 1
                #lists[i] = lists[i].next
                
        dummy = ListNode(0)
        curr = dummy
        
        while minHeap:
            
            val, _, node = heappop(minHeap)
            
            curr.next = node
            curr = curr.next
            
            if node.next:
                heappush(minHeap, (node.next.val, cnt, node.next))
                cnt += 1
        
        return dummy.next
            
 
        
