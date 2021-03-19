N = int(input())#사람의수
P = list(map(int,input().split()))#각 사람이 돈을 인출하는 데 걸리는 시간
sum = 0
P.sort()
for i in range(len(P)):
    for j in range(i+1):
        sum+=P[j]
print(sum)