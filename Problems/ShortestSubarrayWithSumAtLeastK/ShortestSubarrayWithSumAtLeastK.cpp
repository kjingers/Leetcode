/*
Since negative numbers, we can't use standard sliding window.

We must first generate the prefix sum array. Then, use monotonic increasing queue.
- We want smallest x2 - x1 where P[x2] - P[x1] >= k
- Increasing queue, since smaller values do not help us achieve >= k
- At each step, if current Presum - front of queue >= k, then update min and shrink window by popping from front
*/

class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        deque<int> queue;
        vector<long long> prefixSum = {0};
        size_t N = nums.size();
        
        for(int num : nums) {
            prefixSum.push_back(prefixSum.back() + num);
        }
        
        int ans = N + 1;
        
        for(int i = 0; i < prefixSum.size(); i++) {
            long long pSum = prefixSum[i];
            
            while(!queue.empty() && prefixSum[queue.back()] > pSum) {
                queue.pop_back();
            }
            
            while(!queue.empty() && (pSum - prefixSum[queue.front()]) >= k) {
                ans = min(ans, i - queue.front());
                queue.pop_front();
            }
            queue.push_back(i);
        }
        
        
        return ans == N + 1 ? -1 : ans;
    }
};
