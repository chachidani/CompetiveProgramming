class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
       summ = 0
       pref = []
       for num in nums:
           summ +=num
           pref.append(summ)
       return pref
