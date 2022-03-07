'''
Many different methods to get acceptable answers.

One Simple way to for each index except the last one, set out[i] = i + 1. Then for the last index, set to -sum


another idea is to use series. Ex:

n = 1: [0]
n = 2: [-1, 1]
n = 3: [-2, 0, 2]
n = 4: [-3, -1, 1, 3]
n = 5: [-4, -2, 0, 2, 4]

So, out[i] = i * 2 - n + 1
Or, range(-n + 1, n, 2)
'''

# Set Out[i] = i + 1. Last index, set to -sum
'''
class Solution:
    def sumZero(self, n: int) -> List[int]:
        out = [0 for i in range(n)]
        arrSum = 0
        
        for i in range(n-1):
            out[i] = i + 1
            arrSum += out[i]
            
        out[n - 1] = -arrSum
        
        return out
'''
    
# Using Series
class Solution:
    def sumZero(self, n: int) -> List[int]:
        out = range(-n + 1, n, 2)
        return out
            
        
        
