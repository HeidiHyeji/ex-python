import sys
result = []
for i in range(4):
    s = list(map(int,sys.stdin.readline().split()))
    m = [[0 for j in range(3)] for _ in range(6)]
    for j in range(6):
        for k in range(3):
            m[j][k] = s[3*j+k]
    
    totwin=0;totlose=0;totmu=0
    for j in range(6):
        if m[j][0] + m[j][1] + m[j][2] != 5: 
            break
        totwin += m[j][0]
        totmu  += m[j][1]
        totlose+= m[j][2]
    same = []
    for j in range(6):
        same.append(m[j][1])
    same.sort()
    f = True
    for j in range(0,6,+2):
        if same[j]!=same[j+1]:
            f = False
    if (totwin == totlose and totwin + (totmu/2) == 15) and (f):
        result.append(1)
    else:
        result.append(0)
for i in range(len(result)):
    if i == len(result)-1:
        print(result[i],end='')
    else: print(result[i],end=' ')
    