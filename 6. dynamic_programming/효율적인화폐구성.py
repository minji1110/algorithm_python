# 이코테 - 효율적인 화폐 구성 1 : 0원 ~ m원까지 최소갯수 계산하기 
# dp[i] = dp[i - c]+1 의 최솟값 , c는 동전의 종류
import sys

def find_min(coins, dp, i):
    for coin in coins:
        if i-coin > 0:
            if dp[i-coin]+1 < dp[i] :
                dp[i]=dp[i-coin] + 1

n,m = map(int, sys.stdin.readline().rstrip().split())
coins=[]
# n가지 동전 append
for _ in range(n):
    coin=int(sys.stdin.readline().rstrip())
    coins.append(coin)
coins.sort()

dp=[10001] * (m+1) # 0~m
for c in coins:
    if c<=m : dp[c]=1

min_coin = coins[0]
for i in range(min_coin,m+1):
    find_min(coins, dp, i)

if dp[m]==10001:
    print(-1)
else:
    print(dp[m])


# 이코테 - 효율적인 화폐 구성 2 : 동전 종류를 돌면서 화폐 개수 채워가기 (교재방법)
# dp[i] = min(dp[i], dp[i-c]+1)
n,m = map(int, input().split())
coins=[]
for i in range(n):
    coins.append(int(input()))

d=[10001] * (m+1)

d[0]=0
for coin in coins:
    for i in range(coin, m+1):
        if d[i-coin]!=10001:
            d[i]=min(d[i],d[i-coin]+1)

if dp[m]==10001:
    print(-1)
else:
    print(dp[m])