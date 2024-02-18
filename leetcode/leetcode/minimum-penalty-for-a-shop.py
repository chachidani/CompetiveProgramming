class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pref = [0]*(len(customers)+1)
        suf = [0]
        for i in range(len(customers)):
            if customers[i] == 'Y':
                pref[i+1] = 0 + pref[i]
            elif customers[i] == 'N' :
                pref[i+1] = 1+pref[i]
        for i in range(len(customers)-1,-1,-1):
            if customers[i] == 'N':
                suf.append(0) 
                
            elif customers[i] == 'Y' :
                suf.append(1)
        
        for i in range(1,len(suf)):
            suf[i] = suf[i]+suf[i-1]
        suf = suf[::-1]
       
        for i in range(len(pref)):
            pref[i] = pref[i]+suf[i]
        minn = min(pref)
        for ind,val in enumerate(pref):
            if val == minn:
                return ind

        

        