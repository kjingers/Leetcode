# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
Looks like "K Way Merge pattern". Push a tuple with a counter onto heap, so that it never has to resort to
Listnode object which does not have __lt__ defined.

Time Complexity: O(n*log(2))
Space: O(2)
'''

import heapq

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 or not list2:
            return list2 if list2 else list1
        
    
        minHeap = []
        
        heappush(minHeap, (list1.val, 0, list1))
        heappush(minHeap, (list2.val, 1, list2))
        
        cnt = 2
        
        dummy = ListNode(0)
        curr = dummy
        
        while minHeap:
            
            val, _, node = heappop(minHeap)
            
            curr.next = node
            curr = curr.next
            
            # If there is a next node from list, push it to heap
            if node.next:
                heappush(minHeap, (node.next.val, cnt, node.next))
                cnt += 1
                
        return dummy.next





'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 or not list2:
            return list2 if list2 else list1
        
    
        minHeap = []
        
        heappush(minHeap, (list1.val, 0, list1))
        heappush(minHeap, (list2.val, 1, list2))
        
        cnt = 2
        
        head = None
        curr = None
        
        while minHeap:
            val, _, node = heappop(minHeap)
            
            if not head:
                head = node
                curr = head
            else:
                curr.next = node
                curr = curr.next
            
            if node.next:
                heappush(minHeap, (node.next.val, cnt, node.next))
                cnt += 1
                
            
                
        return head
'''
                
                
       
