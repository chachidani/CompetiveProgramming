class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pref = [0]*len(nums)
        suf = [0]*len(nums)
        for i in range(1 ,len(nums)):
            pref[i] = (nums[i]-nums[i-1])*i + pref[i-1]
        nums = nums[::-1]
        for i in range(1 ,len(nums)):
            suf[i] = (nums[i-1]-nums[i])*i + suf[i-1]
        suf = suf[::-1]
    
        for i in range(len(pref)):
            pref[i] = pref[i]+suf[i]
        return pref


        


        