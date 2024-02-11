class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        l = n
        while True:
            if l % 2 == 0 and l % n == 0 :
                return l
            l +=1
        return 
            