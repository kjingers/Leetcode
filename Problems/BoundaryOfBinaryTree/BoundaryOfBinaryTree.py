# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
We should make three functions
    1. One to add Left Boundary
    2. One to add Leaves
    3. One to add right boundary bottom to top
    
Left Boundary:
    - Preorder Traversal. THat way, we print top to bottom
    - DFS to left node. If no left node, then right node

Leaves:
    - In order traversal. That way, nodes are left to right.
    - Add to boundary if leaf node

Right Boundary:
    - Post ORder traversal, so that we add bottom up
    - DFS to right node. If no right node, then left
'''

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        boundary = [root.val]
        
        if root.left is None and root.right is None:
            return boundary
        
        self.dfs_left(root.left, boundary)
        self.dfs_leaves(root, boundary)
        self.dfs_right(root.right, boundary)
        
        return boundary
        
        
    # Top Down (PreOrder) Left Boundary  
    def dfs_left(self, node, boundary):
        
        # If none or is leaf node
        if node is None or not node.left and not node.right:
            return
        
        boundary.append(node.val)
        
        if node.left:
            self.dfs_left(node.left, boundary)
        else:
            self.dfs_left(node.right, boundary)
            
        
    # In-Order Leaves
    def dfs_leaves(self, node, boundary):
        
        if node is None:
            return
        
            
        self.dfs_leaves(node.left, boundary)
        
        # If Leaf Node
        if node.left is None and node.right is None:
            boundary.append(node.val)
    
        self.dfs_leaves(node.right, boundary)
        
    # Bottom-up (PostOrder) Right Boundary
    def dfs_right(self, node, boundary):
        
        # If None or is leaf node
        if node is None or not node.left and not node.right:
            return
        
        if node.right:
            self.dfs_right(node.right, boundary)
        else:
            self.dfs_right(node.left, boundary)
            
        boundary.append(node.val)
            
        
        
    
        
