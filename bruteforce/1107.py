def checkBtn(num):
    listnum = list(map(int,list(str(num))))
    for i in listnum:
        if i not in btn:
            return False
    return True

N = int(input())
M = int(input())
btn = [0,1,2,3,4,5,6,7,8,9]
rbtn = []
if M > 0:
    rbtn = list(map(int,input().split()))
btn = [x for x in btn if x not in rbtn]
plumi = N-100 if N-100>0 else 100-N
cnt1 = 0
cnt2 = 0
flagcnt1 = False
if M == 10:
    print(N-100 if N-100>0 else 100-N)
else:
    for i in reversed(range(N+1)): #N에서 부터 0까지 가능한지 체크
        if checkBtn(i):
            cnt1 += len(str(i))
            flagcnt1 = True
            break
        else: 
            cnt1+=1
    i = N
    while cnt2<cnt1 if flagcnt1 else cnt2<plumi: #N에서 부터 cnt2가 최소일때까지 가능한지 체크
        if checkBtn(i):
            cnt2 += len(str(i))
            break
        else: 
            cnt2+=1
            i+=1
    if flagcnt1:
        print(min(cnt1,cnt2,plumi))
    else:
        print(min(cnt2,plumi))
