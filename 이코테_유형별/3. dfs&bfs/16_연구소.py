import sys
from itertools import combinations
from collections import deque
def input(): return sys.stdin.readline().rstrip()

n,m=map(int,input().split())
dx=[0,0,-1,1]
dy=[1,-1,0,0]

# target번째칸 -> x,y
def find_xy(target):
    x=target//m
    y=target%m
    return x,y

# visited 리스트 초기화
def reset_visited(visited):
    for i in range(n):
        for j in range(m):
            visited[i][j]=False

# copy 리스트 초기화
def copy_matrix(matrix,matrix_copy):
    for i in range(n):
        for j in range(m):
            matrix_copy[i][j]=matrix[i][j]
        

# 안전지대 수 구하기
def find_safe_area(matrix_copy):
    spread_virus(matrix_copy)
    cnt=0
    for i in range(n):
        for j in range(m):
            if matrix_copy[i][j]==0 :
                cnt+=1
    return cnt


def spread_virus(matrix_copy):
    for i in range(n):
        for j in range(m):
            if matrix_copy[i][j]==2 and not visited[i][j]:
                bfs(matrix_copy,i,j)

def bfs(matrix_copy,i,j):
    q=deque()
    q.append((i,j))
    visited[i][j]=True

    while q:
        x,y = q.popleft()
        for d in range(4):
            next_x=x+dx[d]
            next_y=y+dy[d]
            # 탐색 조건
            if 0<=next_x<n and 0<=next_y<m and matrix_copy[next_x][next_y]!=1 and not visited[next_x][next_y]:
                matrix_copy[next_x][next_y]=2
                visited[next_x][next_y]=True
                q.append((next_x,next_y))


matrix=[]
visited=[]
answer=0

for _ in range(n):
    matrix.append(list(map(int,input().split())))
    visited.append([False for _ in range(m)])

# 벽 세우기
for combi in list(combinations(range(n*m),3)):
    ix,iy= find_xy(combi[0])
    jx,jy= find_xy(combi[1])
    kx,ky= find_xy(combi[2])

    if(matrix[ix][iy]!=0 or matrix[jx][jy]!=0 or matrix[kx][ky]!=0 ):
        continue
    else:
        reset_visited(visited)
        
        matrix_copy=[[0]*m for _ in range(n)]
        copy_matrix(matrix,matrix_copy)
        
        matrix_copy[ix][iy]=1
        matrix_copy[jx][jy]=1
        matrix_copy[kx][ky]=1
        safe_area = find_safe_area(matrix_copy)
        
        answer=max(answer,safe_area)

print('answer=',answer)
