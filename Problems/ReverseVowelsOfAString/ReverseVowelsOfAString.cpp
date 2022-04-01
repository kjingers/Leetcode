

class Solution {
public:
    string reverseVowels(string s) {
        int left = 0;
        int right = s.length() - 1;
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        
        while(left < right) {
            while(left < right && vowels.find(tolower(s[left])) == vowels.end()) {
                left++;
            }
            while(left < right && vowels.find(tolower(s[right])) == vowels.end()) {
                right--;
            }
            swap(s[left], s[right]);
            left++;
            right--;
        }
        return s;
        
    }
};
