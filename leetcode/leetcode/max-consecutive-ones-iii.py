class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxx = 0
        r = 0
        l = 0
        zerocount = 0
        while r< len(nums):
            if nums[r] == 0:
                zerocount +=1
            while zerocount > k :
                if nums[l] == 0:
                    zerocount -=1
                l +=1
            maxx = max(r-l+1 , maxx)
            r +=1
        return maxx

            
                

        