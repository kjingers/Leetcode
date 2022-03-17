'''
Binary Search Problem:

Search range is left = min(sweetness), right = sum(sweetness) // (k + 1)
    - If we don't want to use a running max, then we need to make our mid (left + right) // 2 + 1. This is because, if left and right are next to eachother, then we will look forever if we set left = mid.
'''

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        
        left = min(sweetness)
        right = sum(sweetness) // (k + 1)
        
        maxSweetness = 0
        
        while left <= right:
            
            mid = left + (right - left) // 2
            
            if self.checkCuttingPlan(sweetness, mid, k):
                maxSweetness = max(maxSweetness, mid)
                left = mid + 1
            else:
                right = mid - 1
                
        return maxSweetness
        
    def checkCuttingPlan(self, sweetness, minSweetness, k):
        curr = 0
        people = 0
        
        for s in sweetness:
            curr += s
            
            if curr >= minSweetness:
                people += 1
                curr = 0
                
        return True if people >= (k + 1) else False

        
