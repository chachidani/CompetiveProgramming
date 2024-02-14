class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        suf = [1]
        pro = 1
        for i in range(len(nums)-1):
            pro *= nums[i]
            pref.append(pro)
        pro = 1
        for i in range(len(nums)-1 , 0 , -1):
            pro *=nums[i]
            suf.append(pro)
        suf = suf[::-1]
        print(pref)
        print(suf)
        for i in range(len(suf)):
            pref[i] = pref[i]*suf[i]
        return pref


        


        