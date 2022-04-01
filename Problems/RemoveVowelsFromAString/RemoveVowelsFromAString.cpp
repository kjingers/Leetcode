/*
Two Pointers:
    - Left points to current place in output string.
    - Right iterates through string
    - If consonant, then swap s[right], s[left] and increment both
    - If vowel, then increment right pointer only
*/

class Solution {
public:
    string removeVowels(string s) {
        int left = 0;
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};

        for(int right = 0; right < s.length(); right++) {
            
            // If consonant
            if(vowels.find(s[right]) == vowels.end()) {
                swap(s[left++], s[right]);
            }

        }
        
        // Now left is pointing to index of first vowel, which is also the size of new string
        s.resize(left);
        return s;
        
        
        
    }
};
