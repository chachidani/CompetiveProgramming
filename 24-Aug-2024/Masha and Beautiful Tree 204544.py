# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int,input().split()))
    def func():
        op = 0
        def mergeSort(left_half,right_half):
            nonlocal op
            ans = []
            if left_half[0] > right_half[0]:
                op += 1
                ans += right_half + left_half
            else:
                ans += left_half + right_half
            
            return ans
 
 
        def merge(left, right , arr):
            if left == right:
                return [arr[left]]
            mid = (left + right)//2
            left_half = merge(left,mid,arr)
            right_half = merge(mid+1,right,arr)
            return mergeSort(left_half,right_half)
        
        new_arr = sorted(arr)
        
        if merge(0,m-1,arr) == new_arr:
            return op
        else:
            return -1
    print(func())