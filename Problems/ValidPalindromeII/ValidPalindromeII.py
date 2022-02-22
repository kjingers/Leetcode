'''
Similar to the standard two pointer. But, if we find a mismatch, we try to check if skipping the left index
provides a valid palindrome, or skipping the right index. Aka
    - If s[i] != s[j], return s[i+1:j+1] or s[i:j]
'''

# Generalized to k deletes

class Solution:
    def validPalindrome_rec(self, s, left, right, deletes) -> bool:
        
        while left <= right:
            
            if s[left] != s[right]:
                
                if deletes == 0:
                    return False
                
                return self.validPalindrome_rec(s, left + 1, right, deletes - 1) or \
                        self.validPalindrome_rec(s, left, right - 1, deletes - 1)
            left += 1
            right -= 1
            
        return True
    
    def validPalindrome(self, s: str) -> bool:
        return self.validPalindrome_rec(s, 0, len(s) - 1, 1)
            

'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left <= right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
            left += 1
            right -= 1
            
        return True
            
    def isPalindrome(self, s, i, j):
        
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
            
        return True
'''
        
