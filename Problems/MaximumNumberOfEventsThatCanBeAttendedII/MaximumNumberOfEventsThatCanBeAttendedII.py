'''
0/1 Knapsack DP. 

The tricky part is that if we choose an event, we can't just calculate for index + 1. We need to find the next index that starts after the end of the chosen event. The most efficient way to do this is binary search.

Bottom-up:
From our top-down approach, we see: 
            pick = events[index][2] + solve(nextEvent, k - 1)
            skip = solve(index + 1, k)
            
So, we need our index to go down (since we need to know index + 1), and we need our k to go up (since we need to know k - 1)

dp[i][j] = max(dp[i + 1][j], events[next][2] + dp[next][k - 1])
'''

# Top Down
'''
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        starts = [event[0] for event in events]
           
        @functools.lru_cache
        def solve(index, k):

            # Base Cases
            if index == len(events) or k == 0:
                return 0

            nextEvent = bisect.bisect(starts, events[index][1])

            pick = events[index][2] + solve(nextEvent, k - 1)
            skip = solve(index + 1, k)

            return max(pick, skip)
        
        return solve(0, k)
'''
    
# Bottom-up
# Base Case: dp[*][0] = 0 and dp[n][*] = 0
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        starts = [event[0] for event in events]
        n = len(events)
        
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            nextEvent = bisect.bisect(starts, events[i][1])
            for j in range(1, k + 1):
                dp[i][j] = max(dp[i + 1][j], events[i][2] + dp[nextEvent][j - 1])
                
        return dp[0][k]
                

        
        
