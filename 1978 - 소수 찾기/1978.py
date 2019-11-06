#BOJ 1978 - 소수 찾기

import sys
from collections import deque
import math
input = sys.stdin.readline

T = int(input())
arr = list(map(int, input().split()))
cnt = 0

def prime(_n):
    if _n < 2:
        return False
    for i in range(2, int(math.sqrt(_n))+1):
        if _n % i == 0:
            return False
    return True

for i in range(T):
    if prime(arr[i]):
        cnt += 1

print(cnt)
