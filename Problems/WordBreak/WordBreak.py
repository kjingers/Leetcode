'''
Brute-force: From start, iterate end index and check if substring matches a word in wordList. If so, recursively solve with updated start. Base case: if start is equal to len(s), return true

We can memoize. Since a given dp[end] = True if dp[start - 1] = True

Bottom up / BFS is more intuitive.
'''

# Bottom-up. start with dp[0] = True
# Starting from True Index, check if subtring is in wordDict. If so, mark word end index True.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        wordSet = set(wordDict)
        
        for i in range(len(s)):
            if dp[i]: # Only check if words match up to previous index
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] in wordSet:
                        dp[j] = True
        
        return dp[-1]


# Brute Force
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        
        return self.solve(s, set(wordDict), 0)
          
    def solve(self, s, wordDict, start):
        
        # Base case
        if start == len(s):
            return True
        
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordDict:
                return self.solve(s, wordDict, end)
            
        return False
        
'''
        
