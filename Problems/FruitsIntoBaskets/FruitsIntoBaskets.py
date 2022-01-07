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
        
