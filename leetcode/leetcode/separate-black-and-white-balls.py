class Solution:
    def minimumSteps(self, s: str) -> int:
        k = 0
        count = 0
        for i,val in enumerate(s[::-1]):
            if val == '1' :
                count +=k
            elif val == '0' :
                k +=1
        return count



        