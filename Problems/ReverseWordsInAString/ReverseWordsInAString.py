'''
It's not possible for O(1) solution in-place in Python, since strings are immutable
'''

# Using Python Built-ins
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        r = s.split()[::-1]
        return ' '.join(r)
'''
    
# Using reverse then reverse algo. Not actually constant space

class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s[::-1])
        
        l, r, i = 0, 0, 0
        n = len(s)
        
        while i < n:
            
            # Fill the word. Make r point to space after current word
            while i < n and s[i] != ' ':
                s[r] = s[i]
                r += 1
                i += 1
            
            # We have word to process word
            if l < r:
                s[l:r] = list(reversed(s[l:r]))
                
                if r == n:
                    break
                    
                s[r] = ' '
                r += 1
                l = r
            i += 1

        # Get rid of tailing space
        if r > 0 and s[r - 1] == ' ':
            r -= 1
            
        return ''.join(s[:r])
        
                
                
        
