'''
Should probably sort the input, so that we can work with all the seats in a given row
    - Each row has 10 seats
    - So to have 4 in a row, we have 3 possible 4 groups (0-based):
        - [1,4],[3,6],[5,8]
        - But, if [1,4] and [5,8] are available 4 groups, then we cannot also have [3,6] since they overlap

Idea, represent each row as 10 bits. Flip bits for occupied rows.

Since we know max groups of 4 is 2 * n. We can calculate the number of groups we need to remove

This bitwise solution is O(n) time and O(n) space.

We can probably sort the input, then go row by row so that it is O(nlogn) time and O(1) space
'''

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        #reservedSeats.sort(key=lambda x: x[0])
        
        row_bits = defaultdict(int)
        
        for row, res in reservedSeats:
            row_bits[row] = row_bits[row] | (1 << (res - 1)) 
            
        total_possible = 2 * n
        groups_blocked = 0
        
        # For each row that has at least one reserved seat
        for row in row_bits.values():
            blocked_in_row = 0
            blocked_in_row += (row & int('0111100000', 2)) == 0
            blocked_in_row += (row & int('0000011110', 2)) == 0
            blocked_in_row += (row & int('0001111000', 2)) == 0 and blocked_in_row == 0
            
            groups_blocked += (2 - blocked_in_row)
            
        return total_possible - groups_blocked
            
            
            
            
        
        
        
        
            
        
