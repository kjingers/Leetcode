# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
At each node, need to calculate the maximum of left and right.
-   maxchild = max(0, dfs(child)). 
    Because if it is negative, then it's better to not use the child, instead
    having the path terminate at the current node
    
-   Need to return node.val + max(left, right)).
    This is the maxPathSum of tree with root = currentNode. 
    
Must maintain maxSum. I used a list of length 1 so its passed by reference. Probably smarter to
make dfs a local function and use nonlocal variable.
    
'''
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = [float('-inf')]
        rootSum = self.dfs(root, maxSum)
        return maxSum[0]
        
    def dfs(self, node, maxSum):
        
        if not node:
            return 0
        
        maxLeft = max(0, self.dfs(node.left, maxSum))
        maxRight = max(0, self.dfs(node.right, maxSum))
        
        maxSum[0] = max(maxSum[0], node.val + maxLeft + maxRight)
        
        return node.val + max(maxLeft, maxRight)
   
        
        
