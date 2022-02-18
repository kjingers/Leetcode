# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
A BFS makes sense since a level-o.rder traversal makes this easy.
    - At each level, we append the last node to the output
    - Note: we should avoid appending Null nodes, so that we have accurate level length
'''

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        if not root:
            return []
        
        output = []
        
        queue = deque()        
        queue.append(root)
        
        while queue:
            
            levelSize = len(queue)
            cnt = 1
            for _ in range(levelSize):
                
                node = queue.popleft()
                
                if cnt == levelSize:
                    output.append(node.val)
                    
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
                cnt += 1
                    
        return output
                
        
