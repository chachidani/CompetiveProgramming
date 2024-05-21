# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        length = 1
        dp = {}
        
      
        for i in arr:
            if i-difference  in dp:
                dp[i-difference] = max(dp[i-difference],1)
                dp[i] = (dp[i-difference]+1)
                length = max(length,dp[i])
            else:
                dp[i] = 0
        \
        return length 


   
