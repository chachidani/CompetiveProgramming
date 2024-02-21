class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        l = 0
        summ = 0
        while l <k:
            if numOnes != 0 :
                summ +=1
                numOnes -=1
            elif numZeros !=0 :
                summ +=0
                numZeros -=1
            elif numNegOnes != 0 :
                summ +=-1
                numNegOnes -=1
            l += 1
        return summ
            

