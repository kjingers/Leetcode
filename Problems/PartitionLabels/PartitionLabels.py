'''
Two pointers
First, must store the right-most index of each letter.

As we loop through, at each letter, we update our right pointer to the furthest index of lettters we have seen.
    - If our current index catches up to our right, we should start a new partition


'''


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last = {}
        
        for i, v in enumerate(s):
            last[v] = i
            
        left = 0
        right = 0
        res = []
        
        for i, v in enumerate(s):
            
            right = max(right, last[v])
            
            if i == right:
                res.append(right - left + 1)
                left = i + 1
                
        return res
                
            
        
