# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
We can do BFS or DFS and before processing the children, flip them on the current parent node.
'''

# DFS Recursive

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs(root)
        return root
        
    def dfs(self, node):
        
        if not node:
            return
        
        node.left, node.right = node.right, node.left
        
        self.dfs(node.left)
        self.dfs(node.right)
        
# DFS Iterative
'''
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = deque()
        stack.append(root)
        
        while stack:
            node = stack.pop()
            
            if not node:
                continue
                
            node.left, node.right = node.right, node.left
            
            stack.append(node.left)
            stack.append(node.right)
        
        return root
'''
        
        
        
        
