import sys
import heapq
def input(): return sys.stdin.readline().rstrip()
INF=1e9

v,e = map(int,input().split())
start = int(input())

adjacent_list=[[] for _ in range(v+1)]
weights=[INF]*(v+1)

for _ in range(e):
    a,b,w = map(int,input().split())
    adjacent_list[a].append((b,w))

q=[]
weights[start]=0
heapq.heappush(q,(weights[start],start))

while q:
    now_w,now_v = heapq.heappop(q)
    if now_w>weights[now_v]:
        continue
    for adj_v,adj_w in adjacent_list[now_v]:
        if now_w+adj_w < weights[adj_v]:
            weights[adj_v]=now_w+adj_w
            heapq.heappush(q,(weights[adj_v],adj_v))

for i in range(1,v+1):
    if weights[i]==INF:
        print('INF')
    else:
        print(weights[i])