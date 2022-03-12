"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

'''
Thinking - similar to copy graph. Have a dictionary where dict[inlit] = copied node.

Loop Twice. Once to create all the copied nodes. Next to assign next and random pointers.

Can loop once with defaultdict. This lets us create the next and random nodes
'''



from collections import defaultdict

# One pass solution using defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return None
        
        map_new = defaultdict(lambda: Node(0))
        
        # If a next or random pointer is None, we don't want to create a new node
        map_new[None] = None
        
        curr = head
        
        while curr:
            map_new[curr].val = curr.val
            map_new[curr].next = map_new[curr.next] # Creates node if doesn't exist
            map_new[curr].random = map_new[curr.random] # Creates node if doesn't exist
            
            curr = curr.next
            
        return map_new[head]
           
    
    
'''
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return None
        
        d = {}
        
        curr = head
        
        # Loop once to create nodes
        while curr:
            d[curr] = Node(curr.val)
            curr = curr.next
            
        curr = head
        
        # Loop again to assign next and random
        while curr.next:
            d[curr].next = d[curr.next]
            if curr.random:
                d[curr].random = d[curr.random]
            curr = curr.next
            
        if curr.random:
            d[curr].random = d[curr.random]
        
            
        return d[head]
'''
        
        
        
        
