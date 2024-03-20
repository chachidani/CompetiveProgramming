class Solution:
    def findLHS(self, nums: List[int]) -> int:
        que = []
        nums.sort()
        maxx = float('-inf')
        for num in nums:
            if not que:
                que.append(num)
            elif que[0]+1 == num or que[0] == num:
                que.append(num)
                
            elif que[0]+1 != num:
                while que[0]+1 != num and len(que) > 1:
                    que = que[1:]
                if que and que[0]+1 != num:
                    que = []
                que.append(num)
               
            if que[0]+1 == que[-1]:
                maxx = max(len(que),maxx)
            
        return maxx if maxx != float('-inf') else 0
