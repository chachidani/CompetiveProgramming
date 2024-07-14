# Problem: Backspace String Compare
(Easy) - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss = []
        st = []
        
        
        n = len(s)
        
        p = len(t)
        i = 0
        j = 0

        
        while  i < n :
            if s[i] == "#" and len(ss) == 0:
                i +=1
                continue
            elif s[i] == "#" and len(ss) != 0:
                ss.pop()
            else:
                ss.append(s[i])    
            i +=1    
        while j < p : 
            if t[j] == "#" and len(st) == 0:
                j +=1
                continue
             
            elif t[j] == "#" and len(st) != 0:
                st.pop()
                
            else:
                st.append(t[j])    
            j += 1    
            

            
            
        if ss == st:
            return True
        else: 
            return False
        
            
