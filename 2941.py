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


