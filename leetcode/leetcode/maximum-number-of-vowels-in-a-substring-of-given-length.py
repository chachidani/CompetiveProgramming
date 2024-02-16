class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        v = ['a','e','i','o','u']
        

        left = 0
        count = 0
        res = 0

        for right in range(n):
            if s[right] in v:
                count += 1
            k -= 1

            if k == 0:
                res = max(count, res)
                if s[left] in v:
                    count -= 1

                left += 1
                k += 1

        return res



            
            

        