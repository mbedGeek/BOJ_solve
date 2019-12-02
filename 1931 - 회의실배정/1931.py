#BOJ 1931 회의실 배정

import sys
input = sys.stdin.readline

def greedy(meeting):
    cnt = 0
    start = 0
    for item in meeting:
        if item[0] >= start:
            start = item[1]
            cnt += 1
    return cnt

N = int(input())
meeting = []
for i in range(N):
    start, end = map(int, input().split())
    meeting.append((start, end))
meeting = sorted(meeting, key = lambda item:item[0])
meeting = sorted(meeting, key = lambda item:item[1])
print(greedy(meeting))
