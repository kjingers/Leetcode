"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

'''
Looks similar to original Lowest Common Ancestor of a binary tree. However, each node already has reference to parent.
So, we can skip the dfs/bfs to build the parent dictionary.

O(n) worst case I think
'''

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        # Build ancestors for p
        # While q not in p, q = q.parent
        # return q
        
        
        p_ancestors = set()
        
        while p:
            p_ancestors.add(p)
            p = p.parent
            
        while q not in p_ancestors:
            q = q.parent
            
        return q
        
        
        
        
        
        
        
