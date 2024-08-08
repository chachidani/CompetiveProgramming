# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i] and nums[i-1] != 0:
                nums[i-1] = nums[i-1]*2
                nums[i] = 0
        print(nums)
        newnums = [0]*(len(nums))
        l = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                newnums[l] = nums[i]
                l += 1

        return newnums


            
        