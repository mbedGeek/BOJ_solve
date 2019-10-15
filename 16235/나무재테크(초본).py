#16235 BOJ 나무재테크
#jupyter notebook version

#import sys
#input = sys.stdin.readline

N, M, K = map(int, input().split())
A_winter = [list(map(int, input().split())) for _ in range(N)]
A = [[5 for _ in range(N)] for _ in range(N)]
A_tree = [list(map(int, input().split())) for _ in range(M)]
tmp = list()

for i in range(M):
    A_tree[i][0] -= 1
    A_tree[i][1] -= 1
    
for _ in range(K):
    #spring
    for i in range(M - 1, -1, -1):
        if(A[A_tree[i][0]][A_tree[i][1]] >= A_tree[i][2]):
            A[A_tree[i][0]][A_tree[i][1]] -= A_tree[i][2]
            A_tree[i][2] += 1
        elif(A[A_tree[i][0]][A_tree[i][1]] < A_tree[i][2]):
            tmp.append(A_tree[i])
            M -= 1
            A_tree.pop(i)
    
    #summer
    for i in range(len(tmp) - 1, -1, -1):
        A[tmp[i][0]][tmp[i][1]] += (tmp[i][2] // 2)
        tmp.pop(i)
    
    #fall
    for i in range(M):
        if((A_tree[i][2] % 5) == 0):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if((j == 0) and (k == 0)):
                        continue
                    else:
                        if(((A_tree[i][0] + j) < 0) or ((A_tree[i][0] + j) > (N-1)) or ((A_tree[i][1] + k) < 0) or ((A_tree[i][1] + k) > (N-1))):
                            continue
                        else:
                            A_tree.append([A_tree[i][0] + j, A_tree[i][1] + k, 1])
                            M += 1
    
    #winter
    for i in range(N):
        for j in range(N):
            A[i][j] += A_winter[i][j]
                        

print(M)
