class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def comb(fi,path):
            if sum(path) == target:
                if path not in ans:
                    ans.append(path[:])
                    
                return 
            if sum(path[:]) > target: return
            for i in range(fi,len(candidates)):
                path.append(candidates[i])
                comb(i+1,path)
                comb(i,path)
                path.pop()
        ans = []
        comb(0,[])
        return ans
        