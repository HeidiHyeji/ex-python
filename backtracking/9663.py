N = int(input())
isused1 = [False for i in range(N)];isused2 = [False for i in range(2 * N)];isused3 = [False for i in range(2 * N)]
def func(cur):
    global isused1, isused2, isused3
    result = 0
    if cur == N:
        return 1
    for i in range(N):
        if isused1[i] or isused2[i+cur] or isused3[cur-i+N-1]:
            continue
        isused1[i] = True
        isused2[i+cur] = True
        isused3[cur-i+N-1] = True
        result += func(cur+1)
        isused1[i] = False
        isused2[i+cur] = False
        isused3[cur-i+N-1] = False
    return result

print(func(0))