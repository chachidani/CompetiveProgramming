class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def sub(idx,path,ans):
            if idx >= len(nums):
                ans.append(path[:])
                return 
            path.append(nums[idx])
            sub(idx+1,path,ans)
            path.pop()
            while idx+1 <len(nums)and nums[idx]==nums[idx+1]:
                idx +=1
            sub(idx+1,path,ans)
            
            return ans
        return sub(0,[],[])

        