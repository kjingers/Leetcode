'''
Brute Force works for this problem, since the max array length is 16 characters, out time complexity is bounded by: O(2^16), if we had all 1 character arrays.

Brute Force method. For each string:
    - First, skip if it has repeasting characters
    - Then, for each string in dp, if no overlapping characters, append the union
    - Max length in dp is answer
    
DFS + Backtracking solution is more intuitive.
    - For each index, we try solving by taking the current index, or skipping
'''

# DFS + Backtracking solution
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        #self.maxLen = 0
        maxLen = self.dfs(arr, "", 0)
        return maxLen
        
    def dfs(self, arr, st, index):
        
        if len(set(st)) < len(st):
            return 0
        
        #self.maxLen = max(self.maxLen, len(st))
        ret = len(st)
        
        for i in range(index, len(arr)):
            ret = max(ret, self.dfs(arr, st + arr[i], i + 1))
            
        return ret
    
    
# Brute Force - Set Solution
'''
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = []
        # Start with empty set, so that we have something to add to for subsets
        dp.append(set())
        
        for st in arr:
            
            # If string has duplicate letters, just skip
            if len(set(st)) < len(st):
                continue
                
            setst = set(st)
            
            for s in dp:
                if s & setst:
                    continue
                dp.append(setst | s)
                
        return max(len(s) for s in dp)
'''
    
            

        
                
        
