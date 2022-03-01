# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Kind of similar to max path sum. At each node, we need to calculate:
    1. The len of the path from node's left to node's right (node is top of path). Once we get this value,
       we update the max distance if applicable.
    2. We calculate and return the length of a path up THROUGH the node max(node.left, node.right)
    
Iterative Post Order Traversal:

Iterative solution is a little bit trickier. We need to use dict to keep track of which nodes have been processed.
This way, we can do a ppost-order traversal and make sure the node's children have been processed before the node itself.
'''

# DFS Recursive

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxDiameter = 0
        
        def solve(node):
            
            nonlocal maxDiameter
            
            if node is None:
                return 0
            
            leftLen = solve(node.left)
            rightLen = solve(node.right)
            
            # Diameter with node as the top
            maxDiameter = max(maxDiameter, leftLen + rightLen)
            
            # Return diameter passing up through this node
            return 1 + max(leftLen, rightLen)
        
        solve(root)
        return maxDiameter


# DFS Iteratively - Post Order Traversal

'''
from collections import deque

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        stack = deque([root])
        postOrder = {}
        maxDiameter = 0
        
        while stack:
            node = stack[-1]
            
            if node.left and node.left not in postOrder:
                stack.append(node.left)
                
            elif node.right and node.right not in postOrder:
                stack.append(node.right)
                
            else: # No children, or children already processed
                node = stack.pop()
                leftLen = postOrder.get(node.left, 0)
                rightLen = postOrder.get(node.right, 0)
                postOrder[node] = max(leftLen, rightLen) + 1 # This is what we would return recursively
                maxDiameter = max(maxDiameter, leftLen + rightLen)
                
        return maxDiameter
        
'''
                
