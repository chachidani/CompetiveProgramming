class Solution:
    def isPalindrome(self, x: int) -> bool:
        strnum = str(x)
        revers = strnum[::-1]
        if revers == strnum:
            return True
        return False
        

        