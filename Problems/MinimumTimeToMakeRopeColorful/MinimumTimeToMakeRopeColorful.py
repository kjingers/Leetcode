'''
We can use a greedy solution. As we iterate through, if the current baloon matches the previous, we add the min of the two costs to our output, and our "currentMax" is the max of those two. Once the baloon changes color, we reset currentMax is the new color's cost.

    - currMax is the Time Cost that we did not pick. Or, its the timecost of the new color
'''

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        minTime = 0
        currMax = neededTime[0]
        
        for i in range(1, len(colors)):

            # If repeated color
            if colors[i] == colors[i - 1]:
                minTime += min(currMax, neededTime[i])
                currMax = max(currMax, neededTime[i])
            else:
                currMax = neededTime[i]
                
        return minTime
                
            
        
