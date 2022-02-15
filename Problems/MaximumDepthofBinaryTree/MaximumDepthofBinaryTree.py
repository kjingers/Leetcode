# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
We can use DFS or BFS.

For the iterative approaches, we need to push both the node and the level.


'''

# DFS Recursive

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
        
        
    def dfs(self, node):
        
        # Base case
        if not node:
            return 0
        
        return 1 + max(self.dfs(node.left), self.dfs(node.right))

    
# DFS Iterative
'''
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = deque()
        stack.append((root, 0))
        maxLevel = 0
        
        while stack:
            node, level = stack.pop()
            
            if node is None:
                maxLevel = max(maxLevel, level)
                continue
            
            stack.append((node.left, level + 1))
            stack.append((node.right, level + 1))
        
        return maxLevel
'''
    
# BFS Iterative
'''
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque()
        queue.append((root, 0))
        maxLevel = 0
        
        while queue:
            node, level = queue.popleft()
            
            if node is None:
                maxLevel = max(maxLevel, level)
                continue
            
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        
        return maxLevel
'''
                
