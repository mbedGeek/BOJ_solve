#BOJ 1260 DFS와 BFS - Adjecent Index

from collections import deque
import sys
input = sys.stdin.readline

def dfs(_graph, _start):
    visit = list()
    s = list()
    s.append(_start)
    while s:
        node = s.pop()
        if node not in visit:
            visit.append(node)
            if _graph[node] == None:
                return visit
            for i in range(len(_graph[node])-1, -1, -1):
                s.append(_graph[node][i])
    return visit

def bfs(_graph, _start):
    visit = list()
    q = deque()
    q.append(_start)
    while q:
        node = q.popleft()
        if node not in visit:
            visit.append(node)
            if _graph[node] == None:
                return visit
            q.extend(_graph[node])
    return visit
            
n, m, v = map(int, input().split())
graph = [list() for _ in range(n+1)]
for _ in range(m):
    key, child = map(int, input().split())
    graph[key].append(child)
    graph[child].append(key)

#DFS
for i in range(1, len(graph)):
    graph[i].sort()
for item in dfs(graph, v):
    print(item, end=' ')

print()

#BFS
for item in bfs(graph, v):
    print(item, end=' ')
