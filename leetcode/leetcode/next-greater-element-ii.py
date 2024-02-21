class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, L = [], len(nums)
        res = [-1] * L

        for i in range(L*2):
            idx = i % L
            while stack and nums[stack[-1]] < nums[idx]:
                res[stack.pop()] = nums[idx]
            stack.append(idx)
        return res