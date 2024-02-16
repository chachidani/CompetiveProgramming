class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros +=1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -=1
                left +=1
            count = max(right-left +1-zeros , count )
        return count -1 if count == len(nums) else count

            




  

                
            
                
                






        