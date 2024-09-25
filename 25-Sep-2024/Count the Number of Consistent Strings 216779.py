# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        alloweds = Counter(allowed)

        count = 0
        for word in words:
            l = False
            for i in word:
                if i not in alloweds:
                    l = False
                    break
                l = True
            if l:
                count += 1

            
        return count
