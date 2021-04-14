def func(k):
    if k == M:
        arr.sort()
        for j in range(M):
            print(arr[j],end=' ')
        print()
        return
    for i in range(1,N+1):
        if not visited[i]:
            arr[k] = i
            visited[i] = True
            func(k+1)
            visited[i] = False

N,M = map(int,input().split())
visited = [False] * (N+1)
arr  = [0] * M
func(0)