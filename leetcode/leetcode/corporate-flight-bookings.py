class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        curr = [0]*n
        pref = []
        a,b,k = 0,1,2
        for i in range(len(bookings)):
            if bookings[i][b] < n:
                curr[bookings[i][a]-1] += bookings[i][k]
                curr[bookings[i][b]] += -bookings[i][k]
            else:
                curr[bookings[i][a]-1] += bookings[i][k]
        
        summ = 0
        for num in curr:
            summ +=num
            pref.append(summ)
        return pref
                



        