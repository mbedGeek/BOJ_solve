#BOJ 16236 아기상어

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
q = []

def init():
    for i in range(N):
        for j in range(N):
            if(A[i][j] == 9):
                heappush(q, (0, i, j))
                A[i][j] = 0
                return

def bfs():
    body, eat, ans = 2, 0, 0
    check = [[False] * N for _ in range(N)]
    while(q):
        d, x, y = heappop(q)
        if(0 < A[x][y] < body):
            eat += 1
            A[x][y] = 0
            if eat == body:
                body += 1
                eat = 0
            ans += d
            d = 0
            while(q):
                q.pop()
            check = [[False] * N for _ in range(N)]
        for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
            nd, nx, ny = d+1, x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if 0 < A[nx][ny] > body or check[nx][ny]:
                continue
            check[nx][ny] = True
            heappush(q, (nd, nx, ny))
    print(ans)
    
init()
bfs()
