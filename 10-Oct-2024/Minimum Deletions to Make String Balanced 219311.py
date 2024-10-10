# Problem: Minimum Deletions to Make String Balanced - https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        b =0
        c = [0]*(n+1)
        for i in range(len(s)):
            if s[i] == 'b' :
                b += 1
                c[i+1] = c[i]
            elif s[i] == 'a' and b != 0:
                c[i+1] = min(b , c[i] + 1)
        return c[-1]
