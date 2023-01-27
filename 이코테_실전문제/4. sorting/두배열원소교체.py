import sys

n, k = map(int, input().split())

# input() 대신 sys.stdin.readline().rstrip() 사용하기!!
# A=list(map(int,input().split()))
# B=list(map(int,input().split()))

A=list(map(int,sys.stdin.readline().rstrip().split()))
B=list(map(int,sys.stdin.readline().rstrip().split()))

for i in range (k):
    A.sort()
    B.sort()
    if(A[0]<B[n-1]):
        A[0],B[n-1]=B[n-1],A[0]
    else:
        break

print('A=',A)
print('B=', B)
print(sum(A))
