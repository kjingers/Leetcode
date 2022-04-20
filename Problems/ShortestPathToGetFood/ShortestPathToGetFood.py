'''
"SHortest Path", so probably BFS
'''

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        queue = deque()
        stepsTraveled = 0
        
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    queue.append((i, j))
                    grid[i][j] = 'X'
                    
        while queue:
            for _ in range(len(queue)):
                
                x, y = queue.popleft()
                
                grid[x][y] = 'X'
                
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    r = x + dx
                    c = y + dy
                    
                    if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 'X':
                        continue
                        
                    if grid[r][c] == '#':
                        return stepsTraveled + 1
                        
                    queue.append((r, c))
                    grid[r][c] = 'X'
                    
            stepsTraveled += 1
                
        return -1
        
                    
                    
                    
                    
                
                
        
