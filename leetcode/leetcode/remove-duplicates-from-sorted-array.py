class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l = 0
        r = 1
        size = len(nums)
        while l <= r and r < size:
            if nums[l] == nums[r]:
                r +=1
            else:
                nums[l+1] = nums[r]
                l +=1
               
            
        return l+1

        