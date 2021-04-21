import sys
from collections import deque

dx = [0,0,-1,+1]
dy = [-1,+1,0,0]

def bfs():
    while q:
        x,y = q.popleft()
        #box[x][y] = 1
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if cx<0 or cx>=N or cy<0 or cy>=M:
                continue
            if box[cx][cy] == 0:
                box[cx][cy] = box[x][y]+1
                q.append((cx,cy))
                
M,N = map(int,sys.stdin.readline().split())
box = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
#d = [[0 for i in range(M)] for j in range(N)]

q = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i,j))
bfs()
result = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            result = -1
            break
        result = max(result,box[i][j]-1)
    if result == -1:
        break
print(result)