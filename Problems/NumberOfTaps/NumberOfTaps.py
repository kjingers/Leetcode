'''
We can use greedy solution by converting problem into jump game. For each tap,
make the left-most coverage the index, and the right most index the value.
'''


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        maxRanges = [0 for i in range(n + 1)]
        
        # Put values into array to that index is left-most coverage,
        # and value is max distance starting from left
        
        for i, v in enumerate(ranges):
            left = max(0, i - v)
            right = min(n, i + v)
            maxRanges[left] = max(maxRanges[left], right - left)
            
        # Now, similar to Jump Game II

        left = 0
        numTaps = 0
        right = 0
        
        # From first "jump" we need to pick to tap from 0 to maxRange[0] that gives
        # the furthest right distance
        while right < n:
            
            maxSpray = max([i + maxRanges[i] for i in range(left, right + 1)])
            left = right
            right = maxSpray

            numTaps += 1
            
            # If the max ends could not move us passed the first tap
            if left == right:
                return -1
            
        return numTaps
        
            
