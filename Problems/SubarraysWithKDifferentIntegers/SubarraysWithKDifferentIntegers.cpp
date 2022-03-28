class Solution {
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        int atMostK = atMostKDistinct(nums, k);
        int atMostKMinusOne = atMostKDistinct(nums, k - 1);
        //cout << "atMostK: " << atMostK << "  atMostKMinusOne: " << atMostKMinusOne << "\n";
        return atMostK - atMostKMinusOne;
    }
    
    // Returns Number of Subarrays with at most K Distint Integers
    int atMostKDistinct(vector<int>& nums, int k) {
        int left = 0;
        int numSubarrays = 0;
        unordered_map<int, int> freqMap;
        
        for(int right = 0; right < nums.size(); right++) {
            int rightNum = nums[right];
            freqMap[rightNum]++;
            
            while(freqMap.size() > k) {
                int leftNum = nums[left];
                freqMap[leftNum]--;
                if(freqMap[leftNum] == 0) {
                    freqMap.erase(leftNum);
                }
                left++;
            }
            
            // Add all subarrays ending at right
            numSubarrays += (right - left + 1);
        }
        return numSubarrays;
        
    }
};
