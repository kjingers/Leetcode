'''
We can just do two passes with monotonically decreasing stack.

Every element popped off the stack has next greater element of current.

After first pass, everything in the stack doesn't have a next greater element w/o circular part.
Do another pass where we start out with the stack with the leftover indices
'''

from collections import deque

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = deque()
        output = [-1 for i in range(len(nums))]
        
        # Monotonically decreasing stack. Store indices
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                ind = stack.pop()
                output[ind] = nums[i]
            stack.append(i)
            
        # After one pass, the indices we have do not have next greater element w/o circular
        # Do another pass
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                ind = stack.pop()
                output[ind] = nums[i]
            stack.append(i)
            
        return output
                
        
