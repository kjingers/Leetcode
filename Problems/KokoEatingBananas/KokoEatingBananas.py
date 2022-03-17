'''
Brute Force: Start with speed = 1 and calculate the number of hours it takes to eat all the piles.
    - If # hours > h, then increment speed
    - if # hours <= h: return speed
    
O(nm) where m is the min speed

Binary Search: 

If a given speed s works, then we know all speeds >= s work too. Also, if a speed s doesnt work, then all speeds <= s also don't work. So, we can use binary search to find the boundary - the first speed that works.

The search space are speeds from 1 to max(piles)

So can use binary search. At each iteration:
    - m = speed to test
    - Check if mid is a valid speed. If yes, then set right = mid
    - If not valid speed, set left = mid + 1
    
    
Time: O(nlogm), where m is the max speed (largest pile size)
'''
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        
        while left < right:
            mid = left + (right - left) // 2
            
            hours = 0
            # Check if this speed works
            for pile in piles:
                hours += math.ceil(pile / mid)
                
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        
        return left
            
        
