"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        idMap = {}
        
        for i, e in enumerate(employees):
            idMap[e.id] = e
            
        return self.dfs(id, idMap)
            
    def dfs(self, empID, idMap):
        
        subSum = 0
        
        for sub in idMap[empID].subordinates:
            subSum += self.dfs(sub, idMap)
            
        return idMap[empID].importance + subSum
        
