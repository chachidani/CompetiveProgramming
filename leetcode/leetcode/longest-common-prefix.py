class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        outstr = ''
        strs.sort()
        n = len(strs)
        for i in range(len(strs[0])):
            if strs[0][i]==strs[n-1][i]:
                outstr+=strs[0][i]
            else:
                break
        return outstr


            
            
        
            
               
         
        