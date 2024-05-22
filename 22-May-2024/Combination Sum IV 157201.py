# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(tuple)
        def dp(summ):
            if summ  == target:
                return 1
            if summ > target:
                return 0
            state = (summ)
            if state not in memo:
                comb = 0
                
                for p in nums:
                    comb += dp(summ+p)
                    
                memo[state] = comb
            return memo[state]
        return dp(0)





        