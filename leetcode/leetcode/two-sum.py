class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        loc ={} 
        
        for i in range(len(nums)):
            cum = target - nums[i]
            if cum in loc:
                return loc[cum] , i
            loc[nums[i]] = i
        return []
            
            


        