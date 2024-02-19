class Solution:
    def isPalindrome(self, s: str) -> bool:
        mystree = ''
        for i,val in enumerate(s):
           
            if val.isalpha() and val.isupper():
                mystree += val.lower()
            elif val.isalpha()or val.isdigit():
                mystree += val
            else:
                continue
        if mystree == mystree[::-1]:
            return True 
        else:
            return False

        