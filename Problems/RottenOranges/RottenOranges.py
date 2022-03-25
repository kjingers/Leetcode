'''
Since each day, all rotten oranges spread by one, we should use BFS instead of DFS.
'''

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        freshCount = 0
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Loop Through. Add rotten oranges to queue. Count fresh ones
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    freshCount += 1
          
        
        numDays = 0
        
        while queue and freshCount > 0:
            currDay = len(queue)
            numDays += 1
            
            # Process each day seperately
            for _ in range(currDay):
                i, j = queue.popleft()
                
                for x, y in DIRS:
                    r = i + x
                    c = j + y
                    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != 1:
                        continue
                        
                    freshCount -= 1 # Decrement freshCount
                    grid[r][c] = 2 # Make rotten
                    queue.append((r, c)) # Add rotten to queue
          
        
        return -1 if freshCount > 0 else numDays
                    
    
                    
            
        
