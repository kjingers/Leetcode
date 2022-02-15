# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Since level order, we go with BFS
'''

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        result = []
        
        while queue:
            levelSize = len(queue)
            levelList = []
            for _ in range(levelSize):
                node = queue.popleft()
                if not node:
                    continue
                levelList.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            
            if levelList:
                result.append(levelList)
        
        return result
               
