'''
For the two-sum case, we don't have to sort. Instead, we can use a hashmap to store each num and index.
Then, as we iterate, we see if (target - num) is in the hash map. This is probably easiest, since we need
the indices of both nums of the original list.

But for >= three sum, need to be sorted, so that we can avoid duplicate pairs (?)
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i, v in enumerate(nums):
            if target - v in vals:
                return [vals[target - v], i]
            vals[v] = i
            
        return [-1, -1]
