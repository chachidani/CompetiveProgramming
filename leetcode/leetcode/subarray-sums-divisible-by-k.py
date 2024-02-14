class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref = [0]
        for num in nums:
            pref.append(pref[-1]+num)
        store={}
        count = 0
        for num in pref:
            if num%k in store:
                count += store[num%k]
                store[num%k] +=1
            else:
                store[num%k] = 1
        return count
            
            
            