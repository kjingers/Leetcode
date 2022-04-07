'''
Union Find can work. Just iterate through edges, and attempt to Union them. If the edge is connecting nodes that are already connected, then we return it.

Basic Union Find passes. Can optimize with path compression and union-by-rank.
'''
# Union-Find

class DSU:
    def __init__(self, size):
        self.par = [x for x in range(size + 1)]
        self.rank = [0 for _ in range(size + 1)]
        
    def find(self, x):
        if self.par[x] != x:
            # Sets parent of all nodes to head node
            # So follow-up finds are faster
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        
        # Union by rank is all about deciding which to make leader
        # We choose leader with higher following, or, "rank"
        if xr == yr:
            return False
        elif self.rank[xr] > self.rank[yr]:
            self.par[yr] = xr
        elif self.rank[yr] > self.rank[xr]:
            self.par[xr] = yr
        else:
            self.par[yr] = xr
            self.rank[xr] += 1
        return True
        
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for edge in edges:
            if not dsu.union(edge[0], edge[1]):
                return edge
        return []
        
        
