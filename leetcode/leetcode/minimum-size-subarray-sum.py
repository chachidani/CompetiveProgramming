class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        
        total = 0
        minc = float('inf')
        for r in range(len(nums)):
            total += nums[r]
            
            while total >= target:
                minc = min(r-l+1 , minc)
                total -= nums[l]
                l += 1
            
            

        return 0 if minc == float('inf') else minc
        
        
            
            
            




        