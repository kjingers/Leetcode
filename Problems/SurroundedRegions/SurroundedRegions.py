'''
Graph/Matrix Traversal Problem.
    - Essentially, any region with a path to the border cannot be captured. All other regions should be captured
    - So We can start with all regions on border and DFS/BFS. Mark all of these regions to know that they are safe (ex. "S")
    - After processing border, go through graph and mark all "O" cells as captured "X". And all "S" cells back as "O"
    
    
    
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        # Top and bottom borders
        for i in (0, len(board) - 1):
            for j in range(0, len(board[0])):
                if board[i][j] == "O":
                    self.dfs(board, i, j)
        
        # Left and bottom borders
        for i in range(0, len(board)):
            for j in (0, len(board[0]) - 1):
                if board[i][j] == "O":
                    self.dfs(board, i, j)
                    
        # Now, mark remaining regions as captured and mark safe regions back to "O"
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"
                    
    def dfs(self, board, i, j):
        
        # Base Case
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != "O":
            return
        
        board[i][j] = "S"
        
        for (x, y) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            self.dfs(board, i + x, j + y)
            
        return
            
                
                
        
