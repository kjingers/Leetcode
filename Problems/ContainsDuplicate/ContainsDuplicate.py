'''
Even though it's trivial, it's easier for me to relate problem as a sliding window.
- Ex: Similar to finding largest subarray with distinct characters. However, if our window ever has duplicates,
-     then we just return true.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        windowStart = 0
        seen = set()
        for windowEnd in range(len(nums)):
            if nums[windowEnd] in seen:
                return True
            seen.add(nums[windowEnd])
        return False
        
