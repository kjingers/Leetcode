# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Found a couple different strategies in discussion section

1.  Can DFS to find each node. While we DFS, we maintain a list of the path.
    Once we have both lists, we can compare to find LCA.
   
2.  DFS To find each node. As we dfs, we can store into hashmap d[child] = parent. Then, we
    can create a set of p's ancestors using the hash map. Finally, while q is not in ancestors,
    keep comparing its parent.
    
Essentially, we need a way to keep track of the path/parents for each node p and q.
'''

# Iterative DFS

from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # Maps node : parent.
        parent = {root : None}
        stack = deque([root])
        
        while stack:
            node = stack.pop()
            
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
                
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
                
        
        ancestors = set()
        
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        
        return q
                
            
        
