# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        memo = defaultdict(tuple)
        def dp(summ,final):
            if summ  == amount:
                return 1
            if summ > amount:
                return 0
            state = (summ,final)
            if state not in memo:
                comb = 0
                
                for p in coins:
                    if final <= p:
                        comb += dp(summ+p,p)
                    
                memo[state] = comb
            return memo[state]
        return dp(0,0)
        

        
        