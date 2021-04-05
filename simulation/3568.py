s = list(input().replace(',','').replace(';','').split())
for i in range(1,len(s)):
    tmp = s[0]
    for j in reversed(range(len(s[i]))):
        if s[i][j] == '*' or s[i][j] == '&':
            tmp+=s[i][j]
        elif  s[i][j] == '[':
            tmp+=']'
        elif  s[i][j] == ']':
            tmp+='['
        else:
            tmp= tmp+ ' ' + s[i][0:j+1] +';'
            break
    print(tmp)
    
