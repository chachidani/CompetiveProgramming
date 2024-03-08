class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        summ = 0
        l = 0
        maxsum = float('-inf')
        store = {}
        for r in range(len(nums)):
            print(summ)
            if nums[r] not in store:
                store[nums[r]] = 1
                summ += nums[r]
                maxsum = max(summ,maxsum)
            else:
                while nums[l] != nums[r]:
                    del store[nums[l]]
                    summ -= nums[l]
                    maxsum = max(summ,maxsum)
                    l +=1
                l +=1
        return maxsum if maxsum != float('-inf') else 0
                

        