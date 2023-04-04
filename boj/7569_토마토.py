from collections import deque

M,N,H=map(int,input().split())
#1은 익은 토마토, 0 은 익지 않은 토마토, -1은 토마토가 들어있지 않은 칸
matrix=[] 
visited=[[[False]*M for _ in range(N)] for _ in range(H)]
rest=0 #익지 않은 토마토 수
days=0 #일수
q=deque()

#앞,뒤,좌,우,상,하
dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]

for i in range(H):
    h_list=[]
    for j in range(N):
        h_list.append(list(map(int,input().split())))
        for k in range(M):
            if h_list[j][k]==0:
                rest+=1
            elif h_list[j][k]==1:
                q.append((i,j,k,0))
                visited[i][j][k]=True
    matrix.append(h_list)

# 모든 토마토가 익었는지 반환
def is_all_ripen():
    return rest==0

#익음
def ripe():
    global matrix,visited, days, rest

    while q:
        z,x,y,day=q.popleft()
        days=day
        for d in range(6):
            nx,ny,nz=x+dx[d],y+dy[d],z+dz[d]
            if 0<=nx<N and 0<=ny<M and 0<=nz<H:
                if matrix[nz][nx][ny]==0 and not visited[nz][nx][ny]:
                    q.append((nz,nx,ny,day+1))
                    visited[nz][nx][ny]=True
                    matrix[nz][nx][ny]=1
                    rest-=1

ripe()
if is_all_ripen():
    print(days)
else:
    print(-1)