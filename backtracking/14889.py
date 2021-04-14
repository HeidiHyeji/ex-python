import sys,itertools
N = int(input())
S = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
MEM = set(range(0,N))
MEMP = list(itertools.combinations(MEM,N//2))
result = float("inf")
for i in range(len(MEMP)//2):
    starsum = 0;linksum = 0
    startmem = list(MEMP[i])
    linkmem = list(MEM-set(startmem))
#    if tuple(linkmem) in MEMP:
#        MEMP.remove(tuple(linkmem))
    for j in range(N//2):
        for k in range(j+1,N//2):
            starsum += S[startmem[j]][startmem[k]]
            starsum += S[startmem[k]][startmem[j]]
            linksum += S[linkmem[j]][linkmem[k]]
            linksum += S[linkmem[k]][linkmem[j]]
    tmp = abs(starsum-linksum)
    if tmp<result: result = tmp
print(result)