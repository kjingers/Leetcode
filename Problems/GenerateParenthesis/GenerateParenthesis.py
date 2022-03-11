'''
Thoughts: At each step, we have two options.   
    1. An open parenthesis. 
    2. If remaining closed paren > remaining open, then closed parenthesis
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.recursive_solve([], n, n, result)
        return result
        
        
    def recursive_solve(self, currList, remaining_open, remaining_closed, result):
        
        # Base Case
        if remaining_open == 0 and remaining_closed == 0:
            result.append(''.join(currList))
            return
        
        # Try Open Parenthesis
        
        if remaining_open > 0:
            currList.append('(')
            self.recursive_solve(currList, remaining_open - 1, remaining_closed, result)
            currList.pop()
        
        if remaining_closed > remaining_open:
            currList.append(')')
            self.recursive_solve(currList, remaining_open, remaining_closed - 1, result)
            currList.pop()
            
        return
        
        
        
        
