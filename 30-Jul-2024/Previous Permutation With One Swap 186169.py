# Problem: Previous Permutation With One Swap - https://leetcode.com/problems/previous-permutation-with-one-swap/description/

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n-1, 0, -1):
            if arr[i-1] > arr[i]:
                break
        maxElement = arr[i]
        maxIndex = i

        for j in range(i, n):
            print("j = ",j)
            if (maxElement < arr[j]) and (arr[j] < arr[i-1]):
                maxElement = arr[j]
                maxIndex = j
      
        arr[i-1], arr[maxIndex] = arr[maxIndex], arr[i-1]
        return arr