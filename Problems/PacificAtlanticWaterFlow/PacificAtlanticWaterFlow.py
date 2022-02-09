'''
We can make two nxm matricies, one for Pacific and one for Atlantic. In each, we mark tiles 1 if it can reach each
respective ocean.

We start from all the elements in a row or column that are touching each ocean. From each element, we dfs to other
tiles with a greater value and update either pacific or atlantic visited along the way

- matrix[i][0] Touches pacific
- matrix[i][n-1] Touches Atlantic
- matrix[0][i] Touches pacific
- matrix[m-1][i] Touches Atlantic

'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m = len(heights)
        n = len(heights[0])
        
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        # Iterate over rows for first col (Pacific) and last (Atlantic)
        for i in range(m):
            self.dfs(heights, i, 0, p_visited, m, n)
            self.dfs(heights, i, n - 1, a_visited, m, n)
            
        # Iterate over cols for first row (Pacific) and last (Atlantic)
        for i in range(n):
            self.dfs(heights, 0, i, p_visited, m, n)
            self.dfs(heights, m - 1, i, a_visited, m, n)
            
        result = []
        for i in range(m):
            for j in range(n):
                if a_visited[i][j] and p_visited[i][j]:
                    result.append([i, j])
                    
        return result
        
    def dfs(self, matrix, i, j, visited, m, n):

        if visited[i][j]:
            return
        visited[i][j] = True
        
        for dir in self.directions:
            x = dir[0] + i
            y = dir[1] + j
            
            # If out of bounds or current cell is less than previous cell
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] < matrix[i][j]:
                continue
                
            self.dfs(matrix, x, y, visited, m, n)
            
        
        
        
