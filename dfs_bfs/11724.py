import sys
sys.setrecursionlimit(10000)

def dfs(c):
    visited[c] = True
    for i in g[c]:
        if not visited[i]:
            dfs(i)

N,M = map(int,sys.stdin.readline().split())
g = [[] for i in range(N+1)]
for i in range(M):
    u,v = map(int,sys.stdin.readline().split())
    g[u].append(v)
    g[v].append(u)

visited = [False] * (N+1)

cnt = 0
for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        cnt+=1
print(cnt)

