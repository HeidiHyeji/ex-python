def function(x):
    a=3
    b=5
    y= a * x + b
    return y

c= function(10)
print(c)
print(1+1==2)

def exam():
    ans = input('1+2=') #문자열 입력 받기
    return 1+2==int(ans) #문자열을 정수로 변환
print(exam())