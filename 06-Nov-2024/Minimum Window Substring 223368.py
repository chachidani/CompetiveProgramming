# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            return ""

        countT, window = {}, {}

        for c in str2:
            countT[c] = 1 + countT.get(c, 0)

        result = [-1,-1] # this is to save the result pointers
        resLen = float("infinity")
        have , need = 0 , len(countT)

        l = 0 # left pointer, r is right pointer 
        for r in range(len(str1)):
            chr = str1[r] # character from str1 
            window[chr] = 1 + window.get(chr, 0)

            if chr in countT and window[chr] == countT[chr]:
                have += 1
            
        

            while have == need:
                if (r - l + 1) < resLen:
                    result = [l, r]
                    resLen = (r - l + 1)
                
              
              


                window[str1[l]] -= 1

          

                if str1[l] in countT and window[str1[l]] < countT[str1[l]]:
                    have -= 1
                l += 1
            
        l, r = result
        return str1[l:r+1] if resLen != float("infinity") else ""


