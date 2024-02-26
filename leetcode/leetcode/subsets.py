class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sub(idx,path,ans):
            
            if idx >= len(nums):
                ans.append(path[:])
                return 
            path.append(nums[idx])
            sub(idx+1,path,ans)
            path.pop()
            sub(idx+1,path,ans)
            return ans
        
        return sub(0,[],[])
        
        