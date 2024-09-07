# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(idx,path,num):
            if idx >= len(num):
                i = 1
                while i <= len(path)-1 :
                    if path[i-1] == path[i]+1:
                        i += 1
                        if i == len(path):
                            ans.append(path[:])
                            return 
                        continue
                    else:
                        break
                return 

            for i in range(idx,len(num)):
                val = int(num[idx:i+1])
                if len(path) > 0 and path[-1] < val:
                    continue
                path.append(val)
                dfs(i+1,path[:],num)
                
                path.pop()
        ans = []
        dfs(0,[],s)
        return True if ans else False

        

        