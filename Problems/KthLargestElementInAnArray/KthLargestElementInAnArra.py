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
    
    



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth largest is n - k smallest
        n = len(nums)
        left = 0
        right = n - 1
        kth = 0
        while left <= right:
            pivot_index = self.partition(nums, left, right)
            if pivot_index == n - k:
                kth = nums[pivot_index]
                break
            elif pivot_index < n - k:
                left = pivot_index + 1
            else:
                right = pivot_index - 1
                
        return kth
        
    def partition(self, nums, left, right):
        pivot_index = random.randint(left, right)
        pivot = nums[pivot_index]
        
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        base = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[base], nums[i] = nums[i], nums[base]
                base += 1
                
        nums[right], nums[base] = nums[base], nums[right]
        
        return base
        
        
