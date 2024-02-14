class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref = [0]*len(nums)
        store = {0:1}
        summ = 0
        count = 0
        for i in range(len(nums)):
            summ +=nums[i]
            pref[i] = summ
        for i in range(len(pref)):
            if pref[i]-goal in store:
                count += store[pref[i]-goal]
            store[pref[i]] = store.get(pref[i] , 0)+1
        return count
