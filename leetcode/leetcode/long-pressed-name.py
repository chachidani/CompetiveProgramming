class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        l = 0
        r = 0
        while l < len(typed) and r <= len(name):
       
            if r < len(name) and typed[l] == name[r]:
                l +=1
                r +=1
            elif r != 0 and typed[l] == name[r-1]:
                l +=1
            else:
                return False
        return r == len(name) and l == len(typed)

        