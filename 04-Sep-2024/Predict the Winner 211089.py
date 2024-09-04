# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def solve(st,en):
            if st == en:
                return nums[en]
            start = nums[st] - solve(st+1 , en)
            end = nums[en] - solve(st , en-1)
            return max(start,end)
            
        return solve(0,len(nums)-1) >=0
        