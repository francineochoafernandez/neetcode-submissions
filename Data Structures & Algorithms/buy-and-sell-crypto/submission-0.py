#Can I know the values of all days?
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1 #left=buy, #right=sell
        max_profit=0

        while right<len(prices):

            if prices[left] < prices[right]:
                profit= prices[right] - prices[left] #Future value - value bought
                max_profit=max(max_profit,profit)
            else:
                left = right
            
            right +=1
        
        return max_profit
