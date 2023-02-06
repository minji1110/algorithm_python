# 다시
from collections import deque

# 왼위, 오위, 왼아래, 오아래
# 이동후 좌표, 대각선 좌표 dxdy
rot_to_1=[
    [(-1,0),(-1,1)],[(-1,1),(-1,0)],[(1,0),(1,1)],[(1,1),(1,0)]
]

# 왼위, 왼아래, 오위, 오아래
rot_to_0=[
    [(0,-1),(1,-1)],[(1,-1),(0,-1)],[(0,1),(1,1)],[(1,1),(0,1)]
]

def dfs(board,visited,start):
    n=len(board)
    x,y,dir,t=start

    # print(x,y,dir,t)
    
    #가로 방향
    if dir==0:
        if x==n-1 and y==n-2: # 도착
            if board[n-1][n-1]==0: board[n-1][n-1]=t+1
            else: board[n-1][n-1]=min(board[n-1][n-1],t+1)
        else:
            visited[x][y]=True
            #오
            if y+2<n and not visited[x][y+2]:
                print('오른쪽 이동')
                dfs(board,visited,(x,y+1,0,t+1))
                visited[x][y+1]=False
            #왼
            if 1<y and not visited[x][y-2]:
                print('왼 이동')
                dfs(board,visited,(x,y-2,0,t+1))
                visited[x][y-1]=False
            # 회전
            for i in range(4):
                print('회전')
                nx,ny=rot_to_1[i][0]
                rx,ry=rot_to_1[i][1]

                if 0<=nx<n and 0<=ny<n and 0<=rx<n and 0<=ry<n:
                    if board[rx][ry]==0 and board[nx][ny]==0 and not visited[nx][ny]:
                        if i<=1:
                            dfs(board,visited,(nx,ny,1,t+1))
                            visited[nx][ny]=False
                        elif i==2:
                            dfs(board,visited,(x,y,1,t+1))
                            visited[x][y]=False
                        else:
                            dfs(board,visited,(x,y+1,1,t+1))
                            visited[x][y+1]=False
    # 세로 방향
    else:
        if x==n-2 and y==n-1: # 도착
            if board[n-1][n-1]==0: board[n-1][n-1]=t+1
            else: board[n-1][n-1]=min(board[n-1][n-1],t+1)
        else:
            visited[x][y]=True
            #아래
            if x+2<n and not visited[x+2][y]:
                dfs(board,visited,(x+1,y,1,t+1))
                visited[x+1][y]=False
            #위
            if 1<x and not visited[x-2][y]:
                dfs(board,visited,(x-1,y,1,t+1))
                visited[x-2][y]=False
            # 회전
            for i in range(4):
                nx,ny=rot_to_0[i][0]
                rx,ry=rot_to_0[i][1]

                if 0<=nx<n and 0<=ny<n and 0<=rx<n and 0<=ry<n:
                    if board[rx][ry]==0 and board[nx][ny]==0 and not visited[nx][ny]:
                        if i<=1:
                            dfs(board,visited,(nx,ny,0,t+1))
                            visited[nx][ny]=False
                        elif i==2:
                            dfs(board,visited,(x,y,0,t+1))
                            visited[x][y]=False
                        else:
                            dfs(board,visited,(x+1,y,0,t+1))
                            visited[x+1][y]=False

def solution(board):
    answer = 1e9
    n=len(board)
    visited=[[False]*(n) for _ in range(n)]
    
    dfs(board,visited,(0,0,0,0))

    answer=board[n-1][n-1]
    return answer

board=[
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]]	

print(solution(board))