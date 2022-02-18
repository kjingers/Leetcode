# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Looked at solutions. A common approash it to do a standard DFS. But along the way, we maintain a "height".

    - The Base case for NULL node is to return 0. When we call the recursive DFS, we add 1. So, the leaf
      nodes will have a height of 1. After they are "removed" the new leaves have height of 2, etc.
      
    - When we return from left and right dfs. We append node to output list based on height:
      output[height - 1].append(node.val)
      
    - The tricky thing to grasp, is depth = max(dfs(left), dfs(right)) + 1. 
    
Iterative Post Order Traversal is tricky.
'''

# DFS Recursive

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        self.dfs(root, output)
        return output
     
    
    # Returns height of node
    def dfs(self, node, output):
        
        if not node:
            return 0
        
        # This is the height of the current node
        height = max(self.dfs(node.left, output), self.dfs(node.right, output)) + 1
        
        if len(output) < height:
            output.append([])
            
        output[height - 1].append(node.val)
        
        return height



        
