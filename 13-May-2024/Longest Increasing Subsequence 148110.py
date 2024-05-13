# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [0]*len(nums)
        def dp(i):
            if i >= len(nums):
                return 0
            

            if memo[i] == 0:
                memo[i] = 1
                for j in range(i+1,len(nums)):
                    if nums[j] > nums[i]:
                        memo[i] = max(1+dp(j),memo[i])
            return memo[i]
        
       
        res = -float('inf')
        for i in range(len(nums)):
            res = max(res,dp(i))

        return res
        