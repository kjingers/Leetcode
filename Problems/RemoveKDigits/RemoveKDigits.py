'''
To accomplish this, we want to remove the first k digits that are larger than their right neighbor.

We want FIRST instance of this because it affects the overall value more (tens place vs ones place)
We want LARGER THAN RIGHT neighbor, because this replaces the current (larger) value with a smaller value

Since we want to find next smaller element, we can use monotonically increasing stack.
"popped" digits are removed digits. Once we have popped k digits, we can stop popping.

Note: Don't append leading 0s to stack.

After creating monotonic increasing stack, if k > 0, then pop k rightmost digits
'''
from collections import deque

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if k >= len(num):
            return "0"
        
        stack = deque()
        
        # Monotonically Increasing Stack
        for i, v in enumerate(num):
            while stack and stack[-1] > v and k > 0:
                stack.pop()
                k -= 1
                
            if v == "0" and not stack:
                continue
            stack.append(v)
            
        # If we had less than k "peaks", then the largest digits are at the end
        # Pop leftover value of k
        while stack and k > 0:
            stack.pop()
            k -= 1
            
        # It's possible our stack is empty due to not appending leading 0s
        return ''.join(list(stack)) if stack else "0"
                
        
        
        
        
