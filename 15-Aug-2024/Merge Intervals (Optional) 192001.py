# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1,len(intervals)):
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = intervals[i][1] if intervals[i][1] > ans[-1][1] else ans[-1][1] 
            else:
                ans.append(intervals[i])
        return ans


        