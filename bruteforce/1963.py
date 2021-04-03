import sys
from collections import deque
def isSosu(k):
    for h in range(2, k):
        if k%h == 0:
            return False
    return True

def getGraph(s,g):
    lists = list(s)
    if s == B or int(s) > 9999 or len(g[int(s)])!=0: return

    for i in range(len(s)):
        news = lists.copy()
        for j in range(0,10):
            if lists[i] == str(j):
                continue
            else:
                news[i] = str(j)
                newpwd = int("".join(news))
                if newpwd in g[int(s)]:
                    continue
                if isSosu(newpwd):
                    g[int(s)].append(newpwd)
                    getGraph(str(newpwd),g)
def bfs(A,g):
    queue = deque([int(A)])
    visited[int(A)] = True
    while queue:
        x = queue.popleft()
        for i in g[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[x]+1

T = int(sys.stdin.readline().strip())
g = [[] for _ in range(10000)]
for v in range(T):
    A,B = sys.stdin.readline().split()
    visited = [False] * 10000
    distance = [0] * 10000
    getGraph(A,g)
    bfs(A,g)
    print(distance[int(B)])
    