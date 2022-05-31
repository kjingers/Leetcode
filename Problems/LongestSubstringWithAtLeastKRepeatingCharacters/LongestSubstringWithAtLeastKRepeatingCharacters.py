'''
"Longest Substring" Makes me first consider sliding window. Can I enlarge window and then invalidate it to shrink?

Tricky, must do multiple sliding windows, ranging from unqiues 1 to num_uniques.
    - So for each "num_uniques", check all substrings with "num_unqiues" unqiue characters
    - Keep track of number of unique characters and number of characters that occur k or more times
    - If we don't yet have "num_unqiues" unqiue characters, then need to grow window
    - 
'''

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        num_uniques = len(set(s))
        result = 0
        
        # Check all substrings with "unique_check" unique characters only
        for unique_check in range(1, num_uniques + 1):
            
            curr_uniques = 0
            num_found = 0
            counts = [0 for _ in range(26)]
            start = 0
            
            # Now Sliding Window
            for end in range(len(s)):
                
                index = ord(s[end]) - ord('a')
                counts[index] += 1
                
                if counts[index] == 1:
                    curr_uniques += 1
                if counts[index] == k:
                    num_found += 1
                    
                # Shrink Window if curr_unqiues > unique_check
                # This go round, we only want "unqiue_check" unique characters
                while curr_uniques > unique_check:
                    index = ord(s[start]) - ord('a')
                    counts[index] -= 1
                    if counts[index] == 0:
                        curr_uniques -= 1
                    if counts[index] == k - 1:
                        num_found -= 1
                    start += 1
                        
                if num_found == unique_check:
                    result = max(result, end - start + 1)
        
        return result
                        
                    
        
        
        
