'''
Solution:

Standard Sliding Window Problem. Use hashmap with fruits as the key and counts as the value. 
Our condition to shrink the window is when len(d) > 2, since this is the number of keys (distinct fruits) in the window.
When count hits 0 for a fruit, we delete the fruit from the map.

Complexity:
Time Complexity: O(n)
Space Complexity: O(k) --> O(1) Since k=2
'''


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        windowStart = 0
        maxFruits = 0
        
        # Dictionary will contain Fruit : Count
        d = {}
        
        if not fruits:
            return 0
        
        
        for windowEnd in range(len(fruits)):
            
            # Need to add the fruit pointed to by windowEnd
            rightFruit = fruits[windowEnd]
            
            # If this fruit is not yet in window, then add to dictionary
            if rightFruit not in d:
                d[rightFruit] = 0
                
            # Increment fruit count by 1
            d[rightFruit] += 1
            
            # While we have more than 2 different fruits in window,
            # Shrink window by incrementing windowStart
            while len(d) > 2:
                leftFruit = fruits[windowStart]
                # Decrement Count of outgoing Fruit
                d[leftFruit] -= 1
                
                # If count is 0, remove from map
                if d[leftFruit] == 0:
                    del d[leftFruit]
                    
                windowStart += 1
                
            # Update global maximum
            maxFruits = max(maxFruits, windowEnd - windowStart + 1)
        
        return maxFruits
        
