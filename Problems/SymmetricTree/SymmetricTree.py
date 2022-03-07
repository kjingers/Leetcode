# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
We need a function that takes two nodes (a left and a right) and reeturns true if the nodes are a mirror of each other.

At each node, we call isMirror for the inner nodes, and again for the outer nodes.


'''

# Recursive DFS-Like

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, left, right):
        
        # If both are None
        if left is None and right is None:
            return True
        
        # If only one is None
        if left is None or right is None:
            return False
        
    
        if left.val != right.val:
            return False
        
        
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        

'''    
# Iterative DFS
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        stack = deque([(root.left, root.right)])
        
        while stack:
            
            left, right = stack.pop()
            
            if left is None and right is None:
                continue
                
            if left is None or right is None:
                return False
            
            if left.val != right.val:
                return False
            
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
            
        return True
        
'''
        
        
