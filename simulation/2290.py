def ha(s):
    return ' ' + '-' * s + ' '
def hz(s):
    return ' '*(s+2)
def vb(s):
    return '|'+ ' '*s + '|'
def vl(s):
    return '|'+ ' '*s + ' '
def vr(s):
    return ' '+ ' '*s + '|'
def paint(h,s,i):#h:높이,s:간격표준,i:그리는숫자
    if h == 0: #첫째줄
        if i == 1 or i == 4:
            return hz(s)
        else:
            return ha(s)
    elif h == (2*s+2)/2: #중간줄
        if i == 1 or i == 7 or i == 0:
            return hz(s)
        else:
            return ha(s)
    elif h == 2*s+2: #마지막줄 
        if i == 1 or i == 4 or i ==7:
            return hz(s)
        else:
            return ha(s)
    elif h < (2*s+2)/2:
        if i == 4 or i == 8 or i ==9 or i ==0:
            return vb(s)
        elif i== 5 or i ==6:
            return vl(s)
        else:
            return vr(s)
    elif h > (2*s+2)/2:
        if i == 6 or i == 8 or i == 0:
            return vb(s)
        elif i == 2:
            return vl(s)
        else:
            return vr(s)
s,n = input().split()
s = int(s)
for h in range(2*s+3):
    tmp = ''
    for i in range(len(n)):
        tmp+=paint(h,s,int(n[i]))
        if i != len(n)-1:
            tmp+=' '
    print(tmp)