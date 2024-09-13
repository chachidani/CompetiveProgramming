# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pref = []
        count = 0
        for i,val in enumerate(nums):
            if val%2 != 0:
                nums[i] = 1
            else:
                nums[i] = 0
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            pref.append(summ)
        
        store = {0:1}
        for i in range(len(pref)):
            if pref[i]-k in store:
                count += store[pref[i]-k]
                
            store[pref[i]] = store.get(pref[i] , 0)+1
        
        return count


