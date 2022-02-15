# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
We can have a second function that compares the structure of two trees based on root. It
will return True if both trees have the same structure.

In our main function, we can dfs/bfs our main tree until node.val == root2.val. Then we can call
sameTree(node, root2)

'''

# Recursive
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)
        
    def dfs(self, node, subRoot):
        
        if not node:
            return False
        
        if node.val == subRoot.val and self.sameTree(node, subRoot):
            return True
        
        return self.dfs(node.left, subRoot) or self.dfs(node.right, subRoot)

    def sameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        
        
        if not root1 or not root2 or root1.val != root2.val:
            return False
        
        return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)
    
        
            

# Iterative
'''
from collections import deque
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        queue = deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            
            if not node:
                continue
                
            if node.val == subRoot.val:
                if self.sameTree(node, subRoot):
                    return True
                
            queue.append(node.left)
            queue.append(node.right)
            
        return False
        
        
        
    def sameTree(self, root1, root2):
        q1 = deque()
        q2 = deque()
        
        q1.append(root1)
        q2.append(root2)
        
        while q1 and q2:
            
            node1 = q1.popleft()
            node2 = q2.popleft()
            
            # If Both are None, continue comparing
            if not node1 and not node2:
                continue
                
            
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            q1.append(node1.left)
            q1.append(node1.right)
            q2.append(node2.left)
            q2.append(node2.right)
            

        return False if q1 or q2 else True
            
'''
        
        
        
