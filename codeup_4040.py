n,m = map(int,input().split())#n:여름 성수기 총기간, m:방의개수
r = [list(input()) for i in range(n)]
s,t = map(int,input().split()) #s: 펜션 도착, t:펜션떠나는날
s=s-1;t=t-1;cnt=0
p = [0 for i in range(m)]
for j in range(s,t):
    for i in range(m):
        if r[j][i] == 'O':
            p[i]+=1
        else:
            if p[i]!= 0 and max(p)==p[i]:
                cnt+=1
            p[i]=0
    if sum(p) == 0:
        cnt=-1
        break
print(cnt)