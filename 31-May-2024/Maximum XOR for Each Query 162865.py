# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
   
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        
        prefix_sum = [nums[0]]
        for a in range(1, len(nums)):
            prefix_sum.append(prefix_sum[len(prefix_sum)-1] ^ nums[a])
        
        comparison = 2 ** maximumBit
        ans = []
       
        for i in range(len(prefix_sum)-1, -1, -1):
          
            current_res = prefix_sum[i]

            res = current_res ^ (comparison - 1)
            ans.append(res)
        return ans