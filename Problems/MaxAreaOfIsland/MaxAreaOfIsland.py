'''
Definitely a matrix bfs/dfs traversal problem.

Time: O(m*n)
Space: O(1)

For Iterative BFS, we will want to call a new BFS when we find a 1 in our initial traversal. 
Whenever we pop from queue, we add 1 to answer. Only put coords in queue if in-bounds and a 1. That way,
whever we pop, we add 1. When queue becomes empty, the entire island has been processed so we can return area
of current island.
'''

# Recursive DFS
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                count = self.dfs(grid, i, j)
                maxArea = max(maxArea, count)
                
        return maxArea
                
    def dfs(self, grid, i, j):
        
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
            return 0
        
        grid[i][j] = 0
        
        count = 0
        
        for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            count += self.dfs(grid, i + x, j + y)
            
        return 1 + count
        
