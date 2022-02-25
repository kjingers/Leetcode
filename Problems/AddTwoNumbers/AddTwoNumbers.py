# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
Pretty much like adding normal numbers (ones place first). For example, add the two digits. Place
a node with the right digit and carry the left digit.

Note, when loop ends, if we still have a carry, we must add one additional node
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        currNode = dummy
        carry = 0
        
        while l1 or l2:
            
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
                
            currNode.next = ListNode(carry % 10)
            currNode = currNode.next
            carry //= 10
           
        if carry == 1:
            currNode.next = ListNode(carry)
            
        return dummy.next
        
