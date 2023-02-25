import sys
from itertools import permutations
def input(): return sys.stdin.readline().rstrip()

def calculate(a,op,b):
    if op==0:
        return a+b
    elif op==1:
        return a-b
    elif op==2:
        return a*b
    else:
        if a<0:
            return -((-a)//b)
        return a//b

N=int(input())
nums=list(map(int,input().split()))
ops_cnt=list(map(int,input().split()))

# 0(+), 1(-), 2(*), 3(%)
ops=[]
for i in range(4):
    for _ in range(ops_cnt[i]):
        ops.append(i)
orders=list(set(permutations(ops,N-1)))

maximum=-1e9
minimum=1e9
for order in orders:
    result=nums[0]
    for i in range(1,N):
        op=order[i-1]
        result=calculate(result,op,nums[i])
    maximum=max(maximum,result)
    minimum=min(minimum,result)

print(maximum)
print(minimum)