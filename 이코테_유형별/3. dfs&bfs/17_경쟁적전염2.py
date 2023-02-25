import sys
import heapq
def input(): return sys.stdin.readline().rstrip()

#상, 하, 좌, 우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

matrix=[]
viruses=[]

N,K=map(int,input().split())
for i in range(N):
    matrix.append(list(map(int,input().split())))
    for j in range(N):
        if matrix[i][j]>0:
            heapq.heappush(viruses,(0,matrix[i][j],i,j))

S,X,Y=map(int,input().split())

while viruses:
    t,no,x,y=heapq.heappop(viruses)
    if t==S:
        break
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<N and 0<=ny<N and matrix[nx][ny]==0:
            matrix[nx][ny]=no
            heapq.heappush(viruses,(t+1,no,nx,ny))

print(matrix[X-1][Y-1])