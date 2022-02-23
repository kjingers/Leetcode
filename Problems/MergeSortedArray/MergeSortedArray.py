'''
Use two pointers starting at the end of each array. And a third pointer pointing to the end of full size array 1.
    - Place the greater of the numbers into the output array and decrement
Essentially, k-way merge but starting with max values

Once m == 0 or n == 0, if n==0, then we are done. But if n > 0, then that means nums2 still has elements that need
to be moved over. It also means that all elements in num1 have been placed correctly in indices beyond remaining n.
So we just need to copy the remaining elements in nums2 into the same indices in num1.
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
                
        # Once we get here, if n > 0, then we need to copy over
        
        while n > 0:
            nums1[n - 1] = nums2[n - 1]
            n -= 1
        
