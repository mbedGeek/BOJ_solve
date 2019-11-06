#4ms faster version

import sys
input = sys.stdin.readline

T = int(input())
arr = list(map(int, input().split()))
cnt = 0

def prime(_n):
    if _n < 2:
        return False
    for i in range(2, _n//2+1):
        if _n % i == 0:
            return False
    return True

for i in range(T):
    if prime(arr[i]):
        cnt += 1

print(cnt)
