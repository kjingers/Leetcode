# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
Get Length of Linked List.
Then skip len - n nodes
Remove the next node


'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Get length
        
        curr = head
        length = 0
        
        # Get length of Linked List
        while curr:
            curr = curr.next
            length += 1
         
        curr = head
        prev = None
        
        # Skip (length - n) nodes
        # After loop, curr will be node to remove
        for _ in range(length - n):
            prev = curr
            curr = curr.next
            
        # If prev is still None, then we need to remove head
        if not prev:
            newHead = head.next
            head.next = None
            return newHead
        else:
            prev.next = curr.next
            curr.next = None
            return head
            
            
            
        
