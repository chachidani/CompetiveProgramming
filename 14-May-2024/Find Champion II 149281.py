# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(int)
        incoming = [0]*n
        for a,b in edges:
            graph[a] = b
            incoming[b] += 1
       
        count = Counter(incoming)
        for i in range(n):
            if count[incoming[i]]== 1 and incoming[i] == 0:
                return i
            
        return -1