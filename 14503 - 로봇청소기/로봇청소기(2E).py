#import sys
from collections import deque
#input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)
A[r][c] = 2

def simulation(r, c, d, done):
    while True:
        cnt = False
        for i in range(4):
            nd = (d + 3) % 4
            nr = r + dr[nd]
            nc = c + dc[nd]
            d = nd
            if not A[nr][nc]:
                A[nr][nc] = 2
                r, c = nr, nc
                done += 1
                cnt = True
                break
        if not cnt:
            if A[r-dr[d]][c-dc[d]] == 1:
                return done
            r -= dr[d]
            c -= dc[d]
            
print(simulation(r, c, d, 1))
