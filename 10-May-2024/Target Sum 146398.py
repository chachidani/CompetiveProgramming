# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict(tuple)
        
        def dp(i,tar):
        
            if i  >=  len(nums):
                return 1 if tar == target else 0 
            state = (i,tar)
            if state not in memo:
                memo[state] = dp(i+1,tar+nums[i]) + dp(i+1,tar-nums[i] ) 
            else:
                return memo[state]
            
            
            return memo[state]
        return dp(0,0)
       

                
                
            

                
        