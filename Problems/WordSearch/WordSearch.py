'''
Typical Matrix DFS problem. If word[i] == cell, then we must mark the cell so that we don't revisit it
in current word check. As we return from each dfs, we need to replace cell with it's original letter.

For this reason, we don't need a seperate visited matrix.

-   Base case is if index == len(word), then we've successfully matches all indicies of the word so far,
    so we can return True.
-   Need to mark cell to '#' so taht we don't revisit it in current iteration. Once we return, from
    successive dfses, then we need to change cell back to original, so that it can be used for future
    checks.

'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, 0, i, j):
                    return True
        
    def dfs(self, board, word, index, i, j):

        if index == len(word):
            return True

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[index] != board[i][j]:
            return False

        board[i][j] = '#'
        found = False
        for x,y in ((0,1), (0,-1), (1,0), (-1,0)):
            found = found or self.dfs(board, word, index + 1, i + x, j + y)

        board[i][j] = word[index]

        return found
