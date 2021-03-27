N, M, K = map(int,input().split())
cnt = 0
while N+M >= K and N >= 0 and M >= 0:
    N -= 2
    M -= 1
    cnt +=1
cnt = cnt - 1 if cnt > 0 else 0
print(cnt)
