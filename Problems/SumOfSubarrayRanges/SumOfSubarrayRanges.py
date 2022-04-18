'''
Brute Force: Look at all subarrays and sum += (max - min)

Maybe we can try to see, for each index, how many subarrays it is the min and how many is it the max.

Since we need "next greater" and "next smaller" monotonic stack could work.
    - For each nums[i], we want to find the index of the next element on left and right that is smaller.
        - (# indexes to left) * (# indexes to eight) = # Subarrays where nus[i] is minimum
    - Repeat for next greater to get maximum
    
    
'''

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        decStack = deque()
        incStack = deque()
        stack = deque()
        #nextGreater = [0 for _ in range(len(nums))]
        res = 0
        
        # Boundaries to find prev greater and next greater
        forDec = [math.inf] + nums + [math.inf]
        
        for i, num in enumerate(forDec):
            
            # First, add maxes using decreasing stack
            # We are adding for all subarrays where nums[midIndex] is the max
            # The math.inf values never get popped so don't have to worry about accidently
            # calculating those.
            while stack and forDec[stack[-1]] < num:
                midIndex = stack.pop()
                leftIndex = stack[-1]
                numSubarrays = (midIndex - leftIndex) * (i - midIndex)
                res += forDec[midIndex] * numSubarrays
                
            stack.append(i)
            
        stack = deque()
            
        forInc = [-math.inf] + nums + [-math.inf]
        
        for i, num in enumerate(forInc):
            
            while stack and forInc[stack[-1]] > num:
                midIndex = stack.pop()
                leftIndex = stack[-1]
                numSubarrays = (midIndex - leftIndex) * (i - midIndex)
                res -= forInc[midIndex] * numSubarrays
                
            stack.append(i)
            
        return res
                
                
                            
        
