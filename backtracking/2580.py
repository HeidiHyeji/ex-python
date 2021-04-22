import sys
pan = [];isusedX=[];isusedY=[];isusedN=[];box = []
def func(cur):
    if cur == len(box):
        return True
    for k in range(cur,len(box)):
        x,y = box[k]
        for i in range(1,10):
            if isusedX[x][i] or isusedY[y][i] or isusedN[3*(x//3)+(y//3)][i]:
                continue
            isusedX[x][i] = True
            isusedY[y][i] = True
            isusedN[3*(x//3)+(y//3)][i] = True
            pan[x][y] = i
            if func(k+1): 
                return True
            pan[x][y] = 0
            isusedX[x][i] = False
            isusedY[y][i] = False
            isusedN[3*(x//3)+(y//3)][i] = False            
        return False
for _ in range(9):
    pan.append(list(map(int,sys.stdin.readline().split())))
    isusedX.append([False]*10)
    isusedY.append([False]*10)
    isusedN.append([False]*10)
for i in range(9):
    for j in range(9):
        if pan[i][j] == 0:
            box.append((i,j))
        else:
            isusedX[i][pan[i][j]] = True
            isusedY[j][pan[i][j]] = True
            isusedN[3*(i//3)+(j//3)][pan[i][j]] = True
func(0)
print()
for i in range(9):
    for j in range(8):
        print(pan[i][j],end = ' ')
    print(pan[i][8])
'''
반례
0 6 0 0 0 0 2 0 9
0 0 0 8 2 0 5 0 0
0 1 0 9 0 3 0 0 0
3 7 0 0 9 0 0 0 6
1 0 0 0 0 0 0 0 8
2 0 0 0 4 0 0 5 1
0 0 0 5 0 4 0 9 0
0 0 3 0 7 9 0 0 0
5 0 9 0 0 0 0 6 0
'''