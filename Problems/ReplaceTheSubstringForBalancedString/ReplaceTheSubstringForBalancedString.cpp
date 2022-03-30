/*
So, we want to find the smallest substring, where when it's removed, the rest of the string has letter counts <= n / 4.
Sliding window can achieve this. Letters in window can be subtracted counts from hash map.

*/

class Solution {
public:
    int balancedString(string s) {
        
        unordered_map<char, int> cnts;
        int n = s.length();
        int k = n / 4;
        int start = 0;
        int res = n;
        
        
        for(const auto& c : s) {
            cnts[c]++;
        }
        
        
        for(int end = 0; end < s.length(); end++) {
            char rightChar = s[end];
            cnts[rightChar]--;
            
            // Shrink Window
            while(start < n && cnts['Q'] <= k && cnts['W'] <= k && cnts['E'] <= k && cnts['R'] <= k) {
                res = min(res, end - start + 1);
                cnts[s[start]]++;
                start++;
            }
        }
        return res;
        
    }
};
