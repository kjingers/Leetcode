'''
Again, "Minimum" leads me to think a dynamic programming approach. WRONG, sliding window.

The hard part is identifying this as sliding window. From the problem statement, need to see that we want 1s GROUPED TOGETHER. So since we want as subarray, we must consider sliding window.

First, Count number of 1s. Then we need to find the best window where we have to do the minimum number of swaps.


'''

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        numOnes = data.count(1)
        n = len(data)
        
        if numOnes < 2 or numOnes == len(data):
            return 0
        
        # need to find window of length (numOnes) that has the most ones
        left = 0
        onesCount = 0
        maxOnes = 0
        for right in range(n):
            onesCount += data[right]
            
            # Our window is size of numOnes.
            # Update Max and remove left most element.
            if right - left + 1 == numOnes:
                maxOnes = max(maxOnes, onesCount)
                onesCount -= data[left]
                left += 1
        
        return numOnes - maxOnes
        
        
        
