'''
Iterate through string. 
    - If same as prevChar, then count += 1.
    - If not, then print char followed by count if > 1
        - For count >= 10, must increment index more than one time
        
Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if len(chars) < 2:
            return len(chars)
        
        outIndex = 0
        prevChar = chars[0]
        count = 1
        
        for i in range(1, len(chars)):
            
            if chars[i] == prevChar:
                count += 1
            else:
                outIndex = self._to_output(chars, prevChar, outIndex, count)
                count = 1
                prevChar = chars[i]
        
        outIndex = self._to_output(chars, prevChar, outIndex, count)
                
        return outIndex
                    
    
    # Inserts character and count to list. Returns updated outputIndex
    def _to_output(self, chars, char, index, count):
        chars[index] = char
        index += 1
        if count > 1:
            for c in str(count):
                chars[index] = c
                index += 1
            
        return index
        
