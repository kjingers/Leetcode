'''
The goal is: for each index, find the number of subarrays where arr[i] is the min.

This can be found by, for each index: find the previous less element and next less element.
Then, the number of subarrays where arr[i] is the min is left[i] * right[i]

Then, our answer is: A[i] * left[i] * right[i]

'''
from collections import deque

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        # Default arrays so that each index has no prev/next smaller element
        # This way, if prev/smaller element is not found, we don't need to update
        left = [i + 1 for i in range(len(arr))]        
        right = [len(arr) - i for i in range(len(arr))]
        
        # Find previous lower element
        lstack = deque()
        for i in range(len(arr)):
            while lstack and arr[lstack[-1]] > arr[i]:
                lstack.pop()
            if lstack:
                left[i] = i - lstack[-1] # Before we push, top of stack is prev smaller
            lstack.append(i)
            
        # Find next lower element
        rstack = deque()
        for i in range(len(arr)):
            while rstack and arr[rstack[-1]] > arr[i]:
                ind = rstack.pop() # Top of stack's next smaller is current index
                right[ind] = i - ind
            rstack.append(i)
            
        
        output = 0
        mod = 10**9 + 7
        
        for i in range(len(arr)):
            output = (output + arr[i] * left[i] * right[i]) % mod
            
        return output
            
        
        
        
        
