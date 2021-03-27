A, B = map(str, input().split()) # 두 정수를 문자열로 입력받음

NA = int("".join(reversed(list(A)))) #두 문자열을 list로 전환 후 뒤집어 정렬함.그리고 요소끼리 문자열자체를 합침
NB = int("".join(reversed(list(B))))
print((lambda a,b:a if a>b else b)(NA,NB)) # 람다식 이용하여 큰 수 출력
