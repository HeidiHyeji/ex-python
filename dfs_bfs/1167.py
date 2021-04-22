import sys
from collections import deque

def bfs(c):
    queue = deque([c])
    visited[c] = True
    while queue:
        x = queue.popleft()
        i = 0
        while i < len(graph[x]):
            if not visited[graph[x][i]]:
                queue.append(graph[x][i])
                value[graph[x][i]] = value[x] +  graph[x][i+1]
                visited[graph[x][i]] = True
            i+=2

V = int(input())
graph = [[] for i in range(V+1)]
visited = [False] * (V+1)
value = [0] * (V+1)

for i in range(V):
    tmp = list(map(int,sys.stdin.readline().split()))
    first = tmp[0]
    del tmp[0];tmp.pop()
    graph[first] = tmp

bfs(1)
t = value.index(max(value))
value = [0] * (V+1)
visited = [False] * (V+1)
bfs(t)
print(max(value))
