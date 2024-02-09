class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pref = [0]*1001
        k,a,b = 0,1,2
        for i in range(len(trips)):
            if trips[i][b]<1000:
                pref[trips[i][a]] += trips[i][k]
                pref[trips[i][b]] += -trips[i][k]
            else:
                pref[trips[i][a]] += trips[i][k]
        summ = 0
        for i in range(1001):
            summ += pref[i]
            pref[i] = summ
            if summ > capacity:
                return False
        print(summ)
        return True




        


        