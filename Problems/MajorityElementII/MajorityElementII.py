'''
Easy approach uses O(n) space. Better approach is to use Boyer-Moore Majority Vote Algorithm.
Since we can have up to 2 nums that appear MORE than n//3 times, we kee two candidate values.

Essentially, we keep two candidate (since we can have max two answers). For each num, if it equals one of the candidates, we increment the corresponding counter. If any of the counters are 0, we set the counter to 1 and the corresponding candidate value to the current num.

If doesn't match either candidate and both counters are > 0, then we decrement both counters.
'''

    
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        
        for num in nums:
            
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                count1 += 1
                candidate1 = num
            elif count2 == 0:
                count2 += 1
                candidate2 = num
            else:
                count1 -= 1
                count2 -= 1
        
        return [i for i in (candidate1, candidate2) if nums.count(i) > len(nums) // 3]
        
'''        
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        n = len(nums)                
        return [val for val, cnt in counts.items() if cnt > n // 3]
        
'''
                
                
