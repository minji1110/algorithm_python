n=int(input())
coins=list(map(int,input().split()))
coins.sort()

answer=1
if coins[0]==1:
    possible=0
    target=1

    for coin in coins:
        if coin>target:
            answer=target
            break
        possible=possible+coin
        target=possible+1
        answer=target

print(answer)
