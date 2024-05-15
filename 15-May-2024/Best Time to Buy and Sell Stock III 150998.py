# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i,stoke,k):
            if i >= len(prices) or k == 0:
                return 0
            state = (i,stoke,k)
            if state in memo:
                return memo[state]
            passing = dp(i+1,stoke,k)
            selling = 0
            if stoke:
                selling = dp(i+1,not stoke,k-1)+prices[i]
                memo[state] = max(selling,passing)
            else:
                buying = dp(i+1,not stoke,k)-prices[i]
                memo[state] = max(buying,passing)
            return memo[state]
        return dp(0,False,2)


        
