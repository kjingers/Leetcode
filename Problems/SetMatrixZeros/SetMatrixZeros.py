'''
1.  First Check if first column or first row contains a 0. If so, set corresponding variable to True.
    This is because we will use the first element in each row/column to indicate if we need to set
    that row or column to 0s as we go through the rest of the matrix.
2. Go through all rows. If element is 0, set first element to 0
3. Go through all cols. If element is 0, set first element to 0
4. Go through matrix again. For each element, if matrix[0][i] or matrix[i][0] is 0, then set element to 0


Time Complexity: O(nm)
Space Complexity: O(1)
'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m = len(matrix)
        n = len(matrix[0])
        
        firstRowZero = False
        firstColZero = False
        
        # Check to see if first row has a 0
        for i in range(n):
            if matrix[0][i] == 0:
                firstRowZero = True
                break
                
        # Check to see if first col has a 0        
        for i in range(m):
            if matrix[i][0] == 0:
                firstColZero = True
                break
                
        # Check cells except first row and col.
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set 0s based on first row and col
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Process First Row
        if firstRowZero:
            for i in range(n):
                matrix[0][i] = 0
        
        
        # Process First Col
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0
                
        return matrix
                
                
        
