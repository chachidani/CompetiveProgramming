class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prif = [0]*len(s)
        a,b,k =0,1,2
        for i in range(len(shifts)):
            if shifts[i][b] < len(s)-1:
                prif[shifts[i][a]] += -1 if shifts[i][k]==0 else 1
                prif[shifts[i][b] + 1] += 1 if shifts[i][k]==0 else -1
            else:
                prif[shifts[i][a]] += -1 if shifts[i][k]==0 else 1
            
        prif_num = [] 
        summ = 0
        for i in prif:
            summ += i
            prif_num.append(summ)
        new_s= ""
        for i,letter in enumerate(s):
            val = ord(letter)-97+ prif_num[i]

            new_letter = chr(val%26 + 97)
            new_s += new_letter
            
        return new_s

        
        