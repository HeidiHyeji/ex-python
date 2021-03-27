N = int(input())#토핑 종류 수
A,B = map(int,input().split())#A: 도우가격,B: 토핑가격
C = int(input())#도우 칼로리
D = []#토핑 칼로리
S = []#선택한 토핑 
for i in range(N):
    D.append(int(input()))

D.sort()
D.reverse()


#칼로리/전체가격 (C+sum(S))/(A+len(S)*B)
for i in D:
    if (C+sum(S))/(A+len(S)*B) < (C+sum(S)+i)/(A+(len(S)+1)*B):
        S.append(i)
print(int((C+sum(S))/(A+len(S)*B)))