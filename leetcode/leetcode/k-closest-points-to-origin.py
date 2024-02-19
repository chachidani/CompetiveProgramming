class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        store = []
        value = 0
        ans = []
        for i,val in enumerate(points):
            store.append([i,sqrt(val[0]**2 + val[1]**2)])
        def sort(arr):
            return arr[1]
        store.sort(key=sort)
        r = 0
        while k > 0 and r<len(store):
            ans.append(points[store[r][0]])
            k-=1
            r+=1
        return ans

            
            
        