N = int(input())
arr = []
tmp = -10001
for i in range(N):
    x = int(input())
    arr.append(x)
    if x > tmp and x <= 0:
        tmp = x

arr.sort()
indexTmp = list(filter(lambda x: arr[x] == tmp, range(len(arr))))
t = indexTmp[len(indexTmp)-1] if len(indexTmp)>0 else -1
a1 = arr[0:t+1] 
a2 = arr[t+1:] 
sum = 0
i = 0

while i < len(a1):
    mul = a1[i]
    if i+1 < len(a1):
        mul *= a1[i+1]
    sum += mul
    i+=2
a2.reverse()
i = 0
while i < len(a2):
    mul = a2[i]
    if i+1 < len(a2):
        if a2[i+1] == 1:
            sum += 1
        mul *= a2[i+1]
    sum += mul
    i+=2
print(sum)