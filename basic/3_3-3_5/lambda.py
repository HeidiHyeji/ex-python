#lambda 인자: 표현식

def hap(x,y):
    return x+y
print(hap(10,20))

#람다 형식
(lambda x,y: x + y)(10,20)  

#map(함수,리스트)
test=list(map(lambda x: x**2,range(5)))
print(test)

'''
reduce(함수,순서형 자료)
순서형 자료의  원소들을 누적적으로 함수에 적용
'''
from functools import reduce
test2=reduce(lambda x,y:x+y,[0,1,2,3,4])
print(test2)

test3=reduce(lambda x,y:y+x,'abcde')
print(test3)

'''
filter(함수,리스트)
리스트에 들어있는 원소들을 함수에 적용시켜서 
결과가 참인 값들로 새로운 리스트를 만들어준다
'''
test4=list(filter(lambda x: x<5,range(10)))
print(test4)

test5=list(filter(lambda x: x%2,range10)) #0은 거짓,1은 참
print(test5)
