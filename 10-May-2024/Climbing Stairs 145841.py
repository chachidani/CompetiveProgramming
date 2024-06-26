# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache
        def dp(n):
            if n < 3:
                return n
           
            return dp(n-1) + dp(n-2)
     
        return dp(n)



        