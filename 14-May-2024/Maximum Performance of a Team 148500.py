# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        zipp = list(zip(efficiency, speed))
        zipp.sort(reverse=True)
        possible = []
        total, rst = 0, 0
        for eff, spd in zipp:
            heappush(possible, spd)
            total += spd
            if len(possible) > k:
                total -= heappop(possible)
            rst = max(rst, eff*(total))
            
        return rst%(10**9 + 7)