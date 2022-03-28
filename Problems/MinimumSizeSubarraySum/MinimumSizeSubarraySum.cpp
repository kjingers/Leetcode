/*
Positive Integers, so sliding window should work. 

Else, we would probably have to use prefix sum. Our dictionary would keep the index of the most recent occurance of each
prefix sum value.
*/
#include <climits>

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left = 0;
        int minSize = INT_MAX;
        int runningSum = 0;
        
        for(int right = 0; right < nums.size(); right++) {
            int rightNum = nums[right];
            runningSum += rightNum;            
            
            while(runningSum >= target) {
                minSize = min(minSize, right - left + 1);
                int leftNum = nums[left];
                runningSum -= leftNum;
                left++;
            }
        }
        return minSize == INT_MAX ? 0 : minSize;
        
    }
};
