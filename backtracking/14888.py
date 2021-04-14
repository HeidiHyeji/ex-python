import itertools
def funcop(nums,listop):
    if len(nums) == 1:
        return nums[0]
    #return funcop(nums)+마지막값
    op = listop.pop()
    num = nums.pop()
    if op == '+':
        return funcop(nums,listop)+num
    elif op == '-':
        return funcop(nums,listop)-num       
    elif op == '*':
        return funcop(nums,listop)*num  
    elif op == '//':
        tmp = funcop(nums,listop)
        if tmp<0:
            return ((tmp*-1)//num)*-1
        else:
            return tmp//num
result = []
N = int(input())
A = list(map(int,input().split()))
OPCNT = list(map(int,input().split()))#+-*//
OP = ['+' for _ in range(OPCNT[0])]
OP += ['-' for _ in range(OPCNT[1])]
OP += ['*' for _ in range(OPCNT[2])]
OP += ['//' for _ in range(OPCNT[3])]

PerOP = list(set(itertools.permutations(OP,N-1)))
for i in range(len(PerOP)):
    result.append(funcop(A.copy(),list(PerOP[i])))
print(max(result))
print(min(result))