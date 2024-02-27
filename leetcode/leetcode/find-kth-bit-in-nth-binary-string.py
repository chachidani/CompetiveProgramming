class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            new_s = ''
            for i,val in enumerate(s):
                if val == '0':
                    new_s += '1'
                else:
                    new_s += '0'
            return new_s
        def reverse(s):
            return s[::-1]
                    

        def find(n):
            if n == 1:
                return '0'
            return find(n-1) + '1' + reverse(invert(find(n-1)))
        x = find(n)
        return x[k-1]

        