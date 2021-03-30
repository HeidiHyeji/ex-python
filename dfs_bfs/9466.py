import sys
sys.setrecursionlimit(10**8)

def dfs(i,num):
    if i == partner[i]:
        return
    visited[i] = True
    number[i] = num
    p = partner[i]
    if not visited[p]:
        dfs(p,num)
    else:
        if number[p] == number[i] and p!=i:
            teams.append(num)

T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    partner = list(map(int,sys.stdin.readline().split()))
    partner.insert(0,0)
    teams = [] # 정상 종료시 팀번호를 추가한다. 
    number = [0] * (n+1) #요소들의 팀번호
    visited = [False] * (n+1)
    num = 1
    for j in range(1,n+1):
        if not visited[j] and j!=partner[j]:
            dfs(j,num)
            num += 1
    
    cnt = 0
    for k in range(1,n+1):
        if number[k] not in teams:
            cnt += 1
        if k == partner[k]:
            cnt -=1
    print(cnt)
