class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        sec = 0
        
        
        for i , val in enumerate(tickets):
            if val > tickets[k] and i<k:
                sec += tickets[k]
            elif val >= tickets[k] and i>k:
                sec += tickets[k]-1

            else:
                sec += val
        return sec

        