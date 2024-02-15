class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for i in range(len(nums)):
            for j in range(len(nums)-1 , i , -1):
                if int(str(nums[j])+str(nums[j-1])) > int(str(nums[j-1])+str(nums[j])):
                    nums[j-1] , nums[j] = nums[j] , nums[j-1]
                else:
                    pass
        ans = ''.join(map(str , nums))
        if int(ans) == 0:
            return '0'
        return ans

        


        

        

        