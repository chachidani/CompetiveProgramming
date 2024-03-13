class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = float('inf')
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] >= nums[left]:
                result = min(nums[left],result)
                left = mid+1
            elif nums[mid] < nums[left]:
                result = min(nums[mid],result)
                right = mid-1
        return result
            

        