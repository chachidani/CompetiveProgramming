class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        has = dict()
        l =  0
        
        length = 0

        for  r in range(len(s)):
            has[s[r]] = has.get(s[r], 0) + 1

            if ((r-l +1) - max(has.values())) <= k:
                
                
                length = max(r-l+1, length)
            else:
                has[s[l]] -= 1
                if not has[s[l]]:
                    has.pop(s[l])
                l += 1
                
             

        return length

                
            
           
            



        