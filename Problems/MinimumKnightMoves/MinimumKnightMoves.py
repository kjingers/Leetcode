'''
"Minimum" number makes me think BFS, or possibly DP. Naive BFS gives TLE
First, we can solve for abs(x) and abs(y) to reduce search space into a quarter
'''

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x = abs(x)
        y = abs(y)
        
        # To allow to going outside bound by 2
        dp = [[-1 for _ in range(y + 3)] for _ in range(x + 3)]
        
        num = self.move_recursive(x, y, dp)
        
        return num
        
    def move_recursive(self, x: int, y: int, dp: List[List[int]]):
        
        if x + y == 0:
            return 0
        
        # to avoid going negative.
        # at (1,1), (2,0), or (0, 2), takes 2 moves to origin
        if x + y == 2:
            return 2
        
        if dp[x][y] != -1:
            return dp[x][y]
        
        move_one = self.move_recursive(abs(x - 2), abs(y - 1), dp)
        move_two = self.move_recursive(abs(x - 1), abs(y - 2), dp)
        
        dp[x][y] = min(move_one, move_two) + 1
        
        return dp[x][y]
