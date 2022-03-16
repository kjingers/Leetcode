'''

Dynamic programming. Default lostPos to -1, for index just before start of array 0.

At each char, we
    - Subtract previous contributions of char in substring
    - calc # substrings where char is unique (i - lastPos)
    - Add new contributions to runningTotal
    - update new lastPos for char
    - increment res

At each loop, the calculated currTotal is the sum number of unique chars in all substrings ending at i.

'''

# Tracking contribution of each character for each substring ending at i
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        
        contributions = [0 for _ in range(26)]
        lastPos = [-1 for _ in range(26)]
        currTotal = 0
        res = 0
        
        for i, char in enumerate(s):
            char_idx = ord(char) - ord('A')
            currTotal -= contributions[char_idx]
            contributions[char_idx] = i - lastPos[char_idx]
            currTotal += contributions[char_idx]
            lastPos[char_idx] = i
            res += currTotal
            
        return res



        
        
