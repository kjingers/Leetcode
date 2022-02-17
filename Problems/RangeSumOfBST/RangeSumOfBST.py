# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Can just do DFS / BFS. At each node, add if value is in range.
'''


# Recursive DFS
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.dfs(root, low, high)
        
        
    def dfs(self, node, low, high):
        
        # Base Case
        if not node:
            return 0
        
        sum = 0
        
        if low <= node.val <= high:
            sum += node.val
            
        sum += self.dfs(node.left, low, high) + self.dfs(node.right, low, high)
        
        return sum
        

    
# Iterative DFS
'''
from collections import deque

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        stack = deque([root])
        rangeSum = 0
        
        while stack:
            node = stack.pop()
            
            if node is None:
                continue
            
            if low <= node.val <= high:
                rangeSum += node.val
                
            stack.append(node.left)
            stack.append(node.right)
        
        return rangeSum
'''                
            
                
        
        
        
        
        
        
        
        
        
        
        
