'''
BFS starting from each gate. When we run into an empty cell without a distance, then put distance (current cell + 1)
'''

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        
        queue = deque()
        
        EMPTY = 2**31 - 1
        
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        
        
        # Now BFS
        while queue:
            x, y = queue.popleft()
            
            for r, c in ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)):
                
                if r < 0 or c < 0 or r >= len(rooms) or c >= len(rooms[0]) or rooms[r][c] != EMPTY:
                    continue
                    
                rooms[r][c] = 1 + rooms[x][y]
                
                queue.append((r, c))
        
        return
                    
        
        
