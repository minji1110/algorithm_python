import heapq
import sys

N=int(input())
cards=[]
for _ in range(N):
    heapq.heappush(cards,int(input()))

result=0
while len(cards)>1:
    a=heapq.heappop(cards)
    b=heapq.heappop(cards)

    result+=(a+b)
    heapq.heappush(cards,a+b)

print(result)