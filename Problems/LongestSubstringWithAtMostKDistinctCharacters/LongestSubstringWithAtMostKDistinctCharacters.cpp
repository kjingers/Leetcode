class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        int windowStart = 0;
        int maxSize = 0;
        unordered_map<char, int> charFrequencyMap;
        
        for(int windowEnd = 0; windowEnd < s.length(); windowEnd++) {
            char rightChar = s[windowEnd];
            charFrequencyMap[rightChar]++;
            
            while((int)charFrequencyMap.size() > k) {
                char leftChar = s[windowStart];
                charFrequencyMap[leftChar]--;
                if(charFrequencyMap[leftChar] == 0) {
                    charFrequencyMap.erase(leftChar);
                }
                windowStart++;
            }
            maxSize = max(maxSize, windowEnd - windowStart + 1);
            
                
        }
        return maxSize;
            
        
    }
};
