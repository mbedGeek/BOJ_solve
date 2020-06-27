from collections import deque, Counter

import sys
input = sys.stdin.readline

hist = list()
stack = list()

T = int(input())

maxNo = 0

for i in range(T):
    hist.append(int(input()))
    while stack and (hist[stack[-1]] > hist[i]):
        j = stack[-1]
        stack.pop()
        width = i
        if stack:
            width -= stack[-1] + 1
        compare = hist[j] * width
        if maxNo < compare:
            maxNo = compare
        else:
            maxNo = maxNo
    stack.append(i)

while stack:
    j = stack[-1]
    stack.pop()
    width2 = T
    if stack:
        width2 -= stack[-1] + 1
    compare2 = hist[j] * width2
    if maxNo < compare2:
        maxNo = compare2
    else:
        maxNo = maxNo

print(maxNo)