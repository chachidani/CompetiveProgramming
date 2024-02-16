class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        pref = 0
        op = 0
        for i in range(len(nums)):
            while pref+1  < nums[i]:
                pref += pref+1
                op +=1
                if pref>n: break
            pref += nums[i]
            if pref>n: break
            
        while pref < n:
            pref +=pref+1
            op +=1
        return op


        