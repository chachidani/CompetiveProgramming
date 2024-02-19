class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        store = {}
        ans = []
        r = 0
        while r<len(nums2):
            if not stack:
                stack.append(nums2[r])
                r +=1
            elif nums2[r] > stack[-1] and len(stack)>0:
                store[stack[-1]] = nums2[r]
                stack.pop()
            elif nums2[r] > stack[-1] and len(stack)== 0:
                store[stack[-1]] = nums2[r]
                stack.pop()
                stack.append(nums2[r])
                r +=1
            elif nums2[r] < stack[-1]:
                stack.append(nums2[r])
                r +=1

            
                
        
        while stack:
            if nums2[-1] > stack[-1]:
                store[stack[-1]] = nums2[-1]
            else:
                store[stack[-1]] = -1
            stack.pop()
        for num in nums1:
            ans.append(store.get(num , -1))
        
        return ans




