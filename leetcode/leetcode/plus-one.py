class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        strr = ''
        for i, val in enumerate(digits):
            strr +=str(val)
        strr = str(int(strr)+1)
        for i, val in enumerate(strr):
            ans.append(int(val))
        return ans
        