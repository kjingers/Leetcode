'''
The tricky part is knowing to represent equations as a directed, weighted graph.

From a, to b, edge weight: 2.0 Represented as graph[a] = [(b, 2.0)]
Also make edge from b to a with inverse value.

Once graph is made, for each query, we just traverse graph from first value to next value
'''


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        
        # Build Graph
        for i in range(len(equations)):
            f = equations[i][0]
            t = equations[i][1]
            v = values[i]
            
            graph[f].append((t, v))
            graph[t].append((f, 1/v))
        
        #print(dict(graph))
        res = []
        for f, t in queries:
            if f not in graph or t not in graph:
                res.append(-1.0)
                continue
            #print("From %s, To %s" % (f, t))
            res.append(max(-1.0, self.dfs(graph, f, t, 1.0, set([f]))))
        return res
        
    def dfs(self, graph, node, target, value, visited):
        
        #if target == "x4":
        #    print("Node: %s, Target: %s, Value: %d" % (node, target, value))
        
        #print("Node: ", node, "Target: ", target)
        ret = -float('inf')
        if node == target:
            return value
        
        for edge in graph[node]:
            if edge[0] in visited:
                continue
            visited.add(edge[0])
            ret = max(ret, self.dfs(graph, edge[0], target, value * edge[1], visited))
        
        return ret
        
            
            
        
