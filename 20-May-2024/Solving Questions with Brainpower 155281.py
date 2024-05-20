# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo  = {}
        @cache
        def dp(ind):
            if ind >= len(questions):
                return 0
            
            # if ind in memo:
            #     return memo[ind]

            po,powr = questions[ind]
            
            return  max(dp(ind+powr+1)+po , dp(ind+1))
            
        return dp(0)
        