class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        if not piles:
            return 0
        piles = sorted(piles)
        count = 0
        n = len(piles)//3
        for i in range( n , len(piles)-1 ,2):
            count += piles[i]
       
        return count
        

        



        