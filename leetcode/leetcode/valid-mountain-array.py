class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        r = 0
        while r<len(arr)-1:
            if arr[r]<arr[r+1]:
                r +=1
                continue
            else:
                break
        if r == len(arr)-1 or r==0:
            return False
        else:
            while r<len(arr)-1:
                if arr[r]>arr[r+1]:
                    r+=1
                    continue
                else:
                    return False
            return True



        