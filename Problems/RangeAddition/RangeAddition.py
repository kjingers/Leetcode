'''
[1,3,2]

[0,0,0,0,0]
Adding [1, 3, 2]: [0,2,0,0,-2,0]
Adding [2, 4, 3]: [0,2,3,0,-2,-3]
Adding [0,2,-2]: [-2,2,3,2,-2,-3]

Prefix Sum: [-2,0,3,5,3,0]

Then pop right-most elemenet

[]


'''

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        
        output = [0 for _ in range(length + 1)]
        
        for start, end, inc in updates:
            output[start] += inc
            output[end + 1] -= inc
            
        # Now prefix sum
        
        for i in range(1, len(output)):
            output[i] += output[i - 1]
            
        output.pop()
        return output
            
            
            
        
