w = list(input())
w.append('0')
w.append('0')
c,i = 0,0
while i < len(w)-2:
    if (w[i]=='c' and (w[i+1] == '=' or w[i+1] == '-')) or (w[i] == 'd' and w[i+1] == '-') or ((w[i]=='l' or w[i] =='n') and w[i+1] == 'j') or ((w[i] == 's' or w[i]=='z') and w[i+1] == '='):
        i+=2
    elif (w[i] == 'd' and (w[i+1]=='z' and w[i+2] == '=')):
        i+=3
    else:
        i+=1
    c+=1
print(c)
'''
#2941문제 모범 답안
c=input().count;
print(c('')-1-sum(map(c,['-','=','nj','lj','dz='])))
#총길이에서 크로아티아 알파벳가 나올 경우 빼준다
#특수문자가 혼자 들어가는 경우는 세지 않음(즉,-1되어야함)--> 이말은 즉슨 앞에 어떤 문자가 들어와도 -1해야한다는 것임
# nj,lj일 경우도 -1해야함 
#dz= 같은 경우는 -2해야함
'''

