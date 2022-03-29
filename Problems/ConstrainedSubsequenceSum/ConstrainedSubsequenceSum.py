'''
Tricky Problem. Thinking of it as DP, where dp[i] is the max subsequence that must include nums[i].
    - dp[i] = max(dp[i - k], dp[i - k + 1], ..., dp[i - 1], 0) + nums[i]
        - if all previous max within i - k are negative, then we just use nums[i] (even if it itself is negative)
        
Using this approach, the Time is O(n*k)

How can we maintain the max(dp[i - k], dp[i - k + 1], ..., dp[i - 1]) and access it? Monotonic decreasing queue.
This way, we can compare against the max value at the head. And if the head is out 
'''

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        
        queue = deque()
        queue.append(dp[0])
        
        for i, num in enumerate(nums[1:], 1):
            
            # First, Get rid of i - k - 1 if in queue
            if i > k and queue[0] == dp[i - k - 1]:
                queue.popleft()
                
            tmp = max(queue[0], 0) + num
            
            dp[i] = tmp
            
            # Update Queue
            while queue and queue[-1] < tmp:
                queue.pop()
            
            queue.append(tmp)
            
        return max(dp)
        
