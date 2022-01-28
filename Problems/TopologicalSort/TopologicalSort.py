from collections import deque

def topological_sort(vertices, edges):
  sortedOrder = []
  sources = deque()
  graph = {}
  inDegrees = {}
  
  # If the number of vertices is 0, return empty list
  if vertices <= 0:
    return sortedOrder


  # Initialize Adjacency List and Indegrees Hashmap
  graph = {i: [] for i in range(vertices)}
  inDegrees = {i: 0 for i in range(vertices)}

  # Build the graph and Indegrees Hashmap
  for parent, child in edges:
    graph[parent].append(child)
    inDegrees[child] += 1

  # Add sources to source queue
  for vertex in inDegrees:
    if inDegrees[vertex] == 0:
      sources.append(vertex)

  # While source queue, pop source. 
  # - Add to sourtedOrder list
  # - Decrement indegrees map
  # - If 0 indegrees, add to sources queue
  while sources:
    source = sources.popleft()
    sortedOrder.append(source)
    for child in graph[source]:
      inDegrees[child] -= 1
      if inDegrees[child] == 0:
        sources.append(child)

  return sortedOrder


def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
