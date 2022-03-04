# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Thinking: As we traverse, we need to keep track of max value seen for a given path. dfs() can return count of nodes. Preorder traversal so that we process node before node's children.
'''

# Recursive DFS
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        return self.dfs(root, root.val)
    
    def dfs(self, node, maxVal):
        
        if node is None:
            return 0
       
        count = 0
        if node.val >= maxVal:
            count += 1

        count += self.dfs(node.left, max(maxVal, node.val))
        count += self.dfs(node.right, max(maxVal, node.val))
        
        return count

'''    
# Iterative DFS
# Stack will contain (node, maxValOnPath)
from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        stack = deque()
        stack.append((root, root.val))
        count = 0
        
        while stack:
            
            node, maxVal = stack.pop()
            
            if node is None:
                continue
                
            if node.val >= maxVal:
                count += 1
                
            stack.append((node.left, max(maxVal, node.val)))
            stack.append((node.right, max(maxVal, node.val)))
            
        return count
        
'''

        
        
        
        
        
