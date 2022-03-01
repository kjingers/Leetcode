'''
Array where each index contains the number of 1s in it's binary form. 

Brute Force: Is to obviouly convert each number to binary representation and count number of 1s. This has Time complexity O(n * len(binstring))

However, we can use these rules of binary numbers:
    - Count(n) = Count(n // 2) for even numbers, since doubling an even number just adds a 0 to the right
    - Count(n) = Count(n // 2) + 1 for odd numbers
    
So, we can combine into one statement by adding (i % 2), which is 1 when odd and 0 when even
'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = [0]
        
        for i in range(1, n + 1):
            cnt = counts[i // 2] + (i % 2)
            counts.append(cnt)
            
        return counts
        
