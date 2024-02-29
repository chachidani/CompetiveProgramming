class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def perm(idx,path):
            if len(path) == len(nums):
                ans.append(path[:])
                return 

            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    perm(i+1,path[:])
                    path.pop()
                
        ans = []
        perm(0,[])
        return ans
        
        