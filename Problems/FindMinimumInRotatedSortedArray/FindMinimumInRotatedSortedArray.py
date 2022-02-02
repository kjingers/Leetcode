'''
Follows binary search pattern. Instead of comparing mid to a target, we will first:
- compare nums[mid] with nums[mid + 1]
- compare nums[mid] with nums[mid - 1]
If num goes from high to low in any of these 3 positions, then we know the pivot point (minimum)

If pivot point is not in one of these 3 indices, then we need to see which side has all ascending nums.
We can do this by compare nums[mid] with nums[start] and nums[end]. Once we know this, we shrink
window to the non-sorted side, since the pivot point will be in the non-sorted side.
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        start, end = 0, len(nums) - 1
        
        while start < end:
            mid = start + (end - start) // 2
            
            # First check if mid, mid-1, or mid+1 contain pivot point
            if mid > start and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif mid < end and nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            
            # If not found, need to determine which side is sorted
            # Pivot point will be in non-sorted side
            if nums[mid] < nums[end]:
                end = mid - 1
            else:
                start = mid + 1
             
        # If we get to here, then there is no pivot point. So the first element is the min
        return nums[0]
            
        
