class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        sScore = score[:] 
        sScore.sort(reverse=True)
        store = {sScore[i]:i+1 for i in range(len(sScore))}
      
        answer = []
        
        for s in score:
         
            if store[s] == 1:
                answer.append("Gold Medal")
            elif store[s] == 2:
                answer.append("Silver Medal")
            elif store[s] == 3:
                answer.append("Bronze Medal")
            else:
                answer.append(str(store[s]))
      
        return answer