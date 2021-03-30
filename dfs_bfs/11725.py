import sys
from collections import deque

def bfs():
    queue = deque([1])
    while queue:
        x = queue.popleft()
        for i in tree[x]:
            if parent[i] == 0:
                queue.append(i)
                parent[i] = x

N = int(input())
tree = [[] for i in range(N+1)]
parent = [0] * (N+1)
for i in range(N-1):
    u,v = map(int, sys.stdin.readline().split())
    tree[u].append(v) #인접리스트 생성
    tree[v].append(u) 

bfs()
for i in range(2,N+1):
    print(parent[i])