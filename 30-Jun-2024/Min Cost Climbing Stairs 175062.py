# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # -1: -1+1 or -1+2
        # -1+1= 0 : 0+1 or 0+2 
        memo = {}
        def dp(i):
            if i >= len(cost)-2:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = min(dp(i+1)+cost[i+1],dp(i+2)+cost[i+2])

            return memo[i]
        return dp(-1)