import sys

def dfs(c):
    visited[c] = True
    if not visited[graph[c]]:
        dfs(graph[c])
    
T = int(input())
for i in range(T):
    N = int(sys.stdin.readline())
    graph = list(map(int,sys.stdin.readline().split()))
    graph.insert(0,0)
    visited = [False] * (N+1)
    cnt = 0
    for j in range(1,N+1):
        if not visited[j]:
            dfs(j)
            cnt += 1
    print(cnt)