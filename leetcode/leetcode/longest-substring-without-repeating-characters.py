class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
             return 0
        start = 0
        end = 1
        window = dict()
        window[s[start]] = 1
        c = len(window)
        l = len(window)
        while end < len(s):
            if s[end] in window:
                del window[s[start]]
                start +=1 
            else: 
                window[s[end]] = 1
                end += 1
             
            c = len(window)
            l = max(c,l)
        return l
            

