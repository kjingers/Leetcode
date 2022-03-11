# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
First, need to get length of linked list. Then traverse length - k spots. Make that node.next = None. Go to next node. Traverse until end. Make last node.next = head. Return node at length - k + 1 as head.
'''
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        curr = head
        length = 0
        
        while curr is not None:
            curr = curr.next
            length += 1
        
        k = k % length
        
        if k == 0:
            return head
        
        curr = head
        # Traverse to new tail node
        for _ in range(length - k - 1):
            curr = curr.next
        
        # Make new tail node have no next
        newTail = curr
        curr = newTail.next
        newTail.next = None
        newHead = curr
        
        # Traverse to last node. Make it's next node the previous head
        for _ in range(k - 1):
            curr = curr.next
            
        curr.next = head
        
        return newHead
            
            
        
        
