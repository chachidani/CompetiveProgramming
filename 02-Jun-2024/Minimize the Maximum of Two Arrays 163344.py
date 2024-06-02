# Problem: Minimize the Maximum of Two Arrays - https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution:
    def minimizeSet(self, d1: int, d2: int, uc1: int, uc2: int) -> int:

        lcm = (d1 * d2) // math.gcd(d1, d2)
        def is_valid(n):

            only1 = n // d2 - n // lcm
            only2 = n // d1 - n // lcm
            both = n - n // d1 - n // d2 + n // lcm
            return max(0, uc1 - only1) + max(0, uc2 - only2) <= both
        
        l = -1
        r = 10**16
        while r > l + 1:
            mid = (r + l) // 2
          
            if is_valid(mid):
                r = mid
            else:
                l = mid
        return r
