'''
Very similar to "Number Of Subarrays With Exactly K Different Integers"
- Instead of having a freqMap, we just keep track of numOdd
'''

# One Pass Solution
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddCount = 0
        left = 0
        counter = 0
        numSubarrays = 0
        
        
        for right in range(len(nums)):
            rightNum = nums[right]

            # Only reset counter if we hit an odd number
            if rightNum & 1:
                oddCount += 1
                counter = 0
            
            # Shrink Window
            # Everytime we shrink, we should add one to count since it is a valid subarray
            while oddCount == k:
                leftNum = nums[left]
                oddCount -= leftNum & 1
                counter += 1
                left += 1
                
            numSubarrays += counter
            
        return numSubarrays
                


# Two Pass Solution
'''
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        atMostK = self.atMostK(nums, k)
        kMinusOne = self.atMostK(nums, k - 1)

        return atMostK - kMinusOne
        
    def atMostK(self, nums, k):
        oddCount = 0
        left = 0
        numSubarrays = 0
        #print("k = ", k)
        
        for right in range(len(nums)):
            rightNum = nums[right]
            oddCount += rightNum & 1
            while oddCount > k:
                leftNum = nums[left]
                oddCount -= leftNum & 1
                left += 1
            
            numSubarrays += right - left + 1
            
        return numSubarrays
'''
