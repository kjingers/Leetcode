'''
Can use same idea as Basic Calculator II, where we don't have brackets. When we see bracket, we call our function recursively.
    - Want to end with sum of values. Calc * and / first
'''

class Solution:
    def calculate(self, s: str) -> int:
        return self.calc_rec(s, 0)
    
    
    # Process inner bracket equation recursively.
    def calc_rec(self, s: str, index: int):
        
        stack = deque()
        num = 0
        operator = "+"
        
        while index < len(s):
            if s[index].isdigit():
                num = 10*num + int(s[index])
            elif s[index] in "+-*/":
                self.update(stack, operator, num)
                num = 0
                operator = s[index]
            elif s[index] == '(': # Recursively solve. Jump ahead
                num, j = self.calc_rec(s, index + 1)
                index = j
            elif s[index] == ')':
                self.update(stack, operator, num)
                return sum(stack), index
            index += 1
        
        self.update(stack, operator, num)
        return sum(stack)
    
    def update(self, stack, operator, num):
        if operator == '+':
            stack.append(num)
        elif operator == '-':
            stack.append(-num)
        elif operator == '*':
            stack.append(stack.pop() * num)
        else:
            stack.append(int(float(stack.pop()) / num))
                
            
        
        
        
    
        
