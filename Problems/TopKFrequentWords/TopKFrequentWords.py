'''
Of course can use minHeap to keep track of k most frequent works
    - Might need to create class to sort lexicographically if frequencies are the same
    
Another option is to use bucket sort. Then, we would just need to sort each bucket.
    - I think at work, all works could be in the same bucket though
'''

from heapq import *
from collections import Counter


class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word
        
    def __lt__(self, other):
        return self.count < other.count or ((self.count == other.count) and (self.word > other.word))
        

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        minHeap = []
        
        counts = Counter(words)
        
        for word, count in counts.items():
            
            heappush(minHeap, Element(count, word))
            if len(minHeap) > k:
                heappop(minHeap)
                
        
        res = []
        
        while minHeap:
            res.append(heappop(minHeap).word)
            
        return reversed(res)
        
