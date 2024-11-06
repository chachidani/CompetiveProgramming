# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        store = []
        for ch in s:
            x = ord(ch)-96
            store.append(f'{x}')
        m = ''.join(store)
        while k > 0:
            ans = 0
            for i in m:
                ans += int(i)
            k -= 1
            m = str(ans)
        return int(m)