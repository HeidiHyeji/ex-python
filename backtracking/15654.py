def func(k):
    if k == M:
        for i in range(M):
            print(arr[i],end=' ')
        print()
        return
    for i in num:
        if not visited[i]:
            arr[k] = i
            visited[i] = True
            func(k+1) 
            visited[i] = False

N, M = map(int, input().split())
num = list(map(int,input().split()))
num.sort()
arr = [0] * M
visited = [False]*(max(num)+1)
func(0)