# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def dp(i,d):
            state = (i,d)
            if d > days[-1]:
                return 0
            if state in memo:
                return memo[state]

            while i < len(days) and d > days[i]:
                i += 1
            
            if i >= len(days) :
                return 0
           
           
            
            memo[state] = min(dp(i,days[i]+1)+costs[0],
            dp(i,days[i]+7)+costs[1],
            dp(i,days[i]+30)+costs[2]
            )
            
            return memo[state]
        return dp(0,days[0])

            

        