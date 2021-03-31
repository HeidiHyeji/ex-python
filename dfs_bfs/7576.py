import sys
from collections import deque

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    #box[i][j] = 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            tx = x + mx[k]
            ty = y + my[k]
            if tx < 0 or ty < 0 or tx >= N or ty >= M or box[tx][ty] == -1 or box[tx][ty] == 1:
                continue
            if box[tx][ty] != 0 and box[tx][ty] <= box[x][y]+1:
                continue

            queue.append((tx,ty))
            box[tx][ty] = box[x][y] + 1
            
M, N = map(int,input().split())
box = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

mx = [0,0,-1,+1]
my = [-1,+1,0,0]

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:           
            bfs(i,j)

#결과 출력
m = 0
notomato = False
already = True
for i in range(N):
    if max(box[i]) > m:
        m = max(box[i])
    if 0 in box[i]:
        notomato = True
    if 2 in box[i]:
        already = False
    '''
    for j in range(M):
        if box[i][j] > max:
            max = box[i][j]
        if box[i][j] == 0:
            notomato = True
        if box[i][j] > 1:
            already = False
    '''
if already: # 모든 토마토가 처음부터 익어있는 상태
    print(0)
elif notomato: # 하나라도 안익은게 있는 상태
    print(-1)
else:
    print(m-1)