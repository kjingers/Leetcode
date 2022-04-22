'''
First add to set for Constant lookup time.

Loop through each word and see if it can be made up of other words. Backtracking solution.

Time = O(n * k) Where n is num of words and k is lenth of word

Not sure if can memoize, because we remove different words from set each time
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
           
            
        
        
