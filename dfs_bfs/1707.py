import sys
from collections import deque

def bfs(c):
    queue = deque([c])
    visited[c] = True
    bi[c] = True

    while queue:
        k = queue.popleft()
        for i in graph[k]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                bi[i] = not bi[k]
            else:
                if bi[i] == bi[k]:
                    return False
    return True
    

K = int(input())
for i in range(K):
    V, E = map(int,sys.stdin.readline().split())
    graph = [[] for x in range(V+1)]
    visited = [False] * (V+1)
    bi = [None] * (V+1)
    for j in range(E):
        u,v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    result = 'YES'
    for c in range(1,V+1):
        if not visited[c]:
            if not bfs(c):
                result = 'NO'
    print(result)