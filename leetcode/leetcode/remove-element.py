class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i,k in enumerate(nums):
            if val  != k:
                nums[count] = nums[i] 
                count += 1
        
        return count 
        