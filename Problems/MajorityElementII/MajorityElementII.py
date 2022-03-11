from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        n = len(nums)
        output = []
                
        return [val for val, cnt in counts.items() if cnt > n // 3]
                
        #return output
                
