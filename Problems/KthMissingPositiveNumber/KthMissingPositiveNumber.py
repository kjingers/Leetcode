'''
Option 1, use set. Then, loop from 1 to len(arr) + k checking if num is in set.

Option 2: Binary Search
Since the array is sorted, and since log(n) is better time complexity, then binary search might be an option.

Example: 

[2, 3, 4, 7, 11, 12] and k = 5
B = [2 - 1, 3 - 2, 4 - 3, 7 - 4, 11 - 5, 12 - 6] = [1, 1, 1, 3, 6, 6].

B represents the number of missing nums at each index. So, from B, need to find fist num >= k. We can use binary search to accomplish this.


'''

# Binary search solution
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid
        return right + k
                

# Set Solution
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_set = set(arr)
        
        for i in range(1, len(arr) + k + 1):
            if i not in arr_set:
                k -= 1
            if k == 0:
                return i
'''

        

            
                
            
        
        
