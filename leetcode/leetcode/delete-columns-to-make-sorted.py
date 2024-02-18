class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        strs = zip(*strs)
        col = 0
        
        for i in strs:
            if list(i) != sorted(i):
                col +=1
        return col

        