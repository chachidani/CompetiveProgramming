class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        maxnum =nums[-1]
        space = 0
        for i in range(len(nums)-2, -1,-1):
            if maxnum < nums[i]:
                space += math.ceil(nums[i]/maxnum)-1
                maxnum = nums[i]//math.ceil(nums[i]/maxnum)
                
            else:
                maxnum = nums[i]
        return space
        


        