'''
When dealing with subarray sums, then prefix sum is useful.

As we add prefix sum counts into dict, we check if current preSum - k is in dict. This means that we have at least one subarray that increases sum by k (giving us a valid subarray). 
    - Must start with 0, or else we will miss sums, since the subarray sum technically starts from 0
    - Each loop we increment dictionary[preSum] since we have another preSum with this value
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        preSum = [0]
        res = 0
        d[0] = 1
        
        for num in nums:
            preSum.append(num + preSum[-1])
            
            if preSum[-1] - k in d:
                res += d[preSum[-1] - k]
                
            d[preSum[-1]] = d.get(preSum[-1], 0) + 1
            
        return res
                
        
        
        
