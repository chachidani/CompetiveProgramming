class Solution:
    def isValid(self, s: str) -> bool:
        par = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        stack = []
        for i in range(len(s)):
            if s[i] in par:
                stack.append(s[i])
            elif len(stack)==0 or s[i] != par[stack.pop()]:
                return False
               
        return len(stack) == 0
                

        