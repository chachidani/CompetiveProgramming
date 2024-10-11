# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        d = []
        for crr in pattern:
            d.append(pattern.count(crr))
        ans = []
        for word in words:
            i = [word.count(j) for j in word]
            if i == d and ([*map(word.index ,word )] ==  [*map(pattern.index , pattern)]):
                ans.append(word)
        return ans
        