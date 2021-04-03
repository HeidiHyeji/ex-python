import itertools
def toMax(l):
    sum = 0
    for i in range(len(l)-1):
        tmp = l[i]-l[i+1]
        sum += tmp if tmp>0 else -1*tmp
    return sum
    
N = int(input())
A = list(map(int,input().split()))
p = list(itertools.permutations(A))
m = 0
for i in range(len(p)):
    tmp = toMax(p[i])
    if tmp>m:
        m = tmp
print(m)    