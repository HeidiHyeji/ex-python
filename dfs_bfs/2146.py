import sys
from collections import deque
sys.setrecursionlimit(10**8)

def bfs(num):
    while queue:
        cx,cy = queue.popleft()
        for i in range(4):
            nx = cx+mx[i]
            ny = cy+my[i]
            if nx<0 or nx>= N or ny<0 or ny>=N: #범위를 벗어날 경우
                continue
            if d[nx][ny] != 0:
                continue
            if zido[nx][ny] == 0: #바다인 경우
                d[nx][ny] = d[cx][cy]+1
                queue.append((nx,ny))
            elif zido[nx][ny] != num:
                return d[cx][cy] - 1            
    return N*N

def dfs(number,x,y):
    visited[x][y] = True
    zido[x][y] = number
    for i in range(4):
        nx = x+mx[i]
        ny = y+my[i]
        if nx<0 or nx>= N or ny<0 or ny>=N: #범위를 벗어날 경우
            continue
        if zido[nx][ny] == 0: #바다인 경우
            beach[number].append((x,y))
            continue
        if not visited[nx][ny]:
            dfs(number,nx,ny)
    
N = int(input())
result = N*N
zido = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited = [[False for i in range(N)] for j in range(N)]

mx = [0,0,-1,+1]
my = [+1,-1,0,0]
number = 0
beach = [[] for i in range(int(N*N))]

for i in range(N):#O(N**2) = 10000
    for j in range(N):
        if not visited[i][j] and zido[i][j] == 1:
            number += 1
            dfs(number,i,j)

for i in range(1,number):#O(N**4/2)= 50000000
    beach[i] = list(set(beach[i]))
    queue = deque()
    d = [[0 for i in range(N)] for _ in range(N)]
    for j in range(len(beach[i])):
        ti,tj = beach[i][j]
        queue.append((ti,tj))
        d[ti][tj] = 1
    tmp = bfs(i)
    if tmp < result:
        result = tmp
print(result)
'''
5
1 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 0 0 1
'''