'''
A common way to rotate clockwise is:
1. Reverse the elements in each column (row 0 befores row m-1)
2. Flip elements: matrix[i][j] becomes matrix[j][i]

1 2 3        7 8 9        7 4 1
4 5 6  -->   4 5 6  -->   8 5 2
7 8 9        1 2 3        9 6 3

Transpose the matrix. Make sure second loop only goes to i, so that we don't repeat elements
'''


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Reverse elements in each column (row 0 becomes row n - 1, etc)
        # Also matrix.reverse()
        l = 0
        r = n - 1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
                
            
        # Transpose the matrix
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        
            
        
