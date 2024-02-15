class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(len(heights)):
            lar = i
            for j in range(i+1,len(heights)):
                if heights[lar] < heights[j]:
                    lar = j
            heights[i],heights[lar] = heights[lar],heights[i]
            names[i],names[lar] = names[lar],names[i]
        return names
                
        