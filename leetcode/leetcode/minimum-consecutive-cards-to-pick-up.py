class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left = 0
        count = float('inf')
        store = {}
        for right in range(len(cards)):
            if cards[right] in store:
                
                store[cards[right]] +=1
                while cards[left] != cards[right]:
                    count = min(count, right-left+1)
                    del store[cards[left]]
                    left +=1
                count = min(count, right-left+1)
                store[cards[left]] -=1
                left +=1
                
            else:
                store[cards[right]] = 1
        return count if count != float('inf') else -1



        