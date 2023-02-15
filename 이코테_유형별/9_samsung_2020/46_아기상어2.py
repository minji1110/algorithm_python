import sys
from collections import deque
def input() : return sys.stdin.readline().rstrip()

N=int(input())
shark_size=2
shark_x,shark_y=0,0
fishes=[]
for i in range(N):
    fishes.append(list(map(int,input().split())))
    for j in range(N):
        if fishes[i][j]==9:
            shark_x,shark_y=i,j

# 아기상어의 위치에서 각 좌표까지의 거리를 반환. 갈 수 없는경우 -1
def get_distances():
    # 상, 하, 좌, 우
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    distances=[[-1]*N for _ in range(N)]
    visited=[[False]*N for _ in range(N)]
    
    q=deque()
    distances[shark_x][shark_y]=0
    visited[shark_x][shark_y]=True
    q.append((shark_x,shark_y,0)) #x,y,dis

    while q:
        x,y,dis=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if not visited[nx][ny] and fishes[nx][ny]<=shark_size:
                    distances[nx][ny]=dis+1
                    visited[nx][ny]=True
                    q.append((nx,ny,distances[nx][ny]))
    return distances

# 가장 작은 거리의 좌표를 반환 ( 자신보다 작은 물고기만 가능 )
def get_min_xy(distances): 
    min_distance=1e9
    min_x,min_y = -1,-1

    for i in range(N):
        for j in range(N):
            if distances[i][j]>0 and 0<fishes[i][j]<shark_size:
                if distances[i][j]<min_distance:
                    min_x,min_y=i,j
                    min_distance=distances[i][j]
    return min_x,min_y, min_distance

move=0
eat_cnt=0
while True:
    distances=get_distances()
    next_x, next_y, distance = get_min_xy(distances)
    
    if next_x==next_y==-1:
        break
    
    # 아기상어 이동
    move+=distance
    fishes[shark_x][shark_y]=0
    fishes[next_x][next_y]=9
    shark_x,shark_y=next_x,next_y
    # 크기 증가 여부 확인
    eat_cnt+=1
    if eat_cnt==shark_size:
        shark_size+=1
        eat_cnt=0

print(move)