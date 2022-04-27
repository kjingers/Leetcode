class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0 for _ in range(n)]
        self.cols = [0 for _ in range(n)]
        self.diag1 = 0
        self.diag2 = 0
        self.n = n
        
        
    def move(self, row: int, col: int, player: int) -> int:
        # player 1: -1, player2: 1
        diff = 2 * player - 3
        self.rows[row] += diff
        self.cols[col] += diff
        
        # Top left to Bottom Right 
        if row == col:
            self.diag1 += diff
        
        # Bottom Left to Top right
        if row + col == self.n - 1:
            self.diag2 += diff
            
        if diff * self.n in [self.rows[row], self.cols[col], self.diag1, self.diag2]:
            return player
        
        return 0
        

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
