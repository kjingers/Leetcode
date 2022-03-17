'''
Can use many different solutions

minHeap: O(nLogk)
minHeap is definitely the easiest to implement

quickselect: O(n) on average

bucketsort: O(n)

1. Create n buckets, since the frequency for any element cannot exceed n
2. Create counts dict
3. Put elements to bucket based on freq
4. Starting from right (highest freq), add to output list

Bucket sort is good too since we don't have to sort each bucket
'''


from collections import Counter
from heapq import *

# Bucket Sort
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = [[] for _ in range(len(nums) + 1)]
        counts = Counter(nums)
        res = []
        
        for num, cnt in counts.items():
            buckets[cnt].append(num)
            
        for i in range(len(nums), -1, -1):
            bucket = buckets[i]
            if bucket:
                for num in bucket:
                    res.append(num)
                    
        return res[:k]
'''
'''
# Using minHeap    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        minHeap = []
        
        for num, cnt in counts.items():
            heappush(minHeap, (cnt, num))
            
            if len(minHeap) > k:
                heappop(minHeap)
                
        return [num for (_, num) in minHeap]
'''
    
# Using Quick Select
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        cntk = self.quickSelect(list(counts.values()), k)
        
        return [num for num, cnt in counts.items() if cnt >= cntk]
        
        
    def quickSelect(self, cnts, k):
        pivot = random.choice(cnts)
        
        left = [x for x in cnts if x > pivot]
        right = [x for x in cnts if x < pivot]
        mid = [x for x in cnts if x == pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.quickSelect(left, k)
        elif k > L + M:
            return self.quickSelect(right, k - L - M)
        else:
            return mid[0]
        

        
