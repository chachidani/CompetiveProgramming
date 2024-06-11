# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

minn = 1
        l = 0
        r = len(nums)

        while l < len(nums):
            if nums[l] <= 0 or nums[l] > r or nums[l] == l+1 :
                l +=1
            elif nums[l] != l+1 and nums[l] <= r  :
                correct = nums[l]-1
                if nums[l] == nums[correct]:
                    l += 1
                else: 
                    nums[l] , nums[correct] =  nums[correct],nums[l]

        for i in range(len(nums)):
            if nums[i] == minn:
                minn +=1
        return minn