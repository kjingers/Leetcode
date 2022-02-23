'''
A memory-efficient way to store sparse vector is by using hashmap. Only add to map if num != 0.

When calculating dot product, only multiply if key is in vec.dict too.
'''


class SparseVector:
    def __init__(self, nums: List[int]):
        self.dict = {}
        
        for i, num in enumerate(nums):
            if num != 0:
                self.dict[i] = num
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for i, num in self.dict.items():
            if i in vec.dict:
                ans += num * vec.dict[i]
        return ans
            
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
