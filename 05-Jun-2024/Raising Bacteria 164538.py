# Problem: Raising Bacteria - https://codeforces.com/contest/579/problem/A

n = int(input())
counter = 0
while n:
    counter += n&1
    n >>= 1
print(counter)