'''
First add to set for Constant lookup time.

Loop through each word and see if it can be made up of other words. Backtracking solution.

Time = O(n * k) Where n is num of words and k is lenth of word

Not sure if can memoize, because we remove different words from set each time

Option 2: Use Bottom Up solution from WOrd Break I and buid on that with backtracking.
'''

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordDict = set(words)
        res = []
        
        for word in words:
            if len(word) == 0:
                continue
                
            wordDict.remove(word)
            
            if self.wordBreak(word, wordDict):
                res.append(word)
            
            wordDict.add(word)
            
        return res
        
        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        #wordSet = set(wordDict)
        
        for i in range(len(s)):
            if dp[i]: # Only check if words match up to previous index
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] in wordDict:
                        dp[j] = True
        
        return dp[-1]


'''
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        wordDict = set(words)
        res = []
        
        for word in words:
            wordDict.remove(word)
            
            if self.check(word, wordDict):
                res.append(word)
            
            wordDict.add(word)
            
        return res
    
    
    def check(self, word, wordDict):
        
        # Base Case
        if word in wordDict:
            return True
        
        # Loop backwards in word. If you find a prefix that is in dict, and the remaining suffix
        # can be made up of words in dict, then return True
        # Example: When i = 3, word[:i] = "cat", word[i:] = "dog", so will return True
        # Key is, must beck if prefix is in d, since there must be a prefix that is directly in d
        for i in range(len(word), 0, -1):
            if word[:i] in wordDict and self.check(word[i:], wordDict):
                return True
        
        return False
'''

           
            
        
        
