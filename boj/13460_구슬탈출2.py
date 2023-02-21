# 틀림
import sys
from collections import deque
def input():return sys.stdin.readline().rstrip()

board=[]
visited=[]
red_x,red_y=-1,-1 # 빨간 구슬 위치
blue_x,blue_y=-1,-1 # 파란 구슬 위치

# 상, 하, 좌, 우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# dir 방향으로 굴린 후의 좌표를 반환
def get_next(dir,x,y,ox,oy):
    if 0<=dir<=1:
        nx=x+dx[dir]
        while 0<=nx<N and board[nx][y]=='.' and not((nx==ox) and y==oy):
            x=nx
            nx=x+dx[dir]
    else:
        ny=y+dy[dir]
        while 0<=ny<M and board[x][ny]=='.' and not (x==ox and (ny==oy)):
            y=ny
            ny=y+dy[dir]
    return x,y

N,M=map(int,input().split())
for i in range(N):
    board.append(list(input()))
    for j in range(M):
        if board[i][j]=='R':
            red_x,red_y=i,j
        elif board[i][j]=='B':
            blue_x,blue_y=i,j

q=deque()
q.append((0,red_x,red_y,blue_x,blue_y))
visited.append((red_x,red_y,blue_x,blue_y))
board[red_x][red_y],board[blue_x][blue_y]='.','.'

found=False
answer=-1
while not found and q:
    distance,rx,ry,bx,by=q.popleft()
    if distance>10:
        break
    
    for i in range(4):
        # 빨간 구슬 이동
        r_nx,r_ny=get_next(i,rx,ry,bx,by)

        # 다음 칸이 구멍
        if board[r_nx+dx[i]][r_ny+dy[i]]=='O':
            b_nx,b_ny=get_next(i,bx,by,-1,-1)
            if board[b_nx+dx[i]][b_ny+dy[i]]=='O':
                continue
            answer=distance+1
            found=True
            break
        
        # 다음 칸이 파란구슬
        elif r_nx+dx[i]==bx and r_ny+dy[i]==by:
            b_nx,b_ny=get_next(i,bx,by,-1,-1)
            if board[b_nx+dx[i]][b_ny+dy[i]]=='O':
                continue
            r_nx,r_ny=get_next(i,r_nx,r_ny,b_nx,b_ny)

        # 다음 칸이 벽 -> 파란 구슬 이동
        else:
            b_nx,b_ny=get_next(i,bx,by,r_nx,r_ny)
            if board[b_nx+dx[i]][b_ny+dy[i]]=='O':
                continue
        if (r_nx,r_ny,b_nx,b_ny) not in visited:
            visited.append((r_nx,r_ny,b_nx,b_ny))
            q.append((distance+1,r_nx,r_ny,b_nx,b_ny))

print(answer)