class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = k-1
        right =len(cardPoints)-1
        c = 0
        summ = sum(cardPoints[:left+1])
        count = summ
        
        while left >= -1  and c < k :
             
               
            num = summ-cardPoints[left] + cardPoints[right]
            summ = num
            print(num)
            count = max(count,num )
            left -=1
            right -=1
            c +=1
        return count


            



