'''
Standard Sliding Window.
d.values() runs in o(N) time, so better to keep track of the max value in a variable in each loop

Time: O(N)
Outer loop runs N times. But the inner loop only processes each letter once. So it's O(N + N) -> O(N)
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        start = 0
        d = {}
        maxLen = 0
        maxCount = 0
        for end in range(len(s)):
            endChar = s[end]
            
            if endChar not in d:
                d[endChar] = 0
            
            d[endChar] += 1
            
            maxCount = max(maxCount, d[endChar])
            
            # Window Size - max value in d is the number of other characters that need to be replaced
            while (end - start + 1) > (maxCount + k):
                startChar = s[start]
                
                d[startChar] -= 1
                
                start += 1
            
            maxLen = max(maxLen, end - start + 1)
            
        return maxLen
        
