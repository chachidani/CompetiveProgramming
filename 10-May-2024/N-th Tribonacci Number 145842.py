# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        def tribona(n):
            arr = [0 for i in range(38)]
            arr[0] = 0
            arr[1] = 1
            arr[2] = 1
            a = 0
            b = 1
            c = 1
           
            for i in range(3,38):
                arr[i] = a + b + c
                a = arr[i-2]
                b = arr[i-1]
                c = arr[i]
         
            return arr[n]

        return tribona(n)

        