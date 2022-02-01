'''
Unlinke the leetcode challenge, we are just returning the first good answer. Also, we were provided with an "isSafe()" function

Time Complexity: O(N^N)
'''

def isSafe(i, j, board):
  for c in range(len(board)):
    for r in range(len(board)):
      if board[c][r] == 'q' and i==c and j!=r:
        return False
      elif board[c][r] == 'q' and j==r and i!=c:
        return False
      elif (i+j == c+r or i-j == c-r) and board[c][r] == 'q':
        return False
  return True 

# Recursive Helper Function
def nQueens(r, n, board):

  # Base Case: We have placed a queen on every row
  if n == r:
    return True

  for i in range(n):
    if isSafe(r, i, board):
      board[r][i] = 'q'
      okay = nQueens(r + 1, n, board)

      # If we successfully placed a queen on every row, continue returning
      # up the call stack. 
      if okay:
        return True
      
      # If not good placement, then we need to backtrack that queen position
      # and try the next one
      board[r][i] = '-'
  
  return False


def placeNQueens(n, board):

  okay = nQueens(0, n, board)
  return board
