# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def timetominute(time):
            hour = int(time[:2])
            minute = int(time[3:])
            return hour*60 + minute
        minutes = [timetominute(time) for time in timePoints ]
        minutes.sort()
        print(minutes)
        ans = float('inf')
        for i in range(1 , len(minutes)):
            ans = min(ans,minutes[i] - minutes[i-1])
        ans = min(ans, 1440 + minutes[0] - minutes[-1])
        return ans

        