'''
Keep dictionary of counts of each modulo % 60. As we loop through:
    - Calculate remainder = time % 60
    - target = (60 - remainder) % 60
    - Check if 60 - remainger in dict
    - If it is, then count += dict[60 - remainder]
    - dict[remainder] += 1
'''



class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = {}
        count = 0
        
        for t in time:
            remainder = t % 60
            target = (60 - remainder) % 60 # Handles case if remainder is 60
                  
            if target in remainders:
                count += remainders[target]
            
            remainders[remainder] = remainders.get(remainder, 0) + 1
            
        return count
        
        
