class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i , v in enumerate(s):
            lastIndex[v] = i
        size = end = 0
        out =[]
        for i , v in enumerate(s):
            end = max(end,lastIndex[v])
            size +=1
            if i == end:
                out.append(size)
                size = 0

        return out
        