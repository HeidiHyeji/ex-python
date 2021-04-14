import sys,itertools
N = int(input())
S = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
MEM = [i for i in range(N)]
MEMP = list(itertools.combinations(MEM,N//2))
listmin = []
for i in range(len(MEMP)//2):
    starsum = 0;linksum = 0
    startmem = list(MEMP[i])
    linkmem = [x for x in MEM if x not in startmem]
    if tuple(linkmem) in MEMP:
        MEMP.remove(tuple(linkmem))
    startmem = list(itertools.combinations(startmem,2))
    linkmem = list(itertools.combinations(linkmem,2))
    for j in range(len(startmem)):
        starsum += S[startmem[j][0]][startmem[j][1]]
        starsum += S[startmem[j][1]][startmem[j][0]]
        linksum += S[linkmem[j][0]][linkmem[j][1]]
        linksum += S[linkmem[j][1]][linkmem[j][0]]
    listmin.append(abs(starsum-linksum))
print(min(listmin))