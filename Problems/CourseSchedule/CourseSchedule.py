'''
Topological Sort. If len(sortedList) == numCourses, then we can finish all the courses.

Topological Sort:
1. Initialize Graph and inDegrees
2. Build Graph and inDegrees
3. Add sources to queue
4. For each source, for each of it's children:
- Add to sortedOrder output
- "Remove" Source by decrementing inDegrees for each child
- If inDegrees is 0, then child is now a source so add to queue

Time Complexity: O(V + E)
'''
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # 1. Initialize graph and inDegrees
        graph = {i:[] for i in range(numCourses)}
        inDegrees = {i:0 for i in range(numCourses)}
        
        # 2. Build graph and inDegrees
        for child, parent in prerequisites:
            graph[parent].append(child)
            inDegrees[child] += 1
            
        # 3. Put sources in queue
        sources = deque()
        for vertex, val in inDegrees.items():
            if val == 0:
                sources.append(vertex)
                
        # 4. Go through sources, build sortedOrder
        sortedOrder = []
        while sources:
            course = sources.popleft()
            sortedOrder.append(course)
            for child in graph[course]:
                inDegrees[child] -= 1
                if inDegrees[child] == 0:
                    sources.append(child)
                    
        if len(sortedOrder) == numCourses:
            return True
    
        return False
                
        
        
