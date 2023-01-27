# 플로이드-워셜 알고리즘
# 모든 노드로부터 다른 모든 노드로까지의 최단경로를 구하는 알고리즘
# dp 이용, v1 -> v2 의 최단거리 = min(v1 -> v2 , v1 -> vk -> v2) 임을 이용

import sys
INF = int(1e9)
def input() : return sys.stdin.readline().rstrip()

nv=int(input())
ne=int(input())

matrix = [[INF] * (nv+1) for _ in range(nv+1)]
for i in range(nv+1): matrix[i][i]=0

for _ in range(ne):
    v1,v2,weight = map(int, input().split())
    matrix[v1][v2]=weight

for k in range(1,nv+1):
    for v1 in range(1,nv+1):
        for v2 in range(1,nv+1):
            matrix[v1][v2]=min(matrix[v1][v2], matrix[v1][k]+matrix[k][v2])

for i in range(1,nv+1):
    for j in range(1,nv+1):
        if matrix[i][j]==INF : print(-1, end=' ')
        else : print(matrix[i][j],end=' ')
    print()

