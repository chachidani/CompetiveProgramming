class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        x = Counter(nums)
        for key , value in x.items():
            if value > n//3:
                ans.append(key)
        return ans

        