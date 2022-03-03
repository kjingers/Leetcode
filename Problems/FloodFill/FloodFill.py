'''
Another matrix BFS / DFS.

Instead of performing dfs on every cell, we jusst start from one cell
'''
from collections import deque
# Iterative BFS

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        oldColor = image[sr][sc]
        m = len(image)
        n = len(image[0])
        
        if oldColor == newColor:
            return image
        
        queue = deque([(sr, sc)])
        
        while queue:
            
            i, j = queue.popleft()
            
            if i < 0 or j < 0 or i >= m or j >= n or image[i][j] != oldColor:
                continue
                
            image[i][j] = newColor
                
            for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                queue.append((i + x, j + y))
                
        return image
                
            

        
        










# DFS Recursive
'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        oldColor = image[sr][sc]
        m = len(image)
        n = len(image[0])
        
        if oldColor == newColor:
            return image
        
        def dfs(image, i, j):
            
            if i < 0 or j < 0 or i >= m or j >= n or image[i][j] != oldColor:
                return
            
            image[i][j] = newColor
            
            for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                dfs(image, i + x, j + y)
                

            
        dfs(image, sr, sc)
        return image
'''
    
        
