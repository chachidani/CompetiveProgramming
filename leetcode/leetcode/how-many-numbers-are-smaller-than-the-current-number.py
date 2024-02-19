class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:  
        ans = []
        count = 0
        numb = nums.copy()
        numb.sort()
        for i in range(len(nums)):
            count =len(numb[:numb.index(nums[i])])
            ans.append(count)
        return ans
        
                
            
