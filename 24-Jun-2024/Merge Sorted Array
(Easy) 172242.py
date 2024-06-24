# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        \
        l =0 
        for i in range(len(nums1)-m):
            
                

            if nums2:
                nums1[m] = nums2[l]
                
                l+=1
                m+=1
        
        for i in range(len(nums1)):
            for j in range(len(nums1)-i-1):
                if nums1[j] >nums1[j+1]:
                    nums1[j],nums1[j+1] = nums1[j+1],nums1[j]
        return nums1




                
            
               


        