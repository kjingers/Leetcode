'''
First time trying monotonic stack. 

My thinking: we can use decreasing stack (bottom to top). We can store a temp with tuple: (temp, index).
Then, whenever we need to pop off smaller temps, we store the index difference in the output index of the popped element.

In fact, we can just store the index in the stack. For each new temp, we compare with temp[stack[-1]]

'''
from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output = [0 for _ in range(len(temperatures))]
        stack = deque()
        
        for i, temp in enumerate(temperatures):
            
            # We want stack to be decreasing
            # When we get greater temp, then we can update output
            while stack and temperatures[stack[-1]] < temp:
                prevIndex = stack.pop()
                output[prevIndex] = i - prevIndex
            
            stack.append(i)
            
        return output
        
        
        
