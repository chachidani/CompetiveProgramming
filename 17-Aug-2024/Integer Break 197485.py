# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache
        def dp(num):
            if n == 1:
                return 1
            res = 0
            for i in range(1,num):
                val =  dp(num-i)*i
                res = max(val,res,(num-i)*i)
            return res
        return dp(n)
                

        