import sys
import heapq
def input(): return sys.stdin.readline().rstrip()
INF = 1e9

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def get_shortest_path(n,matrix):
    q=[]
    distance=[[INF]*n for _ in range(n)]

    distance[0][0]=matrix[0][0]
    heapq.heappush(q,(distance[0][0],0,0))

    while q:
        dis,x,y=heapq.heappop(q)
        if distance[x][y]<dis:
            continue
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n :
                if distance[nx][ny]>dis+matrix[nx][ny]:
                    distance[nx][ny]=dis+matrix[nx][ny]
                    heapq.heappush(q,(distance[nx][ny],nx,ny))
                    
    return distance[n-1][n-1]

tc = int(input())
for _ in range(tc):
    matrix = []
    n=int(input())
    
    for _ in range(n):
        matrix.append(list(map(int,input().split())))
    
    print(get_shortest_path(n,matrix))
