# 다익스트라 알고리즘
# 특정 시작노드로부터 나머지 노드들까지 각각의 최단거리를 구하는 알고리즘
# 시작노드로부터 각 노드까지 최단거리를 담은 리스트를 유지(heapq), 가장 작은 노드를 선택하는 과정을 반복
# 이 가장 작은 노드와 인접하는 노드들에 대해, 최단거리를 업데이트, 최단거리 테이블을 갱신(distance)

import sys
import heapq
INF = int(1e9)
def input() : return sys.stdin.readline().rstrip()

v,e=map(int, input().split())
start=int(input())
graph = [[] for _ in range(v+1)]

# graph 초기화
for _ in range(e):
    v1, v2, weight = map(int, input().split())
    graph[v1].append((v2, weight))

distance = [INF]*(v+1)  # start로부터의 최단거리 리스트
distance[start]=0

q=[]
heapq.heappush(q,(0,start))

while q:
    weight, now = heapq.heappop(q)
    # 새로운 값으로 업데이트된 경우 heapq에 중복 위치할 것. 
    # 그 중에 최소값이 가장 먼저 선택되었을 것이므로 나머지는 무시함.
    if weight > distance[now] : continue
    print('weight , now = ',weight,',',now)

    for adjacent in graph[now]:
        adjacent_v = adjacent[0]
        adjacent_weight = adjacent[1]
        # 현재 노드 거쳐서 가는게 더 짧은 경우 거리 업데이트
        if distance[adjacent_v] > adjacent_weight+weight:
            distance[adjacent_v] = adjacent_weight+weight
            heapq.heappush(q,(distance[adjacent_v], adjacent_v))
    
for i in range(1,v+1):
    print(start,'=>',i,' 의 최단거리 : ', end=' ')
    if distance[i]==INF: print("도달 불가")
    else: print(distance[i])


#input
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
