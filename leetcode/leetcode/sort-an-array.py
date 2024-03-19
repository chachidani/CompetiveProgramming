class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def do(left_half,right_half):
                l = 0
                r = 0
                newArr = []
                while l<len(left_half) and r < len(right_half):
                    if left_half[l] < right_half[r]:
                        newArr.append(left_half[l])
                        l+=1
                    elif left_half[l] > right_half[r]:
                        newArr.append(right_half[r])
                        r+=1
                    elif left_half[l] == right_half[r]:
                        newArr.append(left_half[l])
                        newArr.append(right_half[r])
                        l+=1
                        r+=1
                if r< len(right_half):
                    for i  in range(r,len(right_half)):
                        newArr.append(right_half[i])
                elif l< len(left_half):
                    for i  in range(l,len(left_half)):
                        newArr.append(left_half[i])
                return newArr
                        
          
        def sortArr(left,right):
            if left == right:
                return [nums[left]]
                
            mid = (left+right)//2
            left_half  = sortArr(left,mid)
            right_half = sortArr(mid+1,right) 

            return  do(left_half,right_half)
        return sortArr(0,len(nums)-1)

        