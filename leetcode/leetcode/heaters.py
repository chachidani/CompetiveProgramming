import bisect
class Solution:    
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def isValid(r):
            h = 0
            for i in range(len(heaters)):
                while h < len(houses) and heaters[i] - r <= houses[h] <= heaters[i] + r:
                    h += 1
                
            return h == len(houses)



       
        left = 0
        right = max(max(houses[:]), max(heaters[:]))
    
      
        while left < right:
            mid = (left+right)//2
            if isValid(mid):
                
                right = mid
            else:
                left = mid+1
        return right

        


       
            
            

            


        