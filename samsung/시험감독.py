import sys
def input() : return sys.stdin.readline().rstrip()

n=int(input())
a=list(map(int,input().split()))
b,c = map(int,input().split())

total = n

for i in range(n):
    rest = a[i]-b
    if rest<=0: 
        continue
    elif rest%c==0:
        total+=rest//c
    else:
        total+=rest//c+1

print(total)

