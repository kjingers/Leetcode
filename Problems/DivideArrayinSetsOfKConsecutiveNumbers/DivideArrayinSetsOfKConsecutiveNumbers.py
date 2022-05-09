'''
SHould sort keys rather than check min each time.
Also, starting from smallest, we can go ahead and subtract the number of the smallest.
'''


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums_count = Counter(nums)
        
        for num in sorted(nums_count):
            if nums_count[num] > 0:
                count = nums_count[num]
                for i in range(0, k):
                    nums_count[num + i] -= count
                    if nums_count[num + i] < 0:
                        return False
                    
        return True



