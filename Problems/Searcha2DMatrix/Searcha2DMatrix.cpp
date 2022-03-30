/*
Binary Search

From 0 to m*n-1. 

When mid is calculated, calculate row and col based on mid value.:
row[i][j] --> i = (index / m), j = index % m
*/

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
        int m = matrix.size();
        int n = matrix[0].size();
        
        int left = 0;
        int right = m * n - 1;
        
        // Binary Search
        while(left <= right) {
            int mid = left + (right - left) / 2;
            int col = mid % n;
            int row = mid / n;
            
            if(matrix[row][col] == target) {
                return true;
            }
            else if(target < matrix[row][col]) {
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
            
            
        }
        return false;
        
        
        
    }
    
    
};
