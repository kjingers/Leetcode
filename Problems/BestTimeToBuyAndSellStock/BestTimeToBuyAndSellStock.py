'''
We can loop through all prices. At each price we:
- Update the minimum seen so far
- Calculate the profit of price - min. 
- Update maxProfit if necessary

For each price, the best profit so far will be if we buy at the minimum price seen so far.

Time Complexity: O(n)
Space Complexity: O(1)

'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = float('inf')
        maxProfit = 0
        
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
        
        return maxProfit
