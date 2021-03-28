import sys
sys.setrecursionlimit(10000)
def dfs(g,c,visited):
    visited[c] = True
    for i in g[c]:
        if not visited[i]:
            dfs(g,i,visited)
    return True

N,M = map(int,input().split())
g = [[] for i in range(N+1)]
for i in range(M):
    u,v = map(int,input().split())
    g[u].append(v)
    g[v].append(u)

visited = [False] * (N+1)

cnt = 0
for i in range(1,N+1):
    if not visited[i]:
        dfs(g,i,visited)
        cnt+=1
print(cnt)