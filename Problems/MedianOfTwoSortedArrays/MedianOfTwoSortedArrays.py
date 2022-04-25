'''
Basically, if we need the find kth value, then we compare A[k//2] and B[k//2]. If A[k//2] < B[k//2], Then we know we can eliminate A[0:k//2].

Another solution is to get medium of both arrays. 
    - If median indexes are less than k, then we can eliminate the smaller first half and shrink k. 
    - If median indexes are greater than k, then we can eliminate the larger second half and keep k.
    
The general idea is, we need to find k. So, we get median of both arrays. Based on median values, we can eliminate half of one of the arrays.
    - if median indexes sum are < k, then we know that median does not reside in elements before and including smaller median
    - if median indexes sum are >= k, then we know that median is <= larger median. So we can eliminate elements past greater median.
'''

# 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        
        # If Odd
        if l % 2:
            return self.kth(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, l // 2)
        else:
            middle1 = self.kth(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, (l // 2) - 1)
            #print(middle1)
            middle2 = self.kth(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, l // 2)
            return (middle1 + middle2) / 2.0
        
    def kth(self, A, start1, end1, B, start2, end2, k):
        
        #print(start1, end1, start2, end2, k)
        
        # If No more from A, then we know we've eliminated "start1" smaller values from k
        if start1 > end1:
            return B[k - start1]
        
        if start2 > end2:
            return A[k - start2]
        
        
        middle1 = (end1 + start1) // 2
        middle2 = (end2 + start2) // 2
        
        middleValue1 = A[middle1]
        middleValue2 = B[middle2]
        
        # Sum of median indexes less than k. 
        # So, the smaller of the medians can be ruled out since all of these values are guarenteed smaller than median
        if middle1 + middle2 < k:
            if middleValue1 > middleValue2:
                return self.kth(A, start1, end1, B, middle2 + 1, end2, k)
            else:
                return self.kth(A, middle1 + 1, end1, B, start2, end2, k)
            
        # Sum of median index >= k
        # The array with larger median - that median value is >= true median value. So we can safely remove everything past median's index
        else:
            if middleValue1 > middleValue2:
                return self.kth(A, start1, middle1 - 1, B, start2, end2, k)
            else:
                return self.kth(A, start1, end1, B, start2, middle2 - 1, k)
        
        
        
        
        

# Recursive Solution with Array Slicing
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        # These will be same if total is odd
        leftMid = (m + n + 1) // 2
        rightMid = (m + n + 2) // 2
        
        return (self.getKth(nums1, nums2, leftMid) + self.getKth(nums1, nums2, rightMid)) / 2.0
        
    def getKth(self, A, B, k):
        
        # Base Cases
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]
        
        if k == 1:
            return min(A[0], B[0])
        
        
        m = len(A)
        n = len(B)
        
        aCmp = min(m, k // 2)
        bCmp = min(n, k // 2)
        
        # Can eliminate B[:bCmp]
        if A[aCmp - 1] > B[bCmp - 1]:
            return self.getKth(A, B[bCmp:], k - bCmp)
        else:
            return self.getKth(A[aCmp:], B, k - aCmp)
'''
            
        
        
