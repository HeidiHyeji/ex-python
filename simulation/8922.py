import sys
T = int(sys.stdin.readline().strip())
for t in range(T):
    area = [(0,0)]
    d = (0,+1)#북(0,-1),서(-1,0),동(+1,0)
    oper = list(sys.stdin.readline().strip())
    for i in range(len(oper)):
        s = oper[i]
        cur = area[i]
        if s == 'F':
            area.append((cur[0]+d[0],cur[1]+d[1]))
        elif s == 'B':
            area.append((cur[0]-d[0],cur[1]-d[1]))
        elif s == 'L':
            if d == (0,+1):
                d = (-1,0)
            elif d == (0,-1):
                d = (+1,0)
            elif d == (-1,0):
                d = (0,-1)
            else:
                d = (0,+1)
            area.append(cur)
        elif s == 'R':
            if d == (0,+1):
                d = (+1,0)
            elif d == (0,-1):
                d = (-1,0)
            elif d == (+1,0):
                d = (0,-1)
            else:
                d = (0,+1)
            area.append(cur)
    minX = 0;maxX = 0;minY = 0;maxY = 0
    for i in range(len(area)):
        x,y = area[i]
        if minX>x:
            minX = x
        if maxX<x:
            maxX = x
        if minY>y:
            minY = y
        if maxY<y:
            maxY = y
    print((maxY-minY)*(maxX-minX))
    