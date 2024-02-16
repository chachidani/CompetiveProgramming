class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = r = 0
        while cur<=r and r<len(nums):
            if nums[r]==0:
                r+=1
            elif nums[r] != 0 and nums[cur] != 0:
                r +=1
                cur +=1
            elif nums[r] != 0 :
                nums[cur],nums[r] = nums[r],nums[cur]
                cur += 1
                r+1
            
        return nums
        