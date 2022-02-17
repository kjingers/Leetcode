# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Very Similar to Binary Tree Vertical Order. But in this case, if two nodes are at the same
row and column, the smaller valued node comes first (instead of the left one of level order traversal)

So we can:
    - Have dictionary d[x] = (y, node.val). This way, we can sort by the value, which will first sort by 
      y coordinate (higher first) then by value if y coordinates are equal
    - Defaultdict so we don't have to check if key is in dict before appending
    - Keep track of lowest x and highest x, so we can just iterate through these keys (and not have to sort again)
    
Note: Adding to y as I traverse to make it 
'''

from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        d = defaultdict(list)
        queue = deque()
        low_x, high_x = float('inf'), -float('inf')
        
        queue.append((root, 0, 0))
        
        while queue:
            node, x, y = queue.popleft()
            
            if not node:
                continue
            
            low_x = min(low_x, x)
            high_x = max(high_x, x)
            
            d[x].append((y, node.val))
            
            queue.append((node.left, x - 1, y + 1))
            queue.append((node.right, x + 1, y + 1))
            
        output = []

        for i in range(low_x, high_x + 1):
            output += [[j for i, j in sorted(d[i])]]
            
        return output
