'''
Want to buy at local minimums and sell at local maximums.
    - If current price is higher than previous price, then we want to buy at previous price.
    - Then, if current price is less that previous price, we want to sell at previous price
    
Also added logic to print the days to buy and sell.
    

'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        buy_days = []
        sell_days = []
        
        if n <= 1:
            return 0
        
        i = 1
        profit = 0
        
        while i < n:
            
            while i < n and prices[i] <= prices[i - 1]:
                i += 1
                
            buy = i - 1
            buy_days.append(buy)
            
            while i < n and prices[i] >= prices[i - 1]:
                i += 1
                
            sell = i - 1
            sell_days.append(sell)
            
            profit += prices[sell] - prices[buy]
        
        
        for j in range(len(sell_days)):
            if buy_days[j] == sell_days[j]:
                break
            print("Buy Day: %d. Sell Day: %d" % (buy_days[j], sell_days[j]))
        
        return profit
            
            
        
