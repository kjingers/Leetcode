'''
Can DFS/BFS from each unvisited node. When return, add 1.

Also can use Union Find. Union all edges. Then loop through and find all nodes, add parent to set. Length of set is number of connected components.
'''

# BFS Iteratively
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()
        graph = [[] for _ in range(n)]
        res = 0
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        for node in range(n):
            if node not in visited:
                visited.add(node)
                self.bfs(graph, node, visited)
                res += 1
        return res
        
    def bfs(self, graph, node, visited):
        
        queue = deque()
        queue.append(node)
        visited.add(node)
        
        while queue:
            curr = queue.popleft()
            
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return
            
        


# DFS Recursively
'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()
        graph = [[] for _ in range(n)]
        res = 0
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        for node in range(n):
            if node not in visited:
                visited.add(node)
                self.dfs(graph, node, visited)
                res += 1
        
        return res
    
    def dfs(self, graph, node, visited):
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                self.dfs(graph, neighbor, visited)
'''
                
    
                

# Union Find Solution
'''
class DSU:
    def __init__(self, n):
        self.parents = [x for x in range(n)]
        self.rank = [0 for _ in range(n)]
        
    # Find with Path Compression
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        
        if xRoot != yRoot:
            if self.rank[yRoot] < self.rank[xRoot]:
                self.parents[yRoot] = xRoot
            elif self.rank[yRoot] > self.rank[xRoot]:
                self.parents[xRoot] = yRoot
            else:
                self.parents[yRoot] = xRoot
                self.rank[xRoot] += 1
            
            return True
        
        return False
        
        
        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        disjointSet = DSU(n)
        
        for x, y in edges:
            disjointSet.union(x, y)
        
        distinctRoots = set()
        for i in range(n):
            distinctRoots.add(disjointSet.find(i))
        
        return len(distinctRoots)
'''
            
        
        
        
        
        
            
        
