class Solution:
    def splitString(self, s: str) -> bool:
        
        def additive(idx,path,num):
            if  idx >= len(num):
                i = 1
                while i <= len(path)-1:
                    if  path[i-1] ==  path[i]+1:
                        i+=1
                        if i == len(path):
                            ans.append(path[:])
                            return 
                        continue 
                    else:
                        break
                return 
        
            for i in range(idx,len(num)):
                val = int(num[idx:i+1])
                
                if len(path)>=1 and  path[-1] < val:
                    continue
                
                path.append(val)
                additive(i+1,path[:],num)
                path.pop()
                

        ans = []
        additive(0,[],s)
        print(ans)
        return True if ans else False



        
        
        
    

        