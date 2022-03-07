'''
Since we have to solve WITHOUT modifying input array, we can't use cyclic sort.

One technique: Fast and SLow pointers

at each index, jump to index = nums[index]. If there is a duplicate number, then there will be a cycle. Multiple indixes will lead to the same next index.

We know a duplicate exists, since we have n + 1 integers in range [1, n] inclusive. So we must have as least one diplicate since the array is not big enough.

One fast and slow meet, we can find meeting point by resetting one of the pointers, and moving each one step at a time until they meet.

Proof:

x = common dist
y = dist traveled in loop before meeting
z = remaining dist traveled in loop by fast before meeting

When they initially met:

slow traveled: x + y
fast traveled: x + y + z + y

Since fast = 2*slow

2(x + y) = x + 2y + z
x = z

So, one we reset one of the pointers, the reset pointer travels x distance, and other travels z. They meet at start of loop.


Another Technique: Binary Search O(nlog(n))

For each mid, we count all nums in array <= mid. If count > mid, then we have a duplicate in first half, so we shrink search space to 1, mid. Else, duplicate in space mid, end

'''

# Fast and slow pointers

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = nums[0]
        fast = nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        fast = 0
        
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
            
        return slow


# Binary Search
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = start + (end - start) // 2
            
            if sum(i <= mid for i in nums) <= mid:
                start = mid + 1
            else:
                end = mid
        
        return start
'''
            
        
        
        
        
