'''
Can use minHeap and Euclidean distance.

Quick select is technically the fastest algo
'''

from heapq import *

# Using maxHeap
'''
class Point:
    def __init__(self, coord):
        self.x = coord[0]
        self.y = coord[1]
        self.dist = (self.x * self.x) + (self.y * self.y)
    
    # Use > since we want largest on top
    def __lt__(self, other):
        return self.dist > other.dist
    
    
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        
        for p in points:
            heappush(maxHeap, Point(p))
            
            if len(maxHeap) > k:
                heappop(maxHeap)
                
        res = []
        while maxHeap:
            p = heappop(maxHeap)
            res.append([p.x, p.y])
        
        return res
'''    
'''
# Using maxHeap without class definiton
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        euclidean = lambda x, y : x * x + y * y
        maxHeap = []
        
        for i, (x, y) in enumerate(points):
            d = euclidean(x, y)
            heappush(maxHeap, (-d, i))
            if len(maxHeap) > k:
                heappop(maxHeap)
                
        
        return [points[i] for (_, i) in maxHeap]
'''           


# Using Quickselect
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        euclidean = lambda x, y : x * x + y * y
        distances = [euclidean(p[0], p[1]) for p in points]
        dist = self.quickSelect(distances, k)
        
        return [p for p in points if euclidean(p[0], p[1]) <= dist]
        
    def quickSelect(self, distances, k):
        pivot = random.choice(distances)
        
        left = [x for x in distances if x < pivot]
        right = [x for x in distances if x > pivot]
        mid = [x for x in distances if x == pivot]
        
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.quickSelect(left, k)
        elif k > L + M:
            return self.quickSelect(right, k - L - M)
        else:
            return mid[0]
        
