   
'''
Start off binary search like normal. Calculate mid. Then, 
- Determine which side is sorted
- Check if target is in that sorted side
- If is in sorted side, shrink window to that side
- Else, shrink window to other side
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        
        # Use <= since need to check when start == mid == end
        while start <= end:
            mid = start + (end - start) // 2
            
            # Check if mid is target
            if nums[mid] == target:
                return mid
            
            # Right side is sorted
            if nums[mid] < nums[end]:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else: # Left side is sorted
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            
        return -1
        
