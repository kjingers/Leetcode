

'''

Have 4 pointers:
 - rowBegin = 0
 - rowEnd   = m - 1
 - colBegin = 0
 - colEnd   = n - 1
 
 
 Have four for loops iterating the four directions to the corresponding bounds. After each loop, 
 increment/decrement the bound accordingly.


'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m, n = len(matrix), len(matrix[0])
        
        rowBegin, rowEnd = 0, m - 1
        colBegin, colEnd = 0, n - 1
        
        result = []
        
        while rowBegin <= rowEnd and colBegin <= colEnd:
            
            # Loop Right
            for i in range(colBegin, colEnd + 1):
                result.append(matrix[rowBegin][i])
                
            rowBegin += 1
            
            # Loop Down
            for i in range(rowBegin, rowEnd + 1):
                result.append(matrix[i][colEnd])
                
            colEnd -= 1
            
            # For these next two loops, we need to check if the conditions are still valid.
            # The previous adjustments to rowBegin and colEnd could make us repeat cells
            
            # For ex, we could have colEnd == colBegin, but no more rows (rowEnd < rowBegin)
            
            # Loop Left
            if len(result) < n*m:
                for i in range(colEnd, colBegin - 1, -1):
                    result.append(matrix[rowEnd][i])

                rowEnd -= 1
            
            # Loop Up
            if len(result) < n*m:
                for i in range(rowEnd, rowBegin - 1, -1):
                    result.append(matrix[i][colBegin])

                colBegin += 1
            
        
        return result
            
            
        
