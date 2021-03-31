import sys
sys.setrecursionlimit(10**8)

def before(i):
    if i != -1: print(chr(i+65),end='')
    for j in t[i]:
        if j!=-1:
            before(j)
def middle(i):
    if t[i][0] != -1:
        middle(t[i][0])
    if i != -1: print(chr(i+65),end='')
    if t[i][1] != -1:
        middle(t[i][1])
def after(i):
    for j in t[i]:
        if j!=-1:
            after(j)
    if i != -1: print(chr(i+65),end='')

N = int(input())
t = [[] for _ in range(N)]
for i in range(N):
    c,l,r = sys.stdin.readline().split()
    c = ord(c)-65
    l = ord(l)-65 if l != '.' else -1; t[c].append(l)
    r = ord(r)-65 if r != '.' else -1; t[c].append(r)
before(0)
print()
middle(0)
print()
after(0)