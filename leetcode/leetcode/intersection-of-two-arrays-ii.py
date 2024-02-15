class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out =[]
        s1 = sorted(nums1)
        s2 = sorted(nums2)
        l=0
        r=0
        
        while l < len(nums1) and  r < len(nums2):
            
            if s1[l] == s2[r]:
                out.append(s1[l])
                l +=1
                r +=1
            elif s1[l] < s2[r]:
                l += 1
            else:
                r += 1
        return out

                
        