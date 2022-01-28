'''
Same as normal Topological Sort. 

If there is a cycle, then the length of the sorted order will not equal the number of tasks/vertices.
'''

from collections import deque

def is_scheduling_possible(tasks, prerequisites):
      sortedOrder = []
      sources = deque()
      graph = {i: [] for i in range(tasks)}
      inDegrees = {i: 0 for i in range(tasks)}

      # Build Graph and inDegrees
      for parent, child in prerequisites:
            graph[parent].append(child)
            inDegrees[child] += 1
      
      # Add all sources to queue
      for vertex, numInDegrees in inDegrees.items():
            if numInDegrees == 0:
                  sources.append(vertex)

      # While sources: pop source, add to sorted order
      # Decrement inDegrees. Add to sources if 0 inDegrees
      while sources:
            source = sources.popleft()
            sortedOrder.append(source)
            for vertex in graph[source]:
                  inDegrees[vertex] -= 1
                  if inDegrees[vertex] == 0:
                        sources.append(vertex)
      
      
      return tasks == len(sortedOrder)
  


def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()
