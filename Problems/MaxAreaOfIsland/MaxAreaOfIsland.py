'''
Graph traversal problem.
    - Can edit in-place to avoid need for visited data structure\
    - Base case: return 0
    
Iteative BFS/DFS:
    - Easiest to perform in a function, so can easily keep track of current area
    - Must mark cell as 0 when adding to queue.
'''

# DFS Recursive
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0
        for i in range(len(grid)):
            for j in  range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.dfs(grid, i, j))
        
        return maxArea
    
    def dfs(self, grid, i, j):
        
        # Base Condition
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
            return 0
        
        grid[i][j] = 0
        currArea = 0
        
        for (x, y) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            currArea += self.dfs(grid, i + x, j + y)
            #currMax = max(currMax, self.dfs(grid, i + x, j + y))
            
        return 1 + currArea
    
# BFS Iterative
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0
        for i in range(len(grid)):
            for j in  range(len(grid[0])):
                if grid[i][j] == 1:
                    #area = self.bfs(grid, i, j)
                    #print("i: %d, j: %d, area: %d" % (i, j, area))
                    maxArea = max(maxArea, self.bfs(grid, i, j))
        
        return maxArea
    
    def bfs(self, grid, i, j):
        
        queue = deque([(i, j)])
        currArea = 0
        
        while queue:
            x, y = queue.popleft()
            #print("x: %d, y: %d" % (x, y))
            currArea += 1
            grid[x][y] = 0
            
            for (dx, dy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                r = x + dx
                c = y + dy
                
                if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != 1:
                    continue
                
                grid[r][c] = 0
                queue.append((r, c))
                
        
        return currArea
            
            
        
        
        
