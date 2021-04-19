import sys
visited=[];tolk = [];cnt = 0;tottolk=[]
def dfs(color,i,j):
    global tolk,visited
    if i<0 or i>=6 or j<0 or j>=12:
        return

    if cur[i][j] == color and not visited[i][j]:
        visited[i][j] = True
        tolk.append((i,j))
        dfs(color,i,j+1)
        dfs(color,i,j-1)
        dfs(color,i+1,j)
        dfs(color,i-1,j)
def removetolk():
    global tottolk,cnt
    tottolk.sort()
    for i in range(len(tottolk)):
        x,y = tottolk[i]
        del cur[x][y]
        cur[x].insert(0,'.')
    tottolk = []
    cnt+=1
def puyo(cur):
    global cnt,visited,tolk,tottolk
    visited = [[False for _ in range(12)] for x in range(6)]
    tolk = []
    for i in reversed(range(12)):
        for j in reversed(range(6)):
            if cur[j][i] == '.':
                continue
            dfs(cur[j][i],j,i)
            if len(tolk) >= 4:
                tottolk += tolk
            tolk = []
    if len(tottolk)>0:
        removetolk()
        puyo(cur)
    

cur = [['.' for i in range(12)] for j in range(6)]
for i in range(12):
    tmp = list(sys.stdin.readline().strip())
    for j in reversed(range(6)):
        cur[j][i] = tmp[5-j]
puyo(cur)
print(cnt)
'''9
......
......
......
......
.....
.....Y
.G...Y
.B.BRB
.RBGBB
Y.RBGR
..RBGR
R.RBGR
'''

