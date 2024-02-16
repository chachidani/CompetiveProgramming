class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ , max_sum = 0 , nums[0]
        for num in nums:
            summ +=num
            max_sum = max(summ , max_sum)
            if summ < 0:
                summ = 0
        return max_sum
        


        