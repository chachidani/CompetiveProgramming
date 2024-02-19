class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        valid = 0
        
        for i,val in enumerate(s):
            if val=='(' :
                stack.append(val)
            elif val == ')' and len(stack)>0:
                stack.pop()
            elif val == ')' and len(stack)==0:
                valid +=1
        if stack:
            valid += len(stack)
        return valid
            
            



        