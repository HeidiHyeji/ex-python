import sys

def dfs(i,num):
    visited[i] = True
    number[i] = num

T = int(input())
for i in range(T):
    n = int(sys.stdin.readline())
    partner = list(map(int,sys.stdin.readline().split()))
    partner.insert(0,0)
    teams = [] # 정상 종료시 팀번호를 추가한다. 
    number = [0] * (n+1)
    visited = [False] * (n+1)
    num = 1
    for j in range(1,n+1):
        if not visited[j]:
            dfs(j,num)
            
