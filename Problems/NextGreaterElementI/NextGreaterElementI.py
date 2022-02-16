'''
Next Greater Element - so monotonic decreasing stack makes sense.

Can find the next greater element of each value in nums2. When found store in hashmap[value] = nextGreaterValue
'''


from collections import defaultdict, deque

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = deque()
        d = defaultdict(lambda: -1)
        
        # Monotonic decreasing Stack
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                d[stack.pop()] = nums2[i]
            stack.append(nums2[i])
            
        output = []
        
        # Append next greater element of each value to output
        for i in range(len(nums1)):
            output.append(d[nums1[i]])
            
        return output
                
        
