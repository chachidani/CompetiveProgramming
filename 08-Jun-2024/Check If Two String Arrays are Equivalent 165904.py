# Problem: Check If Two String Arrays are Equivalent - https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        x = ''
        y = ''
        for word in word1:
            x += word
        for word in word2:
            y += word
        if x==y:
            return True
        return False

        