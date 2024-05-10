# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = prices[0]
        ans = 0
        for i in range(1,len(prices)):
            if minn > prices[i]:
                minn = prices[i]
            elif minn < prices[i]:
                ans = max(prices[i]-minn,ans)
        return ans

        
       
       
       

        