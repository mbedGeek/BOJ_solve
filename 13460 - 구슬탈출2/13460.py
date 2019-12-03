#BOJ 13460 구슬탈출2

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(input().strip()) for _ in range(N)]
check = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx, dy = (-1, 0, 1, 0), (0, -1, 0, 1)
q = deque()

def init():
    _rx, _ry, _bx, _by = [0] * 4
    for i in range(N):
        for j in range(M):
            if(A[i][j] == "R"):
                _rx = i
                _ry = j
            elif(A[i][j] == "B"):
                _bx = i
                _by = j
    q.append((_rx, _ry, _bx, _by, 0))
    check[_rx][_ry][_bx][_by] = True

def move(_x, _y, _dx, _dy, _c):
    while A[_x + _dx][_y + _dy] != '#' and A[_x][_y] != 'O':
        _x += _dx
        _y += _dy
        _c += 1
    return _x, _y, _c

def bfs():
    while q:
        rx, ry, bx, by, d = q.popleft()
        if(d >= 10):
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)
            
            if(A[nbx][nby] == 'O'):
                continue
            if(A[nrx][nry] == 'O'):
                print(d + 1)
                return
            if (nrx == nbx and nry == nby):
                if(rc > bc):
                    nrx, nry = nrx - dx[i], nry - dy[i]
                else:
                    nbx, nby = nbx - dx[i], nby - dy[i]
            if (not check[nrx][nry][nbx][nby]):
                check[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, d+1))
    print(-1)


init()
bfs()
