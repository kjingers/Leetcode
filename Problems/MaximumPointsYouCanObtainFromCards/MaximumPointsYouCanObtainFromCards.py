'''
Exmaple: k = 3

- Can take 0 from left. 3 from right.
- 1 from left, 2 from right
- 2 from left, 1 from right
- 3 from left, 0 from right

k + 1 possibilities

Naive - trying all poosilibites: Time Complexity: O( (K + 1) * (k)) = O(k^2)

To reduce repeating calculations, sliding window

Time Complexity: O(k + k) = O(k)
Space: O(1)
'''

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)
        left = 0
        
        currSum = sum(cardPoints[n - k:])
        maxSum = currSum
        
        while left < k:
            currSum -= cardPoints[n - k + left]
            currSum += cardPoints[left]
            maxSum = max(currSum, maxSum)
            left += 1
            
        return maxSum
        
        '''
        [0, 1, 2, 3, 4, 5, 6]
        
        n = 7, k = 3 example
        First: (left = 0)
        currSUm -= pts[4]
        currSUm += pts[0]
        
        Second: (left = 1)
        -= pts[5]
        += pts[1]
        
        Thirs (left = 2)
        -=pts[6]
        += pts[2]
        
        '''
