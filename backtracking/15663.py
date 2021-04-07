def func(k):
    if k == M:
        for i in range(M):
            print(arr[i],end=' ')
        print()
        return
    temp = 0
    for i in range(N):
        if not visited[i] and num[i]!= temp:
            visited[i] = True
            arr[k] = num[i]
            temp = num[i]
            func(k+1)
            visited[i] = False
N, M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
arr = [0] * M
visited = [False]*N

func(0)
