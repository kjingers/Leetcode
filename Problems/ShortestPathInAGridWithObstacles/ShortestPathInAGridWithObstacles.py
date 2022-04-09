'''
BFS:

In queue, we store: x, y, # Obstacles, # Steps
'''

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        
        mDist = lambda x, y : m + n - 2 - x - y
        
        if mDist(0, 0) <= k:
            return mDist(0, 0)
        
        queue = deque()
        seen = set([0, 0, k])
        
        queue.append((0, 0, k, 0))
        
        while queue:
            x, y, elimRem, numSteps = queue.popleft()
            #print("%d, %d" % (x, y))
            
            # Check if we can end early
            #if mDist(x, y) <= elimRem:
            #    print("x: %d, y: %d" % (x, y))
            #    return numSteps + mDist(x, y)
            if x == m - 1 and y == n - 1:
                return numSteps
            
            for dx, dy in ((0, 1), (1, 0), (-1, 0), (0 ,-1)):
                r = x + dx
                c = y + dy
                
                if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                    continue
                    
                new_elim = elimRem - grid[r][c]
                new_state = (r, c, new_elim)
                
                if new_state in seen or new_elim < 0:
                    continue
                
                seen.add(new_state)    
                queue.append((r, c, new_elim, numSteps + 1))
                
        return -1
        
        
