# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        store = defaultdict(int)
        for i in arr:
            store[i%k] += 1
        if store[0]%2:
            return False

            
        
        for key,val in store.items():
            if val  != store[(k-key)%k]:
                return False
        return True

        