class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
    
        def additive(idx,path,num):

            
            if  idx >= len(num):
               
                i = 2
                while i <= len(path)-1:
                    if path[i-2] + path[i-1] == path[i]:
                        i+=1
                        if i == len(path):
                            ans.append(path[:])
                            return True 
                        continue 
                    else:
                        break
                return 
            
            
            for i in range(idx,len(num)):
                val = int(num[idx:i+1])
                if val > 0 and  num[idx] == '0':
                    continue
                if len(path)>1 and path[-2] + path[-1] != val:
                    continue
                
                path.append(val)
                additive(i+1,path[:],num)
                path.pop()
                

        ans = []
        additive(0,[],num)
        # print(ans)
        return True if ans else False




        