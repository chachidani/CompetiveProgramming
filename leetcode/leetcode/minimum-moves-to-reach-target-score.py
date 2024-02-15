class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        opration = 0
        while maxDoubles > 0 and target != 1:
            if target%2 == 0:
                opration +=1
                target = target//2
            else:
                opration +=2
                target = target//2
                
            maxDoubles -= 1
           
        else:
            opration += target-1
            target -= target-1
            

        return opration
            
        