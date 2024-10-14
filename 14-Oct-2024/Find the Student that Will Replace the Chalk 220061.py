# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        k = k%sum(chalk)
        for i in range(len(chalk)):
            if k == 0 or k < chalk[i]:
                return i
            
            k -= chalk[i]
        return 0


        