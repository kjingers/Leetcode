'''
This problem requires topological sort in addition to subsets algorithm.

We will generate the graph and inDegrees and initial sources like usual.
For this one, we will create a function that we will call recursively.
- We will loop through all the sources and call the recursive function for each source.
- After the recursive call, we will backtrack - removing the vertex from the output sortedOrder
- If len(sortedOrder) == tasks, then we have a valid order of tasks, so print


'''
from collections import deque

def print_orders(tasks, prerequisites):
  sources = deque()
  sortedOrder = []

  # 1. Initialize graph and inDegrees
  graph = {i: [] for i in range(tasks)}
  inDegrees = {i: 0 for i in range(tasks)}

  # 2. Build graph and inDegrees
  for parent, child in prerequisites:
    graph[parent].append(child)
    inDegrees[child] += 1

  # 3. Add initial sources
  for vertex in inDegrees:
    if inDegrees[vertex] == 0:
      sources.append(vertex)

  # 4. Call recursive function with initial sources and empty sortedOrder
  print_all_orders_rec(graph, inDegrees, sources, sortedOrder)
  
def print_all_orders_rec(graph, inDegrees, sources, sortedOrder):
  if sources:

    # Loop through all current sources.
    # We will call recursively to get all combinations where the next vertex
    # in the soortedOrder is the current vertex
    for vertex in sources:

      # Make copy of sources. Remove current vertex
      nextSources = deque(sources)
      nextSources.remove(vertex)

      sortedOrder.append(vertex)

      # Update inDegrees. Update nextSources in necessary
      for child in graph[vertex]:
        inDegrees[child] -= 1
        if inDegrees[child] == 0:
          nextSources.append(child)

      # Call this funtion recursively
      print_all_orders_rec(graph, inDegrees, nextSources, sortedOrder)

      # Backtrack - Remove current vertex from sortedOrder and replace routes
      # By incrementing inDegrees
      sortedOrder.pop()
      for child in graph[vertex]:
        inDegrees[child] += 1

  if len(sortedOrder) == len(graph):
    print(sortedOrder)

def main():
  print("Task Orders: ")
  print_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
