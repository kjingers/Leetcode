'''
Basically implement bisect_left and bisect_right
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        res[0] = bisect_left(nums, target)
        res[1] = bisect_right(nums, target) - 1
        
        return [-1, -1] if res[0] == len(nums) or nums[res[0]] != target else res
        
    
    def bisect_left(nums, target):
        
        start = 0
        end = len(nums) # valid output of bisect_left
        mid = start + (end - start) // 2
        
        while start < end:
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        
        return start
    
    def bisect_left(nums, target):
        
        start = 0
        end = len(nums) # valid output of bisect_left
        mid = start + (end - start) // 2
        
        while start < end:
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid
        
        return start
        
        
