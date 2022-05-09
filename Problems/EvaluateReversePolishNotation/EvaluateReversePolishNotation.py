'''
["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
'''


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = deque()

        for token in tokens:
            if token in "+-*/":
                right_num = stack.pop()
                left_num = stack.pop()
                if token == '+':
                    stack.append(left_num + right_num)
                elif token == '-':
                    stack.append(left_num - right_num)
                elif token == '*':
                    stack.append(left_num * right_num)
                else:
                    #print(float(left_num) / right_num)
                    #print(int(float(left_num) / right_num))
                    stack.append(int(float(left_num) / right_num))
            else:
                stack.append(int(token))

        return stack.pop()

        
