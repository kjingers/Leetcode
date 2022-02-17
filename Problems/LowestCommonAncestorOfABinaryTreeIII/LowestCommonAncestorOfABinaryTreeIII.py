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

Another solution for O(1) space, is to find merge point similar to how you would in Linked List.
- p's path to root is: a + c
- q's path to root is: b + c
Where c is the path after they have converged. a and b is the length of path to the convergence point for p and q respectively.

So, we make both nodes travel the full distance:
    p: a + c + b
    q: b + c + a
    
These disctances are equivalent and both nodes are at the merge point, which  is also the LCA.
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
        
        
        
        
        
        
        
