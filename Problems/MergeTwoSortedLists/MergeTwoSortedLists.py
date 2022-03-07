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
K-Way merge pattern. Since we only have two linked lists, we can just check the current val for each list, then take the smaller value, and move to the next node in that list.
'''
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        dummy = ListNode(0)
        curr = dummy
        
        while list1 and list2:
            
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
                
            curr = curr.next
        
        if list1:
            curr.next = list1
            list1 = list1.next
            
        if list2:
            curr.next = list2
            list2 = list2.next
        
        return dummy.next
'''
                
                
       
