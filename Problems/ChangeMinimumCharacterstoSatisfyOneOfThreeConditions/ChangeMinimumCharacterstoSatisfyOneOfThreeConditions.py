'''
"Minimum Number" makes me think DP. Except, position doesn't matter.

Prefix sum for each string:
prefixSumA[i] is number of characters <= i
prefixSumB[i] is number of characters <= i

So First we try all possible counts to make a less than b

for i in range(25):
    # Moves To make i smallest character in A, and all character larger than i in B
    num_moves = m - preSumA[i] + preSumB[i]

    - preSumB[i] is the number of character <= i. So this is the number of moves to make all bigger than i
    - (m - preSumA[i]) is the number of character > i. So this is the number of moves to make all <= i
    
We try this for each character and update res as required.

'''


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        
        cnt_a = Counter(a)
        cnt_b = Counter(b)
        
        m = len(a)
        n = len(b)
        
        presum_a = []
        presum_b = []
        
        res = float('inf')
        
        condition3 = m - max(cnt_a.values()) + n - max(cnt_b.values())
        
        sum_a = 0
        sum_b = 0
        
        
        for i in range(26):
            sum_a += cnt_a[chr(ord('a') + i)]
            sum_b += cnt_b[chr(ord('a') + i)]
            presum_a.append(sum_a)
            presum_b.append(sum_b)
            
        # presum_a[i] is number of letters <= i
        
        for i in range(25):
            # Moves to get a <= i and b > i
            moves = m - presum_a[i] + presum_b[i]
            res = min(res, moves)
            
        for i in range(25):
            # Moves to get b <= i and a > i
            moves = n - presum_b[i] + presum_a[i]
            res = min(res, moves)
            
        return min(res, condition3)
        
        
        
