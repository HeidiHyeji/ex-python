R,C = map(int,input().split())
L = [list(map(int,input().split())) for i in range(R)]

tmp = ''

if R % 2 == 1:
    for i in range(1,R+1):
        if i % 2 == 1:
            tmp += 'R'*(C-1) + 'D'
        else:
            tmp += 'L'*(C-1) + 'D'
    tmp = tmp[:-1]
else:
    if C % 2 == 1:
        for i in range(1,C+1):
            if i % 2 == 1:
                tmp += 'D'*(R-1) + 'R'
            else:
                tmp += 'U'*(R-1) + 'R'
        tmp = tmp[:-1]
    else:
        c1 = sum(L[R-1])
        c2 = sum([L[R-1][x] for x in range(C)])
        if c1 > c2:
            for i in range(1,C):
                if i % 2 == 1:
                    tmp += 'D'*(R-1) + 'R'
                else:
                    tmp += 'U'*(R-1) + 'R'
        else:
            for i in range(1,R):
                if i % 2 == 1:
                    tmp += 'R'*(C-1) + 'D'
                else:
                    tmp += 'L'*(C-1) + 'D' 
print(tmp)
         