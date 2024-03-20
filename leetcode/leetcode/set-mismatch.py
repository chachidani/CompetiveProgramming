class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans  =[]
        comp = []
        maxx = len(nums)
      
        for i in range(maxx):
            comp.append(i+1)

        print(comp)
        l = 0
        r = 0
        while r < len(comp) and l < len(nums):
            if comp[r] == nums[l]:
                r +=1
                l +=1
            elif comp[r] < nums[l]:
                ans.append(comp[r])
                r +=1
            elif comp[r] > nums[l]:
                ans = [nums[l]] + ans
                l += 1
        ans += comp[r:]
        ans  = nums[l:] + ans
            
        return ans
                

        
        
        