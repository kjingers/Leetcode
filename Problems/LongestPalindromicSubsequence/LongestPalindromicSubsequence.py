'''
Brute Force Top-Down:

Start with two pointers, one at each end. At each step, we check if substring is a palindrome:
    1.  If s[left] == s[right], then we can recursively call to check if the rest of the substring is a palindrome.
        If it is, then return 2 + remainingLength
    2. We make two recursivecalls skipping either the beginning or the end. Return the max of these two.
    
Better method is to try all i and j in main loop, so that we can keep track of max length and update
return string accordingly.

Since Top-down gets TLE, must use bottom-up.

if s[startIndex] == s[endIndex], and 
        if the remaing string is of zero length or dp[startIndex+1][endIndex-1] is a palindrome then
   dp[startIndex][endIndex] = true
   
And, when startIndex == endIndex, then True. So we can fill out dp[i][i] = True. And start from there
to fill out the rest of the dp table.

Only filling out top right of table, where end >= start
    

'''

# Bottom up

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        maxLen = 1
        start = 0
        res = ""
        
        # True when start == end, since all 1 length strings are palindromes
        for i in range(len(s)):
            dp[i][i] = True
            
        # Need to fill top-right of dp. So need to start where i == j and move towards right,
        # since we know when i == j then dp[i]j[] = True, we can use that to solve the subsequent problems
        # Also, since we need dp[start + 1][end - 1] to solve problem, it makes sense to loop start down
        # (so that we know start + 1) and loop end up (so that we know end - 1)
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                
                if s[i] == s[j]:
                    # If 2 character string, or inner string is true, then set to true
                    #print("i: " + str(i) + "  j: " + str(j))
                    
                    if (j - i) == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if (j - i + 1) > maxLen:
                            maxLen = j - i + 1
                            start = i
                                        
        return s[start:start + maxLen]
        
        
        


'''
# Top Down (TLE)
# Must keep track of maxLen in main loop. So have to try i and j in main loop
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        dp = [[-1 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
        
        res = ""
        maxLen = 0
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j, dp):
                    if (j - i + 1) > maxLen:
                        maxLen = (j - i + 1)
                        res = s[i:j+1]
                        
        return res
        
        
        
    def isPalindrome(self, s, i, j, dp):
        
        if i > j:
            dp[i][j] = True
            return True
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        if s[i] != s[j]:
            dp[i][j] = False
            return False
        
        dp[i][j] = self.isPalindrome(s, i + 1, j - 1, dp)
        return dp[i][j]
'''  
        
        
    
        

        
        
