class Solution:
    def sortSentence(self, s: str) -> str:
        l = list(map(str, s.split(' ')))
        def sort(strr):
            return strr[-1]
        l.sort(key=sort)
        for i in range(len(l)):
            l[i] = l[i][:len(l[i])-1]
        return ' '.join(l)
        
           
        