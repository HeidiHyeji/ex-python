A, P = input().split()
arr = []
while int(A) not in arr:
    arr.append(int(A))
    sum = 0
    for i in A:
        sum+=(int(i))**(int(P))
    A = str(sum)
print(arr.index(int(A)))

