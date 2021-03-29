from collections import deque

def dfs(g,V,visited):
    # 현재 노드를 방문처리
    visited[V] =  True
    print(V, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in g[V]:
        if not visited[i]:
            dfs(g,i,visited)

def bfs(g,V,visited):
    q = deque([V])
    visited[V] = True

    while q:
        c = q.popleft()
        print(c, end = ' ')

        for i in g[c]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
        
            

N, M, V = map(int,input().split())

# 각 노드가 연결된 정보를 표현
g = [[] for i in range(N+1)]
for i in range(M):
    n1,n2 = map(int,input().split())
    g[n1].append(n2)
    g[n2].append(n1)
    g[n1].sort()
    g[n2].sort()


# 각 노드가 방문된 정보를 표현
visited = [False] * (N+1)

# 정의된 DFS 함수 호출
dfs(g, V, visited)
print()
visited = [False] * (N+1)
# 정의된 BFS 함수 호출
bfs(g,V,visited)
