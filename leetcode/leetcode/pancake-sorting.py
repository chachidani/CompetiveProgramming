class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []
        def revarr(arr , start , end):
            while start < end:
                arr[start] , arr[end] = arr[end] , arr[start]
                start +=1
                end -=1
            
        for target in range(n,0,-1):
            ind = arr.index(target)
            revarr(arr,0,ind)
            ans.append(ind+1)

            revarr(arr,0,target-1)
            ans.append(target)
        return ans

        



        

            


        
        