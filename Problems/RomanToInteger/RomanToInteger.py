'''
Symbol        Value
I               1
IV              4
V               5
IX              9
X               10
XL              40
L               50
XC              90
C               100
CD              400
D               500
CM              900
M               1000

For this one, we have two cases from left toright:
    - if s[i] < s[i + 1]: Then we need to subtract s[i]'s value
    - else, just add s[i]
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        
        for i in range(len(s) - 1):
            
            if roman_values[s[i]] < roman_values[s[i + 1]]:
                result -= roman_values[s[i]]
            else:
                result += roman_values[s[i]]
        
        result += roman_values[s[-1]]
        
        return result
        
