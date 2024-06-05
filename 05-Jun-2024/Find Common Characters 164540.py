# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        com = Counter(words[0])
        ans = []
        for i in range(1 ,len(words)):
            com &= Counter(words[i])
        return com.elements()


        
        