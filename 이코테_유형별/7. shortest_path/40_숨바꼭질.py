import sys
import heapq
def input(): return sys.stdin.readline().rstrip()
INF = 1e9

n,m = map(int,input().split())
matrix = [[-1]*(n+1) for _ in range(n+1)]
distance=[INF]*(n+1)
distance[1]=0

for _ in range(m):
    a,b=map(int,input().split())
    matrix[a][b]=1
    matrix[b][a]=1

q=[]
heapq.heappush(q,(0,1)) # 거리, 헛간번호

while q:
    dis,x = heapq.heappop(q)
    if distance[x]<dis:
        continue
    for next in range(1,n+1):
        if matrix[x][next]>0:
            if distance[next]>dis+1:
                distance[next]=dis+1
                heapq.heappush(q,(dis+1, next))

answer_number=0
answer_distance=0
answer_duplicated=0

for i in range(2,n+1):
    if distance[i]>answer_distance:
        answer_number=i
        answer_distance=distance[i]
        answer_duplicated=1
    elif distance[i]==answer_distance:
        answer_duplicated+=1

print(answer_number, answer_distance, answer_duplicated)