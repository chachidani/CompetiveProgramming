class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        pref = [0]
        suf = [0]
        for i in range(len(nums)):
            if nums[i] == 0:
                pref.append(1)
            elif nums[i] == 1:
                pref.append(0)
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 1:
                suf.append(1)
            elif nums[i] == 0:
                suf.append(0)
        for i in range(1,len(pref)):
            pref[i] = pref[i] + pref[i-1]
            suf[i] = suf[i] + suf[i-1]
        suf = suf[::-1]
        ans = []
        for i in range(len(pref)):
            pref[i] = pref[i]+suf[i]
        maxx = max(pref)
        for i,val in enumerate(pref):
            if val == maxx:
                ans.append(i)
        return ans





        
        