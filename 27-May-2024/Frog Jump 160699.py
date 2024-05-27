# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        target = stones[-1]
        stones = set(stones)
        def valid(new_val, val):
            return new_val in stones and new_val > val

        memo = {}
        def dp(val, k):
        
            if val == target:
                return True
            if (val, k) in memo:
                return memo[(val,k)]
            res = False
            if valid(val + k + 1, val):
                res = res or dp(val +  k + 1, k+1)
            if valid(val + k , val):
                res = res or dp(val +  k , k)
            if valid(val + k - 1,val ):
                res = res or dp(val +  k - 1, k-1)
            memo[(val, k)] = res
            return memo[(val, k)]
        
        return dp(0, 0)
