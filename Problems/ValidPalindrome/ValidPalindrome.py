'''
Two Pointer from beginning and end. We loop each pointer until we get a a letter or digit.
Compare char/digit. Then move each pointer to next char/digit.

Note: Us .isalnum() to check if number or letter


'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s) - 1
        
        while left < right:
            
            while left < right and not s[left].isalnum():
                left += 1
                
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].upper() != s[right].upper():
                return False
            
            left += 1
            right -= 1
            
        return True
                
        
        
        
