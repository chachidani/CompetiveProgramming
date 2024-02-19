class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        i = 0
        j = 0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i +=1
                j +=1
                count +=1
            elif g[i]  > s[j]:
                j +=1
        return count
        