import sys
from itertools import permutations
def input(): return sys.stdin.readline().rstrip()

'''
+,-,*,%
0,1,2,3
'''
def calculate(a,op,b):
    if op==0:
        return a+b
    elif op==1:
        return a-b
    elif op==2:
        return a*b
    else:
        if a<0:
            return -(-a//b)
        return a//b

N=int(input())
nums=list(map(int,input().split()))
ops_input=list(map(int,input().split()))

ops=[]
for i in range(4):
    for _ in range(ops_input[i]):
        ops.append(i)
cases=list(set(permutations(ops,len(ops))))

answer_max=-1e9
answer_min=1e9
for case in cases:
    result=nums[0]
    for i in range(N-1):
        result=calculate(result,case[i],nums[i+1])
    
    if result>=answer_max:
        answer_max=result
    if result<=answer_min:
        answer_min=result

print(answer_max)
print(answer_min)