'''
Brute Force. Try each node as root and calculate height

2 x DFS: There can be a max of two nodes that provide minimum height tree. And, the node(s) is the middle node of the longest path tree.

Option 3: Top Sort. We start with leaf nodes and work our way in. Once we have 1 or 2 nodes left, in a level, then those are the roots for minimum height tree
'''
# Topological Sort
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1:
            return [0]
        
        adjList = defaultdict(list)
        inDegrees = defaultdict(int)
        
        # Build Adjacency List and inDegrees
        for x,y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
            inDegrees[x] += 1
            inDegrees[y] += 1
          
        queue = deque()
        
        for node in inDegrees:
            if inDegrees[node] == 1:
                queue.append(node)
                
        res = []
        
        while queue:
            res.clear()
            size = len(queue)
            
            for i in range(size):
                source = queue.popleft()
                res.append(source)
            
                for neigh in adjList[source]:
                    inDegrees[neigh] -= 1
                    if inDegrees[neigh] == 1:
                        queue.append(neigh)
                        
        return res
            
            
                
            
            
        
        
        
        
# Brute Force
'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
            
        heights = defaultdict(int)
        res = []
        minHeight = float('inf')
        
        for root in range(0, n):
            visited = set([root])
            height = self.dfs(root, adj, visited)
            minHeight = min(minHeight, height)
            heights[root] = height
            
                
        return [node for node in heights if heights[node] == minHeight]
        

    def dfs(self, node, adj, visited):
        
        height = 0
        for neigh in adj[node]:
            if neigh not in visited:
                visited.add(neigh)
                height = max(height, 1 + self.dfs(neigh, adj, visited))
                
        return height
        
'''
