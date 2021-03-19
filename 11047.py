N, K = map(int,input().split())
A=[]
for i in range(N):
    A.append(int(input()))
A.sort()
A.reverse()
result,cnt = K,0
for i in range(N):
    cnt += result // A[i]
    result %= A[i]
print(cnt)
    