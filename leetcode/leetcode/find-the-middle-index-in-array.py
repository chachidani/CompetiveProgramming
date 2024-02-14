class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        summ = 0
        pref,suf = [],[]
        for i in range(len(nums)):
            summ += nums[i]
            pref.append(summ)
        summ = 0
        for i in range(len(nums)-1,-1,-1):
            summ += nums[i]
            suf.append(summ)
        suf = suf[::-1]
        
        for i , num in enumerate(pref):
            if num == suf[i]:
                return i
        return -1

        