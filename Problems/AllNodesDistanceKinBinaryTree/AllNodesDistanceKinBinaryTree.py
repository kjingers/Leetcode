# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Looked at solutions. Common approach is to build a graph using adjacency lists. Then, perform BFS K times.
The nodes that are in the queue at the end are a distance K from target.

A graph is a good approach, because the parent/child relationship is bidirectional. We want K steps away in all directions.
'''
from collections import defaultdict

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = defaultdict(list)
        stack = deque([root])
        
        # First Convert to graph using iterative DFS
        while stack:
            node = stack.pop()
            
            if not node:
                continue
            
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                
            stack.append(node.left)
            stack.append(node.right)
            
        seen = set()
        queue = deque([target.val])
        
        # Now BFS through k levels
        # 
        for i in range(k):
            levelSize = len(queue)
            for j in range(levelSize):
                node = queue.popleft()
                seen.add(node)

                for neighbor in graph[node]:
                    if neighbor not in seen:
                        queue.append(neighbor)
                    
        
        return list(queue)
            
            
                
            
        
        
        
