class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        def isValid(mid):
            summ = 0
            for i in range(len(nums)):
                summ += ceil(nums[i]/mid)
            return summ
        left =  1
        right = nums[-1]
        while left <= right:
            mid = (left + right)//2
            if isValid(mid) <= threshold:
                right = mid - 1
            elif isValid(mid) > threshold:
                left = mid + 1
        return left