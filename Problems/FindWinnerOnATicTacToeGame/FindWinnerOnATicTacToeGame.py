'''
Just like in "Design Tic Tac Toe", we can just give player A +1 and player B -1. Then add for each row and col.

Best to have "rows" and "cols" both with length n. Then Player 1 can +1 and player 2 can -1. At each move, check winner.
This way, we can adapte board for more than 3 rows/cols.

'''

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        n = 3
        
        cols = [0 for _ in range(n)]
        rows = [0 for _ in range(n)]
        
        diag1 = 0 # Top left to bottom-right
        diag2 = 0 # Bottom left to top right
        
        index = 1
        for x, y in moves:
            rows[x] += index
            cols[y] += index
            
            if x == y:
                diag1 += index
                
            if x + y == n - 1:
                diag2 += index
                
            #print("Row Sum: %d, Col Sum: %d, Diag1 Sum: %d, Diag2 Sum: %d" % (sum(rows), sum(cols), diag1, diag2))
                
            if abs(rows[x]) == n or abs(cols[y]) == n or abs(diag1) == n or abs(diag2) == n:
                return "A" if index == 1 else "B"
            
            index *= -1
        
        return "Draw" if len(moves) == n ** 2 else "Pending"
        
            
        
        
