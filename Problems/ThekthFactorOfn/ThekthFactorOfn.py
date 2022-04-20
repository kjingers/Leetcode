'''
Brute Force: Loop from 1 to n and check if factor (n % i == 0), if so add to list, or increase count. 

Can also optimize time and use more sapce by only looping to sqrt(n), since all low factors will come before sqrt(n).
Append small factors to small list. Append large factor (n // i) to big list. If k > len(smallList), then go through big list.
'''

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
            
            if count == k:
                return i
        
        return -1
        
