import sys
def input() : return sys.stdin.readline().rstrip()

n=int(input())
T=[0 for _ in range(n+1)]
P=[0 for _ in range(n+1)]
dp = [0 for _ in range(n+2)]

for i in range(1,n+1):
    T[i],P[i] = map(int,input().split())

if T[n]==1:
    dp[n]=P[n]

for i in range(n-1,0,-1):
    if i+T[i]-1<=n:
        include = P[i]+dp[i+T[i]]
        exclude = dp[i+1]
        dp[i]=max(include,exclude)
    else:
        dp[i]=dp[i+1]

print(dp[1])


