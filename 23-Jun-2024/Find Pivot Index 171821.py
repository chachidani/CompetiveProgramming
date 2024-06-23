# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        total = sum(nums)
        for i in range(len(nums)):
            right = total - nums[i]-left
            if right == left:
                return i
            left +=nums[i]
        return -1

       
            
