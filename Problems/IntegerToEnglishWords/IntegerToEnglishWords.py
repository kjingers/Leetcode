'''
0 <= num <= 2^31 - 1, so up to billions

Recusive Solution:

If > 1 billion: Call helper(# billions) + "Billion" + helper(num % billion)


The num >= 100 and nums >= 20 cases need right space stripped off, because the second helper function may not return anything.
This is handled in all larger cases, because, all larger calls end up in the >= 100 and >= 20 case
'''

class Solution:
     
    def __init__(self):
        
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
        self.ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", \
                     "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    
    
    def numberToWords(self, num: int) -> str:
        
        if num == 0:
            return "Zero"
        
        return self.helper(num).rstrip()
        
        
    def helper(self, num):
        

        
        if num >= 1000000000:
            return self.helper(num // 1000000000) + " Billion " + self.helper(num % 1000000000)
        
        if num >= 1000000:
            return self.helper(num // 1000000) + " Million " + self.helper(num % 1000000)
        
        if num >= 1000:
            return self.helper(num // 1000) + " Thousand " + self.helper(num % 1000)
        
        if num >= 100:
            return (self.helper(num // 100) + " Hundred " + self.helper(num % 100)).rstrip()
        
        if num >= 20:
            return (self.tens[num // 10] + " " + self.helper(num % 10)).rstrip()
        
        return self.ones[num]
        
        
    
    
        
