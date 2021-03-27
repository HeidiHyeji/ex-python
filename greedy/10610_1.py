N = list(input())
if '0' not in N or sum(map(int,N)) % 3 != 0:
    print(-1)
else:
    print("".join(sorted(N,reverse=True)))