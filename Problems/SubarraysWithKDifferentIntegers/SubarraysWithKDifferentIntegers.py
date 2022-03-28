'''
Can solve by using "numberOfSubarraysWithAtMostK(k) - numberOfSubarraysWithAtMostK(k - 1)"

This is the most straightforward, because with exactly K distint, it is not as easy to add all of the subarrays
'''

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        atMostK = self.subarraysWithAtMostKDistinct(nums, k)
        atMostKMinusOne = self.subarraysWithAtMostKDistinct(nums, k - 1)
        return atMostK - atMostKMinusOne
        
    def subarraysWithAtMostKDistinct(self, nums: List[int], k: int) -> int:
        windowStart = 0
        charFrequencyMap = {}
        numSubarrays = 0
        
        for windowEnd in range(len(nums)):
            rightNum = nums[windowEnd]
            
            charFrequencyMap[rightNum] = charFrequencyMap.get(rightNum, 0) + 1
            
            while len(charFrequencyMap) > k:
                leftNum = nums[windowStart]
                
                charFrequencyMap[leftNum] -= 1
                
                if charFrequencyMap[leftNum] == 0:
                    del charFrequencyMap[leftNum]
                    
                windowStart += 1
            
            # Add the number of subarrays ending at windowEnd (equal to size of window)
            numSubarrays += windowEnd - windowStart + 1
        
        return numSubarrays
        
        
