class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def countDays(count):
            summ = 0
            count_days = 1
            for i in range(len(weights)):
                
                if summ + weights[i] > count:
                    count_days +=1
                    summ =    0 
                summ += weights[i]
            
            return count_days
        first = max(weights)
        last = sum(weights[:])

        while first<= last:
            mid = (first+last)//2

            if countDays(mid) > days:
                first = mid + 1
            elif countDays(mid) <= days:
                last = mid-1
        return first


        





        