#BOJ 14503 로봇청소기

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split()) #N: 세로크기 / M: 가로크기
r, c, d = map(int, input().split()) #d -> 0:북 / 1:동 / 2:남 / 3:서
A = [list(map(int, input().split())) for _ in range(N)] #0: 빈 곳 / 1: 벽
dxy = deque([(0, -1), (-1, 0), (0, 1), (1, 0)])
done, cnt = 1, 0
A[r][c] = 2
dxy.rotate(-d)
y, x = r, c
while True:
    dxy.rotate(-1)
    dx, dy = dxy[0] 
    if(cnt == 4):
        cnt = 0
        x -= dx
        y -= dy
        if A[y][x] == 1:
            print(done)
            break
    if(A[y+dy][x+dx] != 0):
        cnt += 1
    else:
        x += dx
        y += dy
        done += 1
        A[y][x] = 2
        cnt = 0
