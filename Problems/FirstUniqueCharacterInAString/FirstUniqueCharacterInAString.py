'''
Pretty simple so options are:

1. Normal Sort, then check which letter is not same as prev. Always skip ahead to last instance of letter before checking
2. Bucket Sort. First bucket with len 1 is first unique
3. Two passes. First pass, count num occurances of each char. Next pass, if unique, return index. Can use arrays for faster indexing

'''

    
# Using Dict - simpler
class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_counts = Counter(s)
        
        for i, ch in enumerate(s):
            if letter_counts[ch] == 1:
                return i
        
        return -1
    
# Keeping counts in hash map using array
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        letter_counts = [0 for _ in range(26)]
        
        for ch in s:
            letter_counts[ord(ch) - ord('a')] += 1
        
        for i, ch in enumerate(s):
            if letter_counts[ord(ch) - ord('a')] == 1:
                return i
        
        return -1
'''
        
        
        
        
