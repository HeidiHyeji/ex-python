def func(k,p):
    if k == M:
        for i in range(M):
            print(arr[i],end=' ')
        print()
        return
    for i in range(p,len(num)):
        arr[k] = num[i]
        func(k+1,i+1)

N, M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
arr = [0] * M
func(0,0)

