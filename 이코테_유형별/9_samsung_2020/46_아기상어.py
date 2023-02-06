import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

n=int(input())
visited=[[False]*n for _ in range(n)]
space=[]
# 상, 좌, 하, 우
dx=[-1,0,1,0]
dy=[0,-1,0,1]

# x,y로부터의 거리 배열을 반환
def set_distance(x,y):
    q=deque()
    visited=[[False]*n for _ in range(n)]
    distance=[[-1]*n for _ in range(n) ]

    q.append((x,y)) #x,y,이동칸수 
    distance[x][y]=0
    visited[x][y]=True

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if space[nx][ny]<=body:
                    q.append((nx,ny))
                    visited[nx][ny]=True
                    distance[nx][ny]=distance[x][y]+1
    return distance

# 다음 위치 반환
def find_next(x,y):
    distance=set_distance(x,y)
    min_distance=1e9
    next_x,next_y=-1,-1
    
    for i in range(n):
        for j in range(n):
            if space[i][j]!=0 and space[i][j]<body:
                if distance[i][j]>0 and min_distance>distance[i][j]:
                    next_x,next_y=i,j
                    min_distance=distance[i][j]

    return next_x,next_y,min_distance

x,y=0,0
body=2
body_cnt=0
answer=0
for i in range(n):
    space.append(list(map(int,input().split())))
    for j in range(n):
        if space[i][j]==9:
            x,y=i,j

while True:
    next_x,next_y,move = find_next(x,y)
    if next_x==-1 and next_y==-1:
        break
    
    space[x][y]=0
    space[next_x][next_y]=9
    x,y=next_x,next_y

    body_cnt+=1
    answer+=move

    if body==body_cnt:
        body=body_cnt+1
        body_cnt=0

print(answer)