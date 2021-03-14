n = int(input())
cnt = 0
for i in range(n):
    s = list(map(str,input()))#단어를 리스트로 저장
    a = [s[0]];s.insert(0,s[0])
    for j in range(1,len(s)):
        if s[j] != s[j-1]:
            if s[j] in a:
                break
            a.append(s[j])
        if j == len(s)-1:
            cnt+=1
print(cnt)
'''
#모범답안
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find): #word에서 찾은 문자대로 정렬됨(기존순서유지)
        result += 1
print(result)
'''