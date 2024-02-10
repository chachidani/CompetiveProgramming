class Solution:
    def maxScore(self, s: str) -> int:
        pref = []
        suf =[]
        for i in range(len(s)-1):
            if s[i] == '0':
                pref.append(1) 
            else:
                pref.append(0)
        for i in range(len(s)-1 , 0 , -1):
            if s[i] == '1':
                suf.append(1)
            else:
                suf.append(0)
        print(pref)
        suf = suf[::-1]
        print(suf)

        summ = 0
        summ2 = 0
        for i in range(len(pref)):
            summ += pref[i]
            pref[i] = summ
        for i in range(len(suf)-1 , -1 , -1):
            summ2 += suf[i]
            suf[i] = summ2
        print(pref)
        print(suf)
        ans = 0
        for i in range(len(pref)):
            pref[i] = pref[i]+suf[i]
            ans = max(pref[i] , ans)
        print(pref)

        
        return ans
        