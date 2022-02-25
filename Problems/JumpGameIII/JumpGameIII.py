'''
Since we can ONLY jump to i + arr[i] or i - arr[i], then we can't use greedy approach like other jump games.
In this case, at each index, we only have 2 options. So, we can do BFS similar to tree traversal, since we only
have 2 options.

    - Must keep track of visited using a set, or make elements in array negative in-place
'''

from collections import deque

# Iterative BFS

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()
        seen.add(start)
        
        queue = deque([start])
        
        while queue:
            
            index = queue.popleft()
            
            if arr[index] == 0:
                return True
            
            for j in (index - arr[index], index + arr[index]):
                if j < 0 or j >= len(arr) or j in seen:
                    continue
                seen.add(j)
                queue.append(j)
                
        return False


# Recursive DFS
'''
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()
        return self.dfs(arr, start, seen)
        
    def dfs(self, arr, index, seen):
        
        if index < 0 or index >= len(arr) or index in seen:
            return False
        
        if arr[index] == 0:
            return True
        
        seen.add(index)
        
        return self.dfs(arr, index + arr[index], seen) or self.dfs(arr, index - arr[index], seen)
'''
        
                    
