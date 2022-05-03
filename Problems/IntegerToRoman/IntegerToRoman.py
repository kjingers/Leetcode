'''
Can use greedy apprach to always use the largest symbol possible. To make it easier, we can put "IV", "XL", and "CD" into the has map, so that we don't have to calculate the two roman digits seperately.

Instead of map, use list of tuples, so that we can loop from largest to biggest.

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
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_values = [("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10), 
                        ("XL", 40), ("L", 50), ("XC", 90), ("C", 100), ("CD", 400), 
                        ("D", 500), ("CM", 900), ("M", 1000)]
        
        # SHould have Did biggest to smallest...
        
        roman_values = roman_values[::-1]
        result = []
        
        for symbol, value in roman_values:
            
            if num == 0:
                break
                
            if value > num:
                continue
                
            count = num // value
                        
            result.append(symbol * count)
            
            num -= (value * count)
                
        return ''.join(result)
        
