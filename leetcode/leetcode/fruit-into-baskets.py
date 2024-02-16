class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        has = dict()
        l ,r= 0 ,0
        lar = 0
        while r < len(fruits):
            has[fruits[r]] = has.get(fruits[r],0)+1
            if len(has) <=2:
                lar = max(lar, r - l + 1)
            if len(has) > 2:
                while len(has) > 2:
                    has[fruits[l]] -=1
                    if has[fruits[l]]  == 0:
                        del has[fruits[l]] 
                    l += 1
            r +=1
        return lar

            


        