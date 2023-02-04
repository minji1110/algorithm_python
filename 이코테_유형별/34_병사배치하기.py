# 틀림 
# 나 + next[i] 했을때 해당 next 는 next가 포함되지 않은 값이 최대일 수 있음
# ex) 12 2 5 3 2 10 8 7 일때
# 2에서 최대는 본인 제외 3 인데,  3에서 그냥 next 더하면 1+3 = 4 가 됨

import sys
def input() : return sys.stdin.readline().rstrip()

n=int(input())
power=list(map(int,input().split()))
power.append(0)

next=[n]*n # 나보다 전투력 낮은 다음인덱스
for i in range(n):
    for j in range(i+1,n):
        if power[i]>power[j]:
            next[i]=j
            break

dp=[0]*(n+1)
for i in range(n-1,-1,-1):
    # max(나 포함 , 나 제외)
    dp[i]=max(1+dp[next[i]],dp[i+1])

print(n-dp[0]) 