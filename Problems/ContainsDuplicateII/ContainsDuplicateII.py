'''
Need two nums equal to each other that are <= k indexes apart.

Can use a dictionary to keep track of num:index. 
    - If num is in dict, than check if curr index - d[num] <= k. If not, update d[num] with current index
    - if not in dict, simply add it.
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if k == 0:
            return False
        
        d = {}
        
        for i, v in enumerate(nums):
            if v in d and i - d[v] <= k:
                return True
            d[v] = i
            
        return False
                
        
        
        
