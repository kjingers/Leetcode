# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Intuition: As we traverse through the list, keep a reference to the most recent node with a different value. Keep iterating until 
'''

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        dummy = ListNode(-101)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr:
            
            # If next val == curr val. Loop to get next node with diff val
            if curr.next and curr.val == curr.next.val:
                
                # Point curr to last node with duplicate value
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                   
                # Connect prev (diff val) to next (diff val)
                prev.next = curr.next
            else: # Adjust prev to point to the new previous different val node
                prev = prev.next
            
            # Always iterate curr
            curr = curr.next
            
        return dummy.next
                    
        
        
        
        
            
            
            
            
        
