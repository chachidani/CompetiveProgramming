# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        num = [0]*(n)
     
        meetings.sort()
        minheap = []
        for i in range(n):
            heappush(minheap,i)
    
        maxheap = []
        for i in range(len(meetings)):
            while maxheap and  maxheap[0][0] <= meetings[i][0]:
                end,room = heappop(maxheap)
                heappush(minheap,room)
                
            if minheap:
                room = heappop(minheap)
                heappush(maxheap,[meetings[i][1],room])
               
                num[room] += 1
            else:
                end,room = heappop(maxheap)
                num[room] += 1
                heappush(maxheap,[end+meetings[i][1]-meetings[i][0],room])
        
        maxx = max(num)
        for i in range(n):
            if num[i] == maxx:
                return i
            
            



with open('user.out', 'w') as f:
    testcases = list(stdin)
    for n, meetings in zip(testcases[::2], testcases[1::2]):
        f.write(f"{str(Solution().mostBooked(loads(n), loads(meetings)))}\n")
exit()


        