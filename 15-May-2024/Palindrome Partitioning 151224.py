# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        def dp(ind,c):
            if ind == len(s):
                ans.append(c[:])
                return 

            for end in range(ind+1,len(s)+1):
                strr = s[ind:end]
                if strr == strr[::-1]:
                    c.append(strr)
                    dp(end,c)
                    c.pop()
      
        dp(0,[])
        return ans

        