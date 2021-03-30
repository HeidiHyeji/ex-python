import sys

def dfs(i,j,num):
    if i < 0 or j < 0  or i >= N or j >= N:
        return False
    elif map[i][j] == 0:
        return False
    if map[i][j] == 1:
        map[i][j] = 0
        if len(danji) < num+1: 
            danji.insert(num,1)
        else: 
            danji[num]+=1
        dfs(i,j+1,num)
        dfs(i,j-1,num)
        dfs(i+1,j,num)
        dfs(i-1,j,num)
        return True
    return False
            
N = int(input())
map = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
num = 0
danji = []
for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            if dfs(i,j,num):
                num +=1
danji.sort()
print(len(danji))
for i in danji:
    print(i)