# Problem: Divide intervals into minimum number of groups - https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        ans = []
        for left,right in intervals:
            if not ans:
                heappush(ans , right)
            else:
                if  ans[0] >= left:
                    heappush(ans , right)
                else:
                    heappop(ans)
                    heappush(ans , right)
        return len(ans)
        