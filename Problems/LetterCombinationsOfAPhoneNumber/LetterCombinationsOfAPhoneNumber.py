'''
Just need all combinations of letters from the numbers.

Can have index into digits
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        self.mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        result = []
        if len(digits) == 0:
            return []
        
        self.recursive_solve(digits, 0, [], result)
        return result
        
    def recursive_solve(self, digits, dig_index, curr, result):
        
        # Base case
        if dig_index == len(digits):
            result.append(''.join(curr))
            return

        curr_num = int(digits[dig_index])
        curr_letters = self.mapping[curr_num]
        
        # Loop through each letter for current digit. Backtrack 
        for i in range(len(curr_letters)):
            #curr.append(curr_letters[i])
            #self.recursive_solve(digits, dig_index + 1, curr, result)
            #curr.pop()
            
            # If we don't want to backtrack, we can just copy a new list
            self.recursive_solve(digits, dig_index + 1, curr + [curr_letters[i]], result)

        
        return
                
            
            
        
