"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''
We must traverse through input graph, and for each node, create a new node for the output.

We can use with BFS or DFS to accomplish this. 
- We can use hashmap to store {Input graph node: Copied Graph node}

When we DFS / BFS, for each node, loop through it's neighbors. 

For each neighbor, if neighbor is not in the hashmap, then we:
1. If node is not in hashmap, then add copy to hashmap {Input Node : Output Node}
2. Add neighbor to queue/stack or dfs
Then for all neighbors regardless of condition above, we append copied neighbor to copied node
'''
from collections import deque


# DFS Recursively

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        
        m = {node: Node(node.val)}
        self.dfs(node, m)
        return m[node]
        
    def dfs(self, node, m):
        for neigh in node.neighbors:
            if neigh not in m:
                m[neigh] = Node(neigh.val)
                self.dfs(neigh, m)
            m[node].neighbors.append(m[neigh])
            
# DFS Iteratively
'''
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        
        m = {node: Node(node.val)}
        stack = deque()
        stack.append(node)
        
        while stack:
            curNode = stack.pop()
            for neigh in curNode.neighbors:
                if neigh not in m:
                    m[neigh] = Node(neigh.val)
                    stack.append(neigh)
                m[curNode].neighbors.append(m[neigh])
        
        return m[node]
'''
    
# BFS 
'''
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        
        m = {node: Node(node.val)}
        queue = deque()
        queue.append(node)
        
        while queue:
            curNode = queue.popleft()
            for neigh in curNode.neighbors:
                if neigh not in m:
                    m[neigh] = Node(neigh.val)
                    queue.append(neigh)
                m[curNode].neighbors.append(m[neigh])
        
        return m[node]
'''
