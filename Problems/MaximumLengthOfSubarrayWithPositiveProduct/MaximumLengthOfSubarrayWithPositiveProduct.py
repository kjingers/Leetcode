'''   
Brute Force: Two nested loops to check product of all subarrays and update max lengths

DP Problem:

pos[i] is the length of positive product subarray ending at i

'''


# DP using just prev var
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        negLen, posLen = 0, 0
        maxPos = 0        
        
        pos, neg = 0, 0
            
        maxPos = pos
            
        for i in range(len(nums)):
            if nums[i] > 0:
                pos = pos + 1
                neg = neg + 1 if neg > 0 else 0
            elif nums[i] < 0:        
                pos, neg = neg + 1 if neg > 0 else 0, pos + 1
            else:
                pos, neg = 0, 0
             
            maxPos = max(maxPos, pos)
            
        return maxPos

# DP using two arrays
'''
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        negLen, posLen = 0, 0
        maxPos = 0
        
        pos = [0 for _ in range(len(nums))]
        neg = [0 for _ in range(len(nums))]
        
        if nums[0] > 0:
            pos[0] = 1
        
        if nums[0] < 0:
            neg[0] = 1
            
        maxPos = pos[0]
            
        for i in range(1, len(nums)):
            if nums[i] > 0:
                pos[i] = pos[i - 1] + 1
                neg[i] = neg[i - 1] + 1 if neg[i - 1] > 0 else 0
            elif nums[i] < 0:
                pos[i] = neg[i - 1] + 1 if neg[i - 1] > 0 else 0
                neg[i] = pos[i - 1] + 1
            maxPos = max(maxPos, pos[i])
            
        return maxPos
'''
              
     
