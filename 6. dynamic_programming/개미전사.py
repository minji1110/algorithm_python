# 이코테 - 개미전사
import sys

n=int(sys.stdin.readline().rstrip())
dp=list(map(int, sys.stdin.readline().rstrip().split()))

dp[1]=max(dp[0],dp[1])
for i in range(2,n):
    dp[i] = max(dp[i-1], dp[i-2]+dp[i])

print(dp[n-1])
