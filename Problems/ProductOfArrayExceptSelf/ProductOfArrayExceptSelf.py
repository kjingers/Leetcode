'''
Technically Sliding Window?
We can do 2 passes of the array:
1. Left to right - For each index, calculate the product of all nums to the left
2. Right to left - For each index, calculate the product of all nums to the right

With these two arrays, we can multiply the numbers at each index in both arrays together to get
the sum of all numbers in array except self.
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
