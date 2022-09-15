# 이테코 5-11. 미로탈출
from collections import deque

# 상,하,좌,우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(graph,visited):
    queue=deque()

    graph[0][0]=1
    visited[0][0]=True

    queue.append((0,0))

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nextX,nextY=x+dx[i],y+dy[i]
            if(0<=nextX<len(graph) and 0<=nextY<len(graph[0]) and not visited[nextX][nextY] and graph[nextX][nextY]==1):
                graph[nextX][nextY]=graph[x][y]+1
                visited[nextX][nextY]=True
                queue.append((nextX,nextY))


n,m=map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

visited=[[False]*m for _ in range(n)]

start_x,start_y=0,0
graph[0][0]=1
visited[0][0]=True

bfs(graph,visited)
print(graph[n-1][m-1])
