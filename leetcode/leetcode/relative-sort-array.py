class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        size = len(arr1)
        s = {}
        for i in range(len(arr2)):
            s[arr2[i]] = i 
        def relativeSort(x):
            if x in s:
                return s[x]
            return size + x
        arr1.sort(key=relativeSort)
        return arr1
                
        