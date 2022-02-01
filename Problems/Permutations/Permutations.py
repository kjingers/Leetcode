'''
This is permutations of a list.

Since we are passing in a copy of currPerm + nums[i], we do not need to backttrack. If we appending and passed in reference to currPerm,
we we would need to pop() after recursive call.

Time Complexity: O(N!)
- For a string with len of 3, we have 3 calls, each with 2 calls, each with 1 call. So 3x2x1 = 3!
'''
    
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        self.permute_rec(nums, [], output)
        return output
        
    def permute_rec(self, nums, currPerm, outputPerms):
        
        # Base Case (Empty list)
        if not nums:
            outputPerms.append(currPerm)
            return
        
        for i in range(len(nums)):
            self.permute_rec(nums[:i] + nums[i+1:], currPerm + [nums[i]], outputPerms)


