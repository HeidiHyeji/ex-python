import sys
N, M = map(int,input().split())
g = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]

listsum = []
for i in range(2**(N*M)):
    strb = format(i,'b').zfill(N*M) #세로1,가로0
    bg = [[ 0 for _ in range(M)] for z in range(N)]
    for a in range(N): # 이진 그래프 초기화
        for b in range(M):
            bg[a][b] = strb[a*M+b]

    #가로 구하기
    sum = 0
    for a in range(N):
        listn =[]
        for b in range(M):
            if  bg[a][b]=='0':
                listn.append(str(g[a][b]))
            if  bg[a][b]=='1' or b==M-1:
                sum+=int("".join(listn)) if len(listn)>0 else 0
                listn.clear()
    #세로 구하기
    for b in range(M):
        listn =[]
        for a in range(N):
            if bg[a][b] == '1':
                listn.append(str(g[a][b]))
            if bg[a][b] == '0' or a==N-1:
                sum+=int("".join(listn)) if len(listn)>0 else 0
                listn.clear()
    listsum.append(sum)
print(max(listsum))