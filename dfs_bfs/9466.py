import sys
sys.setrecursionlimit(10**8)
cnt=0
def dfs(i):
    global cnt
    visited[i] = True
    p = partner[i]
    if not visited[p]:
        dfs(p)
    elif not finished[p]:
        j = p
        while j!=i:
            cnt+=1
            j = partner[j]
        cnt+=1
    finished[i] = True

T = int(sys.stdin.readline())
for t in range(T):
    n = int(sys.stdin.readline())
    partner = list(map(int,sys.stdin.readline().split()))
    partner.insert(0,0)

    visited = [False] * (n+1) #방문여부
    finished = [False] * (n+1) #팀확인여부
    cnt = 0
    
    for j in range(1,n+1):
        if not visited[j]:
            dfs(j)
    print(n-cnt)
