# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Can do iterative DFS or BFS and compare node by node
'''

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        
        pstack = deque()
        qstack = deque()
        
        pstack.append(p)
        qstack.append(q)
        
        while pstack and qstack:
            pnode = pstack.pop()
            qnode = qstack.pop()
            
            if not pnode and not qnode:
                continue
            
            if not pnode or not qnode or pnode.val != qnode.val:
                return False
            
            pstack.append(pnode.left)
            pstack.append(pnode.right)
            qstack.append(qnode.left)
            qstack.append(qnode.right)
            
        return False if pstack or qstack else True
            
            
        
        
        
