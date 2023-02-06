import sys
def input():return sys.stdin.readline().rstrip()

N=int(input())
coins=list(map(int, input().split()))
coins.sort()

maximum=coins[-1]
possible = [False]*(N*maximum+1)

for coin_cnt in range(1,N+1):
    print('coin_cnt=',coin_cnt)
    for start in range(0,N-coin_cnt+1):
        sum_of_coins=0
        for i in range(start,start+coin_cnt):
            sum_of_coins+=coins[i]
        if not possible[sum_of_coins]:
            print('sum_of_coins=',sum_of_coins)
            possible[sum_of_coins]=True
                    
for i in range(1,len(possible)):
    if not possible[i]:
        print(i)
        break