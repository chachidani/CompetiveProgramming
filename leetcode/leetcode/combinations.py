class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def comb(fi,path):
            if len(path) == k:
                ans.append(path[:])
                return 
            for i in range(fi,n+1):
                path.append(i)
                comb(i+1,path)
                path.pop()
        ans = []
        comb(1,[])
        return ans



        