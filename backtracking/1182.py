import itertools

N, S = map(int,input().split())
nums = list(map(int, input().split()))
cnt = 0 
for j in range(1,N+1):
    listcom = list(itertools.combinations(nums,j))
    for i in range(len(listcom)):
        if sum(listcom[i]) == S:
            cnt += 1
print(cnt)