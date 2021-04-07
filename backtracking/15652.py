def func(k,p):
    if k == M:
        for i in range(M):
            print(arr[i],end=' ')
        print()
        return
    for i in range(p,N+1):
        arr[k] = i
        func(k+1,i)
N, M = map(int,input().split())
arr = [0]*M
func(0,1)