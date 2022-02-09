'''
I think this is supposed to be a union find problem, but I haven't learned that yet.

To achieve O(n) time, we can put all numbers into a set, which takes O(n). Then, we can just check streaks
by looking for numbers in the set.
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        maxStreak = 0
        
        for num in nums:
            
            # If num is beginning of a streak
            if num - 1 not in nums:
                next = num + 1
                
                while next in nums:
                    next += 1
                    
                maxStreak = max(maxStreak, next - num)
                
        return maxStreak
                
        
        
        
