#BOJ 17143 낚시왕

import sys
from collections import deque
input = sys.stdin.readline

#r - X좌표
#c - Y좌표
#s - 속력
#d - 방향 (1: 위 / 2: 아래 / 3: 오른쪽 / 4: 왼쪽)
#z - 크기

R, C, M = map(int, input().split())
A = [[[0, 0, 0] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    x, y, s, d, z = map(int, input().split())
    A[x-1][y-1] = [s, d-1, z]
dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)
ans = 0

for t in range(C):
    b = [[[0, 0, 0] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        _, _, z = A[i][t]
        if(z):
            ans += z
            A[i][t] = [0, 0, 0]
            break
    for i in range(R):
        for j in range(C):
            s, d, z = A[i][j]
            if(z):
                if(d < 2):
                    ns, nd, ni = s % ((R-1)*2), d, i
                    for _ in range(ns):
                        if ni == 0 and nd == 0:
                            nd = 1
                        if ni == R-1 and nd == 1:
                            nd = 0
                        ni += dx[nd]
                    _, _, bz = b[ni][j]
                    if z > bz:
                        b[ni][j] = [s, nd, z]
                else:
                    ns, nd, nj = s % ((C-1)*2), d, j
                    for _ in range(ns):
                        if nj == 0 and nd == 3:
                            nd = 2
                        if nj == C-1 and nd == 2:
                            nd = 3
                        nj += dy[nd]
                    _, _, bz = b[i][nj]
                    if z > bz:
                        b[i][nj] = [s, nd, z]
                A[i][j] = [0, 0, 0]
    A = b[:]

print(ans)
