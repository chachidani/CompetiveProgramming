class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                threesum = nums[i] + nums[left] + nums[right]
                if threesum < 0:
                    left += 1
                elif threesum > 0:
                    right -=1
                else:
                    triplate = [nums[i],nums[left],nums[right]]
                    result.append(triplate)
                    while left < right and  nums[left] == triplate[1]:
                        left +=1
                    while left < right and nums[right] == triplate[-1]:
                        right -=1
        return result
                

                
        




        