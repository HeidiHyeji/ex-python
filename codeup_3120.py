c,p = input().split()
cnt = 0
m = int(p)-int(c)
if m < 0:
    m= m*-1
if m%10>=0: 
    cnt += m//10
    m = m%10
#한자리수
if m > 5:
    cnt+=min(10-m+1,m-5+1)
else:
    cnt+=min(5-m+1,m)
print(cnt)
