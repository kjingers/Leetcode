# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
As we iterate, keep track of range of valid values and make sure each node falls in range
'''
import math

# Iterative BFS approach
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        minVal = -math.inf
        maxVal = math.inf
        
        queue.append((root, minVal, maxVal))
        
        while queue:
            node, currMin, currMax = queue.popleft()
            
            if node.val <= currMin or node.val >= currMax:
                return False
            
            if node.left:
                queue.append((node.left, currMin, node.val))
            if node.right:
                queue.append((node.right, node.val, currMax))
                
        return True
            
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        minVal = -math.inf
        maxVal = math.inf
        
        return self.dfs(root, minVal, maxVal)
        
        
        
    # Returns bool if node and all subtrees are valid  
    def dfs(self, node, minVal, maxVal):
        
        # Base Case
        if node is None:
            return True
        
        
        if node.val >= maxVal or node.val <= minVal:
            return False
        
        leftValid = self.dfs(node.left, minVal, node.val)
        rightValid = self.dfs(node.right, node.val, maxVal)
        
        return leftValid and rightValid
        
'''
        
    
        
