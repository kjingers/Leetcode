# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
As we traverse, we need some way of keeping track of which column each node is in.
-   Using BFS ensures the left node comes first for a given row
-   We can start with (root, 0). Then (root.right, 0 + 1) and (root.left, 0 - 1)
-   For each node, add to cols dictionary

When done with BFS, we can sort dict keys and return list.

Time Complexity: O(nlogn)

We can make O(n) by keeping track of left-most and right-most columns. That way, we can just iterate cols
from leftmost to rightmost, instead of having to sort.
'''

from collections import deque, defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)
        queue = deque([(root, 0)])
        
        while queue:
            node, col = queue.popleft()
            
            if not node:
                continue
                           
            cols[col].append(node.val)
                       
            queue.append((node.left, col - 1))
            queue.append((node.right, col + 1))
            
        return [cols[i] for i in sorted(cols)]
                    
            
        
        
        
