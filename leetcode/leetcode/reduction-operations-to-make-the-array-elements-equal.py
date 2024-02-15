class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        op = 0
        pre = 0
        nums = sorted(nums)
        for i in range(1 ,len(nums)):
            if nums[i] != nums[i-1]:
                op += pre + 1
                pre += 1
            else:
                op += pre + 0
                pre += 0
        return op


            
                



        