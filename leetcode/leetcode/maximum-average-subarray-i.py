class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
       
        l = 0
        maxx =  float("-inf")
        av = sum(nums[:k])
        maxx =  av/k
        while l+k<len(nums):
            av -= nums[l]
            av += nums[l+k]
            maxx = max(av/k , maxx)
            l +=1
          
        

        return maxx

        