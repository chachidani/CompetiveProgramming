class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums:
            return True
        ans = True
        position = len(nums) - 1
        for i in range(len(nums)-2,-1,-1):
            if position - i > nums[i]:
                ans = False
            else:
                position -= position - i
                ans = True
        return ans




        