import sys
from collections import deque

def bfs():
    dq = deque()
    dq.append((0,0))
    while dq:
        x,y = dq.popleft()
        for i in range(4):
            tx = x+mx[i]
            ty = y+my[i]

            #미로 밖일 경우
            if tx<0 or ty<0 or tx>=N or ty>=M:
                continue
            #벽이거나 방문한적 있는 경우
            elif miro[tx][ty] != 1 or (tx == 0 and ty == 0):
                continue
            miro[tx][ty] = miro[x][y]+1
            dq.append((tx,ty))

N, M = map(int,input().split())
miro = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]

mx = [0,0,-1,+1]
my = [-1,+1,0,0]

##0,0부터 bfs
bfs()

print(miro[N-1][M-1])

