'''
For this, we can to find a complete order of the alphabet. From the input sorted words, we can figure out
the order of some of the letters. We can put these orders into a graph (adjacency list) and perform
Topological Sort.
'''

from collections import deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        graph = {}
        inDegrees = {}
        sortedOrder = []
        
        # Initialize graph and inDegrees with a key for each distinct character
        for word in words:
            for char in word:
                graph[char] = []
                inDegrees[char] = 0
                
        for i in range(1, len(words)):
            left = words[i - 1]
            right = words[i]
            
            for j in range(min(len(left), len(right))):
                if left[j] != right[j]:
                    if right[j] not in graph[left[j]]:
                        graph[left[j]].append(right[j])
                        inDegrees[right[j]] += 1
                    break
                # If word2 is a subset of word1 (ex "abc, "ab"), then this cannot be
                # a valid sorted order of words. return
                elif j == min(len(left), len(right)) - 1 and len(left) > len(right):
                    return ""
                              
        print(graph)
        
        # Put Sources into queue
        sources = deque()
        for vertex, inD in inDegrees.items():
            if inD == 0:
                sources.append(vertex)
                
        
        while sources:
            source = sources.popleft()
            sortedOrder.append(source)
            for child in graph[source]:
                inDegrees[child] -= 1
                if inDegrees[child] == 0:
                    sources.append(child)
                    
        
        return ''.join(sortedOrder) if len(sortedOrder) == len(graph) else ""
            
            
        
                
        
                
        
