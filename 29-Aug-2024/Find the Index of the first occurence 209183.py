# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0
        r =  len(needle)-1
        m = len(needle)
        while r < len(haystack):
            if haystack[l:r+1] == needle:
                return l
            l +=1
            r +=1
        return -1