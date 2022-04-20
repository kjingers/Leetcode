'''
Tricky part is to get minimum value in constant time. We can store the minimum value with each value on the stack.

That way, tho get the minimum, we just have to look at the minimum value stored at the top.

To save space, we can have two stacks. One normal, and one decreasing stack with min value on top.
    - If we push a value that is <= top of min stack, then push to minStack too
    - If the value we pop is == value on top of minStack, then pop from minStack too
    
To further optimize, for min stack, we can store (val, count), rather repeatedly push min value.
'''

class MinStack:

    def __init__(self):
        self.stack = []
        
        

    def push(self, val: int) -> None:
        newMin = val if not self.stack else min(self.stack[-1][1], val)
        self.stack.append((val, newMin))
        
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
