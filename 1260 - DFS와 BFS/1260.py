#BOJ 1260 DFS와 BFS

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
            if node not in _graph:
                return visit
            for item in _graph[node]:
                s.append(item)
    return visit

def bfs(_graph, _start):
    visit = list()
    q = deque()
    q.append(_start)
    while q:
        node = q.popleft()
        if node not in visit:
            visit.append(node)
            if node not in _graph:
                return visit
            q.extend(_graph[node])
    return visit
        
n, m, v = map(int, input().split())
graph = dict()
for _ in range(m):
    key, child = map(int, input().split())
    if key not in graph:
        graph[key] = list()
    if child not in graph:
        graph[child] = list()
    graph[key].append(child)
    graph[child].append(key)
    
for key in graph:
    graph[key].sort(reverse=True)
for item in dfs(graph, v):
    print(item, end=' ')
print()
for key in graph:
    graph[key].sort()
for item in bfs(graph, v):
    print(item, end=' ')
