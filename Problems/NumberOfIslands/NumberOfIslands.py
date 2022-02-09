'''
We can loop though all cells and dfs from each cell. When we dfs, we change 1s to "V" in place. When out dfs returns, 
we add one to our count.

Essentially, when we see a 1, we add 1, since our dfs will mark all connected land cells
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        self.directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)
                    
        return count
                
        
    def dfs(self, grid, i, j):
        
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        
        grid[i][j] = "V"
        
        for dir in self.directions:
            self.dfs(grid, i + dir[0], j + dir[1])
        
