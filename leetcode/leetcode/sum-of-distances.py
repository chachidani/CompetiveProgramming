class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        pref = [0]*len(nums)
        suf = [0]*len(nums)
        store = {}
        store2 = {}
        for i , e in enumerate(nums):
            if e in store:
                ind , count = store[e]
                pref[i] = i-ind + pref[ind] + (i-ind)*count

                store[e] = [i , count+1 ]
            else:
                store[e] = [i , 0 ]
        for i in range(len(nums)-1 , -1 ,-1):
            if nums[i] in store2:
                ind , count = store2[nums[i]]
                suf[i] = ind-i + suf[ind] + (ind-i)*count
                store2[nums[i]] = [i , count+1 ]
            else:
                store2[nums[i]] = [i , 0]
        for i in range(len(pref)):
            pref[i] = pref[i]+suf[i]
        return pref

                


        
        