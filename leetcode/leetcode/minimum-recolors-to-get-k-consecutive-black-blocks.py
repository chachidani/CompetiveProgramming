class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = float('inf')
        left = 0
        white = 0
        for right in range(len(blocks)):
            if blocks[right] == 'W':
                white +=1
            if right-left+1 == k:
                count = min(white , count)
                if blocks[left] == 'W':
                    white -=1
                left +=1
        return count
        
                    


            

        