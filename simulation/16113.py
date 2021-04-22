N = int(input())
s = list(input())
g = [[] for _ in range(5)]
isEmpty = [False for _ in range(N//5)]

for i in range(5): #시그널 그리기#빈칸 빼기
    for j in range(N//5):
        if i == 0:
            if (j == 0 or j == N//5-1) and s[i*(N//5)+j] == '.':#맨 앞,뒤 공백 제거
                isEmpty[j] = True
            else:# 공백 제거
                back = s[i*(N//5)+(j+1)]
                if s[i*(N//5)+j] == '.' and back == '.':
                    isEmpty[j] = True
        if not isEmpty[j]:
            g[i].append(s[i*(N//5)+j])

sero = ''
for j in range(len(g[0])):
    for i in range(5):
        sero+=g[i][j]
sero = sero.replace('######...######','0')
sero = sero.replace('#.####.#.####.#','2')
sero = sero.replace('#.#.##.#.######','3')
sero = sero.replace('###....#..#####','4')
sero = sero.replace('###.##.#.##.###','5')
sero = sero.replace('######.#.##.###','6')
sero = sero.replace('#....#....#####','7')
sero = sero.replace('######.#.######','8')
sero = sero.replace('###.##.#.######','9')
sero = sero.replace('#####','1')
sero = sero.replace('.....','')
'''
while len(g[0])>0:
    clue = []
    for i in range(1,4): #시그널 해독하기       
        garo = "".join(g[i][0:3])
        if i == 1:
            if garo == '#.#':
                clue += [0,4,8,9]
            elif garo == '#..':
                clue += [5,6,1]
            elif garo == '.#.' or garo == '#' or garo == '.#' or garo =='#.':
                clue += [1]
            else:
                clue += [2,3,7]
        elif i == 3:
            if garo == '..#':
                clue = [x for x in clue if x in [3,4,5,7,9]]
            elif garo == '#..':
                clue = [x for x in clue if x in [2,1]]
            elif garo == '.#.' or garo == '#' or garo == '.#' or garo =='#.':
                clue = [x for x in clue if x in [1]]
            else:
                clue = [x for x in clue if x in [0,6,8]]
        elif i == 2:
            if garo == '#.#':
                clue = [x for x in clue if x in [0]]
            elif garo == '###':
                clue = [x for x in clue if x in [2,3,4,5,6,8,9]]
            elif garo == '.#.' or garo == '#..' or garo == '#' or garo == '.#' or garo =='#.':
                clue = [x for x in clue if x in [1]]
            elif garo == '..#':
                clue = [x for x in clue if x in [7]]
    if len(clue) > 0: print(clue[0],end='')
    for i in range(5): #해독한 숫자 빼기
        tmp = 0
        if len(clue) <= 0:
            tmp = 3
        elif len(g[i]) < 4:
            tmp = len(g[i])
        else: tmp = 4
        for j in range(tmp):
            del g[i][0]
    if len(g[0]) >  0:
        while g[0][0]=='.':
            for i in range(5):
                del g[i][0]
'''
print(sero)