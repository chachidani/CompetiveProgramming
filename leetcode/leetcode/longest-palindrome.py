class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = 1
        count = Counter(s)
        length = 0
        
        for key , val  in count.items():

            if val%2 == 0:
                length += val
            elif val%2 !=0 and odd==1:
                length += val
                odd -=1
            elif val%2 !=0 and odd ==0:
                length += val-1
            
                
        return length



        