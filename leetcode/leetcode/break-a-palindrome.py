class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome=list(palindrome)
        for i in range(int(len(palindrome)/2)):
            if palindrome[i]!="a":
                palindrome[i]='a'
                return "".join(palindrome)
        palindrome[len(palindrome)-1] = 'b'
        if len(palindrome)>1:
            return "".join(palindrome)
        else:
            return ""