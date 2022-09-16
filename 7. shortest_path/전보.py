import sys
import heapq
INF=int(1e9)
def input(): return sys.stdin.readline().rstrip()

n,m,start = map(int, input().split())   # 도시 수, 통로 수, 메세지 보내는 도시
graph=[[] for _ in range(n+1)]
times = [INF]*(n+1)

for _ in range(m):
    v1,v2,t=map(int,input().split())
    graph[v1].append((v2,t))    #(도시, 시간) 순서

def dijkstra(start):
    q=[]
    times[start]=0
    heapq.heappush(q, (0, start))   # (시간, 도시) 순서

    while q:
        time, city = heapq.heappop(q)
        
        if time>times[city] : continue

        for adjacent in graph[city]:
            adjacent_v=adjacent[0]
            adjacent_t=adjacent[1]
            if times[adjacent_v] > time + adjacent_t:
                times[adjacent_v]=time+adjacent_t
                heapq.heappush(q,(times[adjacent_v], adjacent_v))

dijkstra(start)

numOfCity=0
maxTime=0
for i in range(1,n+1):
    if times[i]!=INF:
        numOfCity+=1
        if times[i]>maxTime:
            maxTime=times[i]

print(numOfCity-1,maxTime)