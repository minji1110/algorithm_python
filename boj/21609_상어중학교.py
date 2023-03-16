import heapq
from collections import deque

N,M=map(int,input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int,input().split())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

# 볼록 그룹 찾기
def get_block_groups():
    global matrix
    pq=[]
    visited=[[False]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and 0<matrix[i][j]<=M:
                #bfs
                blocks=[]
                rainbow_blocks=[]
                
                color=matrix[i][j]
                block_q=deque()
                block_q.append((i,j))
                visited[i][j]=True

                while block_q:
                    x,y=block_q.popleft()
                    blocks.append((x,y))

                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                            if matrix[nx][ny]==0 or matrix[nx][ny]==color:
                                if matrix[nx][ny]==0:
                                    rainbow_blocks.append((nx,ny))
                                block_q.append((nx,ny))
                                visited[nx][ny]=True
                
                if len(blocks)>=2:
                    heapq.heappush(pq,(-len(blocks),-len(rainbow_blocks),-i,-j,blocks))
                    for rx,ry in rainbow_blocks:
                        visited[rx][ry]=False
    return pq

# 중력 작용
def gravity_works():
    global matrix

    for row in range(N-2,-1,-1):
        for col in range(N):
            if matrix[row][col]==-1:
                continue
            last=row
            while(last<N-1):
                if matrix[last+1][col]==M+1:
                    last+=1
                else:
                    break
            if last!=row:
                matrix[last][col]=matrix[row][col]
                matrix[row][col]=M+1

# 반시계방향 90도 회전
def rotate_matrix():
    global matrix
    matrix=list(map(list,zip(*matrix)))[::-1]

score=0
while True:
    block_groups = get_block_groups()
    if not block_groups:
        break

    # 1. 크기가 가장 큰 블록 그룹을 찾는다. 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹, 
    # 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그 것도 여러개이면 열이 가장 큰 것을 찾는다.
    total_cnt, rainbow_cnt, i, j, blocks=heapq.heappop(block_groups)

    # 2. 1에서 찾은 블록 그룹의 모든 블록을 제거한다. 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B2점을 획득한다.    
    for x,y in blocks:
        matrix[x][y]=M+1 #빈칸
    score+=total_cnt**2

    # 3. 격자에 중력이 작용한다.
    gravity_works()

    # 4. 격자가 90도 반시계 방향으로 회전한다.
    rotate_matrix()
    
    # 5. 다시 격자에 중력이 작용한다.
    gravity_works()

print(score)