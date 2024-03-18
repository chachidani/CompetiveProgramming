class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        if len(nums)<3:
            return max(nums)

        k = 3
        maxx = float('-inf')
        for i in range(len(nums)):
            
            if k > 0 and nums[i] != maxx :
                k -=1
                maxx = nums[i]
                if k == 0:
                    return maxx
            else:
                continue
        return max(nums)
            
        