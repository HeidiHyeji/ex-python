def func(k):
    if k == M:
        for i in range(M):
            print(arr[i],end = ' ')
        print()
        return
    for i in range(1,N+1):
        if not isused[i]:
            arr[k] = i
            isused[i] = True
            func(k+1)
            isused[i] = False

N,M = map(int,input().split())#nCm
isused = [False] * (N+1)
arr = [0]*M
func(0)