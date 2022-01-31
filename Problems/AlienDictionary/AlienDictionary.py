'''
Similar to typical topological sort problem. 
Main difference is that we don't have the prerequisite pairs. To build the graph, we
must compare all adjacent word pairs. Compare letter by letter until a letter is different.
The different character in the left word is a parent, and the different character in the right
word is the child.

'''

from collections import deque

def find_order(words):
  sortedOrder = []
  sources = deque()


  # Initialize Graph and inDegrees
  graph = {}
  inDegrees = {}

  # Make sure each distint character is a key in both maps
  for word in words:
    for char in word:
      graph[char] = []
      inDegrees[char] = 0

  # Build Graph and inDegrees by comparing adjacent word pairs
  for i in range(len(words)- 1):
    w1, w2 = words[i], words[i+1]
    for j in range(min(len(w1), len(w2))):
      parent = w1[j]
      child = w2[j]
      if parent != child:
        if child not in graph[parent]:
          graph[parent].append(child)
          inDegrees[child] += 1
        break
  
  # Add Sources
  for vertex in inDegrees:
    if inDegrees[vertex] == 0:
      sources.append(vertex)

  # While sources, process each source
  while sources:
    source = sources.popleft()
    sortedOrder.append(source)
    for child in graph[source]:
      inDegrees[child] -= 1
      if inDegrees[child] == 0:
        sources.append(child)

  if len(sortedOrder) != len(graph):
    return ""

  return ''.join(sortedOrder)


def main():
  print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
  print("Character order: " + find_order(["cab", "aaa", "aab"]))
  print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()
