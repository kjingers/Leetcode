'''
Easiest: Sort then pick num[n - k]

Using maxheap:
Keep a heap of size k. Keep inserting and popping if heap > k.

'''

from heapq import *

# Using Heap
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        
        for num in nums:
            heappush(minHeap, num) 
            if len(minHeap) > k:
                heappop(minHeap)
        
        return minHeap[0]
'''
    
    
# Using Quick Select    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelectK(nums, k)
    
    def quickSelectK(self, nums, k):
        pivot = random.choice(nums)
        left = [x for x in nums if x > pivot]
        right = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.quickSelectK(left, k)
        elif k > L + M:
            return self.quickSelectK(right, k - L - M)
        else:
            return mid[0]
            
        
