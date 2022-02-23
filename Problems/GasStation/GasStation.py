'''
Straight greedy.

Brute Force could be to try starting at every index. 

I think a smart approach is to start at the index that has the largest (gas - cost). This is not correct

Instead:
    1. If sum(cost) > sum(gas), return -1. Impossible to have solution
    2. Start at index 0. Calculate gas tank after each stop. If gas tank drops below 0, then move starting index to 
       index + 1.
'''


# Brute Force

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # Impossible to have solution
        if sum(cost) > sum(gas):
            return -1
        
        startIndex = 0
        gasTank = 0
        
        for i in range(len(gas)):
            gasTank += gas[i] - cost[i]
            
            # Out of gas, move starting index to next index
            if gasTank < 0:
                gasTank = 0
                startIndex = i + 1
        
        return startIndex
        
        
            
            
        
