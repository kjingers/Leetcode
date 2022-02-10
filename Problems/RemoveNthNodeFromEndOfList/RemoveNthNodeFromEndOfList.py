# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
1. Iterate though the list to get the length of the list
2. Calculate len - n to get how many nodes we have to skip
3. Remove node

Time Complexity: O(n)
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
