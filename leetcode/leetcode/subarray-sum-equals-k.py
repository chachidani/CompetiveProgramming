class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        store={0:1}
        pref=[]
        summ = 0
        for num in nums:
            summ +=num
            pref.append(summ)
        for i in range(len(pref)):
            if pref[i]-k in store:
                count +=store[pref[i]-k]
            store[pref[i]] = store.get(pref[i],0)+1
        return count
            
        
        


    
        