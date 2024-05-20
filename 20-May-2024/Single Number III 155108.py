# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for e in nums:
            x ^= e
        print(x)
        for i in range(32):
            k = 1 << i
            nx = x
            for e in nums:
                if e&k:
                    nx ^= e
            if nx != x and nx != 0:
                return [nx, x^nx]
        return [0,x]
        