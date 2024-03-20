class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        count = sorted(count, key= lambda x : (-count[x],x))
    
        return count[:k]
        