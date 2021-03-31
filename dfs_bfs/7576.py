import sys
from collections import deque

def bfs():
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            tx = x + mx[k]
            ty = y + my[k]
            # 상자 범위를 벗어난 경우
            if tx < 0 or ty < 0 or tx >= N or ty >= M:
                continue
            # 토마토가 없거나 이미 방문한경우
            elif box[tx][ty] != 0:
                continue

            queue.append((tx,ty))
            day[tx][ty] = day[x][y]+1
            box[tx][ty] = 1
            
M, N = map(int,input().split())
box = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
day = [[0 for _ in range(M)] for i in range(N)]

mx = [0,0,-1,+1]
my = [-1,+1,0,0]
queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:           
            queue.append((i,j))        
bfs()

#결과 출력
m = 0
notomato = False
for i in range(N):
    if max(day[i]) > m:
        m = max(day[i])
    if 0 in box[i]:
        notomato = True
        break

if notomato: # 하나라도 안익은게 있는 상태
    print(-1)
elif m == 0: # 모든 토마토가 처음부터 익어있는 상태
    print(0)
else:
    print(m)