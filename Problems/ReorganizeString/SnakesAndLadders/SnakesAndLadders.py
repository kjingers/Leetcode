'''
"Least Number of steps" makes me think BFS. Looks like only bottom of ladder takes to top. And only head of snake takes to tail. 
    - Use set to avoid revisiting
    - No need to backtrack since we are using bfs. Each cell we visit is visited in the fewest number of steps
    - Can treat as 1D array, since we only move between curr + 1 to curr + 6
    - 
'''

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        num_cells = n ** 2
        jumps = {}
        #jumps = defaultdict(int)
        
        
        # Build dictionary of snake/ladder jumps
        for i in range(n):
            for j in range(n):
                if board[i][j] != -1:
                    tile = self.map_to_tile(i, j, n)
                    jumps[tile] = board[i][j]
        #print(jumps)
        
        
        # BFS
        
        number_of_jumps = 0
        queue = deque()
        seen = set()
        seen.add(1)
        queue.append(1)
        
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                curr_pos = queue.popleft()

                if curr_pos == num_cells:
                    return number_of_jumps
                


                for i in range(1, 7):
                    next_pos = curr_pos + i
                    if next_pos in jumps:
                        next_pos = jumps[next_pos]

                    if next_pos > num_cells or next_pos in seen:
                        continue

                    seen.add(next_pos)
                    queue.append(next_pos)
                        
            number_of_jumps += 1
            
        return -1
                        
                        
                                
                
    def map_to_tile(self, row, col, n):
        left_to_right = ((n - 1 - row) % 2 == 0)
        if left_to_right:
            return (n - 1 - row) * n + (col + 1)
        else:
            return (n - 1 - row) * n + (n - col)
        
        
                
        
        
        
        
