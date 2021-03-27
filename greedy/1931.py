N = int(input())
info = [list(map(int,input().split())) for i in range(N)]
info.sort(key = lambda x: x[0])
print(info)
info.sort(key = lambda x: x[1])
print(info)

cnt = 1
end = info[0][1]
for i in range(1,len(info)):
    if info[i][0] >= end:
        cnt+=1
        end = info[i][1]
print(cnt)
