class Solution:
    def smallestNumber(self, num: int) -> int:
        if not num: return 0
        if num > 0:
            nums =[x for x in str(num)]

            nums = sorted(nums)
            for i in range(len(nums)):
                if nums[i]!="0":
                    nums[0] , nums[i] = nums[i] , nums[0]
                    break
            return int(''.join(map(str,nums)))
                    

            

        else:
            nums =[x for x in str(num)[1:]]

            nums.sort(reverse=True)
            return -int(''.join(map(str,nums)))
        
        
        
        
    
        