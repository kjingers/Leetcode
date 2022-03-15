'''
Initial thought. Just perform all instructions 4 times. If we end up at the same spot, then return True.

Using dict or direction change. But can prbably use array with modulo to avoid two hash maps


Simplier solution:

Instead of hash maps, can just keep track of direction (dx, dy)
    - When right: dx = dy, dy = -dx
    - When left: dx = -dy, dy = dx
    
Also, just perform instructions once. After one run though, as long as we are not facing north, or if we are still at origin, we can return True.
'''

# Better
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dx, dy = 0, 1
        
        for i in instructions:
            if i == 'L':
                dx, dy = -dy, dx
            elif i == 'R':
                dx, dy = dy, -dx
            else:
                x += dx
                y += dy
        
        return True if (x, y) == (0, 0) or (dx, dy) != (0, 1) else False
        

# Initial Solution. Uses 4N space
'''
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        Left = {(0, 1) : (-1, 0), (-1, 0) : (0, -1), (0, -1) : (1, 0), (1, 0) : (0, 1)}
        Right = {}
        
        for k, v in Left.items():
            Right[v] = k
        
        # Start at origin
        x, y = 0, 0
        current_direction = (0, 1)
        
        instructions += instructions * 3
        
        for instruction in instructions:
            if instruction == 'L':
                current_direction = Left[current_direction]
            elif instruction == 'R':
                current_direction = Right[current_direction]
            else:
                x += current_direction[0]
                y += current_direction[1]
        
        return False if x or y else True
'''
            
            
        
