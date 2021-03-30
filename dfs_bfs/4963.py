import sys
sys.setrecursionlimit(10**8)

def dfs(i,j):
    if i<0 or j<0 or i>= h or j >= w:
        return False

    if m[i][j] == 1:
        m[i][j] = 0
        for k in range(8):
            dfs(i+mx[k],j+my[k])
        return True
    return False 
        
while True:
    w, h = map(int,sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    m = [list(map(int,sys.stdin.readline().split())) for _ in range(h)]
    mx  = [0,0,-1,-1,-1,+1,+1,+1]
    my  = [+1,-1,0,+1,-1,0,+1,-1]

    result = 0
    for i in range(h):
        for j in range(w):
            if m[i][j] == 1:
                if dfs(i,j):
                    result += 1
    print(result)