# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Monotonic Decreasing Stack. 
-   If smaller than top of stack, then stack[-1].left = node
-   If larger, then pop off all smaller nodes from stack. The last popped one's right is the current node
'''

from collections import deque

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        stack = deque()
        root = TreeNode(preorder[0])
        stack.append(root)
        popped = None
        
        for val in preorder[1:]:
            new = TreeNode(val)
            
            if val < stack[-1].val:
                stack[-1].left = new
            else:
                while stack and stack[-1].val < val:
                    popped = stack.pop()          
                popped.right = new
                
            stack.append(new)
        
        return root
                   
