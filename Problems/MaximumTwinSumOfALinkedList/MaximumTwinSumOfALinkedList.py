# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Example:
n = 4
i = 0: (4 - 1 - 0) = 3
i = 1: (4 - 1 - 1) = 2

Fast and slow to get middle of linked list.
Reverse second half of linked list. 
Then, traverse through each list and add nodes.
'''
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow = head
        fast = head
        #   0 -> 1 -> 2 -> 3
        #             ^
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # head:                 0 -> 1 (1 will still point to 2)
        # head_second_half:     3 -> 2
        head_second_half = self.reverse(slow)
        
        head_first_half = head
        
        max_pair_sum = 0
        while head_second_half:
            max_pair_sum = max(max_pair_sum, head_first_half.val + head_second_half.val)
            head_first_half = head_first_half.next
            head_second_half = head_second_half.next
            
        return max_pair_sum
            

    # Reverse Linked List in place
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next     
        return prev
        
