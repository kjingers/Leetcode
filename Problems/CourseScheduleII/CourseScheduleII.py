'''
Top Sort problem, since we need order of DAG

Time COmplexity: O(V + E)
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        if numCourses == 1 and prerequisites is None:
            reuturn [0]
        
        graph = {i: [] for i in range(numCourses)}
        inDegrees = {i: 0 for i in range(numCourses)}
        
        for x in prerequisites:
            graph[x[1]].append(x[0])
            inDegrees[x[0]] += 1
        
        sources = deque()
        for v in inDegrees:
            if inDegrees[v] == 0:
                sources.append(v)
        
        res = []
        while sources:
            curr = sources.popleft()
            res.append(curr)
            
            for neighbor in graph[curr]:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    sources.append(neighbor)
                    
        return [] if len(res) != numCourses else res
                
            
        
