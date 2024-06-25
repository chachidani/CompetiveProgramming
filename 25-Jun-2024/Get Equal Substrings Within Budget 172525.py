# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i = 0
        r = 0
        ln = 0
        c = 0
        while r < len(s):
            c += abs(ord(s[r])-ord(t[r]))
            ln +=1
            if c > maxCost:
                c -= abs(ord(s[i])-ord(t[i]))
                i +=1
                ln -=1

            r +=1 
        return ln
        