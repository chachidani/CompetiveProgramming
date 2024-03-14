class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def countK(count):
            summ = 0
            count_k = 1
            for i in range(len(nums)):
                if summ + nums[i] > count:
                    count_k += 1
                    summ = 0
                summ += nums[i]
            
            return count_k
        first = max(nums)
        last = sum(nums)
        while first <= last:
            mid = (first+last)//2
            if countK(mid)> k:
                first = mid+1
            elif countK(mid)<=k:
                last = mid-1
        return first



        