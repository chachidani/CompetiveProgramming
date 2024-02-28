class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float('inf')
        def dist(i,distrbution):
            nonlocal ans
            if i >= len(cookies):
                ans = min(ans,max(distrbution))
                return 
            if distrbution.count(0) > len(cookies) -i:
                return 
            if max(distrbution) > ans: 
                return

            for j in range(k):
                distrbution[j] += cookies[i]
                dist(i+1,distrbution)
                distrbution[j] -= cookies[i]
        
        
        dist(0,[0]*k)
        return ans




        