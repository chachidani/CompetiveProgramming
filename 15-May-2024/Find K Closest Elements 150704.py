# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        ans = []
        for i in range(len(arr)):
            heappush(heap,[abs(arr[i]-x),arr[i]])
        
        for i in range(k):
            ans.append(heappop(heap)[1])
        ans.sort()
        return ans