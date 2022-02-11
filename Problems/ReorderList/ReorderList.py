# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
1. Can use fast and slow pointer so that slow points to middle node (or right middle if even length)
2. Reverse second half of linked list (from slow to end)
3. Interleave them together
4. Make sure to prevent infinite loop case
'''



class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def printList(head):
            copy = head
            while copy is not None:
                print(copy.val, end=" -> ")
                copy = copy.next
            print("None")
            return
        
        slow, fast = head, head
        
        # Fast and Slow pointers so slow points to middle element
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reverses list
        sec_half_head = self.reverse_list(slow)
        first_half_head = head
        
        #printList(first_half_head)
        #printList(sec_half_head)
        
        # Interlave the First and Second Half Lists
        while first_half_head and sec_half_head:
            
            # Connect First half node to Sec Half node
            temp = first_half_head.next
            first_half_head.next = sec_half_head
            first_half_head = temp
            
            # Connect Second half node to next first half
            temp = sec_half_head.next
            sec_half_head.next = first_half_head
            sec_half_head = temp
            
        # In the Even case, the last node will point to itself, creating infinite loop
        if first_half_head:
            first_half_head.next = None
            
        return head
    
    def reverse_list(self, head):
        
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
            
