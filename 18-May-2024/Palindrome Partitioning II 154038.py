# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        memo = {}
        def dp(i,l):
            if i >= n:
                sub = s[l:i]
                if sub == sub[::-1]:
                    return 0
                return n
            if (i,l) in memo:
                return memo[(i, l)]
            min_cut = dp(i + 1,l)
            sub = s[l:i]
            if l != i and sub == sub[::-1]:
                cut = dp(i + 1, i) + 1
                min_cut = min(min_cut, cut)
            memo[(i,l)] = min_cut
            return memo[(i,l)]
        return dp(0,0)
