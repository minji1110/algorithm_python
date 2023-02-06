import sys
import heapq
def input(): return sys.stdin.readline().rstrip()

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def get_shortest_path(n,matrix):
    q=[]
    visited=[[False]*n for _ in range(n)]
    
    heapq.heappush(q,(matrix[0][0],0,0))
    visited[0][0]=True

    while q:
        dis,x,y=heapq.heappop(q)
        if x==y==n-1:
            print(dis)
            break
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                    heapq.heappush(q,(dis+matrix[nx][ny],nx,ny))
                    visited[nx][ny]=True
    return

tc = int(input())
for _ in range(tc):
    matrix = []
    n=int(input())
    
    for _ in range(n):
        matrix.append(list(map(int,input().split())))
    
    get_shortest_path(n,matrix)
