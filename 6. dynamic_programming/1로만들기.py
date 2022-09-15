# 이코테 : 1로만들기
import sys

x= int(sys.stdin.readline().rstrip())
dp=[0] * (x+1) # 0 ~ x

# %5 or %3 or %2 or -1
for i in range(2,x+1):
    dp[i]=dp[i-1]+1
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)
    if i%5==0:
        dp[i]=min(dp[i],dp[i//5]+1)

print(dp[x])