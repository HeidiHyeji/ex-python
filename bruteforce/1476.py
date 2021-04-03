import sys
E, S, M = map(int,sys.stdin.readline().split())#15,28,19
i = 0
while True:
    tmp = 15*i+E 
    rs = tmp % 28 if tmp % 28 != 0 else 28
    rm = tmp % 19 if tmp % 19 != 0 else 19
    if rs == S and rm == M:
        break
    i = i+1
print(tmp)  
